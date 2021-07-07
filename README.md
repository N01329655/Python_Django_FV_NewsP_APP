# Python_Django_FV_NewsP_APP

The project "Newspaper app" was built according to book and aimed to improve my skills in using Django in the development.


The "Newspaper app" has a straightforward interface for new users the web application gives an option to create a new account, whereas
users with accounts can log in, log out, change passwords. Only creation of new accounts required to create 
a template, view, and URL scheme,
in the same time to implement login, log out and change password only templates were required Django took care of everything else.
Last but not least is a feature to reset a password in case the user forgot it. The feature was implemented and relies on the
third-party service which is SendGrid.

The app is a simple "newspaper" blog, where only registered and authenticated users can create new articles and read articles
from other users. In addition, owners of articles can change (edit/delete) their articles whenever they want to do so.
The superuser(admin) has access to all articles and control over them the admin is allowed to delete updates or leave a comment
on the article. Additionally, the admin has access to the user's data such as email, age, and username, 
whereas the password is stored by Django, thus the admin does not have any access to the user's passwords.

To sum up: the proccess of building this project was a greate opportunity to study and develop my skills in using Django
as a framework for development web-applications.

P.S. 
I would like to provide a content of Pipfile:

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"
django-crispy-forms = "*"
sendgrid = "*"

[dev-packages]

[requires]
python_version = "3.9"
