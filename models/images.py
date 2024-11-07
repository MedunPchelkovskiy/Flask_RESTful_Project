from datetime import datetime, timezone

from db import db


class ImageModel(db.Model):
    __tablename__ = "images"

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)
    image_uploading_date_time = db.Column(
        db.DateTime, default=datetime.utcnow()        # now(timezone.utc)
    )
    image_to_project = db.Column(
        db.Integer, db.ForeignKey("projects.id"), nullable=False
    )
    project = db.relationship("ProjectModel", back_populates="project_images")
