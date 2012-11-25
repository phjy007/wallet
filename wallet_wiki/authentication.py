from django.contrib import auth
from tastypie.authentication import Authentication
from wallet_wiki.models import User
# import hashlib

class WalletAuthentication(Authentication):
	def is_authentication(self, request, **kwargs):
		req_username = request.user.username
		req_pwd = request.user.password
		user_result = User.object.get(username=req_username)
		if user_result = None:
			return False
		# if hashlib.md5(user_result.pwd) != req_pwd:
		# 	return False
		return True	
 


class WalletAuthorization():
	pass


def login_view(request):
	auth.logout(request)
