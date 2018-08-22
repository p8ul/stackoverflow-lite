# BUILD A PRODUCT: StackOverflow-lite
[![Build Status](https://travis-ci.org/p8ul/stackoverflow-lite.svg?branch=challenge2)](https://travis-ci.org/p8ul/stackoverflow-lite)
[![Coverage Status](https://coveralls.io/repos/github/p8ul/stackoverflow-lite/badge.svg?branch=B%2Fhome)](https://coveralls.io/github/p8ul/stackoverflow-lite?branch=B%2Fhome)
[![Maintainability](https://api.codeclimate.com/v1/badges/1338baa03482bfc84be9/maintainability)](https://codeclimate.com/github/p8ul/stackoverflow-lite/maintainability)

## Project Overview
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Required Features
    1. Users can create an account and log in.
    2. Users can post questions.
    3. Users can delete the questions they post
    4. Users can post answers
    5. Users can view the answers
    6. Users can accept an answer out of all the answers to his/her queston as they preferred answer

# Challenge 1 - Create UI Templates
**[Complete UI Pages](https://p8ul.github.io/stackoverflow-lite/UI/)**

    * Signup and signin pages
    * Questoins list page
    * View questions and Answers page
    * Post question page
    * User profile page
    * Host UI template on github pages 

## Installation

### To install the stable version:

```
git clone https://github.com/p8ul/stackoverflow-lite

git clone https://github.com/p8ul/stackoverflow-lite.git
cd stackoverflow-lite
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
## Testing
``` 
$ pytest
```
 
 # Challenge 2 - Create UI Templates
 **[Deployed App Link](https://stackoverflow-paul.herokuapp.com/)**

 **[PostMan Published collection](https://web.postman.co/collections/2215758-2951bbbf-7cf0-46cf-97dd-1b18375104b0?workspace=43f47149-032e-44cb-891a-a873a3c4e341#cdb2ba3a-ce26-434b-873f-6b5ef39b493b)**
 
    - user stories to setup and test API endpoints
        Get all questions. 
        Get a question
        Post a question. 
        Update a question
        Post an answer to a question. 
    - Setup the Flask server side of the application
    - Setup pytest python test framework 
    - Version your API using url versioning starting, with the letter “v”
    - Write tests for the API endpoints
    - Integrate ​ TravisCI​ for Continuous Integration in your repository (with ​ ReadMe ​ badge). 
    - Integrate test coverage reporting (e.g. Coveralls) with badge in the ​ ReadMe. 
    - Obtain CI badges (e.g. from Code Climate and Coveralls) and add to ​ ReadMe . ​  
    - Ensure the app gets hosted on Heroku. 

## Api Endpoints
### Questions API endpoints
```
/api/v1/questions
/api/v1/questions/1
/api/v1/questions/1/answer
```
### Users API endpoints

```
/api/v1/users
/api/v1/users/1
```
