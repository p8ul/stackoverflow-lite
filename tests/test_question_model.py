import unittest
from .base import BaseTestCase
from app.questions.models import Question

question = Question()


class QuestionModelTestCase(BaseTestCase):

    def test_question_model_save_unexpected_input(self):
        """
            Example: provide wrong json payload
                    body: string [], title: string {}
        """
        try:
            question.title, question.body, question.user_id = '*', '\\', self.user_id
            question.save()
            assert False
        except AssertionError:
            assert True

    def test_question_model_save_expected_input(self):
        """
            Example:
                body: string "question body",
                title: string "question title"
        """
        question.title, question.body = "Question title", "question body"
        question.user_id = self.user_id
        result_payload = question.save()
        self.data['question_id'] = result_payload.get('id')
        self.assertEqual(result_payload.get('body'), question.body)

    def test_model_question_filter_by_unexpected_boundary(self):
        """
            Example: filter by None
        """
        question.question_id = None
        result_payload = question.filter_by()
        self.assertEqual(result_payload, None)

    def test_model_question_filter_by_expected_input(self):
        """
            Example: question id 1
        """
        question.question_id = 1
        result_payload = question.filter_by()
        self.assertEqual(len(list(result_payload.keys())), 3)

    def test_model_question_filter_by_unexpected_edgecase(self):
        """
            Example: question id {}, []
        """
        question.question_id = {}
        result_payload = question.filter_by()
        self.assertEqual(result_payload, None)

    def test_question_model_filter_user_unexpected_boundary(self):
        """ Example: user_id 'None' """
        question.user_id = None
        query = question.filter_by_user()
        self.assertEqual(query, None)

    def test_question_model_filter_user_unexpected_edge(self):
        """ Example: user_id '{}' """
        question.user_id = {}
        query = question.filter_by_user()
        self.assertEqual(query, None)

    def test_question_model_filter_user_expected(self):
        question.user_id = self.user_id
        query = question.filter_by_user()
        self.assertEqual(type(query.get('question')), type([]))

    def test_question_model_update_unexpected_boundary(self):
        """ Example: question_id 'None' """
        question.question_id = None
        query = question.update()
        self.assertEqual(query, True)

    def test_question_model_update_unexpected_edge(self):
        """ Example: question_id '()', '{}', '[]' """
        question.question_id = ()
        query = question.update()
        self.assertEqual(query, False)

    def test_question_model_update_normal(self):
        question.question_id = self.data.get('question_id')
        question.title = 'Hello'
        query = question.update()
        self.assertEqual(query, True)

    def test_question_model_delete_normal(self):
        query = question.delete()
        self.assertEqual(query, False)

    def test_question_model_init(self):
        keys = question.config.keys()
        self.assertIn(list(keys)[0], ['password', 'user', 'database', 'host'])
        self.assertEqual(len(list(keys)), 4)


if __name__ == '__main__':
    unittest.main()
