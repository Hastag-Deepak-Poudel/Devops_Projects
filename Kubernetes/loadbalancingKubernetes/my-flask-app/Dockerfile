# 1. Use a lightweight Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only requirements first to leverage Docker cache
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Expose the port Flask runs on (default is 5000)
EXPOSE 5000

# 7. Command to run the application
# Use '0.0.0.0' to make the server accessible outside the container
CMD ["python", "app.py"]
