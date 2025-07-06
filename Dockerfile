# Use a slim Python base image
FROM python:3-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/pip

# Copy Streamlit config (optional: one location is enough)
COPY .streamlit /root/.streamlit

# Copy app code
COPY . .

# Streamlit settings: disable auto-reload to avoid inotify errors
ENV STREAMLIT_SERVER_RUNONSAVE=false
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run the app
CMD ["streamlit", "run", "main.py"]
