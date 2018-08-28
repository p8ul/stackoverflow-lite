from flask_restful import Resource, Api
from flask import Blueprint, request
from app.questions.models import Question, Answer

api = Blueprint('api', __name__, url_prefix='/api/v1')
api_wrap = Api(api)

data = []


class ListRetrieveAPIView(Resource):
    def get(self, question_id=None):
        if question_id:
            try:
                response = filter_by(int(question_id))
                if not response:
                    return {"status": "error", "data": "Question Not Found"}, 404
            except Exception as e:
                print(e)  # :TODO log error
                return {"status": "error", "data": "Question Not Found. Please provide a valid question ID"}, 404
        else:
            response = [instance for instance in data]
        return {"status": "success", "data": response}, 200

    def post(self, question_id=None):
        json_data = request.get_json(force=True)
        try:
            question = Question(json_data)
        except Exception as e:
            return {"status": "error", "message": "Bad request"}, 400
        response = add_question(question.query())
        if response:
            return {"status": "success", "data": data}, 201
        return {"status": "error", "message": "Bad request"}, 400


class PostAPIView(Resource):
    def post(self, question_id=None):
        json_data = request.get_json(force=True)
        try:
            answer = Answer(json_data)
        except:
            return {"status": "error", "message": "Bad request"}, 400
        if question_id and answer.answer:
            response = create_answer(question_id, answer.answer)
            if not response:
                return {"status": "error", "data": "Question Not Found"}, 404
        return {"status": "success", "data": json_data}, 201


api_wrap.add_resource(
    ListRetrieveAPIView,
    '/questions/',
    '/questions/<string:question_id>',
    '/questions/<string:question_id>/',
    '/questions/<int:question_id>'
)

api_wrap.add_resource(
    PostAPIView,
    '/questions/<string:question_id>/answer',
    '/questions/<string:question_id>/answer/',
)


def filter_by(instance_id):
    # filter by instance by id
    item_ = next((item for item in data if item.get('id') == int(instance_id)), {})
    return item_


def create_answer(question_id=None, answer=None):
    if question_id:
        result = False
        for i in range(len(data)):
            if data[i].get('id') == int(question_id):
                answer = {'answer': answer}
                data[i]['answers'].append(answer)
                result = True
                break
        return result


def add_question(question):
    if question.get('title') and question.get('body'):
        question['id'] = len(data) + 1
        question['answers'] = []
        data.append(question)
        return question
    return False

