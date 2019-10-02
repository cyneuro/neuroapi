from flask import Blueprint, current_app
from flask_restful import Api

from neuroapi.extensions import apispec
from neuroapi.api.resources import UserResource, UserList, FunctionResource
from neuroapi.api.resources.user import UserSchema


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(FunctionResource, '/function')

@blueprint.before_app_first_request
def register_views():
    apispec.spec.components.schema("UserSchema", schema=UserSchema)
    apispec.spec.path(view=UserResource, app=current_app)
    apispec.spec.path(view=UserList, app=current_app)
    apispec.spec.path(view=FunctionResource, app=current_app)
