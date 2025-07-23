# Install system dependencies and Node.js
RUN apt-get update && \
    apt-get install -y curl ffmpeg aria2 && \
    curl -fsSL https://deb.nodesource.com/setup_19.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN python -m pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Optional: Make script executable (only if needed)
# RUN chmod +x start.py

# Start the bot
CMD ["python3", "start.py"]
