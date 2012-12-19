




class check_superuser(object):
	def __call__(self, obj, request, *args, **kwargs):
		return request.user.is_superuser


def can_get_detail(request, url_argument):
	username = request.user.username
	if username == url_argument:
		return True
	else:
		return False
