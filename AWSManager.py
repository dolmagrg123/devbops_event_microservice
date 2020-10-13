import boto3
from boto3.dynamodb.conditions import Key, Attr
# ​
# ​
# ​
class Events:
    def __init__(self):
        self.__Tablename__ = "devbops_events"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "event_name"
        # self.Primary_key = 1
        self.columns = ["Event_date", "Event_time", "User", "Event_desc", "Event_image", "Event_location", "Online","RSVP"]
        self.table = self.DB.Table(self.__Tablename__)
# ​
    def put(self, Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location, Online, RSVP):

        
        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name: Event_name,
                self.columns[0] : Event_date,
                self.columns[1] : Event_time,
                self.columns[2] : User,
                self.columns[3] : Event_desc,
                self.columns[4] : Event_image,
                self.columns[5] : Event_location,
                self.columns[6] : Online,
                self.columns[7] : RSVP
            }
        )
# ​
        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {
                "Result": True,
                "Error": None,
                "description": "Event was created succesfully",
                "Primary_key":  Event_name
            }
        else:
            return {
                "Results": False,
                "Error": "event was not created"
            }
# ​
    def check_if_event_exists(self,Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location, Online,RSVP):
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(Event_name)
        )
        # print(response["Items"])
        if response["Items"]:
            print("it exists")
            return {
                "Result": False,
                "Error": "Event already exists"
            }
            
        self.put(Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location, Online,RSVP)
            
        return {
            "Result": True,
            "Error": "NONE",
            "description": "Event was created"
            }
# ​
    def update_event(self, Event_name, New_Event_date, New_Event_time, New_User,  New_Event_desc,  New_Event_image, New_Event_location, New_Online):
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(Event_name)
        )
        if len(response["Items"]) > 0:
            primary_key = response["Items"][0]['event_name']
           
            res = self.table.put_item(
                Item = {
                    self.Primary_Column_Name: primary_key,
                    self.columns[0] : New_Event_date,
                    self.columns[1] : New_Event_time,
                    self.columns[2] : New_User,
                    self.columns[3] : New_Event_desc,
                    self.columns[4] : New_Event_image,
                    self.columns[5] : New_Event_location,
                    self.columns[6] : New_Online
                }
            )
            return{
                "Primary Key": primary_key,
                "Error": None,
                "description": "Event was updated"
            }
# ​
        else:
# ​
            print(response["Items"])
            return{
                "Results": False,
                "Error": "Event does not exist in our database"
            }
# ​
# ​
    def delete(self, Event_name):
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(Event_name)
        )
# ​
        if len(response["Items"]) > 0:
            print(response["Items"])
            res = self.table.delete_item(
                 Key={
                     self.Primary_Column_Name:Event_name
# ​
                 }
             )
            return {
                 "Result": True,
                 "Error": None,
                 "description": "event was deleted"
             }
        else:
            print("item does not exists")
            return {
                "Result": False,
                "Error": "Event does not exists"
            }
# ​
    def view(self):
        res = self.table.scan()
        # print(res['Items'])
        return res['Items']
# ​
    def rsvp(self, User,Event_name):
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(Event_name)
        )
        if response["Items"]:
            res = self.table.update_item(
                Key={
                    'event_name' :Event_name,   
                        
                },
            
               UpdateExpression="set RSVP= list_append(RSVP, :i)",
               ExpressionAttributeValues={
                   ':i': [User]
               }
# ​
#    
            )
            #return res
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return {
                    "Result": True,
                    "Error": None,
                    "Description": "RSVP was updated succesfully",
                
                    "BlogName": None
                }
            else:
                return {
                    "Result": False,
                    "Error": "Database error",
                    "Description": "Database error",
                    "BlogName": None
                } 
        else:
            return {
                "Result": False,
                "Error": "Event not found",
                "Description": "Cannot add comment",
                "BlogName": None
            }


# test = Events()
# test.rsvp("Anish", "Hi")