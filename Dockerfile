FROM ghcr.io/astral-sh/uv:python3.12-alpine AS builder

WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Install dependencies into a virtual environment
RUN uv sync --frozen --no-dev

# Copy application code
COPY . .

# Final stage - minimal runtime image
FROM python:3.12-alpine

WORKDIR /app

# Copy the virtual environment and application from builder
COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app .

# Activate virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Run the application
CMD ["python", "main.py"]