import unittest
from lord_of_the_rings_sdk import LordOfTheRings 

class TestEndpoints(unittest.TestCase):
	def test_movie(self):
		api = LordOfTheRings('fDCIpmKnesCL7xZEl4MN')
		resp = api.movie()
		self.assertEqual(resp.status_code, 200)

	def test_quote(self):
		api = LordOfTheRings('fDCIpmKnesCL7xZEl4MN')
		resp = api.quote()
		self.assertEqual(resp.status_code, 200)

unittest.main()