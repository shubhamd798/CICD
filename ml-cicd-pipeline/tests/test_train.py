import unittest
import os

class TestTraining(unittest.TestCase):
    def test_model_exists(self):
        self.assertTrue(os.path.exists("model.pkl"))

if __name__ == '__main__':
    unittest.main()


### FILE: Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]