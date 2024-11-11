from flask import request
from flask_restful import Resource

from helpers.decorators import validate_schema
from managers.authentication import auth
from managers.images import ImagesManager
from managers.projects import ProjectManager, ProjectsManager
from schemas.request.projects import (CreateProjectRequestSchema,
                                      UpdateProjectRequestSchema)
from schemas.response.projects import (CreateProjectResponseSchema,
                                       GetProjectWithImagesResponseSchema,
                                       UpdateProjectResponseSchema)


class ProjectCreateResource(Resource):
    @auth.login_required
    @validate_schema(CreateProjectRequestSchema)
    def post(self):
        data = request.get_json()
        project = ProjectsManager.create_project(data)
        if data["project_images"]:
            image = ImagesManager.upload_image(data, project.id)
        return CreateProjectResponseSchema().dump(project), 201


class GetBestProjectsResource(Resource):
    @staticmethod
    def get():
        projects = ProjectManager.get_all_projects()
        return GetProjectWithImagesResponseSchema(many=True).dump(projects)


class ProjectResource(Resource):
    @staticmethod
    @auth.login_required
    def get(pk):
        project = ProjectManager.get_single_project(pk)
        return GetProjectWithImagesResponseSchema().dump(project)

    @staticmethod
    @auth.login_required
    @validate_schema(UpdateProjectRequestSchema)
    def put(pk):
        data = request.get_json()
        project = ProjectManager.get_project_to_update(pk)
        updated_project = ProjectManager.update_project(data, project)
        key_to_check = "project_images"
        if key_to_check in data:
            ImagesManager.upload_image(data, project.id)

        return UpdateProjectResponseSchema().dump(updated_project), 201

    @staticmethod
    @auth.login_required
    def delete(pk):
        project = ProjectManager.get_single_project(pk)
        project_to_delete = ProjectManager.delete_project(project)

        return "Project was successfully deleted"  # Try to replace "Project" with name of the project"
