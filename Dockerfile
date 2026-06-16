FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir streamlit boto3 python-dotenv
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]