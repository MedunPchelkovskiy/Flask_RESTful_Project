from marshmallow import Schema, fields


class ImageResponseSchema(Schema):

    image_url = fields.String(required=True)
    image_uploading_date_time = fields.DateTime(required=True)