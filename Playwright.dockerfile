FROM mcr.microsoft.com/playwright/python:v1.49.1-jammy

WORKDIR /tests

# Copy all repo files into test container
COPY . .

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
# RUN playwright install --with-deps

CMD ["bash"]
