FROM python:3

VOLUME /app/res
VOLUME /app/log
VOLUME /app/tests
VOLUME /app/results

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY ./requirements.txt /app
COPY src /app/src


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#sh "python3 -m pytest --junitxml results.xml tests/"
CMD ["python -m pytest --junitxml /app/results/results.xml tests/"]
