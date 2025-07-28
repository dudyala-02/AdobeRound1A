# Use Python 3 base image
FROM --platform=linux/amd64 python:3.9-slim

# Set working directory
WORKDIR /app

# Copy your file
COPY 1acode.py /app/1acode.py

# Install necessary libraries
RUN pip install pdfplumber

# Create input/output folders
RUN mkdir /app/input /app/output

# Set command to run your script
CMD ["python", "1acode.py"]
