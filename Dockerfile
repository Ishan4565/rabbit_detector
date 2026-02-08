FROM python:3.10-slim

WORKDIR /app

# We only copy the files first to keep the build fast
COPY . .

# Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
