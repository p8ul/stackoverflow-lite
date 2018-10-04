# StackOverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Heroku deployment
> **[Check it out](https://stackoverflow-paul.herokuapp.com/)**

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
    DATABASE_URL=postgres://username:password@hostname/databasename
    
    $ python manage.py runserver
```

## Testing
``` 
    $ pytest --cov=app
```

### Endpoints

#### Users Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/auth/signup` | Add a user
GET | `/api/v1/auth/users` | Lists all users
GET | `/api/v1/auth/users/{user_id}` | Retrieve a user
POST | `/api/v1/auth/login` | Login a user

#### Questions Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions` | Add a question
GET | `/api/v1/questions` | Lists all questions
GET | `/api/v1/questions/?q={search_string}` | Search a questions
GET | `/api/v1/questions/{question_id}` | Retrieve a question
PUT | `/api/v1/questions/{question_id}` | Edit a question of a logged in user
DELETE | `/api/v1/questions/{question_id}` | Delete a request of a logged in user

#### Answers Endpoints

Method | Endpoint | Functionality
--- | --- | ---
POST | `/api/v1/questions/{question_id}/answers` | Add an answer
GET | `/api/v1/questions/answers` | Lists all answers
GET | `/api/v1/questions/answers/{answerID}` | Retrieve an answer
PUT | `/api/v1/questions/{question_id}/answer/{answerID}` | Edit an answer
DELETE | `/api/v1/questions/{question_id}/answer/{answerID}` | Delete an answer
POST | `/api/v1/questions/answers/vote/{answer_id}` | Upvote/DownVote an answer
POST | `/api/v1/questions/answers/comment/{answer_id}` | Comment on an answer


## Credits
This challenge was part of the Bootcamp 31 NBO Andela.

Credits to [Avinash Tripathi](https://dribbble.com/nashatwork) for an awesome [Stackoverflow redesign concept](https://dribbble.com/shots/2876030-Stackoverflow-redesign?_=1535432246078&utm_source=Clipboard_Shot&utm_campaign=nashatwork&utm_content=Stackoverflow%20redesign&utm_medium=Social_Share). Helped in comming up with some dashboard UI components.

### License
[MIT LICENSE](https://github.com/p8ul/stackoverflow-lite/blob/develop/LICENSE)

### Buy me coffee
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=6WGR3AQ6GTWTL)

## Author
Paul Kinuthia.

