import requests

class LordOfTheRings:
	""" SDK for Lord of the rings api """
	def __init__(self, base_url, token):
		self.base_url = base_url
		self.res = self.set_session(token)

	def set_session(self, token):
		""" sets session """
		session = requests.session()
		session.headers = {'authorization': f'Bearer {token}'}
		return session

	def _base_request(self, path, the_id=None, extra_path=''):
		""" creates the request"""
		if the_id is None:
			url = f'{self.base_url}/{path}'
		else:
			if extra_path:
				url = f'{self.base_url}/{path}/{the_id}/{extra_path}'
			else:
				url = f'{self.base_url}/{path}/{the_id}'
			
		resp = self.res.get(url)
		return resp

	def movie(self, the_id=None, extra_path=''):
		""" Returns movie. If the_id is given returns a specific book"""
		path = 'movie'
		return self._base_request(path, the_id)

	def quote(self, the_id=None, extra_path=''):
		""" Returns quote. If the_id is given returns a specific book"""
		path = 'quote'
		return self._base_request(path, the_id)