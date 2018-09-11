import unittest
from .base import BaseTestCase
from app.votes.models import Vote
from app.answers.models import Answer
from app.questions.models import Question

answer = Answer()
question = Question()
vote = Vote()


class VotesModelTestCase(BaseTestCase):

    def test_model_vote_exist(self):
        query = vote.vote_exists()
        self.assertEqual(query, False)

    def test_model_vote(self):
        question.title, question.body = "Question title", "question body"
        question.user_id = self.user_id
        result_payload = question.save()
        self.data['question_id'] = result_payload.get('question_id')

        answer.question_id = self.data.get('question_id')
        answer.answer_body = 'answer body'
        answer.user_id = self.user_id
        query = answer.save()
        self.data['answer_id'] = query.get('answer_id')
        vote.user_id = self.user_id
        vote.answer_id = self.data.get('user_id')
        vote.vote_value = 'true'
        query = vote.vote()
        self.assertEqual(query, False)

    def test_model_update_vote(self):
        query = vote.update_vote()
        self.assertEqual(query, False)

    def test_model_create_vote(self):
        query = vote.create_vote()
        self.assertEqual(query, False)

    def test_model_init(self):
        keys = vote.config.keys()
        self.assertIn(list(keys)[0], ['password', 'user', 'database', 'host'])
        self.assertEqual(len(list(keys)), 4)


if __name__ == '__main__':
    unittest.main()
