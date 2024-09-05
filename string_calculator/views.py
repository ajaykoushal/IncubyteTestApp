from django.shortcuts import render


class StringCalculator:
    def _process_numbers(self, numbers: str):
        if not numbers:
            return []
        
        numbers = numbers.strip().strip("'\"")

        # Handle custom delimiters
        if numbers.startswith('//'):
            delimiter_end = numbers.find('\n')  
            if delimiter_end != -1:
                custom_delimiter = numbers[2:delimiter_end].strip()
                numbers = numbers[delimiter_end+1:].replace(custom_delimiter, ',')
        else:
            numbers = numbers.replace('\\n', '\n').replace('\n', ',')
        
        return [num.strip() for num in numbers.split(',') if num.strip()]

    def _calculate(self, numbers, operation):
        number_list = self._process_numbers(numbers)
        negatives = [int(num) for num in number_list if int(num) < 0]

        if negatives:
            raise Exception(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
        
        if not number_list:
            return 0
        
        if operation == "add":
            return sum(map(int, number_list))
        elif operation == "subtract":
            return int(number_list[0]) - sum(map(int, number_list[1:]))
        elif operation == "multiply":
            product = 1
            for num in map(int, number_list):
                product *= num
            return product
        elif operation == "divide":
            total = float(number_list[0])
            for num in map(float, number_list[1:]):
                if num == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                total /= num
            return total

    def add(self, numbers: str) -> int:
        return self._calculate(numbers, "add")

    def subtract(self, numbers: str) -> int:
        return self._calculate(numbers, "subtract")

    def multiply(self, numbers: str) -> int:
        return self._calculate(numbers, "multiply")

    def divide(self, numbers: str) -> float:
        return self._calculate(numbers, "divide")


def calculator_view(request):
    result = None
    string_numbers = ""
    error_message = ""
    action_input = ""

    if request.method == 'POST':
        string_numbers = request.POST.get('string_numbers')
        action_input = request.POST.get('action_input')
        calculator = StringCalculator()
        try:
            if action_input == 'add':
                result = calculator.add(string_numbers)
            elif action_input == 'sub':
                result = calculator.subtract(string_numbers)
            elif action_input == 'div':
                result = calculator.divide(string_numbers)
            elif action_input == 'mul':
                result = calculator.multiply(string_numbers)
        except Exception as e:
            error_message = str(e)
    
    return render(request, 'calculator/calculator.html', {
        'string_numbers': string_numbers,
        'result': result,
        'error_message': error_message,
        'action_input': action_input}
    )
