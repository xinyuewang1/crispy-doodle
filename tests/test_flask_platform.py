import unittest

import flask_platform


class Flask_platformTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flask_platform.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to flask_platform', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
