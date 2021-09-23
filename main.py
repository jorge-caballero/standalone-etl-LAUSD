import logging, os, sys
from datetime import date, timedelta
from etl import *
import argparse
from loguru import logger

# Configure the root logger
format_str = '%(levelname)s [%(funcName)s] %(message)s (logger: %(name)s)'
logging.basicConfig(level=logging.INFO, format=format_str)

# Configure the logger for this app
def my_filter(record):
  trace_module_list = ["etl_util.preprocessing", ]
  trace_function_list = ["preprocess_aggregation"]
  debug_module_list = ["etl_util"]
  debug_function_list = []
  
  if ((record["module"] in trace_module_list) or (record["function"] in trace_function_list)):
    return True
  elif ((record["module"] in debug_module_list) or (record["function"] in debug_function_list)):
    return (record["level"].no >= logger.level("DEBUG").no)
  # elif (record["file"].name.startswith("retrieve")):
  #   return True
  else:
    return (record["level"].no >= logger.level("INFO").no) # Print if at least at this level

fmt = "<level>{level: <8}</level> <cyan>[ {function: ^4} ]</cyan> {message}"
logger.remove()
logger.add(sink=sys.stderr, level="TRACE", filter=my_filter, format=fmt, colorize=True,)

# Configure the parser
yesterday = date.today() - timedelta(days=1)
prefix_default = yesterday.strftime("%Y-%m-%dT2200")

parser = argparse.ArgumentParser(description='Download and parse LAUSD COVID-19 data')
                    
parser.add_argument('--prefix', dest='prefix', type=str, nargs='?', default=prefix_default,
                    help=f'the string that will be preppended to the filenames created during this run (Default: "{prefix_default}"')

parser.add_argument('--destination', dest='base_path', type=str, nargs='?',
                    help='the path to the folder where the raw and transformed data will be stored. For example, "/home/username/LAUSD/data"')

parser.add_argument('--force_download', dest='force_download', action='store_true', default=False,
                    help='setting this flag will retrieve the data without checking for existing files, potentially overwriting historical data - USE CAUTIOUSLY (default: False)')

parser.add_argument('--force_transform', dest='force_transform', action='store_true', default=False,
                    help='setting this flag will transform the data without checking for existing files, potentially overwriting historical data - USE CAUTIOUSLY (default: False)')
                    
args = parser.parse_args()


def main():
  # Process the options
  filname_prefix = args.prefix
  uri_root = args.base_path if (args.base_path is not None) else os.getenv('LOCAL_URI_ROOT')
  force_download = args.force_download if (args.force_download is not None) else False
  force_transform = args.force_transform if (args.force_transform is not None) else False
  
  if uri_root is None:
    logger.critical(f'Missing base path.\n')
    raise Exception()
  
  archive_folder_path_str = f'{uri_root}/archive'
  etl_folder_path_str = f'{uri_root}/etl'
  
  print(f'\n===================================\n==========     LAUSD     ==========\n===================================')
  print(f'\n=======     Data Retrieval     ========')
  retrieve(filname_prefix, archive_folder_path_str, etl_params, force_download)
  print(f'\n=======     Data Transform     ========')
  transform(filname_prefix, archive_folder_path_str, etl_folder_path_str, etl_params, force_transform)
  
if __name__ == '__main__':
  main()
