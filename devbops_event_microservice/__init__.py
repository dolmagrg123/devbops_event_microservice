from flask import Flask, request
from devbops_event_microservice.AWSManager import Events

event = Events()
app = Flask(__name__)


# works

@app.route("/create-event", methods=["POST"])
def create():
    # event.put(Event_name = "trPresentation", Event_date = "October 3rd", Event_time = "2pm", User = "Class", Event_desc = "Presenting things", Event_image = "None", Event_location = "Zoom")
    res = request.json
    Event_name = res['Event_name']
    Event_date = res['Event_date']
    Event_time = res['Event_time']
    User = res['User']
    Event_desc = res['Event_desc']
    Event_image = res['Event_image']
    Event_location = res['Event_location']
    Online = res['Online']

    created = event.check_if_event_exists(Event_name=Event_name, Event_date=Event_date, Event_time=Event_time,
                                          User=User, Event_desc=Event_desc, Event_image=Event_image,
                                          Event_location=Event_location, Online=Online, RSVP=[])
    return created


# works 
@app.route("/event-delete", methods=["POST"])
def delete():
    res = request.json
    Event_name = res['Event_name']

    deleted = event.delete(Event_name=Event_name)
    return deleted


# works
@app.route("/event-update", methods=["POST"])
def update():
    res = request.json
    Event_name = res["Event_name"]
    New_Event_date = res['New_Event_date']
    New_Event_time = res['New_Event_time']
    New_Event_desc = res['New_Event_desc']
    New_Event_image = res['New_Event_image']
    New_Event_location = res['New_Event_location']
    New_Online = res['New_Online']

    updated = event.update_event(Event_name=Event_name, New_Event_date=New_Event_date, New_Event_time=New_Event_time,
                                 New_Event_desc=New_Event_desc, New_Event_image=New_Event_image,
                                 New_Event_location=New_Event_location, New_Online=New_Online)


    return updated


@app.route("/event-view", methods=["GET"])
def view_event():
    res = event.view()
    return res


@app.route("/event-rsvp", methods=["POST"])
def rsvp():
    res = request.json
    Event_name = res['Event_name']
    User = res["USER"]

    rsvp = event.rsvp(User=User, Event_name=Event_name)
    return rsvp


@app.route('/history', methods=["POST"])
def history():
    req = request.json
    username = req['UserName']
    res = event.getAllUserEvent(username)
    return res

#######
@app.route('/userRSVP', methods=['POST'])
def userRSVP():
    req = request.json
    username = req['UserName']
    res = event.getUserRvsp(username)
    return res

@app.route('/cancelRSVP', methods=['POST'])
def cancelReservation():
    req = request.json
    username = req['UserName']
    eventname = req['Event_name']
    res = event.cancelRsvp(username, eventname)
    return res


@app.route('/', methods=['GET'])
def TEST():
    return "DOCKER WORKING FINE"

if __name__ == '__main__':
    app.run(debug=True)
