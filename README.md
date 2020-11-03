#  Neighbour-hood

#### Author: [Peris Oduol](https://github.com/PerisOduol618)


* Link to live site: [Instagram](https://perishood.herokuapp.com/)

## Description
A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

As a user of the web application you will be able to:

1. Sign in to the application to start using it.
2. Set up a profile which contains:
    * My name 
    * My location 
    * My neighborhood name 

3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the emergency services 
5. Create Posts that will be visible to everyone in my         neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login	if already have an account |if you dont have , click on the sign up link on te navbar and fill the form  | If login is successful, user is navigated to home page | Click on `Comment` | Taken to where you can comment | Signs In/ Signs Up |
| Edit profile | On the account link, click on the   profile to update| Redirected to the profile page and edit your profile |
| Click on join hood| Redirects to the view/leave hood page | if user clicks on join hood,he/she can view post/business and add post/business|
|Add a new new hood|Click on the new hood at the navbar  redirected to the add hood form|the post will be rendered to the neighborhood  page
| Click on log Out in the accounts| Redirects to the home page | Logs out user  |

## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.6 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.6
* virtual environment
* pip

#### Clone the Repo and rename it to suit your needs.
```bash
git clone https://github.com/PerisOduol618/Neighbour-hood
```
#### Initialize git and add the remote repository
```bash
git init
```
```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY = 'tfpu1z=*m6-fkbiu*d0k8d-y@+r15e+9z7nbr0pt3%c!_9=5(_'
DEBUG=True
DB_NAME='hood'
DB_USER='<your database name>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations
```bash
python3.6 manage.py check
python manage.py makemigrations news
python3.6 manage.py sqlmigrate news 0001
python3.6 manage.py migrate
```

#### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)



## Testing the Application
`python manage.py test insta`
        
## Built With

* [Python3.6](https://docs.python.org/3/)
* Django 2.2.8
* Postgresql 
* Boostrap
* HTML
* CSS


## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :oduolpepe618@gmail.com

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)