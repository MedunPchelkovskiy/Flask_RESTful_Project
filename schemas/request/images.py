from marshmallow import Schema, fields


class UploadImageRequestSchema(Schema):
    # image_to_project = fields.Integer(required=True)
    # image_extension = fields.String(required=True)
    image = fields.String(required=True)
