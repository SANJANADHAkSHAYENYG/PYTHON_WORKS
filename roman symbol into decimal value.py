roman_numeral=input("Enter a Roman numeral:")
def roman_to_decimal(roman):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    d = 0
    pv = 0

    for symbol in reversed(roman):
        value = dict[symbol]
        if value < pv:
            d-= value
        else:
            d+= value
        pv = value
    return d
decimal_number = roman_to_decimal(roman_numeral)
print("The decimal equivalent is:", decimal_number)
