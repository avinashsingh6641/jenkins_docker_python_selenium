FROM mcr.microsoft.com/playwright:v1.45.0-jammy

WORKDIR /tests

# Install any system deps (optional)
# RUN apt-get update && apt-get install -y python3 python3-pip

# Copy your test code
COPY . .

# Install dependencies (if required) jhj
# Example for Python:
# RUN pip install -r requirements.txt

# Example for Node:
# RUN npm install

ENTRYPOINT [ "bash" ]
