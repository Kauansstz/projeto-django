from django.test import TestCase
from authors.forms import RegisterForm


class AuthorRegisterFormUniTest(TestCase):
    def test_first_name_placeholder_is_correct(self):
        form = RegisterForm()
        placeholder = form["first_name"].field.widget.attrs["placeholder"]
        self.assertEqual("First Name...", placeholder)
