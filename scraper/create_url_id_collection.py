from mongodb_handler import MongodbHandler
from custom_logger import CustomLogger

TABLE_NAME = 'url_ids'

if __name__ == '__main__':
    batch_num = 0
    logger = CustomLogger()
    database_handler = MongodbHandler()
    database_handler.connect()

    uniques = database_handler.find_all_uniques('url', ['births', 'marriages', 'deaths'])
    logger.info('Found {} urls'.format(len(uniques)))

    uniques_list = []
    for item in uniques:
        uniques_list.append({'_id': item})

    database_handler.create_table(TABLE_NAME)
    database_handler.insert(uniques_list, table_name=TABLE_NAME)
    logger.info('Finished')
