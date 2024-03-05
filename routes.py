from resources.authentication import UserRegisterResource, UserLoginResource
from resources.forum import TopicsResource, PostResource, TopicResource
from resources.projects import GetBestProjectsResource, ProjectsResource

routes = (
    (GetBestProjectsResource, '/'),
    (ProjectsResource, '/projects'),
    (UserRegisterResource, '/signup'),
    (UserLoginResource, '/signin'),
    (TopicsResource, '/forum'),
    (TopicResource, '/topic/<int:pk>'),
    (PostResource, '/post'),

)
