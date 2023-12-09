# Start from python image 
FROM python:3.10

# Set the working directory
WORKDIR /app


# Copy the application code
COPY . .

# Install nmap
RUN apt-get update && apt-get install -y nmap

# Open port for access to nmap scans 
EXPOSE 4000

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1  

# Run the application
CMD [ "python", "./scanner.py" ]
