from dotenv import load_dotenv

load_dotenv()

import cloudinary
import cloudinary.uploader
import cloudinary.api

import json

config = cloudinary.config(secure = True)
# print("****1. Set up and configure the SDK:****\nCredentials: ", config.cloud_name, config.api_key, "\n")


class ImagesOnCloud:
    @staticmethod
    def upload_image(source_path, name_of_photo):
        cloudinary.uploader.upload(source_path,
                                   public_id=name_of_photo,
                                   unique_filename=True,
                                   overwrite=False)

        # src_url = cloudinary.CloudinaryImage("photo_name").build_url()
        # print("****2. Upload an image****\nDelivery URL: ", src_url, "\n")

    @staticmethod
    def get_asset_info(name_of_photo):
        image_info = cloudinary.api.resource(name_of_photo)
        return json.dumps(image_info['url'])
