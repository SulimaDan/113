# def display_quote():
#     quote = (
#         "Don't compare yourself with anyone in this world…\n"
#         "if you do so, you are insulting yourself.\n"
#         "Bill Gates"
#     )
#     print(quote)

# display_quote()






# def display_even_numbers(start, end):
#     if start > end:
#         start, end = end, start
    
#     print(f"Even numbers between {start} and {end} are:")
    
#     for number in range(start, end + 1):
#         if number % 2 == 0:
#             print(number)

# display_even_numbers(3, 15)



# def display_square(side_length, char, filled):
#     for i in range(side_length):
#         if filled or i == 0 or i == side_length - 1:
#             print(char * side_length)
#         else:
#             print(char + ' ' * (side_length - 2) + char)

# display_square(5, '*', True)
# print()
# display_square(5, '*', False)




# def find_minimum(a, b, c, d, e):
#     return min(a, b, c, d, e)

# minimum = find_minimum(3, 5, 1, 9, 2)
# print(f"The minimum value is: {minimum}")






# def product_in_range(start, end):
#     if start > end:
#         start, end = end, start
    
#     product = 1
#     for number in range(start, end + 1):
#         product *= number
    
#     return product

# result1 = product_in_range(5, 25)
# result2 = product_in_range(25, 5)
# print(f"The product of numbers between 5 and 25 is: {result1}")
# print(f"The product of numbers between 25 and 5 is: {result2}")



# def count_digits(number):
#     number_str = str(abs(number)) 
#     return len(number_str)

# digits_count = count_digits(3456)
# print(f"The number of digits in 3456 is: {digits_count}")

# digits_count = count_digits(-987654)
# print(f"The number of digits in -987654 is: {digits_count}")



# def is_palindrome(number):
#     number_str = str(number)
#     return number_str == number_str[::-1]

# print(is_palindrome(121)) 
# print(is_palindrome(-121)) 
# print(is_palindrome(12321)) 
# print(is_palindrome(123)) 




def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

print(is_palindrome(123321)) 
print(is_palindrome(546645))  
print(is_palindrome(421987))  
print(is_palindrome(12321)) 
print(is_palindrome(12345))  










