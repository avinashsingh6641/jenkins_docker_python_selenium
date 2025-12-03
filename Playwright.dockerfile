FROM mcr.microsoft.com/playwright/python:v1.49.1-jammy

WORKDIR /tests

# Copy all repo files into test container
COPY . .

# Install Python requirements
RUN pip install --no-cache-dir -r requirements.txt

# # Upgrade the Python Playwright library
# RUN pip install --upgrade playwright

# IMPORTANT: Upgrade the browsers too
RUN playwright install --with-deps

CMD ["bash"]
