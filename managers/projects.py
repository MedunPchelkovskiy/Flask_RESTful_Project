from datetime import datetime

from werkzeug.exceptions import BadRequest

from db import db
from managers.authentication import auth
from models import ProjectModel


class ProjectsManager:

    @staticmethod
    def create_project(data):
        current_user = auth.current_user()
        data["project_author"] = current_user.id
        project = ProjectModel(**data)
        db.session.add(project)
        db.session.commit()
        return project


class ProjectManager:
    @staticmethod
    def get_all_projects():
        projects = ProjectModel.query.order_by(ProjectModel.project_views_counter).all()
        return projects

    @staticmethod
    def get_single_project(project_id):
        project = ProjectModel.query.filter_by(id=project_id).first()
        if not project:
            raise BadRequest("Project with this id does not exist")
        project.project_views_counter += 1
        db.session.commit()
        return project

    @staticmethod
    def get_project_to_update(project_id):
        project = ProjectModel.query.get(project_id)
        if not project:
            raise BadRequest("Project with this id does not exist")
        return project

    @staticmethod
    def update_project(data, project):
        current_user = auth.current_user()
        if project.project_author == current_user.id:
            if project.project_name != data["project_name"]:
                project.project_name = data["project_name"]
            if project.project_description != data["project_description"]:
                project.project_description = data["project_description"]
            project.project_last_update_date_time = datetime.utcnow()
            db.session.commit()
        return project

    @staticmethod
    def delete_project(project):
        current_user = auth.current_user()
        if project.project_author == current_user.id:
            db.session.delete(project)
            db.session.commit()
        return
