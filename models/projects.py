from datetime import datetime, timezone

from db import db


class ProjectModel(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(255), nullable=False)
    project_description = db.Column(db.Text, nullable=False)
    project_creation_date_time = db.Column(
        db.DateTime, default=datetime.utcnow()                          # now(timezone.utc)
    )
    project_last_update_date_time = db.Column(db.DateTime, nullable=True)
    project_views_counter = db.Column(db.Integer, default=0)
    project_author = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    project_images = db.relationship(
        "ImageModel", back_populates="project", lazy="dynamic", cascade="all, delete"
    )
    # user = db.relationship('UserModel')
