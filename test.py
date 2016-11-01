import unittest
import json
from main import index, question, question_random, answer

class TestQuestionManager(unittest.TestCase):

    def test_index(self):
        self.assertEqual(index(), 'it\'s alive')

    def test_question(self):
        q1 = question(1)
        self.assertEqual(type(q1), str)
        q1 = json.loads(q1)

        self.assertEqual(q1['id'], 1)
        self.assertEqual(q1['A'], 'that im feeling')


    def test_question_random(self):
        diff = set([])

        for i in range(5):
            q = question_random()
            self.assertEqual(type(q), str)
            q = json.loads(q)
            diff.add(q['id'])

        self.assertTrue(len(diff) > 1)


if __name__ == '__main__':
    unittest.main()
