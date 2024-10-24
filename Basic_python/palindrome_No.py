def is_palindrome(num):
    if num < 0:
        return False
    
    original_num = num
    reversed_num = 0  
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    if original_num == reversed_num:
        print(f"{original_num} is a palindrome.")
    else:
        print(f"{original_num} is not a palindrome.")

num = int(input("Enter a number: "))
is_palindrome(num)
