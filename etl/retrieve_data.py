import os
import requests
from loguru import logger

def retrieve(current_date_prefix_str: str, dst_path_root_str: str, request_params: dict, overwrite: bool = False):
  local_skip_list: list = []
  local_success_list: list = []
  local_error_list: list = []
  
  for request_name in request_params:
    filename = request_name
    params = request_params[request_name]
    dst_subpath = params['dst_subpath']
    url = params['url']
    headers = params['headers']
    payload = params['payload']
    method = params['method']
    
    dst_uri = f'{dst_path_root_str}/{dst_subpath}/{current_date_prefix_str} {filename}.json'

    if (os.path.isfile(dst_uri) and (overwrite == False)):
      local_skip_list.append(filename)
      logger.debug(f'Skipped `{filename}` because destination file already exists')
    elif ((dst_uri != None) and dst_uri.startswith('/')):
      logger.debug(f'Requesting `{filename}` ...')
      response = requests.request(method, url, headers=headers, data=payload)
      if response.status_code == 200:
        # print(f'Writing data to `{dst_uri}` ...')
        with open(dst_uri, 'wt', encoding='utf-8') as f:
          f.write(response.text)
        logger.debug(f'Saved `{filename}` to `{dst_uri}`\n')
        logger.debug(f'Retrieved `{filename}`')
        local_success_list.append(filename)
      else:
        logger.error(f'Failed to retrieve `{filename}`\n')
    else:
      local_error_list.append(filename)
      logger.error(f'Unexpected error encountered while retrieving `{filename}`\n')
  
  print(f'\n  Data Retrieval Summary:\n  =======')
  if len(local_success_list) > 0:
    print(f'    Successful: ({len(local_success_list)}):')
    for item in local_success_list: print(f'      * {item}')
  
  if len(local_skip_list) > 0:
    print(f'    Skipped ({len(local_skip_list)}):')
    for item in local_skip_list: print(f'      * {item}')
  
  if len(local_error_list) > 0:
    print(f'    Failed ({len(local_error_list)}):')
    for item in local_error_list: print(f'      * {item}')
  print()
  