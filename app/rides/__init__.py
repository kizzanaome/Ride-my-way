"""
Ride Application
"""

from flask import Blueprint
from flask_restful import Api
from .import views
from app.rides.views import (RidesView, SingleRideView,RideRequest)


rides = Blueprint('rides', __name__, url_prefix='/api/v1')
ride_api =Api(rides)


ride_api.add_resource(RidesView, '/rides')
ride_api.add_resource(SingleRideView, '/rides/<int:ride_id>')
ride_api.add_resource(RideRequest, '/rides/<int:ride_id>/requests')




