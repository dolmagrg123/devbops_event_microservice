import unittest
import json
from devbops_event_microservice import app
from datetime import date, datetime


class BasicTestCase(unittest.TestCase):

    def setUp(self):
        unittest.TestLoader.sortTestMethodsUsing = None
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_1_viewing(self):
        rv = self.app.get('/event-view')
        data = json.loads(rv.data)
        #print(data['Status'], data['Error'])
        assert data['Result'] == True

    def test_2_creating(self):
        req = {
            'Event_name': "QA_TEST",
            'Event_date': date.today().strftime("%B %d, %Y"),
            'Event_time': datetime.now(),
            'User': "username",
            'Event_desc': "Event_desc",
            'Event_image': "Event_image",
            'Event_location': "Event_location",
            'Online': "Online"
        }

        rv = self.app.post('/create-event', json=req)
        data = json.loads(rv.data)
        #print(data['Status'], data['Error'])
        print(data)
        assert data['Result'] == True

    def test_3_update(self):
        req = {
            'Event_name':  "QA_TEST",
            'New_Event_date': date.today().strftime("%B %d, %Y"),
            'New_Event_time': datetime.now(),
            'New_User': "username",
            'New_Event_desc': "Event_desc",
            'New_Event_image': "Event_image",
            'New_Event_location': "Event_location",
            'New_Online': "Online"
        }

        rv = self.app.post('/event-update', json=req)
        data = json.loads(rv.data)
        #print(data['Status'], data['Error'])
        print(data)
        assert data['Result'] == True

    def test_4_delete(self):
        req = {
            'Event_name': "QA_TEST"
        }

        rv = self.app.post('/event-delete', json=req)
        data = json.loads(rv.data)
        #print(data['Status'], data['Error'])
        print(data)
        assert data['Result'] == True

if __name__ == '__main__':
    unittest.main()

