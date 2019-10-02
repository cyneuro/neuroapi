from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from webargs import fields, validate
from webargs.flaskparser import use_args, use_kwargs, parser, abort

import neuroapi.neuro.core as neurocore

class FunctionResource(Resource):

    #UNCOMMENT FOR REQUIRED AUTHENTICATION
    #method_decorators = [jwt_required] 
    base_directory = "neuroapi.api.neuro."

    query_args = {
    'function': fields.Str(required=True),
    'params': fields.Dict(required=True)
    }
   
    @use_args(query_args)
    def post(self,args):
        return self.call_function(args["function"], args["params"])

    @use_args(query_args)
    def get(self,args):
        return self.call_function(args["function"], args["params"])

    def call_function(self,function,params):
        function_call = "neurocore."+function
        func = eval(function_call)
        try:
            ret = func(**params)
        except Exception as e:
            return {"error":str(e)}, 400
        return {"result":ret}, 200