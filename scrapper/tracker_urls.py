import urllib.parse

""" Gets the correct url for the data type """
def get_url( data_type, riot_id ) -> str:
  username, tag = riot_id.split("#")
  username =  urllib.parse.quote(username)
  tag =  urllib.parse.quote(tag)

  if data_type == 'PROFILE':
    return url_profile( username, tag )

  elif data_type == 'AGENT':
    return url_agent( username, tag )

  elif data_type == 'MAP':
    return url_map( username, tag )

  elif data_type == 'MATCH':
    return url_match( username, tag )

  elif data_type == 'WEAPON':
    return url_weapon( username, tag )

  else:
    return url_profile( username, tag )

def url_profile( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}"
  return tracker_url

def url_match( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/matches/riot/{username}%23{tag}?type=competitive"
  return tracker_url

def url_map( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}/segments/map?playlist=competitive"
  return tracker_url

def url_weapon( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}/segments/weapon?playlist=competitive"
  return tracker_url

def url_agent( username, tag ) -> str:
  tracker_url = f"https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}/segments/agent?playlist=competitive"
  return tracker_url

def url_overview( riot_id ) -> str:
  username, tag = riot_id.split("#")
  username =  urllib.parse.quote(username)
  tag =  urllib.parse.quote(tag)
  profile_url = f"https://tracker.gg/valorant/profile/riot/{username}%23{tag}/overview"
  return profile_url
