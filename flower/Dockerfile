# Pull base image.
FROM python:2.7.11

# Add user
RUN groupadd user && useradd --create-home --home-dir /code -g user user
WORKDIR /code

# Download pip
ENV PYTHON_PIP_VERSION 7.1.2
RUN curl -fSL 'https://bootstrap.pypa.io/get-pip.py' | python2
COPY . /code
RUN pip install -r requirements.txt
EXPOSE 5555

# Define default command.
USER user
CMD ["celery", "flower", "--port=5555", "--broker=redis://redis:6379"]