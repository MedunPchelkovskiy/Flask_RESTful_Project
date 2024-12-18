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
    (
        UserRegisterEmailConfirmationResource,
        "/confirm/<token>",
    ),
    (UserLoginResource, "/signin"),
    (GetBestProjectsResource, "/"),
    (ProjectCreateResource, "/projects"),
    (ProjectResource, "/project/<int:pk>"),
    (ImagesResource, "/project/<int:pk>/image"),
    (TopicsResource, "/forum"),
    (TopicResource, "/forum/topic/<int:pk>"),
    (PostsResource, "/forum/topic/<int:pk>/post"),
    (PostResource, "/post/<int:pk>"),
    (UserResource, "/user/<int:pk>"),
)
