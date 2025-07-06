# Stage 1: Builder (installs dependencies)
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy only dependencies first to leverage caching
COPY requirements.txt .

# Install dependencies without keeping cache
RUN pip install -r requirements.txt --no-deps && \
rm -rf /root/.cache/pip

# Stage 2: Final lightweight image
FROM python:3.11-slim

WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.*/site-packages /usr/local/lib/python3.*/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application files
COPY .streamlit /root/.streamlit
COPY .streamlit /app/.streamlit
COPY . .

# Set entrypoint command
CMD ["streamlit", "run", "main.py"]
