def clean_data_for_image(image_data):
    if image_data["project_name"]:
        image_data.pop("project_name")
    if image_data["project_description"]:
        image_data.pop("project_description")
    if image_data["project_author"]:
        image_data.pop("project_author")
