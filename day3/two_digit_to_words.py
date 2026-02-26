def two_digit_to_words(n):
    """
    Convert a two-digit number to its English words representation.
    """
    if n < 10 or n > 99:
        return "Number out of range"
    
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens_multiple = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    if n >= 10 and n < 20:
        return tens[n - 10]
    else:
        ten_digit = n // 10
        one_digit = n % 10
        words = tens_multiple[ten_digit]
        if one_digit != 0:
            words = words + " " + ones[one_digit]
        return words
    

# Example usage:
print(two_digit_to_words(45))  # Output: Forty Five
print(two_digit_to_words(19))  # Output: Nineteen