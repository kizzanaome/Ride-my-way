import unittest
from unittest import TestCase
from app.rides.models import Ride, rides_list, RequestForRide,requests


class TestRideViews(unittest.TestCase):

    def test_add_ride(self):
        self.assertEqual(len(rides_list),0)
        ride= Ride(1,"name","origin","destination")
        ride.create_ride()
        self.assertEqual(len(rides_list),1)

class TestRequestsForRides(unittest.TestCase):

    def test_create_requests(self):
        self.assertEqual(len(requests),0)
        request= RequestForRide(1,"ride_id","name","accepted")
        request.create_request()
        self.assertEqual(len(requests),1)
        

    




    