import unittest
import json
from datetime import date, datetime
from devbops_event_microservice import app


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
        assert data['Result'] == True

    def test_2_posting(self):
        req = {
            "Event_name": "QATesting",
            "Event_date": date.today().strftime("%B %d, %Y"),
            "Event_time": datetime.now(),
            "User": "QATest",
            "Event_desc": "Test",
            "Event_image": "None",
            "Event_location": "Anywhere, USA",
            "Online": "Yes"
        }

        rv = self.app.post('/create-event', json=req)
        data = json.loads(rv.data)
        assert data['Result'] == True

    # Result should be false
    def test_3_DUPLICATE_posting(self):
        req = {
            "Event_name": "QATesting",
            "Event_date": date.today().strftime("%B %d, %Y"),
            "Event_time": datetime.now(),
            "User": "QATest",
            "Event_desc": "Test",
            "Event_image": "None",
            "Event_location": "Anywhere, USA",
            "Online": "Yes"
        }

        rv = self.app.post('/create-event', json=req)
        data = json.loads(rv.data)
        assert data['Result'] == False

    def test_4_update(self):
        req = {
            "Event_name": "QATesting",
            "New_Event_date": date.today().strftime("%B %d, %Y"),
            "New_Event_time": datetime.now(),
            "New_User": "QATest",
            "New_Event_desc": "Test Number 2",
            "New_Event_image": "None",
            "New_Event_location": "Anywhere, USA",
            "New_Online": "Yes"
        }
        rv = self.app.post('/event-update', json=req)
        data = json.loads(rv.data)
        assert data['Results'] != False
       

    def test_5_NONEXIST_udpate(self):
        req = {
            "Event_name": "__QATesting",
            "New_Event_date": date.today().strftime("%B %d, %Y"),
            "New_Event_time": datetime.now(),
            "New_User": "QATest",
            "New_Event_desc": "Test Number 2",
            "New_Event_image": "None",
            "New_Event_location": "Anywhere, USA",
            "New_Online": "Yes"
        }
        rv = self.app.post('/event-update', json=req)
        data = json.loads(rv.data)
        assert data['Results'] == False

    # def test_6_rsvp(self):
    #     req = {
    #         "Event_name": "QA_Testing"
    #     }
    #     rv = self.app.post('/event-rsvp', json=req)
    #     data = json.loads(rv.data)
    #     assert data['Result'] == True

    def test_9_deleting(self):
        req = {
            "Event_name": "QATesting"
        }

        rv = self.app.post('/event-delete', json=req)
        data = json.loads(rv.data)
        assert data['Result'] == True

    # Result should be false
    def test_10_NONEXIST_deleting(self):
        req = {
            "Event_name": "QATesting"
        }

        rv = self.app.post('/event-delete', json=req)
        data = json.loads(rv.data)
        assert data['Result'] == False



if __name__ == '__main__':
    unittest.main()