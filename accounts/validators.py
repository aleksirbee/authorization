import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8 or len(password) > 15: # password length
            raise ValidationError(
                "The password must be between 8 and 15 characters long.",
            code='password_length',
            )
        if not re.search(r'[A-Z]', password): # password upper letter
            raise ValidationError(
                _("The password must contain at least one uppercase letter."),
            code="password_no_apper",
            )
        if not re.search(r'[a-z]', password): # password lower letter
            raise ValidationError(
                _("The password must contain at least one lower letter."),
            code="password_no_lower",
            )
        if not re.search(r'\d', password): # password contain number
            raise ValidationError(
                _("The password must contain at least one number."),
            code="password_no_number"
            )
        if not re.search(r'[!@#$%^&*()<>?,./:;{}|]', password):
            raise ValidationError(
                ("The password must contain at least one special character."),
            code="password_no_special",
            )
        
    def get_help_text(self):
        return _("The password must be between 8 and 15 characters long and include at least one lowercase and one uppercase letter, one number, and one special character (!, @, #, $, ...).")