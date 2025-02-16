import json
from collections import OrderedDict
from custom_logger import CustomLogger
import os

logger = CustomLogger()
DEFAULT_FILE_PATH = '../data/batch_links.json'
DB_JSON_PATH = '../collections/'
def fix_entries_num(batch_dict):
    fix_counter = 0
    broken_counter = 0
    for province in batch_dict.keys():
        count = len(batch_dict[province]['registers'].keys())
        for i, reg in enumerate(batch_dict[province]['registers'].keys()):
            text = batch_dict[province]['registers'][reg]['entries_num']
            if text is not None:
                if isinstance(text, str) and (text.endswith('pasujących') or text.endswith('dostępnych')):
                    text = int(text.split(' ')[-2])
                    if text == 0:
                        logger.warning(f"Found 0 entries num: {reg}.")
                        broken_counter = broken_counter+1
                    batch_dict[province]['registers'][reg]['entries_num'] = text
                    fix_counter = fix_counter+1
            else:
                logger.warning(f"Found broken entries num: {reg}. Setting entries num to 0" )
                batch_dict[province]['registers'][reg]['entries_num'] = 0
                broken_counter = broken_counter+1
                fix_counter = fix_counter+1

    logger.info(f"Fixed {fix_counter} entries_num")
    logger.info(f"Number of broken batches: {broken_counter}")
    return batch_dict

def fix_ids(db_json, batch_links):
    pass

def count_all_entries(batches):
    total_num = 0
    for province in batch_dict.keys():
        count = len(batch_dict[province]['registers'].keys())
        for i, reg in enumerate(batch_dict[province]['registers'].keys()):
            num = batch_dict[province]['registers'][reg]['entries_num']
            if num:
                total_num = total_num+num

    logger.info(f"Total number of entries found: {total_num}")


def save_to_file(batch_list, filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'w') as f:
            json.dump(batch_list, f)
    else:
        with open(filepath, 'a') as f:
            json.dump(batch_list, f)

def read_json(filepath, mode='r'):
    #batch_dict = None
    with open(filepath, mode) as f:
        batch_dict = json.load(f, object_pairs_hook=OrderedDict)
        return batch_dict

if __name__ == '__main__':

    batch_dict = read_json(DEFAULT_FILE_PATH)
    #with open(DEFAULT_FILE_PATH, 'r') as f:
    #    batch_dict = json.load(f, object_pairs_hook=OrderedDict)
    #db_births = read_json(DB_JSON_PATH + 'births.json')
    fix_entries_num(batch_dict)
    count_all_entries(batch_dict)
    save_to_file(batch_dict, DEFAULT_FILE_PATH)

    #with open(filepath, 'r') as f:
    #    for line in f: