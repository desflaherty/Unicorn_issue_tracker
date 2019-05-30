[![Build Status](https://travis-ci.com/desflaherty/Unicorn_issue_tracker.svg?branch=master)](https://travis-ci.com/desflaherty/Unicorn_issue_tracker)
# Project Name: Unicorn Attractor Bug Issue Tracker
I decided to use the sample brief given to students for the project to create a web application that allows users 
to log Bugs that they find with the fictional application and also to add features they would like developed. They can upvote
bugs and features once they have registered on the site and can add features to a shopping cart and checkout.

* Project has been published to the Heroku website https://bugissue-tracker.herokuapp.com
* The github repository is located at https://github.com/desflaherty/Unicorn_issue_tracker

For testing purposes the admin logon can be used to add new bugs/features, edit existing bugs/features and to add or
change the status of the bugs and features on the site.
* Username:admin
* Password: admin1234

## UX

*Strategy:*
The intention for this project would be to create a bug issue tracker application that is responsive and visually appealing 
and uses the frameworks and technologies covered thus far in the course.

*User Stories:*
As a user of the issue tracker I should be able to: 

* Browse existing bugs and features when not registered
* Register with the site and then login using a username or email address
* View my profile information
* Once logged in add bugs or features that I would like developed
* Upvote bugs and features and also add features to my cart and complete the checkout process
* Search for existing bugs and features that have already been created by other users
* View the status of each bug or feature to see what is currently being worked on
* View graphs summarising the total issues being tracked by the web app by their current status

## A mockup for the proposed app can be viewed on github 
https://github.com/desflaherty/Unicorn_issue_tracker/tree/master/wireframes

## Existing Features
*Header and Footer*
* A navigation bar is displayed with a logo which links to the homepage
* Links are displayed on the right hand side of the navigation menu to allow for browsing of issues or registration
* Once logged in more links become available such as a profile and graphs section
* On mobile or iPad view the navigation bar will collapse to display a tiled dropdown menu
* A footer is displayed at the bottom of the screen throughout the website

*Index/Home*
* This is the homepage displaying a background image
* Text is displayed to inform the user they can browse or register to create a feature
* 'Enter' and 'Register' buttons are displayed in the center of the homepage
* When a user as logged in a welcome message is displayed

*Register & Login*
* A user can create an account and choose a username or use an email address as a username 
* A password can be chosen
* There is a form control implemented where a chosen password and confirmation password must match
* This username will be used to log in and track bugs or features added by the user
* If a username is already taken a  message will be displayed to the user 
* The username must adhear to the format as explained to the user on screen
* The user can login using a combination of username and password

*Profile*
* Displays the username and email of the user

*Bugs*
* Displays the bugs that have been added to the site so far
* Bug name, current status and date/time bug was added as well as a desscription of the bug
* When a user is logged in an 'Add Bug' button is displayed
* A more detailed view of the bug links from here

*Bug Detail*
* A view counter is shown here that will increment on each view
* A user when logged in can now upvote the bug. If not logged in the user will be directed to the login page
* If the admin user is logged in an edit button is displayed where the admin can add a status to the bug to show
if the bug is being worked on
* A comments section is displayed here where the user can post a comment about the bug
* An upvote counter is displayed. When the user upvotes an upvote success message is displayed

*Add Bug*
* A logged in user can add name and description of the bug
* If admin a status is also displayed

*Search*
* Search box that allows the user to search the bugs or features that have been added to the site

*Features*
* Displays the features that have been added to the site so far
* Feature name, current status and date/time feature was added as well as a desscription of the feature
* When a user is logged in an 'Add Feature' button is displayed
* A more detailed view of the feature links from here

*Feature Detail*
* A view counter is shown here that will increment on each view
* A user when logged in can now upvote the feature. If not logged in the user will be directed to the login page
* If the admin user is logged in an edit button is displayed where the admin can add a status to the feature to show
if the feature is being worked on
* A comments section is displayed here where the user can post a comment about the feature
* An upvote counter is displayed. When the user upvotes an upvote success message is displayed
* An add to cart button is displayed where the user can add the feature to their shopping cart.

*Add Feature*
* A logged in user can add name and description of the feature
* If admin a status is also displayed

*Cart*
* Displayes the features that have been added to the cart
* The cost of the individual feature is displayed 
* The overall cost of the features in the cart is shown
* A checkout button is displayed
* The user can link back to the feature detail app and can also delete the feature from the cart here

*Checkout*
* The checkout form is displayed
* Credit card number, CVV code, CC Expiry information is collected here
* The site uses stripe to process payment. If the credit card is invalid or expired a warning message will be displayed

*Graphs*
* When a user is logged in pie charts are displayed here to show the status of the bugs and features that have been added

## Technologies, Programming Languages and Frameworks

*Python*
* Controls functionality of the project
* https://www.python.org

*Django*
* A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* https://www.djangoproject.com/

*Bootstrap*
* An open source toolkit for developing with HTML, CSS, and JS
* Uses a responsive grid system for responsive development
* https://getbootstrap.com

*Bootswatch*
* A template for Bootstrap
* https://bootswatch.com/

*HTML5*
* Positioning and format of html elements.
* https://www.w3schools.com/html/default.asp

*CSS3*
* Styling the HTML elements
* https://www.w3schools.com/css/

*Font Awesome*
* Icons used in the navbar 
* https://fontawesome.com/

*PyGal*
* A python charting library
* http://pygal.org/en/stable/documentation/index.html

*Amazon web services*
* AWS S3 bucket services were used to create a bucket where static files and media are stored

*Stripe*
* Used for the set up and processing of user payments.
* https://stripe.com/ie

*Travis CI*
* Used to build and test software projects hosted on github
* https://travis-ci.com

*GitHub*
* Used for collaboration and version control
* https://github.com/

## Validation
* HTML:Checked with W3C validator. No HTML errors were displayed.
* CSS:Checked with CSS lint. No errors were displayed
* Python: PEP8 was used to check code for any major errors

## Testing

* a href="https://github.com/desflaherty/Unicorn_issue_tracker/blob/master/Manual_Testing.md">Manual Testing</a>
* Travis continuous integration was used to clone the GitHub repository and test the build with a green status of passing 

## Features left to implement
* A page detailing the unicorn attractor app
* Development of more graphs such as line graphs to show issues being worked on & fixed by date
* Bonus points for more active users where they would receive a discount on future development
* A blog for discussion and to generate interest 

## Deployment
### Heroku
* Created a new app called 'bugissue-tracker'
* Under 'Deploy' connected to the githib respository 
* Under 'Resources' add a Postgres database

*In settings.py*
* ALLOWED_HOSTS=['bugissue-tracker.herokuapp.com']

*Terminal*
* pip install dj_database_url, This allows django to connect to the heroku database url.
* pip install psycopg2,to connect to the postgres databases.

*In settings.py*
* Import dj_database_url
* DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

*Terminal*
Create a new database and a superuser
* python manage.py migrate
* python manage.py createsuperuser

*In settings.py*
Host static files in Amazon Web Server

* AWS_STORAGE_BUCKET_NAME = 'desnewbugissuetracker'
* AWS_S3_REGION_NAME = 'eu-west-1'
* AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
* AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
* AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
* STATICFILES_LOCATION = 'static'
* STATICFILES_STORAGE = 'custom_storages.StaticStorage'

*Terminal*
* python3 manage.py collectstatic

*Heroku ConfigVars*
Settings > Config Vars
* DATABASE_URL | <my database_url key>
* SECRET_KEY | <my secret key>
* STRIPE_PUBLISHABLE | <my stripe key>
* STRIPE_SECRET | <my stripe secret key>
* DISABLE_COLLECTSTATIC | 1
* AWS_ACCESS_KEY_ID | <my aws_access_key_id>
* AWS_SECRET_ACCESS_KEY | <my aws_secret_access_key>

*Terminal*
* pip install gunicorn, this will run the application
* pip3 freeze --local > requirements.txt (Creates a .txt file which tells Heroku what dependencies the project is using) 
* echo web: gunicorn.wsgi:application > Procfile (Tells Heroku that this project is a web app and what to run)
* git add .
* git commit -m 'message'
* git push
* https://bugissue-tracker.herokuapp.com

## Running locally

* Clone the respository found here https://github.com/desflaherty/Unicorn_issue_tracker
* Install the applictions found in the requirements file https://github.com/desflaherty/Unicorn_issue_tracker/blob/master/requirements.txt
* In settings.py uncomment import env to import the env.py file

### Env.py
Create an env.py file and enter the following with your own keys.
import os
os.environ.setdefault('SECRET_KEY', <'secret key'>)
os.environ.setdefault("STRIPE_PUBLISHABLE", <'stripe publishable key'>)
os.environ.setdefault("STRIPE_SECRET", <'stripe secret key'>)
os.environ.setdefault("AWS_ACCESS_KEY_ID", <aws_access_key_id)
os.environ.setdefault("AWS_SECRET_ACCESS_KEY","<aws_secret_access_key>")
os.environ.setdefault("DATABASE_URL","<database_url>")

### Stripe
Set up an account https://stripe.com/ie and create an account.
* Dashboard > Developers > API keys to locate your API key
* Take note of your publishable and secret key that gets entered into the env.py file locally and Heroku settings
* For stripe payment use the fake credit card number 4242424242424242 

## Credits 
* Background image was sourced from https://unsplash.com/
* Images used for the graphs were sourced from https://www.flaticon.com/
* https://stackoverflow.com/ was used for coding issues
* The slack forum was used for discussion with students on various topics during project development 





