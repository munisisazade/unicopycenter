class ForceDefaultLanguageMiddleware(object):
	def process_request(self, request):
		try:
			if request.META['HTTP_ACCEPT_LANGUAGE']:
				del request.META['HTTP_ACCEPT_LANGUAGE']
		except:
			pass
