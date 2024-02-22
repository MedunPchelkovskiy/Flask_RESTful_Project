from resources.authentication import UserRegisterResource, UserLoginResource
from resources.forum import TopicsResource

# from resources.images import FileResource

routes = (
    (UserRegisterResource, '/signup'),
    (UserLoginResource, '/signin'),
    (TopicsResource, '/topic'),
)
