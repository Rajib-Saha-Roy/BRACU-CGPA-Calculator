from unittest import TestCase
from model import Model


class TestModel(TestCase):

    def test_possible_credits(self):
        self.assertIn(1, Model.possible_credits(self))
        self.assertIn(1.5, Model.possible_credits(self))
        self.assertIn(3, Model.possible_credits(self))

    def test_possible_grades(self):
        self.assertEqual(12, len(Model.possible_grades(self)))
        self.assertListEqual(["F", "D-", "D", "D+", 'C-', "C", "C+", "B-", "B",
                              "B+", "A-", "A"], Model.possible_grades(self))

    def test_corresponding_point(self):
        self.assertEqual(4, Model.corresponding_point(self, "A"))
        self.assertEqual(3, Model.corresponding_point(self, "B"))
        self.assertEqual(0, Model.corresponding_point(self, "F"))
