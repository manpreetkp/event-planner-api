Project: Event PLanner API

Description: This is an event planner application that has a set of RESTful APIs to manage events. The application supports creating, retrieving, updating, and deleting events, along with specific functionalities to retrieve events by date, and delete all events.

Installation:
 - Clone the repository
 - Navigate to the project directory in your terminal
 - Install the necessary dependencies (flask, flask-restful, pymongo, etc.)
 - Run the application by typing "python3 app.py" in your terminal
 
 API Documentation
 1. Create Event
    Request: POST http://127.0.0.1:5000/events 
    Go within the Body Tab, make sure seeting is on raw and JSON, type like below:
        {
    "event_name": "Christmas Party",
    "event_description": "Anne's Yearly Christmas Carols",
    "date_of_event": "2023-12-25",
    "duration": 300
    }
    Response: "message": "Event has been created"

2. Get All Events
    Request: GET http://127.0.0.1:5000/events 
    Response: 
            {
    "_id": ObjectId('668e722b08e59c8300557161')
    "event_name": "Christmas Party",
    "event_description": "Anne's Yearly Christmas Carols",
    "date_of_event": "2023-12-25",
    "duration": 300
    }

3. Get Event by ID
    Request: GET http://127.0.0.1:5000/events/668dfab40f2513bb5131d75c 
    Response: 
            {
    "_id": ObjectId('668e722b08e59c8300557161')
    "event_name": "Christmas Party",
    "event_description": "Anne's Yearly Christmas Carols",
    "date_of_event": "2023-12-25",
    "duration": 300
    }

4. Update Event by ID
    Request: PUT http://127.0.0.1:5000/events/66869c72a263eded6238408a Go within the Body Tab, make sure seeting is on raw and JSON, type your updates in the correct format
    Response: 
            {
    "_id": ObjectId('66869c72a263eded6238408a')
    "event_name": "Anniversary",
    "event_description": "M&V Anniversary",
    "date_of_event": "2022-03-18",
    "duration": 300
    }

5. Delete Event by ID
    Request: DELETE http://127.0.0.1:5000/events/66869c72a263eded6238408a
    Response: "msg": "Event has been deleted"

6. Get Events by Specific Date
    Request: GET http://127.0.0.1:5000/events/date/2023-12-25 
    Response: 
            {
    "_id": ObjectId('668e722b08e59c8300557161')
    "event_name": "Christmas Party",
    "event_description": "Anne's Yearly Christmas Carols",
    "date_of_event": "2023-12-25",
    "duration": 300
    }

7. Get Events for Current Day
    Request: GET http://127.0.0.1:5000/events/today
    Response: 
            {
    "_id": ObjectId('66869c76a263eded6238408b')
    "event_name": "Test Event",
    "event_description": "This is a test description",
    "date_of_event": "2024-07-10",
    "duration": 100
    }

8. Get Events Between Two Dates
    Request: GET http://127.0.0.1:5000/events/between/2023-12-20/2023-12-30 
    Response: 
            {
    "_id": ObjectId('668e722b08e59c8300557161')
    "event_name": "Christmas Party",
    "event_description": "Anne's Yearly Christmas Carols",
    "date_of_event": "2023-12-25",
    "duration": 300
    }

9. Delete All Events
    Request: DELETE http://127.0.0.1:5000/events
    Response: "msg": f"Deleted all 4 events in the database"


 For any inquiries, email manpreet@getambee.com
