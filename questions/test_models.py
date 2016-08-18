# coding:utf-8


import unittest

import django

from models import QuestionModel, AnswerModel, TagModel
from models import DoQuestion

django.setup()


class QuestionModelTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.tag1 = {
            'name': "tag1"
        }
        self.tag2 = {
            'name': "tag2"
        }

        tag1 = TagModel.objects.create(**self.tag1)
        tag2 = TagModel.objects.create(**self.tag2)

        self.answer = {
            'answer': "answer",
            'detail': "detail"
        }

        answer = AnswerModel.objects.create(**self.answer)

        self.data = {
            'title': 'error',
            # "tags":[]
        }
        question = QuestionModel.objects.create(**self.data)
        question.tags = [tag1, tag2]
        question.answers = [answer]
        question.save()

    def test_get_by_id(self):
        questions = DoQuestion.get_by_id(1)
        print questions


        # def test_detail_info(self):
        #     self.maxDiff = None
        #     invitation = BookingModel.objects.get(pk=self.data['booking_id'])
        #     passenger_info, error = InformationModelUtil.get_by_id(
        #         self.data.pop('passenger_info_id'))
        #     self.data['passenger_info'] = None if error else passenger_info
        #     self.assertEqual(self.data, invitation.detail_info())
        #

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        QuestionModel.objects.all().delete()

# class UserBookingModelTest(unittest.TestCase):
#
#     def setUp(self):
#         unittest.TestCase.setUp(self)
#         self.uucode = 19880521
#         self.model = UserBookingModel(self.uucode, 'xxxx')
#
#     def test_add(self):
#         passenger_info_id = 'xxxx'
#         flag, self.invitation_id = self.model.add(
#             passenger_info_id,
#             '2015-05-28 08:00:00', '5.00', 1, 'xxxx', 'xxx', '13000000000')
#         self.assertEqual(flag, True)
#
#     def test_get_list_auto_delete(self):
#         flag, bookings = self.model.get_list()
#         self.assertEqual(flag, True)
#         self.assertLessEqual(len(bookings), 100)
#
#     def tearDown(self):
#         pass


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(BookingModelTest('test_detail_info'))
# suite.addTest(UserBookingModelTest('test_add'))
# suite.addTest(UserBookingModelTest('test_get_list_auto_delete'))
# unittest.TextTestRunner().run(suite)
