FROM python:3.11-slim-bookworm

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set working directory
WORKDIR /app

# Copy configuration files
COPY pyproject.toml uv.lock ./

# Install dependencies
# We use --system to install into the system python, avoiding the need for a virtualenv in the container
RUN uv sync --frozen --no-dev --system

# Copy source code
COPY src/ ./src/

# Set python path
ENV PYTHONPATH=/app/src

# Command to run
CMD ["python", "-m", "ml_project.main"]
