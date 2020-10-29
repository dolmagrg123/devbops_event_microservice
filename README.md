# Devblops_event_microservice

## Issue Tracker
 - Token should be in header (API Gateway)
 - Comments should have date/time (Backend)

## Event Frontend

### Action: 
 * `C` for create event
 * `R` for retrieve all events
 * `U` for update an event
 * `D` for delete an event
 * `Q` for rsvp an event

### Request methods and templates 
 - Request Body
```
{
    "Token": str <REQUIRED>,
    "Action": str <REQUIRED>,
    "EventSubject": str / null if action = R ,
    "EventBody": str / null if action = R, D, Q ,
    "Location": str / null if action = R, D, Q ,
    "Date": str / null if action = R, D, Q ,
    "Time": str / null if action = R, D, Q,
    "RSVP": str / null if action = C, R, U, D
}
```
 - Response Body
 ```
{
    "statusCode": 200,
    "Status": boolean,
    "EventSubject": str / null,
    "Error": str / null,
    "Description": str,
    "EventDB": Array of dicts / null
}
```

### Route
POST to `https://0c77865x10.execute-api.us-east-1.amazonaws.com/v1/event`


### Examples
 - Create event
 ```
Request body:
{
  "Token": <Token>,
  "Action": "C",
  "EventSubject": "First event",
  "EventBody": "Hello world",
  "Location": <Location>,
  "Date": <Date>,
  "Time": <Time>,
  "RSVP": null
}

Response body:
{
  "statusCode": 200,
  "Status": <boolean>,
  "EventSubject": <Title of the event you just created>,
  "Error": str / null,
  "Description": str
}

```

 - Update event:
```
Request body:
{
  "Token": <Token>,
  "Action": "U",
  "EventSubject": "First Event",
  "EventBody": <Content to be updated>,
  "Location": <New location>,
  "Date": <New Date>,
  "Time": <New Time>,
  "RSVP": null
}

Response body:
{
  "statusCode": 200,
  "Status": <boolean>,
  "EventSubject": null,
  "Error": str / null,
  "Description": str,
  "EventsDB": null
}
```
 - Delete blog:
```
Request body:
{
  "Token": <Token>,
  "Action": "D",
  "EventSubject": "First Event",
  "EventBody": null,
  "Location": null,
  "Date": null,
  "Time": null,
  "RSVP": null
}

Response body:
{
  "statusCode": 200,
  "Status": <boolean>,
  "BlogSubject": null,
  "Error": str / null,
  "Description": str,
  "EventsDB": null
}
```
 - RSVP to an event:
```
Request body:
{
  "Token": <Token>,
  "Action": "Q",
  "EventSubject": "First Event",
  "EventBody": null,
  "Location": null,
  "Date": null,
  "Time": null,
  "RSVP": "RSVP to the event"
}

Response body:
{
  "statusCode": 200,
  "Status": <boolean>,
  "EventSubject": null,
  "Error": str / null,
  "Description": str,
  "EventsDB": null
}
```
 - Get all Events:
```
Request body:
{
  "Token": <Token>,
  "Action": "R",
  "EventSubject": null,
  "EventBody": null,
  "Location": null,
  "Date": null,
  "Time": null,
  "RSVP": null
}

Response body:
{
  "statusCode": 200,
  "Status": <boolean>,
  "EventSubject": null,
  "Error": str / null,
  "Description": "All Events from database",
  "EventDB": [dicts]
}
```