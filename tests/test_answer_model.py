import unittest
from .base import BaseTestCase
from app.answers.models import Answer
from app.questions.models import Question

answer = Answer()
question = Question()


class AnswersModelTestCase(BaseTestCase):

    def test_answer_query_normal(self):
        """ Test retrieve all answers"""
        query = answer.query()
        self.assertIsInstance(query, type([]))

    def test_answer_model_filter_unexpected(self):
        """ Example: answer_id 'None' """
        answer.answer_id = None
        query = answer.filter_by()
        self.assertEqual(query, [])

    def test_answer_model_filter_edgecase(self):
        """ Example: answer_id '[]' """
        answer.answer_id = None
        query = answer.filter_by()
        self.assertEqual(query, [])

    def test_model_save_unexpected(self):
        """ Pass wrong json payload """
        question.title, question.body = "Question title", "question body"
        question.user_id = self.user_id
        result_payload = question.save()
        self.data['question_id'] = result_payload.get('question_id')

        answer.question_id = self.data.get('question_id')
        answer.answer_body = 'answer body'
        answer.user_id = None
        query = answer.save()
        self.assertEqual(query, None)

    def test_model_save_normal(self):
        question.title, question.body = "Question title", "question body"
        question.user_id = self.user_id
        result_payload = question.save()
        self.data['question_id'] = result_payload.get('question_id')

        answer.question_id = self.data.get('question_id')
        answer.answer_body = 'answer body'
        answer.user_id = self.user_id
        query = answer.save()
        self.data['answer_id'] = query.get('answer_id')
        self.assertEqual(query.get('answer_body'), answer.answer_body)

    def test_model_update(self):
        answer.answer_body = 'Update body'
        answer.answer_id = self.data.get('answer_id')
        query = answer.update()
        self.assertEqual(query.get('errors'), 'Please provide correct answer and question id')

    def test_model_delete(self):
        query = answer.delete()
        self.assertEqual(query, False)

    def test_model_question_author(self):
        query = answer.question_author()
        self.assertEqual(query, [])

    def test_model_answer_author(self):
        query = answer.answer_author()
        self.assertEqual(query, False)

    def test_model_accept(self):
        query = answer.update_accept_field()
        self.assertEqual(query, True)

    def test_model_update_answer(self):
        query = answer.update_answer()
        self.assertEqual(query, True)

    def test_model_init(self):
        keys = answer.config.keys()
        self.assertIn(list(keys)[0], ['password', 'user', 'database', 'host'])
        self.assertEqual(len(list(keys)), 4)


if __name__ == '__main__':
    unittest.main()
