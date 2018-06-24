from flask import Flask, render_template
from flask_restful import Resource, Api,abort

 
"""
    global variables rides_list and requests which will hold rides,ride_requests, 
    respectively,the are initially empty.

"""
rides_list = []
requests = []


class Ride():
    def __init__(self, ride_id,name,origin, destination):
        """
            The class "constructor" - It's actually an initializer

        """
        self.ride_id = ride_id
        self.name = name
        self.origin = origin
        self.destination = destination

    def create_ride(self):
        """
             method creates and returns a dictionary 
        """

        ride = {
            "ride_id": self.ride_id,
            "name": self.name,
            "origin": self.origin,
            "destination": self.destination
        }

        rides_list.append(ride)

        return ride

class RequestForRide():
    def __init__(self, request_id, ride_id, Passenger_name, accepted=False):
        self.request_id=request_id
        self.ride_id=ride_id
        self.Passenger_name=Passenger_name
        self.accepted=accepted

    def create_request(self):
        request={
            "request_id":self.request_id,
            "ride_id":self.ride_id,
            "Passenger_name":self.Passenger_name,
            "accepted":self.accepted
        }

        requests.append(request)
        return request