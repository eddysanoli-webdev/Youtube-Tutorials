# [Python Django Tutorial: Full-Featured Web App](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=2&ab_channel=CoreySchafer)<br>(Corey Schafer)

Code created while following the Youtube tutorial imparted by "Programming with Mosh". It includes many individual exercises, as well as a type of final project, which consists of an e-commerce website. Its worth mentioning that this course assumes that you already have some experience with Python and relational databases (SQL).

I decided to include my notes inside of the repository for future use and for anyone that is interested.

## Notes

### Starting Project

```bash
# Install "pipenv" package
pip install pipenv

# Move to the project directory
cd projectDirectory

# Initialize a django project
pipenv install django

# Activate the virtual environment
# (Dot at the end tells Django that the current directory is the project directory)
pipenv shell
django-admin startproject projectName .

# Run web server
# 1. python manage.py: Take the project settings into consideration when running the webserver
# 2. runserver: django-admin command
# 3. 8000: Port. Default is 8000
python manage.py runserver 8000

# Create app (website)
# (After creation make sure to add the app inside settings.py)
python manage.py createapp appName

```

### Concepts

- **IMPORTANT**: After creating an app is important to add a newly created app to the installed apps list inside `settings.py`
- **IMPORTANT**: After installing a new package inside the environment with pipenv, we need to add it inside the INSTALLED_APPS of `settings.py`.
- **IMPORTANT**: The "user" object doesnt need to be passed to a template. Its automatically passed so you can access it any time and get the data of the logged user.


- View function: Takes a request and returns a response (request handler)
- Templates Directory: When adding templates, create a "templates" directory inside the current app folder. Inside said directory, add another directory now named the same as the app itself. Inside that directory is where you put all your templates.
- Searching for the Templates: After creating a template, the main project has to be made aware of the place where the templates are placed. You can do this, by referencing the "app.py" file under your app. You specifically have to add the class found inside that file. Add your app to "settings.py" as follows:

    ```python
    INSTALLED_APP = [
        'appName.apps.AppNameConfig',
        ...
    ]
    ```

- Creating a super user for the admin page:

    ```bash
    # Create the necessary database
    python manage.py makemigrations

    # Apply the migrations
    python manage.py migrate

    # Create the super user
    python manage.py createsuperuser

    # Write the user and password 
    # (eg. Username = test / Password = test)
    ```

- New Model Added: Each time we add a new model, the `makemigrations` and `migrate` commands have to be re-executed.
- Check SQL Commands: You can check the commands that Django is generating from our models by creating a migration with:

    ```bash

    # Create the migration
    python manage.py makemigrations

    # View the SQL code to make the migration
    python manage.py sqlmigrate appName makemigrationsNumber`
    ```

- Migrations Usefulness: We can make changes to the database, even if the database is already populated.
- Access the Django Shell: `python manage.py shell`

- If we have an object that pertains to a specific class, and you want said object to have a more descriptive name, you can add a "dunder" method (double under) of "__str__" to the model class. The return value will be the new name (eg. `return self.title`).

- Queries for the database model

    ```python

    # Import posts object
    from blog.models import Post

    # Import User model
    from django.contrib.auth.models import User

    # Get all posts
    posts = Post.objects.all()

    # List all users
    users = User.objects.all()

    # Get specific users
    User.objects.filter(username="eddysanoli")

    # Get first user of list
    User.objects.first()

    # Get all posts that correspond to a user 
    user = User.objects.all()
    user.post_set.all()

    # Create a new post that pertains to a user
    user = User.objects.all()
    user.post_set.create(title="Blog 3", content="Third post")

    # Get URL of image
    user = User.objects.first()
    user.profile.image.url
    ```

- Add crispy forms to the app by using `pipenv install django-crispy-forms`. Add the pack to the "INSTALLED_APPS" section in the `settings.py` file.
- Add crispy forms styling by adding the parameter "CRISPY_TEMPLATE_PACK" at the end of `settings.py`
- Use a vertical bar (`|`) inside a template variable (`{{}}`) in order to apply a filter to the variable
- The default login page for django redirects the user after a successful operation to the route `routes/profile/`. You can change this by going into the project settings (`settings.py`) and adding the parameter: LOGIN_REDIRECT_URL = name_of_url.
- When you use a decorator of @login_required for a view, if the user is logged out, this will require the user to first login. The cool thing, is that it keeps track of what page you were in, and after the login, will redirect you to said page.

- When using the `ImageField` inside a model, you first need to install Pillow using `pipenv install Pillow`. After that, everything will work correctly, no additions to `settings.py` are required.

- You can access a model from another model, as long as the one you are trying to access has a one to one relationship with the base model.

- You can change the place where images are stored changing the `MEDIA_ROOT` and `MEDIA_URL` settings on `settings.py`

- Some people place their "signals" inside their "models", but the documentation recommends that you create a new "signals.py" file to prevent errors from imports.

### Files

Django_project

- __init__.py: Tells python that the current folder is a package
- settings.py: Configurations and settings
- urls.py: Set URL mappings for different routes
- manage.py: Allows us to run command lines inside the server
- wsgi.py: How the python webapp and the server communicate

App

- __init__.py: Tells python that the current folder is a package
- views.py: Routes for the website. This is the file that manages which HTML document is being rendered.
- forms.py: Modifications to the standard forms that django gives the programmer