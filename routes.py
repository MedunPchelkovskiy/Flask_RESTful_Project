from resources.authentication import UserRegisterResource, UserLoginResource
from resources.forum import TopicsResource, PostResource, TopicResource

# from resources.images import FileResource

routes = (
    (UserRegisterResource, '/signup'),
    (UserLoginResource, '/signin'),
    (TopicsResource, '/forum'),
    (TopicResource, '/topic/<int:pk>'),
    (PostResource, '/post'),

)
