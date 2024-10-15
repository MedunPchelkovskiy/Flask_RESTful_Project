from flask import request
from werkzeug.exceptions import BadRequest


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
