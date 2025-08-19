# Use official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy the calculator script into the container
COPY calculator.py .

# Set default command to run the script (you can change this if needed)
CMD ["python", "calculator.py"]