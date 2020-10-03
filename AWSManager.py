import boto3



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
                self.columns[0]: Event_name,
                self.columns[1] : Event_date,
                self.columns[2] : Event_time,
                self.columns[3] : User,
                self.columns[4] : Event_desc,
                self.columns[5] : Event_image,
                self.columns[6] : Event_location
            }
        )

        print(response["ResponseMetadata"]["HTTPStatusCode"])
        
#t1 = events() 
#t1.put("Event_name", "Event_desc", "Date_time", "Price", "Address", "Virtual")