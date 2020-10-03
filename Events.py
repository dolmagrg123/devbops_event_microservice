from flask import Flask, request
from AWSManager import Events
 
 
app = Flask(__name__)
t1 = Events()

@app.route("/event")
def posting():
    t1.put("Event_name", "Event_desc", "Date_time", "Price", "Address", "Virtual")
    

@app.route("/event/rsvp")
def comment():
    t1.put("Event_name", "Event_desc", "Date_time", "Price", "Address", "Virtual")

@app.route("/event/diff feature")
def comment():
    t1.put("Event_name", "Event_desc", "Date_time", "Price", "Address", "Virtual")

@app.route("/event/diff feature")
def comment():
    t1.put("Event_name", "Event_desc", "Date_time", "Price", "Address", "Virtual")

# @app.route("/viewing", methods= ["GET"])
# def viewing():
#     comment = aws.getAllPost()
#     return content

if __name__ == '__main__':
    app.run(debug=True)