Haven't seen a movie in a while?

## Steps

## Setup

1. Fork and clone [this repository](https://github.com/malthunayan/TASK-Django-M12-Authentication-and-Permissions-II).
2. Install the `requirements` using `pip install -r requirements/dev.lock`.

## Registration

1. Create a new app called `users` and create a `User` model that inherits from `django.contrib.auth.models.AbstractUser` and just `pass`es.
2. Go to `settings.py` and add `AUTH_USER_MODEL = "users.User"`, where `users` is that app name and `User` is the class name we chose for our custom `User` model.
3. Make migrations and migrate by running the following command `./manage.py makemigrations users && ./manage.py migrate`.
   - Do not run `makemigrations` regularly because we want to delay migrating the `movies` app
4. Add a `forms.py` file inside of your `users` app.
5. Add a `RegistrationForm` model form.
   - Make sure to set the model equal to `User`, but do not import your `User` model directly (use `Django`'s helper `get_user_model`, which you can read about [here](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#referencing-the-user-model)).
   - Add a widget for the password field to be hidden (you can read about widgets [here](https://docs.djangoproject.com/en/4.0/ref/forms/widgets/))
6. Add your `register_user` view in `users/views.py`.
   - Create a new instance of your `RegistrationForm`
   - Check if the `request method` is `POST` and then create a new instance of `RegistrationForm` with the first argument passed being `request.POST`
     - Check if the `form` is `valid` and then save the form, but do not commit (i.e., `commit=False`) and assign the return to a variable called `user`
     - Use `user.set_password` to set the password
     - Finally use `user.save` to commit your changes
     - Then use the `login` helper to login (read about it [here](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in))
     - `Redirect` to `home`
   - Create your `context` and add your `form` instance to it
   - `Render` a template called `register.html`
7. Add your `register_user` view to `urls.py` and name it `register`.
8. Add the `register.html` template to `users/templates` (you can use `crispy forms` and `bootstrap` to prettify it).
9. Add a link to `register` in the navbar of `shared/templates/home.html` and `movies/template/movie_list.html`.
10. We have no way right now to tell that we are registered and logged in other than trying to register again and failing. We will see how to make it visible to the user that they're logged in in the upcoming task. Commit and push your changes.

## Logout

1. Add a `logout_user` view that uses the `logout` [helper](https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-out) from `Django`.
2. Add the `logout_user` view to `urls.py` with the name `logout`.
3. Add a conditional in the navbars (`shared/templates/home.html`, `movies/templates/movie_list.html`, etc...) that checks if the `user` is `authenticated`.
   - If the user is authenticated then show the `anchor` tag that will log them out
   - Else show the registration link
4. Commit and push your code.

## Login

1. Add the `LoginForm` in `users/forms.py` that inherits from `Form` not `ModelForm`.
   - `username`: `CharField` which is `required`
   - `password`: `CharField` which is `required` and has a `PasswordInput` widget (read about widgets [here](https://docs.djangoproject.com/en/4.0/ref/forms/widgets/))
2. Add the `login_user` view in `users/views.py`.
   - Create a new `form` instance of `LoginForm`
   - Check if the `request method` is `POST`
     - Create new `form` instance of `LoginForm` with the first argument as `request.POST`
     - Check if the `form` is `valid`
       - Authenticate the user using the `authenticate` [helper](https://docs.djangoproject.com/en/4.0/topics/auth/default/#authenticating-users) from `Django`, which will use the `cleaned_data` from the `form` instance we last created, and assign the return from this helper to a variable called `auth_user`
       - Check if `auth_user` is **not** `None`
         - Use the `login` helper from `Django` to login and `redirect` to `home`
   - Create your `context` and add the `form` instance to it
   - `Render` your `request`, `login.html` template, and `context`
3. Add the `login_user` view to `urls.py`, with the name `login`.
4. Add the `login` template in `users/templates/login.html` (you can use `crispy forms` and `bootstrap` to prettify it).
5. Update all navbars (`shared/templates/home.html`, `movies/templates/movie_list.html`, etc...) to include the link to `login`.
   - Make sure the link only appears if the user is anonymous (i.e., not logged in)
6. Add an `anchor` tag inside your `login.html` template to link new users to the `registration` form.
7. Add an `anchor` tag inside your `register.html` template to link old users to the `login` form.
8. Try out the `login` form.
9. Commit your code.
10. Push your code.
