from django.test import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized


class AuthorRegisterFormUniTest(TestCase):
    @parameterized.expand(
        [
            ("username", "Username..."),
            ("email", "E-mail..."),
            ("first_name", "First Name..."),
            ("last_name", "Last Name..."),
            ("password", "Your password"),
            ("confirm_password", "Confirm Password..."),
        ]
    )
    def test_first_name_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs["placeholder"]
        self.assertEqual(current_placeholder, placeholder)
