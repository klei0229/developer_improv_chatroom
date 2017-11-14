from flask.ext.testing import TestCase
from . import app

class MyTest(TestCase):

    def create_app(self):
        return app

class improv_test(MyTest):
    render_templates = False
    def test_assert_mytemplate_used(self):
        response = self.client.get("/templates/")
        self.assert_template_used('index.html')
