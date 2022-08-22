import time
import json
from selenium.webdriver.common.by import By
from scrapper import chrome_driver, tracker_urls

""" Gets tracker.gg/valorant data based on data type ( profile, map, agent, weapon or match)
    to a given riot id (username#tag)
    returns a json """
def get_by( data_type, riot_id, env ):
  if '#' not in riot_id:
    return invalid_id()

  print(data_type, riot_id, env)
  data = req_tracker_data( data_type, riot_id, env )
  json_data = json.loads(data)
  json_data['trackerProfile'] = tracker_urls.url_overview( riot_id )
  return json.dumps(json_data)
  #return data

def req_tracker_data( data_type, riot_id, env = 'DEV' ):
  driver = chrome_driver.get_chrome( env )
  tracker_url = tracker_urls.get_url(data_type, riot_id )
  driver.get(tracker_url)
  time.sleep(1)

  try:
    info = driver.find_element(By.TAG_NAME, "pre")
    data = info.text
    driver.close()
    return data

  except:
    driver.close()
    return gen_error()


def gen_error():
  return r'{"errors": [ {"code": "scraping error", "sts_code": "500"}]}'

def invalid_id():
  return r'{"errors": [ {"code": "scraping error", "sts_code": "502", "message": "Invalid riot id"}]}'
