import boto3
from boto3.dynamodb.conditions import Key, Attr



class Events:
    def __init__(self):
        self.__Tablename__ = "devbops_events"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "event_name"
        self.Primary_key = 1
        self.columns = ["Event_name", "Event_date", "Event_time", "User", "Event_desc", "Event_image", "Event_location"]
        self.table = self.DB.Table(self.__Tablename__)

    def put(self, Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location):

        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name: Event_name,
                self.columns[0] : Event_date,
                self.columns[1] : Event_time,
                self.columns[2] : User,
                self.columns[3] : Event_desc,
                self.columns[4] : Event_image,
                self.columns[5] : Event_location
            }
        )

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

    def check_if_event_exists(self, Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location):
        response = self.table.scan(
            FilterExpression=Attr("Event_name").eq(Event_name)
        )
        print(response["Items"])
        if response["Items"]:
            print("it exists")
            return {
                "Result": False,
                "Error": "Event already exists"
            }
            
        else:
            self.put(Event_name, Event_date, Event_time, User, Event_desc, Event_image, Event_location)
            

    def update_event(self, Event_name, New_Event_date, New_Event_time, New_User,  New_Event_desc,  New_Event_image, New_Event_location ):
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
                    self.columns[5] : New_Event_location

                }
            )
            return{
                "Primary Key": primary_key,
                "Error": None,
                "description": "Event was updated"
            }

        else:

            print(response["Items"])
            return{
                "Results": False,
                "Error": "Event does not exist in our database"
            }


    def delete(self, Event_name):
        response = self.table.scan(
            FilterExpression=Attr("event_name").eq(Event_name)
        )

        if len(response["Items"]) > 0:
            print(response["Items"])
            res = self.table.delete_item(
                 Key={
                     self.Primary_Column_Name:Event_name

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
    def view(self):
        res = self.table.scan()
        return res['Items']

    def rsvp(self, User):
        return res


t1 = Events()
# t1.check_if_event_exists(Event_name = "cams listening party", Event_date = "to delete", Event_time ="to delete", User ="to delete", Event_desc = "Morbi consequat enim sit amet lacus pretium auctor. Nam porta molestie accumsan. Etiam condimentum tempus pretium. Phasellus mauris magna, convallis eu mollis nec, ultrices sed massa. Fusce rutrum porta condimentum. Sed ultricies, velit nec egestas porta, justo lectus accumsan purus, et euismod justo eros vitae mi. Nulla ac imperdiet ex. Integer eu ante egestas, interdum nisi ut, vulputate augue. Praesent vulputate libero sed libero accumsan tempus. Aenean rutrum felis tellus, pharetra luctus massa gravida sit amet. Phasellus sodales tempus magna, a porttitor enim ornare vel. Maecenas faucibus dictum elit, id lacinia nunc. Quisque lacus ligula, pulvinar id nunc ac, ornare semper neque. Praesent nec ipsum risusMorbi consequat enim sit amet lacus pretium auctor. Nam porta molestie accumsan. Etiam condimentum tempus pretium. Phasellus mauris magna, convallis eu mollis nec, ultrices sed massa. Fusce rutrum porta condimentum. Sed ultricies, velit nec egestas porta, justo lectus accumsan purus, et euismod justo eros vitae mi. Nulla ac imperdiet ex. Integer eu ante egestas, interdum nisi ut, vulputate augue. Praesent vulputate libero sed libero accumsan tempus. Aenean rutrum felis tellus, pharetra luctus massa gravida sit amet. Phasellus sodales tempus magna, a porttitor enim ornare vel. Maecenas faucibus dictum elit, id lacinia nunc. Quisque lacus ligula, pulvinar id nunc ac, ornare semper neque. Praesent nec ipsum risus", Event_image ="to delete", Event_location = "to delete")
t1.update_event(Event_name = "cams listening party", New_Event_date = "xz", New_Event_time ="xz", New_User ="to delete", New_Event_desc = "Morbi consequat enim sit amet lacus pretium auctor. Nam porta molestie accumsan. Etiam condimentum tempus pretium. Phasellus mauris magna, convallis eu mollis nec, ultrices sed massa. Fusce rutrum porta condimentum. Sed ultricies, velit nec egestas porta, justo lectus accumsan purus, et euismod justo eros vitae mi. Nulla ac imperdiet ex. Integer eu ante egestas, interdum nisi ut, vulputate augue. Praesent vulputate libero sed libero accumsan tempus. Aenean rutrum felis tellus, pharetra luctus massa gravida sit amet. Phasellus sodales tempus magna, a porttitor enim ornare vel. Maecenas faucibus dictum elit, id lacinia nunc. Quisque lacus ligula, pulvinar id nunc ac, ornare semper neque. Praesent nec ipsum risusMorbi consequat enim sit amet lacus pretium auctor. Nam porta molestie accumsan. Etiam condimentum tempus pretium. Phasellus mauris magna, convallis eu mollis nec, ultrices sed massa. Fusce rutrum porta condimentum. Sed ultricies, velit nec egestas porta, justo lectus accumsan purus, et euismod justo eros vitae mi. Nulla ac imperdiet ex. Integer eu ante egestas, interdum nisi ut, vulputate augue. Praesent vulputate libero sed libero accumsan tempus. Aenean rutrum felis tellus, pharetra luctus massa gravida sit amet. Phasellus sodales tempus magna, a porttitor enim ornare vel. Maecenas faucibus dictum elit, id lacinia nunc. Quisque lacus ligula, pulvinar id nunc ac, ornare semper neque. Praesent nec ipsum risus", New_Event_image ="to delete", New_Event_location = "to delete")
# t1.delete('maybeee this will work')


