from resources.authentication import UserRegisterResource, UserLoginResource
# from resources.images import FileResource

routes = (
    (UserRegisterResource, '/signup'),
    (UserLoginResource, '/signin'),
    # (UserLoginResource, '/topic'),
)
