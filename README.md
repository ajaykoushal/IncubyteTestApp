# IncubyteTestApp
String calculator

## Description

The String Calculator App is a simple Django web application that performs basic arithmetic operations (addition, subtraction, multiplication, division) on a string of comma-separated or newline-separated numbers. It also supports custom delimiters.

### Features

- **Addition**: Computes the sum of a list of numbers.
- **Subtraction**: Computes the result of subtracting a list of numbers from the first number.
- **Multiplication**: Computes the product of a list of numbers.
- **Division**: Computes the result of dividing the first number by a list of numbers.

### Requirements

- Docker (version 27.1.1 or higher)
- Docker Compose (version 2.23.3 or higher)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ajaykoushal/IncubyteTestApp.git
   cd IncubyteTestApp

2. **Run Application using docker compose**

   ```bash
   # Build the Docker Image
   docker-compose build
   or
   docker-compose -f docker-compose.yml build
   
   #Run the Docker Container
   docker-compose up
   or
   docker-compose -f docker-compose.yml up

3. **Run Tests Cases**
    ```bash
   # Build the Docker Image
   docker-compose run web python manage.py test
   or 
   docker-compose -f docker-compose.yml run web python manage.py test
