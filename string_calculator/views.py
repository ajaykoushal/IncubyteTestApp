from django.shortcuts import render

class StringCalculator:

    # Helper method to process the input string and extract valid numbers
    def _process_numbers(self, numbers: str):
        # Return an empty list if the input is an empty string
        if not numbers:
            return []
        
        # Strip leading/trailing spaces and remove extra quotes (single or double) if present
        numbers = numbers.strip().strip("'\"")

        # Check for custom delimiter syntax (e.g., "//[delimiter]\n[numbers...]")
        if numbers.startswith('//'):
            delimiter_end = numbers.find('\n')
            if delimiter_end != -1:
                # Extract the custom delimiter and replace it with a comma in the string
                custom_delimiter = numbers[2:delimiter_end].strip()
                numbers = numbers[delimiter_end + 1:].replace(custom_delimiter, ',')
        else:
            # If no custom delimiter is provided, handle newline and default commas as delimiters
            numbers = numbers.replace('\\n', '\n').replace('\n', ',')

        # Split the processed string by commas and remove any extra spaces around each number
        return [num.strip() for num in numbers.split(',') if num.strip()]

    # General method to handle different arithmetic operations (add, subtract, multiply, divide)
    def _calculate(self, numbers, operation):
        # Process the input string to get a list of numbers
        number_list = self._process_numbers(numbers)

        # Collect negative numbers for validation
        negatives = [int(num) for num in number_list if int(num) < 0]

        # Raise an exception if there are any negative numbers
        if negatives:
            raise Exception(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        # Handle the case of an empty input list
        if not number_list:
            # Return 0 for all operations except multiply (where the neutral element is 1)
            return 0 if operation != "multiply" else 1
        
        # Perform the requested arithmetic operation
        if operation == "add":
            return sum(map(int, number_list))  # Sum all numbers
        elif operation == "subtract":
            # Subtract all numbers from the first number in the list
            return int(number_list[0]) - sum(map(int, number_list[1:]))
        elif operation == "multiply":
            # Multiply all numbers together
            product = 1
            for num in map(int, number_list):
                product *= num
            return product
        elif operation == "divide":
            # Divide the first number by the subsequent numbers, raising an exception if division by zero occurs
            total = float(number_list[0])
            for num in map(float, number_list[1:]):
                if num == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                total /= num
            return total

    # Method for adding numbers (delegates to _calculate with the 'add' operation)
    def add(self, numbers: str) -> int:
        return self._calculate(numbers, "add")

    # Method for subtracting numbers (delegates to _calculate with the 'subtract' operation)
    def subtract(self, numbers: str) -> int:
        return self._calculate(numbers, "subtract")

    # Method for multiplying numbers (delegates to _calculate with the 'multiply' operation)
    def multiply(self, numbers: str) -> int:
        return self._calculate(numbers, "multiply")

    # Method for dividing numbers (delegates to _calculate with the 'divide' operation)
    def divide(self, numbers: str) -> float:
        return self._calculate(numbers, "divide")


# Django view to handle the input from the HTML form and display the calculation result
def calculator_view(request):
    # Initialize variables to store the result, input string, and error messages
    result = None
    string_numbers = ""
    error_message = ""
    action_input = ""

    # Handle POST requests (form submission)
    if request.method == 'POST':
        # Get the numbers string and selected operation (add, subtract, multiply, divide) from the POST data
        string_numbers = request.POST.get('string_numbers')
        action_input = request.POST.get('action_input')

        # Initialize the calculator instance
        calculator = StringCalculator()

        try:
            # Perform the operation based on the selected action and compute the result
            if action_input == 'add':
                result = calculator.add(string_numbers)
            elif action_input == 'sub':
                result = calculator.subtract(string_numbers)
            elif action_input == 'div':
                result = calculator.divide(string_numbers)
            elif action_input == 'mul':
                result = calculator.multiply(string_numbers)
        except Exception as e:
            # Capture and display any error (e.g., negative numbers or division by zero)
            error_message = str(e)

    # Prepare the context for rendering the result in the template
    context = {
        'string_numbers': string_numbers,
        'action_input': action_input,
        'result': result,
        'error_message': error_message
    }

    # Render the template with the result and context
    return render(request, 'calculator/calculator.html', context)