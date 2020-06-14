import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={'/': {'origins': '*'}})

    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type, Authorization, true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/categories')
    def get_all_categories():
        try:
            categories = Category.query.all()
            categories_dict = {}
            for category in categories:
                categories_dict[category.id] = category.type
            return jsonify({
                'success': True,
                'categories': categories_dict
            }), 200
        except Exception:
            abort(500)

    @app.route('/questions')
    def get_questions():
        page = request.args.get('page', 1, type=int)
        start = (page-1)*10
        end = start + 10

        questions = Question.query.order_by(Question.id).all()
        questions = [question.format() for question in questions]
        total_questions = len(questions)
        categories = Category.query.order_by(Category.id).all()

        current_questions = questions[start:end]

        if (len(current_questions) == 0):
            abort(404)

        categories_dict = {}
        for category in categories:
            categories_dict[category.id] = category.type

        return jsonify({
            'success': True,
            'total_questions': total_questions,
            'categories': categories_dict,
            'questions': current_questions
            }), 200

    @app.route('/questions/<int:id>', methods=['DELETE'])
    def delete_question(id):
        try:
            question = Question.query.get(id)
            question.delete()
            return jsonify({
                    'success': True,
                    'message': "Question successfully deleted"
                }), 200
        except Exception:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def create_question():
        data = request.get_json()

        question = data.get('question', '')
        answer = data.get('answer', '')
        difficulty = data.get('difficulty', '')
        category = data.get('category', '')

        if (question == ''):
            abort(422)
        if (answer == ''):
            abort(422)
        if (difficulty == ''):
            abort(422)
        if (category == ''):
            abort(422)
        try:
            question = Question(
                question=question,
                answer=answer,
                difficulty=difficulty,
                category=category)

            question.insert()

            return jsonify({
                'success': True,
                'message': 'Question successfully created!'
            }), 201
        except Exception:
            abort(422)

    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        data = request.get_json()
        search_term = data.get('searchterm', '')

        if search_term == '':
            abort(422)

        try:
            questions = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')
                ).all()

            if len(questions) == 0:
                abort(404)

            page = request.args.get('page', 1, type=int)
            start = (page-1)*10
            end = start + 10
            questions = [question.format() for question in questions]
            total_questions = len(questions)

            current_questions = questions[start:end]

            # return response if successful
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': total_questions
            }), 200
        except Exception:
                abort(404)

    @app.route('/categories/<int:id>/questions')
    def get_questions_by_category(id):
        category = Category.query.filter_by(id=id).one_or_none()

        if (category is None):
            abort(422)

        questions = Question.query.filter_by(category=id).all()

        page = request.args.get('page', 1, type=int)
        start = (page-1)*10
        end = start + 10
        questions = [question.format() for question in questions]
        total_questions = len(questions)
        current_questions = questions[start:end]

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': total_questions,
            'current_category': category.type
        })

    @app.route('/quizzes', methods=['POST'])
    def play_quiz_question():
        data = request.get_json()
        previous_questions = data.get('previous_questions')
        quiz_category = data.get('quiz_category')

        if ((quiz_category is None) or (previous_questions is None)):
            abort(400)

        if (quiz_category['id'] == 0):
            questions = Question.query.all()
        else:
            questions = Question.query.filter_by(
                category=quiz_category['id']
                ).all()

        def get_random_question():
            return questions[random.randint(0, len(questions)-1)]

        next_question = get_random_question()

        found = True
        while found:
            if next_question.id in previous_questions:
                next_question = get_random_question()
            else:
                found = False

        return jsonify({
            'success': True,
            'question': next_question.format(),
        }), 200

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'Bad request error'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Resource not found'
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'An error has occured, please try again'
        }), 500

    @app.errorhandler(422)
    def unprocesable_entity(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'Unprocessable entity'
        }), 422

    return app
