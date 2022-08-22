import time
import urllib.parse
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

""" Sets selenium chrome web driver.
    If you want a hadless driver set env to other thing than DEV into main.py """
def get_driver( env = 'DEV' ):
  options = Options()
  options.add_argument("--disable-blink-features=AutomationControlled")

  if ( env == 'PROD' ):
    options.add_argument('--headless')

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

  return driver


""" Gets tracker.gg/valorant data based on data type ( profile, map, agent, weapon or match)
    to a given riot id (username#tag)
    returns a json """
def get_by( data_type, riot_id, env ):
  data = req_tracker_data( data_type, riot_id, env )
  json_data = json.loads(data)
  json_data['trackerProfile'] = get_tracker_url_overview( riot_id )
  return json.dumps(json_data)
  #return data

def req_tracker_data( data_type, riot_id, env = 'DEV' ):
  driver = get_driver( env )
  tracker_url = get_tracker_url(data_type, riot_id )
  driver.get(tracker_url)
  time.sleep(1)

  try:
    info = driver.find_element(By.TAG_NAME, "pre")
    data = info.text
    driver.close()
    return data

  except:
    driver.close()
    return r'{"errors": [ {"code": "scraping error", "sts_code": "500"}]}'

""" Gets the correct url for the data type """
def get_tracker_url( data_type, riot_id ) -> str:
  username, tag = riot_id.split("#")
  username =  urllib.parse.quote(username)
  tag =  urllib.parse.quote(tag)

  if data_type == 'PROFILE':
    return get_tracker_url_profile( username, tag )

  elif data_type == 'AGENT':
    return get_tracker_url_agent( username, tag )

  elif data_type == 'MAP':
    return get_tracker_url_map( username, tag )

  elif data_type == 'MATCH':
    return get_tracker_url_match( username, tag )

  elif data_type == 'WEAPON':
    return get_tracker_url_weapon( username, tag )

  else:
    return get_tracker_url_profile( username, tag )

def get_tracker_url_profile( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}"
  return tracker_url

def get_tracker_url_match( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/matches/riot/{username}%23{tag}?type=competitive"
  return tracker_url

def get_tracker_url_map( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}/segments/map?playlist=competitive"
  return tracker_url

def get_tracker_url_weapon( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}/segments/weapon?playlist=competitive"
  return tracker_url

def get_tracker_url_agent( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}/segments/agent?playlist=competitive"
  return tracker_url

def get_tracker_url_overview( riot_id ) -> str:
  username, tag = riot_id.split("#")
  username =  urllib.parse.quote(username)
  tag =  urllib.parse.quote(tag)
  profile_url = f"https://tracker.gg/valorant/profile/riot/{username}%23{tag}/overview"
  return profile_url
