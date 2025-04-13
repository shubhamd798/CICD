import unittest
import os

class TestTraining(unittest.TestCase):
    def test_model_exists(self):
        self.assertTrue(os.path.exists("model.pkl"))

if __name__ == '__main__':
    unittest.main()