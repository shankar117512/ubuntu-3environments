FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy entire project
COPY . .

# Run collectstatic AFTER project is copied
RUN python manage.py collectstatic --noinput

# Start server
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
