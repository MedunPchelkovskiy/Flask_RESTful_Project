from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.authentication import auth


def validate_schema(schema_name):
    def decorated_function(funct):
        def wrapper(*args, **kwargs):
            schema = schema_name()
            data = request.get_json()
            errors = schema.validate(data)
            if not errors:
                return funct(*args, **kwargs)
            raise BadRequest(errors)

        return wrapper

    return decorated_function


def permission_checker(role):
    def function_to_decorate(funct):
        def wrapper(*args, **kwargs):
            user_to_check = auth.current_user()
            if user_to_check.role == role:
                return funct(*args, **kwargs)
            raise Forbidden("You must have permission to do this!")

        return wrapper

    return function_to_decorate
