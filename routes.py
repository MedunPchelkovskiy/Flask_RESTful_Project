from resources.authentication import (UserLoginResource,
                                      UserRegisterEmailConfirmationResource,
                                      UserRegisterResource)
from resources.forum import (PostResource, PostsResource, TopicResource,
                             TopicsResource)
from resources.images import ImagesResource
from resources.projects import (GetBestProjectsResource, ProjectCreateResource,
                                ProjectResource)
from resources.user import UserResource

routes = (
    (UserRegisterResource, "/signup"),
    (UserRegisterEmailConfirmationResource,"/confirm/<token>",),  # confirmation link from email get method not allowed for requested method!!!
    (UserLoginResource, "/signin"),
    (GetBestProjectsResource, "/"),
    (ProjectCreateResource, "/projects"),
    (ProjectResource, "/project/<int:pk>"),
    (ImagesResource, "/image"),
    (TopicsResource, "/forum"),
    (TopicResource, "/forum/topic/<int:pk>"),
    (PostsResource, "/post"),
    (PostResource, "/post/<int:pk>"),
    (UserResource, "/user/<int:pk>"),
)
