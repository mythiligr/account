from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

# ##########################################################
# ## ClassName	: AccountActivationTokenGenerator
#	 Output		: Generate active token for inactive user 	
#	 Usage 		: Signup with email Registration off user
# ###########################################################
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)
        )

account_activation_token = AccountActivationTokenGenerator()