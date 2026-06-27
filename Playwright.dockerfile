FROM mcr.microsoft.com/playwright/python:v1.49.1-jammy

WORKDIR /app

# Copy all repo files into test container
COPY . .

# Install Python requirements
RUN apt-get update && \
    apt-get install -y make && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN python --version
RUN pip --version
RUN python -m pip list
RUN python -m pytest --version

# # Upgrade the Python Playwright library
# RUN pip install --upgrade playwright

# IMPORTANT: Upgrade the browsers too
# RUN playwright install --with-deps

# CMD ["make", "test"]
#CMD ["sh", "-c", "echo PWD=$(pwd) && ls -la && env"]
# CMD ["bash", "-c", "echo 'Starting tests...' && make test"]
CMD ["echo", "Hello from Docker container"]
