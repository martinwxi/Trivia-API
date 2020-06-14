# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

### Getting Started

* API Base URL: `http://127.0.0.1:5000/`

### Error Handling

Errors are returned in the following json format:

```json
{
	"success": "False",
	"error": 400,
	"message": "Bad request error",
}
```

The error codes represented:

* 400 – Bad request error
* 404 – Resource not found
* 422 – Unprocessable entity
* 500 – An error has occured, please try again


### Endpoints

#### GET /categories

- General: 
  - Returns all categories.

- Sample:  `curl http://127.0.0.1:5000/categories`

```json
{
		"categories": {
				"1": "Science", 
				"2": "Art", 
				"3": "Geography", 
				"4": "History", 
				"5": "Entertainment", 
				"6": "Sports"
		}, 
		"success": true
}
```

#### GET /questions
- General:
  - Returns all questions

- Sample: `curl http://127.0.0.1:5000/questions`

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```

#### DELETE /questions/\<int:id>


- General:
  - Deletes a question by id

- Sample: `curl -X DELETE http://127.0.0.1:5000/questions/1`

```json
{
	"success": "True",
	"message": "Question successfully deleted"
}
```

#### POST /questions

- General:
  - Creates a new question

- Sample: `curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/questions -d '{
            "question": "test",
            "answer": "test",
            "difficulty": 1,
            "category": "1"
						}'`

```json
{
	"message": "Question successfully created!",
	"success": true
}
```

#### POST /questions/search

- General:
  - returns questions that containes the search terms

- Sample: `curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/questions/search -d '{
						"searchterm": "Palace"
						}'`

```json
{
	"questions": [
		{
			"answer": "The Palace of Versailles",
			"category": 3,
			"difficulty": 3,
			"id": 14,
			"question": "In which royal palace would you find the Hall of Mirrors?"
		}
	],
	"success": true,
	"total_questions": 1
}
```

#### GET /categories/\<int:id>/questions

- General:
  - Gets questions by category using the category id
	
- Sample: `curl http://127.0.0.1:5000/categories/1/questions`

```json
{
  "current_category": "Science",
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 3
}

```

#### POST /quizzes

- General
  - Takes the category and previous questions in the request.
  - Return random question not in previous questions.

- Sample: `curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5000/quizzes -d '{
						"previous_questions": [1, 3],
						"quiz_category": {
															"type": "Entertainment",
															"id": "5"
															}}'`

```json
{
  "question": {
    "answer": "Apollo 13",
    "category": 5,
    "difficulty": 4,
    "id": 2,
    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
  },
  "success": true
}
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
