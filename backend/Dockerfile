# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install graphics dependencies
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx libgl1
    
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Spacy model
RUN pip install spacy
RUN python -m spacy download en_core_web_sm


# Copy the rest of the app into the container
COPY app/ .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME AIRecruiter

# Run uvicorn when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
