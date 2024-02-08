# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY src .

# Make port 80 available to the world outside this container
# This is optional, adjust according to your needs
EXPOSE 80

# Define environment variable
# This is optional, adjust according to your needs
ENV NAME Stag

# Run app.py when the container launches
CMD ["python", "app.py"]
