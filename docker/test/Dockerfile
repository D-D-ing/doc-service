FROM python:3

VOLUME /app/res
VOLUME /app/log
VOLUME /app/results

# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY python/requirements.txt /app
COPY python/src /app/src
COPY python/tests /app/tests


# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python3","-m", "pytest", "--junitxml", "/app/results/results.xml", "tests/"]
