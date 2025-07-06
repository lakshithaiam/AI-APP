# Use a slim Python base image
FROM python:3-slim

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files (and ignore others with .dockerignore)
COPY requirements.txt .

# Install pip, update it, then install dependencies in a single layer and clean up cache
RUN pip install --upgrade pip && \
    pip install -r requirements.txt --no-deps && \
    rm -rf /root/.cache/pip

# Copy the rest of the application code
COPY .streamlit /root/.streamlit
COPY .streamlit /app/.streamlit
COPY . .

# Command to run the application
CMD ["streamlit", "run", "main.py"]
