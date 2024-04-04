#get square numbers

def get_square_numbers(numbers):
    square_numbers = []
    for n in numbers:
        square_numbers.append(n*n)
    print(square_numbers)
numbers = [2,5,8,9]
get_square_numbers(numbers)        