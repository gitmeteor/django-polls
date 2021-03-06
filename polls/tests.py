from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone

from .models import Question

class QuestionMethodTests(TestCase):
    def test_recently_with_future(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        