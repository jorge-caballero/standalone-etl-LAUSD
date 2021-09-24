import csv, json, os
import jq
import pandas as pd
from loguru import logger

def load_from_file(src_uri: str):
  logger.debug(f'Reading from {src_uri}')
  with open(src_uri, "r") as read_file:
    raw_json = json.load(read_file)
  
  return raw_json["etl_params"]
  
def load(config_path: str):  
    if (os.path.isfile(config_path)):
      logger.debug(f'Loading configuration from `{config_path}`')
      return load_from_file(config_path)
    else:
      logger.error(f'Configuration file not found at `{config_path}`\n')
      return None
  