Portfolio App

The goal of the project is to create a portfolio site and a forum for it.
The idea is to share the creativity of both artists and technically oriented projects.



    User Authentication: User registration, login. Account creation is confirmed via email.
    Project Management: After registering a profile, the user has the opportunity to create his own projects,
    add a short description, photos and a category to each one,
    he can also create new topics in the forum and comment on existing ones.
    File Management: Save files in the cloud via the Cloudinary service.
    Email Management: Send confirmation emails via Gmail API Service.

Prerequisites

    Python 3.12
    PostgreSQL (or a configured database compatible with SQLAlchemy)

    Create a virtual environment (recommended):

        python3 -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate

    Install the dependencies:

        pip install -r requirements.txt

    Set up environment variables: Create a .env file in the root directory and add the following:

DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_db_name
ENVIRONMENT=DevelopmentEnvironment  # or ProductionEnvironment
SECRET_KEY=your_secret_key
CLOUDINARY_URL=your_cloudinary_url
SECURITY_PASSWORD_SALT = your_password_salt
EMAIL_USER=your_email_address
SCOPES='https://mail.google.com/'
MAIL_DEFAULT_SENDER = "noreply@mail.com"

Configuration

The application configuration is handled through environment-based classes in config.py:

    DevelopmentEnvironment: For local development with debug mode enabled.
    ProductionEnvironment: For deployment with debug mode disabled.

Set the environment using the .env file.
Usage

    Run the application

    flask run

        Access the application: Open a web browser and go to http://127.0.0.1:5000.

Database Setup

    Initialize the database:

        flask db init

    Apply migrations:

        flask db migrate -m "Initial migration"
        flask db upgrade

Models

    The application uses SQLAlchemy models for the following entities:

        UserModel: Stores user information and credentials.
        ProjectModel: Represents different types of projects available.
        ImageModel: Stores image information-image link, project relation.
        TopicModel: Stores topic information-topic name, author, category.
        PostModel: Stores info for every post, which topic it belongs to, author and date.


API Endpoints

        POST /signin - public
        POST /signup - public
        GET /        - public, view the projects in descending order starting with
            those with the highest number of views
        GET /projects - login required; rights: user; create new project
        PUT /project/<int:pk> - login required; rights: user; update project
        DELETE /project/<int:pk> - login required; rights: user; delete project
        POST /project/<int:pk>/image - login required; rights: user; upload image to project
        GET /forum - public, view all topics in forum
        POST /forum - login required; rights: user; create new topic in forum
        GET /forum/topic/<int:pk> - public, get single topic with all posts
        PUT /forum/topic/<int:pk> - login required; rights: user; edit topic name
        DELETE /forum/topic/<int:pk> - login required; rights: moderator; delete topic from forum
        POST /forum/topic/<int:pk>/post - login required; rights: user; create new post to topic
        PUT /post/<int:pk> - login required; rights: user; edit post
        DELETE /post/<int:pk> - login required; rights: moderator; delete post
        GET /user/<int:pk> - login required; get user information

Contributing

    Fork the repository.

    Create a new branch (git checkout -b feature/your-feature-name).

    Commit your changes (git commit -m 'Add some feature').

    Push to the branch (git push origin feature/your-feature-name).

    Create a new Pull Request.
