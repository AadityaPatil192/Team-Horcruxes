from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo
from bson import ObjectId
import logging

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://aadityapatil1902:root@cluster0.wvbc0gp.mongodb.net/hr-data"
mongo = PyMongo(app)

logging.basicConfig(level=logging.DEBUG)

def serialize_doc(doc):
    doc['_id'] = str(doc['_id'])
    return doc

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query_a')
def query_a():
    results = mongo.db.details.find({
        "DOJ_Extended": "Yes",
        "Duration_to_accept_offer": { "$lt": 30 },
        "Candidate_relocate_actual": "Yes"
    })
    results_list = [serialize_doc(doc) for doc in results]
    logging.debug(f"Query A Results: {results_list}")
    return jsonify(results_list)

@app.route('/query_b')
def query_b():
    results = mongo.db.details.find({
        "$or": [
            { "DOJ_Extended": "Yes" },
            { "DOJ_Extended": "No", "Duration_to_accept_offer": { "$lt": 10 } }
        ]
    })
    results_list = [serialize_doc(doc) for doc in results]
    logging.debug(f"Query B Results: {results_list}")
    return jsonify(results_list)

@app.route('/query_c')
def query_c():
    results = mongo.db.details.find({
        "DOJ_Extended": "Yes",
        "Percent_hike_offered_in_CTC": { "$gte": 25 }
    })
    results_list = [serialize_doc(doc) for doc in results]
    logging.debug(f"Query C Results: {results_list}")
    return jsonify(results_list)

@app.route('/query_d')
def query_d():
    results = mongo.db.details.find({
        "DOJ_Extended": "Yes",
        "Percent_hike_offered_in_CTC": { "$gte": 25 },
        "Duration_to_accept_offer": { "$lt": 30 },
        "Candidate_relocate_actual": "Yes",
        "Joining_Bonus": "Yes"
    })
    results_list = [serialize_doc(doc) for doc in results]
    logging.debug(f"Query D Results: {results_list}")
    return jsonify(results_list)

@app.route('/query_e')
def query_e():
    pipeline = [
        {
            "$group": {
                "_id": "$Candidate_Source",
                "totalHired": { "$sum": 1 },
                "totalJoined": { 
                    "$sum": { 
                        "$cond": [{ "$eq": ["$Status", "Joined"] }, 1, 0]
                    }
                },
                "totalDeclined": { 
                    "$sum": { 
                        "$cond": [{ "$eq": ["$Status", "Declined"] }, 1, 0]
                    }
                }
            }
        }
    ]
    results = list(mongo.db.details.aggregate(pipeline))
    # Convert ObjectId in _id if present
    for result in results:
        if isinstance(result['_id'], ObjectId):
            result['_id'] = str(result['_id'])
    logging.debug(f"Query E Results: {results}")
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
