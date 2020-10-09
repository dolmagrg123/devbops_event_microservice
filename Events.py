from flask import Flask, request
from AWSManager import Events
 
event = Events()
app = Flask(__name__)


@app.route("/create-event", methods=["POST"])
def create():
    #event.put(Event_name = "trPresentation", Event_date = "October 3rd", Event_time = "2pm", User = "Class", Event_desc = "Presenting things", Event_image = "None", Event_location = "Zoom")
    res = request.json
    Event_name = res['Event_name']
    Event_date = res['Event_date']
    Event_time = res['Event_time']
    User = res['User']
    Event_desc = res['Event_desc']
    Event_image = res['Event_image']
    Event_location = res['Event_location']

    event.check_if_event_exists(Event_name = Event_name, Event_date = Event_date, Event_time = Event_time, User = User, Event_desc= Event_desc, Event_image = Event_image, Event_location = Event_location)
    
@app.route("/event-delete", methods=["POST"])
def delete():
    res = request.json
    Event_name = res['Event_name']
    
    event.delete(Event_name = Event_name)

#not done yet
@app.route("/event-update", methods=["POST"]) 
def update():
    res = request.json
    New_Event_name = res['New_Event_name']
    New_Event_date = res['New_Event_date']
    New_Event_time = res['New_Event_time']
    New_User = res['New_User']
    New_Event_desc = res['New_Event_desc']
    New_Event_image = res['New_Event_image']
    New_Event_location = res['New_Event_location']

    event.update()

@app.route("/event-view", methods= ["GET"])
def view_event():
    res = event.view()
    return res

#still a work in progress
@app.route("/event-rsvp", methods= ["GET"])
def rsvp():
    res = event.rsvp()
    return res
# @app.route("/event/rsvp", methods=["POST"])
# def rsvp():
#      t1.put("Event_name", "Event_date", "Event_time", "User", "Event_desc", "Event_image", "Event_location")

if __name__ == '__main__':
    app.run(debug=True)
