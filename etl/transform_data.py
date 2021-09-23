import csv, json, os
import jq
import pandas as pd
from loguru import logger

def perform_etl(src_uri: str, proc_jqstr: str):
  logger.debug(f'Reading from {src_uri}')
  with open(src_uri, "r") as read_file:
    raw_json = json.load(read_file)
  
  extracted_json = jq.compile(proc_jqstr).input(raw_json).all() # Dump the json objects
  normalized_df = pd.DataFrame(extracted_json).convert_dtypes(infer_objects=True, convert_string=True, convert_integer=True, convert_boolean=True, convert_floating=True)
  filled_df = normalized_df.fillna(method='ffill', inplace=False)
  return filled_df
  
def transform(current_date_prefix_str: str, src_path_root_str: str, dst_path_root_str: str, transform_params: dict, overwrite: bool = False):
  local_skip_list: list = []
  local_success_list: list = []
  local_error_list: list = []
  
  for transform_name in transform_params:
    filename = transform_name
    params = transform_params[transform_name]
    dst_subpath = params['dst_subpath']
    proc_jqstr = params['proc_jqstr']
    
    src_uri = f'{src_path_root_str}/{dst_subpath}/{current_date_prefix_str} {filename}.json'
    dst_uri = f'{dst_path_root_str}/{dst_subpath}/{current_date_prefix_str} {filename}.csv'
    
    if (os.path.isfile(dst_uri) and (overwrite == False)):
      local_skip_list.append(filename)
      logger.debug(f'Skipped `{filename}` because destination file already exists')
    elif (os.path.isfile(src_uri) == False):
      local_skip_list.append(filename)
      logger.warning(f'Skipped `{filename}` because source file is missing')
    elif (proc_jqstr is None):
      local_skip_list.append(filename)
      logger.warning(f'Skipped `{filename}` because no transformation is defined')
    elif ((dst_uri != None) and dst_uri.startswith('/')):
      logger.debug(f'Transforming `{filename}` ...')
      transformed_df = perform_etl(src_uri=src_uri, proc_jqstr=proc_jqstr)
      transformed_df.to_csv(dst_uri, na_rep='', header=False, index=False, quoting=csv.QUOTE_NONNUMERIC, doublequote=True)
      local_success_list.append(filename)
      logger.debug(f'Saved `{filename}` to `{dst_uri}`\n')
      logger.debug(f'Transformed `{filename}`')
    else:
      local_error_list.append(filename)
      logger.error(f'Failed to transform `{filename}`\n')
    
  print(f'\n  Data Transformation Summary:\n  =======')
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
  