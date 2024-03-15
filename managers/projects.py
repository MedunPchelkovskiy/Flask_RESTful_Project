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
    def get_single_project(project_id):
        project = ProjectModel.query.filter_by(id=project_id)
        return project
