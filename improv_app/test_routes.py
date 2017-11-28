from flask.ext.testing import TestCase
from . import app

class MyTest(TestCase):

    def create_app(self):
        return app

class improv_test(MyTest):
    def test_home_page(self):
        self.client.get('/')
        self.assert_template_used('index.html')
    def test_signup_page(self):
        self.client.get('/signup')
        self.assert_template_used('signup.html')
    def test_create_page(self):
        self.client.get('/create')
        self.assert_template_used('create_page.html')
    def test_search_page(self):
        self.client.get('/search')
        self.assert_template_used('search.html')
    def test_chat_page(self):
        self.client.get('/session')
        self.assert_template_used('chatroom.html')
