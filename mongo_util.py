import pymongo
import csv
from logger_util import custom_logger


class mongodb_util:

    def __init__(self, connection_url, db_name, col_name, logfile):
        self.logger = custom_logger(logfile).get_logger()
        self.connection(connection_url, db_name, col_name)

    def connection(self, connection_url, db_name, col_name):
        try:
            self.logger.info("Connecting to the MongoDB...")
            self.client = pymongo.MongoClient(connection_url)
            self.db = self.client[db_name]
            self.col = self.db[col_name]
        except Exception:
            self.logger.exception('Exception raised when connecting to MongoDB')
        else:
            self.logger.info("Connection to the MongoDB successful")

    def storecsv_into_db(self, filepath, delim_csv=','):
        try:
            self.logger.info("Storing the csv data into the DB..")
            # Read the csv file and store all the records into a list
            all_records = []
            with open(filepath, 'r') as f:
                carbon_data = csv.reader(f, delimiter='\n')
                headers = next(carbon_data)[0].split(delim_csv)
                for i, line in enumerate(carbon_data):
                    values = line[0].split(delim_csv)
                    record = {}
                    for i, r in enumerate(headers):
                        record[headers[i]] = values[i]
                    all_records.append(record)

            # Insert into MongoDB database
            self.col.insert_many(all_records)

        except Exception:
            self.logger.exception('Exception raised while storing data into MongoDB.')
        else:
            self.logger.info("Storing into the MongoDB successful")

    def delete_one_record(self, query):
        try:
            self.logger.info("Deleting one records from the MongoDB collection")
            # Delete all records
            self.col.delete_one(query)

        except Exception as e:
            result = 'Exception raised while deleting one record from the MongoDB collection' +e
            self.logger.exception(result)
            return result
        else:
            result = "Deletion of one record from the MongoDB collection successful"
            self.logger.info(result)
            return result

    def delete_many_records(self, query):
        try:
            self.logger.info("Deleting many records from the MongoDB collection")
            # Delete all records
            self.col.delete_many(query)

        except Exception:
            result = 'Exception raised while deleting many records from the MongoDB collection'
            self.logger.exception(result)
            return result
        else:
            result = "Deletion of many records from the MongoDB collection successful"
            self.logger.info(result)
            return result

    def delete_all_records(self):
        try:
            self.logger.info("Deleting all records from the MongoDB collection")
            # Delete all records
            self.col.delete_many({})

        except Exception:
            self.logger.exception('Exception raised while deleting all records from the MongoDB collection')
        else:
            self.logger.info("Deletion of all records from the MongoDB collection successful")

    def drop_collection(self):
        try:
            self.logger.info("Dropping the whole collection of MongoDB")
            # Delete all records
            self.col.drop()

        except Exception:
            self.logger.exception('Exception raised while dropping MongoDB collection')
        else:
            self.logger.info("Dropping MongoDB collection successful.")

    def insert_one_record(self, record):
        try:
            self.logger.info("Inserting one record into MongoDB")
            rec = self.col.insert_one(record)
            self.logger.info("Inserted ids are:")
            self.logger.info(f"1. {rec.inserted_id}")

        except Exception:
            self.logger.exception('Exception raised while inserting one record into the MongoDB.')
        else:
            self.logger.info("Insertion of one record into MongoDB successful")

    def insert_many_records(self, list_records):
        try:
            self.logger.info("Inserting many records into MongoDB")
            rec = self.col.insert_many(list_records)
            self.logger.info("Inserted ids are:")
            for idx, unique_ids in enumerate(rec.inserted_ids):
                self.logger.info(f"{idx}. {unique_ids}")
        except Exception:
            self.logger.exception('Exception raised while inserting many records into the MongoDB.')
        else:
            self.logger.info("Insertion of many records into MongoDB successful")

    def find_one_record(self):
        try:
            self.logger.info("Finding one record in MongoDB")
            record = self.col.find_one()
        except Exception:
            self.logger.exception('Exception raised while finding one record from MongoDB.')
        else:
            self.logger.info("Finding one record in MongoDB successful.")
            return record

    def filter_records(self, query):
        try:
            self.logger.info("Finding records based on query in MongoDB")
            all_records = self.col.find(query)
        except Exception:
            self.logger.exception('Exception raised while finding record based on a query in MongoDB.')
        else:
            self.logger.info("Finding records based on query in MongoDB successful.")
            return all_records

    def find_one_record_and_update(self, id, new_data):
        try:
            self.logger.info("Find and update one record in MongoDB")
            self.col.find_one_and_update(id, new_data)
        except Exception:
            self.logger.exception('Exception raised while finding and updating one record from MongoDB.')
        else:
            self.logger.info("Finding and updating one record in MongoDB successful.")

    def find_all_records(self):
        try:
            self.logger.info("Finding all records in MongoDB")
            all_records = self.col.find()
            for idx, record in enumerate(all_records):
                self.logger.info(f"{idx}: {record}")
        except Exception:
            self.logger.exception('Exception raised while finding all records in MongoDB.')
        else:
            self.logger.info("Finding all records in MongoDB successful.")

    def update_one_record(self, present_data, new_data):
        try:
            self.logger.info("Updating one record in MongoDB")
            self.col.update_one(present_data, new_data)
        except Exception as e :
            result = 'Exception raised while updating one record from MongoDB.' + e
            self.logger.exception(result)
            return result
        else:
            result = "Updating one record in MongoDB successful."
            self.logger.info(result)
            return result

    def update_many_records(self, present_data, new_data):
        try:
            self.logger.info("Updating many record in MongoDB")
            self.col.update_many(present_data, new_data)
        except Exception as e:
            result = 'Exception raised while updating many records in MongoDB.' + e
            self.logger.exception(result)
        else:
            result = "Updating many records in MongoDB successful."
            self.logger.info(result)
            return result