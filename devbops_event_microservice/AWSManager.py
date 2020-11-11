import boto3
from boto3.dynamodb.conditions import Key, Attr

class Events:
    def __init__(self):
        self.__Tablename__ = "devbops_events"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "event_name"
        # self.Primary_key = 1
        self.columns = ["Event_date", "Event_time", "User", "Event_desc", "Event_image", "Event_location", "Online",
                        "RSVP"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location, Online, RSVP):

        response = self.table.put_item(
            Item={
                self.Primary_Column_Name: Event_name,
                self.columns[0]: Event_date,
                self.columns[1]: Event_time,
                self.columns[2]: User,
                self.columns[3]: Event_desc,
                self.columns[4]: Event_image,
                self.columns[5]: Event_location,
                self.columns[6]: Online,
                self.columns[7]: RSVP
            }
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {
                "Result": True,
                "Error": None,
                "Description": "Event was created successfully",
                "EventName": Event_name
            }
        else:
            return  {
                "Result": False,
                "Error": "Event was not created",
                "Description": "Database error",
                "EventName": None
            }

    def check_if_event_exists(self, Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location,
                              Online, RSVP):
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(Event_name)
        )
        # print(response["Items"])
        if response["Items"]:
            return {
                "Result": False,
                "Error": "Event was not created",
                "Description": "Event already exists",
                "EventName": None
            }

        res = self.put(Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location, Online, RSVP)

        return res

    def update_event(self, Event_name, New_Event_date, New_Event_time,  New_Event_desc, New_Event_image,
                     New_Event_location, New_Online):
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(Event_name)
        )
        if len(response["Items"]) > 0:
            self.table.update_item(
                Key={
                    'event_name': Event_name
                },
                UpdateExpression="set Event_date=:d, Event_desc=:c, Event_location=:l, Event_image=:i ,Event_time=:t, #ol=:z",
                ExpressionAttributeValues={
                    ':d': New_Event_date,
                    ':c': New_Event_desc,
                    ':l': New_Event_location,
                    ':t': New_Event_time,
                    ':z': New_Online,
                    ':i': New_Event_image
                },
                ExpressionAttributeNames={
                    "#ol": "Online"
                }
            )

            return {
                "Result": True,
                "Error": None,
                "Description": "Event was updated"
            }
        else:

            return {
                "Result": False,
                "Error": "DB error",
                "Description": "Event does not exist in our database"
            }


    def delete(self, Event_name):
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(Event_name)
        )
        if len(response["Items"]) > 0:
            print(response["Items"])
            res = self.table.delete_item(
                Key={
                    self.Primary_Column_Name: Event_name
                }
            )
            return {
                "Result": True,
                "Error": None,
                "Description": "event was deleted"
            }
        else:
            #print("item does not exists")
            return {
                "Result": False,
                "Error": "Deletion error",
                "Description": "Event not exists"
            }

    def view(self):
        res = self.table.scan()
        # print(res['Items'])
        return {
            "Result": True,
            "Error": None,
            "Description": "All events from database",
            "EventsDB": res['Items']
        }

        # return res['Items']

    def rsvp(self, User, Event_name):
        #print(User)
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(Event_name)
        )



        if response["Items"]:

            if User in response['Items'][0]['RSVP']:
                return {
                    "Result": False,
                    "Error": "Database error",
                    "Description": "Cannot RSVP more than once"
                }

            res = self.table.update_item(
                Key={
                    'event_name': Event_name,

                },

                UpdateExpression="set RSVP= list_append(RSVP, :s)",
                ExpressionAttributeValues={
                    ':s': [User]
                }
                #
            )
            # return res
            if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return {
                    "Result": True,
                    "Error": None,
                    "Description": "RSVP was updated successfully"
                }
            else:
                return {
                    "Result": False,
                    "Error": "Database error",
                    "Description": "Database error"
                }
        else:
            return {
                "Result": False,
                "Error": "Event not found",
                "Description": "Cannot add rsvp"
            }

    def getAllUserEvent(self, username):
        response = self.table.scan()['Items']
        lst = []
        if len(response) > 0:
            for d in response:
                if d['User'] == username:
                    lst.append(d)
            return {
                "Result": True,
                "Error": None,
                "Description": "All events this user created",
                "EventsDB": lst
            }
        else:
            return {
                "Result": False,
                "Error": "No blogs for this user",
                "Description": "This user haven't post any event yet.",
                "EventsDB": lst
            }

    def getUserRvsp(self, username):
        # get current user's rvsp
        lst = []
        response = self.table.scan()['Items']
        for i in response:
            if username in i['RSVP']:
                lst.append(i)

        return {
            "Result": True,
            "Error": None,
            "Description": "All RSVP for this user",
            "RSVP": lst
        }
        #return response
    def cancelRsvp(self, username, eventname):
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(eventname)
        )
        try:
            idx = response['Items'][0]['RSVP'].index(username)
        except:
            return {
                "Result": False,
                "Error": "User not found",
                "Description": "User haven't make RSVP to this event yet"
            }

        if response["Items"]:
            statement = "REMOVE RSVP["+ str(idx)+ "]"

            res = self.table.update_item(
                Key={
                    'event_name': eventname,

                },

                UpdateExpression=statement,

            )
            # return res
            if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return {
                    "Result": True,
                    "Error": None,
                    "Description": "RSVP was cancelled successfully"
                }
            else:
                return {
                    "Result": False,
                    "Error": "Database error",
                    "Description": "Database error"
                }
        else:
            return {
                "Result": False,
                "Error": "Event not found",
                "Description": "Cannot cancel rsvp because event not found"
            }


# test = Events()
# test.rsvp("Anish", "Hi")
if __name__ == "__main__":
    test = Events()
    #print(test.rsvp("hrgutou1", "easdfvent 2"))
    #print(test.getAllUserEvent("user12"))
    #print(test.update_event(Event_name='event 2', New_Event_date='Friday Oct 16th 2020', New_Event_time='12:17 am',  New_Event_desc='updated', New_Event_image="",
    #                New_Event_location="NY", New_Online="Onsite"))
    #test.getUserRvsp("hrgutou1")
    #print(test.getUserRvsp("hrgutou"))
    #print(test.cancelRsvp("hrgutou", "event 2"))
    #print(test.cancelRsvp("user21","event 2"))
    print(test.rsvp("hrgutou1", 'event 2'))