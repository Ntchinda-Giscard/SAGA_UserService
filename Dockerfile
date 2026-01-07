FROM python:slim-bookworm as builder

WORKDIR /app

# Install uv
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Create virtual environment and install dependencies
RUN uv venv /opt/venv
RUN uv sync --python /opt/venv/bin/python

# Final stage
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application code
COPY . .

ENV PATH="/opt/venv/bin:$PATH"

CMD ["python", "main.py"]