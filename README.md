# Primary Key = event_name

# Create Event - Request method type: POST
FOR / create-event, 
{
    "Event_name": {Event_name},
    "Event_date": {Event_date},
    "Event_time": {Event_time},
    "User": {User}
    "Event_desc": {Event_desc}
    "Event_image": {Event_image}
    "Event_location": {Event_location}
    "Online": {Online}
}

## Response will be
{
    "Result": True,
    "Error": None,
    "description": "Event was created succesfully",
    "Primary_key":  Event_name
}

else
{
    "Results": False,
    "Error": "event was not created"
}

# Delete Event - Request method type: POST
FOR /delete,
{
    "Event_name": {Event_name}
}

## Response will be
{
    "Result": True,
    "Error": None,
    "description": "event was deleted"
}

# Update Event- Request method type: POST
FOR /update,
{
    "Event_name": {Event_name},
    "New_Event_date": {New_Event_date},
    "New_Event_time": {New_Event_time},
    "New_User": {New_User},
    "New_Event_desc": {New_Event_desc},
    "New_Event_image": {New_Event_image},
    "New_Event_location": {New_Event_location},
    "New_Online": {New_Event_desc}
}

## Response will be
{
    "Primary Key": primary_key,
    "Error": None,
    "description": "Event was updated"
}

# View Event - Request method type: GET
FOR /view,
{
    res = event.view()
    return res
}

# RSVP Event - Request method type: GET
FOR /rsvp
{
    'event_name':Event_name,
}

## Response will be
{
    "Result": True,
    "Error": None,
    "Description": "RSVP was updated succesfully",
    "BlogName": None
}
