# BUILD A PRODUCT: StackOverflow-lite
[![Build Status](https://travis-ci.org/p8ul/stackoverflow-lite.svg?branch=challenge2)](https://travis-ci.org/p8ul/stackoverflow-lite)
[![Coverage Status](https://coveralls.io/repos/github/p8ul/stackoverflow-lite/badge.svg?branch=B%2Fhome)](https://coveralls.io/github/p8ul/stackoverflow-lite?branch=B%2Fhome)
[![Maintainability](https://api.codeclimate.com/v1/badges/1338baa03482bfc84be9/maintainability)](https://codeclimate.com/github/p8ul/stackoverflow-lite/maintainability)

## Project Overview
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Required Features
    - Users can create an account and log in.
    - Users can post questions.
    - Users can delete the questions they post
    - Users can post answers
    - Users can view the answers
    - Users can accept an answer out of all the answers to his/her queston as they preferred answer
    - Users can upvote or downvote an answer.
    - Users can comment on an answer.
    - Users can fetch all questions he/she has ever asked on the platform
    - Users can search for questions on the platform
    - Users can view questions with the most answers.

#  Complete Tasks
 > **[Complete UI Pages](https://p8ul.github.io/stackoverflow-lite/UI/)** 
 
 > **[Deployed App Link](https://stackoverflow-paul.herokuapp.com/)**
 
 >  **[API End points documentation](https://stackoverflowlite2.docs.apiary.io/#reference)**
 
 >  **[Pivot tracker board](https://www.pivotaltracker.com/n/projects/2189597)**


## Installation

```
    $ git clone https://github.com/p8ul/stackoverflow-lite

    $ git clone https://github.com/p8ul/stackoverflow-lite.git
    $ cd stackoverflow-lite
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt   
```
## Running the application
```
    $ export DATABASE_URL="Your DATABASE_URL here"
``` 
or open .env file and copy your postgres database url
```
    #.env file
    DATABASE_URL=postgresql://stack:stack@127.0.0.1:5432/stack
    
    $ python manage.py runserver
```

## Testing
``` 
    $ pytest --cov=app
```

## Api Endpoints
### Questions API endpoints

```

/api/v1/questions
/api/v1/questions/1
/api/v1/questions/1/answer
```
