def truncate_hundredth(number):
    number_string = str(number)
    if "." in number_string:
        decimal_index = number_string.index(".")
        return number_string[:decimal_index + 3]
    return number_string