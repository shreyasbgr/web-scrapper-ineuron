
from flask import Flask, request, jsonify
from mongo_util import mongodb_util
import json
from bson import json_util

app = Flask(__name__)

@app.route('/insert', methods=['POST'])
def insert_one_mongo():
    record = request.json
    my_mongo_util_obj.insert_one_record(record)
    return jsonify("One record inserted successfully.")

@app.route('/get', methods=['GET'])
def get_one_mongo():
    record = my_mongo_util_obj.find_one_record()
    return jsonify(json.loads(json_util.dumps(record)))

@app.route('/filter', methods=['POST'])
def filter():
    filter = request.json
    all_records = my_mongo_util_obj.filter_records(filter)
    return jsonify([json.loads(json_util.dumps(record)) for record in all_records])

@app.route('/delete-many',methods=['POST'])
def delete_many():
    filter = request.json
    result = my_mongo_util_obj.delete_many_records(filter)
    return jsonify(result)

@app.route('/delete-one',methods=['POST'])
def delete_one():
    filter = request.json
    result = my_mongo_util_obj.delete_one_record(filter)
    return jsonify(result)

@app.route('/update-one',methods=['POST'])
def update_one():
    present_data = request.json['present_data']
    new_data = request.json['new_data']
    result = my_mongo_util_obj.update_one_record(present_data,new_data)
    return jsonify(result)

@app.route('/update-many',methods=['POST'])
def update_many():
    present_data = request.json['present_data']
    new_data = request.json['new_data']
    result = my_mongo_util_obj.update_many_records(present_data,new_data)
    return jsonify(result)

if __name__ == '__main__':
    global my_mongo_util_obj

    # Create the Mongo DB object
    connection_url = "mongodb+srv://root:root@myatlascluster.5nfni.mongodb.net/reviews_scrapper_db?retryWrites=true&w=majority"
    db_name = 'reviews_scrapper_db'
    col_name = 'crawlerDb'
    logfile = 'output.log'
    my_mongo_util_obj = mongodb_util(connection_url,db_name,col_name,logfile)
    app.run(debug=True)
