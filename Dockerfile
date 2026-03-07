# 1. Use an official, lightweight Python 3.12 image
FROM python:3.12-slim

# 2. Set environment variables to make Python run better in containers
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set the working directory inside the container
WORKDIR /code

# 4. Copy ONLY the requirements first (This leverages Docker's caching to speed up builds)
COPY requirements.txt .

# 5. Install dependencies without saving the heavy cache files
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of the application code
COPY ./app /code/app

# 7. Security Best Practice: Create a non-root user to run the app
RUN useradd -m myuser
USER myuser

# 8. Expose the port FastAPI runs on
EXPOSE 8000

# 9. Command to start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]