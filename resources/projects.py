from flask_restful import Resource

from helpers.decorators import validate_schema
from managers.authentication import auth
from flask import request

from managers.projects import ProjectsManager, ProjectManager
from schemas.request.projects import CreateProjectRequestSchema
from schemas.response.projects import CreateProjectResponseSchema, GetProjectWithImagesResponseSchema


class ProjectsResource(Resource):
    @validate_schema(CreateProjectRequestSchema)
    @auth.login_required
    def post(self):
        data = request.get_json()
        project = ProjectsManager.create_project(data)
        return CreateProjectResponseSchema().dump(project), 201


class GetBestProjectsResource(Resource):
    pass


class ProjectResource(Resource):
    @staticmethod
    def get(pk):
        project = ProjectManager.get_single_project(pk)
        return GetProjectWithImagesResponseSchema(many=True).dump(project)

    @staticmethod
    def put(pk):
        pass

    @staticmethod
    def delete(pk):
        pass
