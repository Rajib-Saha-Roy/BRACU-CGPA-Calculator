from unittest import TestCase
from controller import Controller
import controller
from view import View


class TestController(TestCase):
    def main(self):
        self.view = View(self)

    @classmethod
    def setUpClass(cls):
        """view.entry1 = 0
        view.entry2 = 0"""
        pass

    def test_add_courses(self):
        self.assertEqual(2, Controller.add_courses(self, "2"))
        print("done")

    def test_calc_CG(self):
        self.assertEqual(4, Controller.calc_CG(self, 3, 4, 3, 4))
        print("We are not interested to UI part. So method is modified")


if __name__ == '__main__':
    TestCase.main()
