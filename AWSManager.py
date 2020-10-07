import boto3
from boto3.dynamodb.conditions import Attr



class Events:
    def __init__(self):
        self.__Tablename__ = "EventsDB"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "event_id"
        self.Primary_key = 1
        self.columns = ["Event_name", "Event_date", "Event_time", "User", "Event_desc", "Event_image", "Event_location"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location):
        all_items = self.table.scan()
        last_primary_key = len(all_items['Items']) + 1

        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name:last_primary_key,
                self.columns[0]: self.check_if_event_exists(Event_name),
                self.columns[1] : Event_date,
                self.columns[2] : Event_time,
                self.columns[3] : User,
                self.columns[4] : Event_desc,
                self.columns[5] : Event_image,
                self.columns[6] : Event_location
            }
        )

        if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return {
                "Result": True,
                "Error": None,
                "description": "Event was created succesfully",
                "Primary_key": last_primary_key,
                 "Event_name": Event_name,
                 " Event_date":  Event_date,
                 " Event_time":  Event_time,
                 "User": User,
                 " Event_desc": Event_desc,
                 " Event_image":  Event_image,
                 "Event_location": Event_location

            }
        else:
            return {
                "Results": False,
                "Error": "event was not created"
            }

    def check_if_event_exists(self, Event_name):
        response = self.table.scan(
            FilterExpression=Attr("Event_name").eq(Event_name)
        )
        if response["Items"]:
            return {
                "Result": False,
                "Error": "Event already exists"
            }
        else:
            return Event_name

    def update_event(self, Event_name, New_Event_name, New_Event_date, New_Event_time, New_User,  New_Event_desc,  New_Event_image, New_Event_location ):
        response = self.table.scan(
            FilterExpression=Attr("Event_name").eq(Event_name)
        )
        
        if response["Items"]:
             self.Primary_key = response["Items"][0]["event_id"]
             res = self.table.put_item(
                     Item = {
                         self.Primary_Column_Name:self.Primary_key,
                         self.columns[0]: New_Event_name,
                         self.columns[1] : New_Event_date,
                         self.columns[2] : New_Event_time,
                         self.columns[3] : New_User,
                         self.columns[4] : New_Event_desc,
                         self.columns[5] : New_Event_image,
                         self.columns[6] : New_Event_location

                     }
                 
             )

             return {
                 "Primary_key": self.Primary_key,
                 "New_Event_name": New_Event_name,
                 " New_Event_date":  New_Event_date,
                 " New_Event_time":  New_Event_time,
                 "New_User": New_User,
                 " New_Event_desc": New_Event_desc,
                 " New_Event_image":  New_Event_image,
                 "New_Event_location": New_Event_location


             }
        else:
            return {
                "Results": False,
                "Error": "event doesnt exists"
                
            }

    def delete(self, Event_name):
        response = self.table.scan(
            FilterExpression=Attr("Event_name").eq(Event_name)
        )
        if response["Items"]:
             self.Primary_key = response["Items"][0]["event_id"]
             res = self.table.delete_item(
                 Key={
                     self.Primary_Column_Name:self.Primary_key

                 }
             )
             return {
                 "Result": True,
                 "Error": None,
                 "description": "event was deleted"
             }
        else:
            return {
                "Result": False,
                "Error": "Event does not exists"
            }
    

    



        





        
t1 = Events() 
#t1.put("Event_name", "Event_desc", "Date_time", "Price", "Address", "Virtual")
# t1.put("to delete", "leave", "yall", "really", "playying", "with me", "!!")
# t1.update_event(Event_name = "i wanana",  New_Event_name = "Cams lsiting party", New_Event_date = "10-29-2020", New_Event_time="9:30", New_User = "Abdul", New_Event_desc = "listening paty", New_Event_image = "test12", New_Event_location = "Ny" )
# t1.delete("to delete")
t1.check_if_event_exists("to delet")