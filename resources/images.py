from flask import request
from flask_restful import Resource

from helpers.decorators import validate_schema
from managers.authentication import auth
from managers.images import ImagesManager
from schemas.request.images import UploadImageRequestSchema
from schemas.response.images import UploadImageResponseSchema


class ImagesResource(Resource):
    @validate_schema(UploadImageRequestSchema)
    @auth.login_required
    def post(self):
        data = request.get_json()
        image = ImagesManager.upload_image(data)
        return UploadImageResponseSchema().dump(image), 201
