from django.shortcuts import render


class StringCalculator:
    
    def _process_numbers(self, numbers: str):
        if not numbers:
            return []

        # Strip leading and trailing spaces
        numbers = numbers.strip()
        
        # remove additional quotes from string if there any
        if "'" in numbers:
            numbers = numbers.strip("'")
        elif '"' in numbers:
            numbers = numbers.strip('"')


        # Handle custom delimiters
        if numbers.startswith('//'):
            delimiter_end = numbers.find('\n')
            if delimiter_end != -1:
                custom_delimiter = numbers[2:delimiter_end].strip()
                numbers = numbers[delimiter_end+1:]
                # Replace all occurrences of the custom delimiter and newline characters with a comma
                numbers = numbers.replace(custom_delimiter, ',')
        else:
            # Replace default delimiters (comma and newline) with a comma
            numbers = numbers.replace('\\n', '\n').replace('\n', ',')
        
        # Replace all delimiters with a comma
        numbers = numbers.replace(',', ',')
        
        # Split the string by comma and strip any extra spaces
        number_list = numbers.split(',')
        number_list = [num.strip() for num in number_list if num.strip()]

        return number_list

    def add(self, numbers: str) -> int:
        number_list = self._process_numbers(numbers)
        total = 0
        negatives = []

        for num in number_list:
            try:
                n = int(num)
                if n < 0:
                    negatives.append(n)
                total += n
            except ValueError:
                raise ValueError("Invalid input")

        if negatives:
            raise Exception(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

        return total
