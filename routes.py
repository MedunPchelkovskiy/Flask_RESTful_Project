from resources.authentication import UserRegisterResource, UserLoginResource, UserRegisterEmailConfirmationResource
from resources.forum import TopicsResource, PostsResource, TopicResource, PostResource
from resources.images import ImagesResource
from resources.projects import GetBestProjectsResource, ProjectsResource, ProjectResource
from resources.user import UserResource

routes = (
    (UserRegisterResource, '/signup'),
    (UserRegisterEmailConfirmationResource, '/confirm/<token>'),
    (UserLoginResource, '/signin'),
    (GetBestProjectsResource, '/'),
    (ProjectsResource, '/projects'),
    (ProjectResource, '/project/<int:pk>'),
    (ImagesResource, '/image'),
    (TopicsResource, '/forum'),
    (TopicResource, '/topic/<int:pk>'),
    (PostsResource, '/post'),
    (PostResource, '/post/<int:pk>'),
    (UserResource, '/user/<int:pk>'),
)
