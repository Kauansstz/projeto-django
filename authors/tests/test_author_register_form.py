from authors.forms import RegisterForm
from unittest import TestCase
from django.test import TestCase as DjangoTestCase
from parameterized import parameterized
from django.urls import reverse


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand(
        [
            ("username", "Your username"),
            ("email", "Your e-mail"),
            ("first_name", "Ex.: John"),
            ("last_name", "Ex.: Doe"),
            ("password", "Type your password"),
            ("password2", "Repeat your password"),
        ]
    )
    def test_fields_placeholder(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs["placeholder"]
        self.assertEqual(current_placeholder, placeholder)

    @parameterized.expand(
        [
            (
                "username",
                (
                    "Username must have letters, nubemrs or one of those e @.+-_."
                    "The lenght should be between 4 and 150 characters."
                ),
            ),
            ("email", "The e-mail must be valid."),
            (
                "password",
                (
                    "Password must have at least one uppercase letter, "
                    "one lowercase letter and one number. The length should be "
                    "at least 8 characters."
                ),
            ),
        ]
    )
    def test_fields_help_text(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

    @parameterized.expand(
        [
            ("username", "Username"),
            ("first_name", "First name"),
            ("last_name", "Last name"),
            ("email", "E-mail"),
            ("password", "Password"),
            ("password2", "Password2"),
        ]
    )
    def test_fields_label(self, field, needed):
        form = RegisterForm()
        current = form[field].field.label
        self.assertEqual(current, needed)


class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            "username": "user",
            "first_name": "first",
            "last_name": "last",
            "email": "email@anyemail.com",
            "password": "Str0ngP@ssword1",
            "password2": "Str0ngP@ssword1",
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand(
        [
            ("username", "This field must not be empty"),
            ("first_name", "Write your first name"),
            ("last_name", "Write your last name"),
            ("password", "Password must not be empty"),
            ("password2", "Please, repeat your password"),
            ("email", "Email is required"),
        ]
    )
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ""
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode("utf-8"))
        self.assertIn(msg, response.context["form"].errors.get(field))

    def test_username_field_min_lengt_should_be_4(self):
        self.form_data["username"] = "hoa"
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = "Username must have at least 4 characters"
        self.assertIn(msg, response.content.decode("utf-8"))
        self.assertIn(msg, response.context["form"].errors.get("username"))

    def test_username_field_mmax_lengt_should_be_150(self):
        self.form_data["username"] = "a" * 151
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = "Username must have lass than 150 characters"
        # self.assertIn(msg, response.content.decode("utf-8"))
        self.assertIn(msg, response.context["form"].errors.get("username"))

    def test_password_field_have_lower_upper_casa_latters_and_numbers(self):
        self.form_data["password"] = "1AAb15@6"
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = (
            "Password must have at least one uppercase letter, "
            "one lowercase letter and one number. The length should be "
            "at least 8 characters."
        )
        self.assertNotIn(msg, response.context["form"].errors.get("password"))

    def test_password_field_password_and_password_confirmation_are_equal(self):
        self.form_data["password"] = "1AAb15@6"
        self.form_data["password2"] = "1AAb15@6!"
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)

        msg = "Password and password2 must be equal"
        self.assertIn(msg, response.context["form"].errors.get("password"))
        self.form_data["password"] = "1AAb15@6"
        self.form_data["password2"] = "1AAb15@6"
        url = reverse("authors:create")
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertNotIn(msg, response.content.decode("utf-8"))

    def test_send_get_request_to_registration_create_view_return_404(self):
        url = reverse("authors:create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_email_confirmation_are_ok(self):
        url = reverse("authors:create")

        self.client.post(url, data=self.form_data, follow=True)

        response = self.client.post(url, data=self.form_data, follow=True)

        msg = "User e-mail is already in use"
        self.assertIn(
            msg,
            response.context["form"].errors.get("email"),
        )
        self.assertIn(msg, response.content.decode("utf-8"))
