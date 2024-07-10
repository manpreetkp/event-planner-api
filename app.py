## Main Flask application file

## Importing Needed Libraries
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson import ObjectId
from datetime import datetime, date

## Creating a flask application
app = Flask(__name__)

## Creating a connection to MongoDB for the Flask application
app.config["MONGO_URI"] = "mongodb://localhost:27017/eventPlannerDatabase"
mongo = PyMongo(app)

## Create events in the database using POST method
@app.route('/events', methods=['POST'])
def create_event():
    try:
        if not request.json or not 'event_name' in request.json or not 'date_of_event' in request.json or not 'duration' in request.json:
            return jsonify({"error": "Missing required fields"}), 400

        event = {
            "event_name": request.json['event_name'],
            "event_description": request.json.get('event_description', ''),
            "date_of_event": request.json['date_of_event'],
            "duration": request.json['duration']
        }
        result = mongo.db.events.insert_one(event)
        event['_id'] = str(result.inserted_id)
        return jsonify({"message": "Event has been created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

## Retrieve all the events in the database using the GET method    
@app.route('/events', methods=['GET'])
def get_events():
    try:
        events = list(mongo.db.events.find({}, {'_id': False}))
        return jsonify(events), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

## Retrieve an event by specifying the id associated with it in the database using the GET method    
@app.route('/events/<id>', methods=['GET'])
def get_event_by_id(id):
    try:
        event = mongo.db.events.find_one({"_id": ObjectId(id)})
        if event:
            event['_id'] = str(event['_id'])
            return jsonify(event), 200
        else:
            return jsonify({"error": "Event has not been found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

## Update information in any part of an events field by accessing it through the specific id number associated with it using the PUT method
@app.route('/events/<id>', methods=['PUT'])
def update_event(id):
    try:
        if not request.json:
            return jsonify({"error": "Request must be JSON"}), 400

        update_data = {}
        if 'event_name' in request.json:
            update_data['event_name'] = request.json['event_name']
        if 'event_description' in request.json:
            update_data['event_description'] = request.json['event_description']
        if 'date_of_event' in request.json:
            update_data['date_of_event'] = request.json['date_of_event']
        if 'duration' in request.json:
            update_data['duration'] = request.json['duration']

        if update_data:
            result = mongo.db.events.update_one({"_id": ObjectId(id)}, {"$set": update_data})
            if result.modified_count:
                return jsonify({"msg": "Event has been updated"}), 200
            else:
                return jsonify({"error": "No updates have been made"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

## Delete an event by accessing it through the specific id number associated with it using the DELETE method    
@app.route('/events/<id>', methods=['DELETE'])
def delete_event(id):
    try:
        result = mongo.db.events.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return jsonify({"msg": "Event has been deleted"}), 200
        else:
            return jsonify({"error": "Event has not been found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

## Retrieve any event/events by specifying the date you want to retrieve from using the GET method
@app.route('/events/date/<date>', methods=['GET'])
def get_events_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")  
        events = list(mongo.db.events.find({"date_of_event": date}, {'_id': False}))
        return jsonify(events), 200
    except ValueError:
        return jsonify({"error": "Date format is INVALID. Make sure to use YYYY-MM-DD."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

## Retrieve any event/events for today using the GET method
@app.route('/events/today', methods=['GET'])
def get_events_for_today():
    try:
        today = date.today().strftime("%Y-%m-%d")
        events = list(mongo.db.events.find({"date_of_event": today}, {'_id': False}))
        return jsonify(events), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

## Retrieve any event/events in between two specific dates using the GET method
@app.route('/events/between/<start_date>/<end_date>', methods=['GET'])
def get_events_between_dates(start_date, end_date):
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
        events = list(mongo.db.events.find({"date_of_event": {"$gte": start_date, "$lte": end_date}}, {'_id': False}))
        return jsonify(events), 200
    except ValueError:
        return jsonify({"error": "Date format is INVALID. Make sure to use YYYY-MM-DD."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

## Delete all events in the database using the DELETE method
@app.route('/events', methods=['DELETE'])
def delete_all_events():
    try:
        result = mongo.db.events.delete_many({})
        return jsonify({"msg": f"Deleted all {result.deleted_count} events in the database"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
