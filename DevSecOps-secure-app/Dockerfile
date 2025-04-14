FROM python:3.9-slim
WORKDIR /app
COPY app/ ./app/
COPY tests/ ./tests/
COPY requirements.txt .
COPY sonar-project.properties .
RUN pip install -r requirements.txt
# COPY . .
CMD ["python", "app/main.py"]
