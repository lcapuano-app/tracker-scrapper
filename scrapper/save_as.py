import json
import time
import os.path
from pathlib import Path

def json_file( str_data: str, riot_id: str ) -> str:

  ts = str(time.time())
  save_path = 'files/'
  file_name = f"{riot_id}{ts}.json"
  full_path = os.path.join(save_path, file_name)
  try:
    with open(full_path, 'w', encoding='utf-8') as f:
      json_data = json.loads(str_data)
      json.dump(json_data, f, ensure_ascii=False)
      return full_path
  except Exception as e :
    return full_path
