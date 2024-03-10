import os
import uuid

from constants import TEMP_FILES_PATH
from db import db
from helpers.working_with_files import decode_photo
from managers.authentication import auth
from serices.cloudinary_services import ImagesOnCloud


class ImagesManager:
    @staticmethod
    def upload_image(data):
        current_user = auth.current_user()
        complaint_data['user_id'] = current_user.id
        # Преди да създадем оплакване трябва да качим снимката и да вземем само пътя от облака,
        # който да запазим в базата данни!
        photo_name = f'{str(uuid.uuid4())}.{complaint_data.pop("photo_extension")}'
        path_to_store_photo = os.path.join(TEMP_FILES_PATH, photo_name)
        photo_as_string = complaint_data.pop(
            'photo')  # фронт енд-а ни подава снимката като стринг(base64, to convert jpg => string,
        decode_photo(path_to_store_photo,
                     photo_as_string)  # запазваме я временно на сървъра и след това се качва на облака

        try:
            ImagesOnCloud.upload_image(path_to_store_photo, photo_name)
            current_photo_url = ImagesOnCloud.get_asset_info(photo_name)
        except Exception as ex:
            raise Exception('Failed to upload file')
        finally:
            os.remove(path_to_store_photo)

        complaint_data['photo_url'] = current_photo_url
        complaint = ComplaintsModel(**complaint_data)

        full_name = f'{current_user.first_name} {current_user.last_name}'
        amount = complaint_data['amount']
        iban = current_user.iban

        db.session.add(complaint)
        db.session.flush()

        complaint_id = complaint.id
        transfer = ComplaintManager.issue_transaction(amount, full_name, iban, complaint_id)

        db.session.add(transfer)
        db.session.flush()
        db.session.commit()
        return complaint
