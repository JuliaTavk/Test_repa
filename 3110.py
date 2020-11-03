import requests
import unittest

Suscsess_code = 200 
sites_list = ['https://tut.by', 'https://onliner.by', 'https://vk.com', 'https://google.com', 'https://twitter.com']

class TestSites(unittest.TestCase):
	def test_sites_list(self):
		for site in sites_list:
			r = requests.get(site)
			self.assertEqual (r.status_code, Suscsess_code)
			print(site, Suscsess_code)

if __name__ == '__main__':
    unittest.main()