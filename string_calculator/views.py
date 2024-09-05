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

    def _calculate(self, numbers):
        number_list = self._process_numbers(numbers)
        negatives = [int(num) for num in number_list if int(num) < 0]

        if negatives:
            raise Exception(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
        
        if not number_list:
            return 0
        return sum(map(int, number_list))

    def add(self, numbers: str) -> int:
        return self._calculate(numbers)


def calculator_view(request):
    result = None
    string_numbers = ""
    error_message = ""

    if request.method == 'POST':
        string_numbers = request.POST.get('string_numbers')
        calculator = StringCalculator()
        try:
            result = calculator.add(string_numbers)
        except Exception as e:
            error_message = str(e)
    
    return render(request, 'calculator/calculator.html', {
        'string_numbers': string_numbers,
        'result': result,
        'error_message': error_message}
    )
