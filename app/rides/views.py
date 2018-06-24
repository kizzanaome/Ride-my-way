from flask import Flask, render_template, jsonify, make_response, Blueprint
from flask_restful import Resource, Api,abort,reqparse
from .models import rides_list, Ride, requests,RequestForRide


class RidesView(Resource):

    """
    returns all ride created in the list
            
    """
    def get(self):
        if not rides_list:
             return make_response(jsonify({"message":"No rides created yet"}), 204)
        return make_response(jsonify({"rides": rides_list}), 200) 

    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("origin")
        parser.add_argument('destination')
        args =parser.parse_args()

        """
        auto generating a ride id

        """
        
        if len(rides_list)==0:
            ride_id=len(rides_list)+1
        else:
            ride_id=len(rides_list)+1
        #class insatnce
        ride=Ride(ride_id,args["name"], args["origin"], args["destination"])
        ride.create_ride()

        return make_response(jsonify({"massage":"Ride has been created"}), 201)
            
        

class SingleRideView(Resource):
    def get(self, ride_id):
        ride_item=None
        for ride in rides_list:
            if (ride["ride_id"]==ride_id):
                ride_item=ride
                return make_response(jsonify({"Ride":ride_item}),200)
            
        return make_response(jsonify({"message":"item Not Found"}),404)
        
            
class RideRequest(Resource):
    def post(self, ride_id):
        parser=reqparse.RequestParser()
        #parser.add_argument("ride_id")
        parser.add_argument("Passenger_name")
        parser.add_argument("accepted")
        args=parser.parse_args()
        
        """
        auto generating a request id id
            
        """
        
        if len(requests)==0:
            request_id=len(requests)+1
        else:
            request_id=len(requests)+1
        #class insatnce
        request=RequestForRide(request_id, args["Passenger_name"], args["accepted"])
        request.create_request()
        for ride in rides_list:
            if (ride_id==ride["ride_id"]):
                return "a ride request with ride_id {} has been sent please wait for approval". format(ride_id), 201
        return make_response(jsonify(
            { "message":"The requested ride is not found in rides please request for another ride" 
            }),404)




     


            

            
        
        


        
  
       
        
       


