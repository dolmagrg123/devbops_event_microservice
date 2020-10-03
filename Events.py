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
#     comment = request.form['Comment']
#     eventID = request.form['eventID']
#     #each event contains a unique ID
#     status = aws.saveComment(eventID, comment)
#     #if (status == -1) return "Failed"
#     #status :either true or false to show
#     return status #commentID

# @app.route("/viewing", methods= ["GET"])
# def viewing():
#     comment = aws.getAllPost()
#     return content

if __name__ == '__main__':
    app.run(debug=True)