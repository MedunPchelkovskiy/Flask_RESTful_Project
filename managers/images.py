import os
import uuid
from datetime import datetime

from constants import TEMP_FILES_PATH
from db import db
from helpers.working_with_files import decode_photo
from managers.projects import ProjectManager
from models import ImageModel
from serices.cloudinary_services import ImagesOnCloud


class ImagesManager:
    @staticmethod
    def upload_image(image_data):
        current_project_id = image_data["image_to_project"]
        current_project = ProjectManager.get_project_to_update(current_project_id)
        # First upload the image in cloud storage and then we get only the path and store it in the data base.

        photo_name = f"{str(uuid.uuid4())}"
        path_to_store_photo = os.path.join(
            TEMP_FILES_PATH, photo_name
        )  # Save files temporarly to server and delete it after uploading
        photo_as_string = image_data.pop(
            "image"
        )  # фронт енд-а ни подава снимката като стринг(
        # base64, to convert jpg => string
        #  )
        decode_photo(path_to_store_photo, photo_as_string)
        try:
            ImagesOnCloud.upload_image(path_to_store_photo, photo_name)
            image_url = ImagesOnCloud.get_asset_info(photo_name)
        except Exception as ex:
            raise Exception("Failed to upload file")
        finally:
            os.remove(path_to_store_photo)

        image_data["image_url"] = image_url
        image = ImageModel(**image_data)
        current_project.project_last_update_date_time = datetime.utcnow()

        db.session.add(image)
        db.session.commit()

        return image
