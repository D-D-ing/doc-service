FROM python:3

VOLUME /app/res
VOLUME /app/log

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY src/server.py /app
COPY requirements.txt /app
COPY src /app/src


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5002



CMD ["python", "server.py"]