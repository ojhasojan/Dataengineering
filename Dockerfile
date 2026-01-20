# use official python image
FROM python:3.11-slim

#set working directory inside the container
WORKDIR /app

# copy requirements first

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


#COPY application code 
COPY . .

# Run the script
CMD ["python" , "daily_sales_load.py"]