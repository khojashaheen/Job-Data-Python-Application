import unittest
import toml
from main import read_api

class TestMainScript(unittest.TestCase):
    def test_read_api(self):
        app_config = toml.load('../config/config.toml')
        url = app_config['api']['url']
        status_code = read_api(url).status_code
        self.assertEqual(200,status_code)

if __name__ == '__main__':
    unittest.main()