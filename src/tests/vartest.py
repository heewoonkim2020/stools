import unittest
import stools

class TestMain(unittest.TestCase):
    def test_variable_set(self):
        stools.variables.set('case', 'unittest')
        self.assertTrue(stools.variables.get('case') == 'unittest', 'Error on variable get')

if __name__ == '__main__':
    unittest.main(__name__)