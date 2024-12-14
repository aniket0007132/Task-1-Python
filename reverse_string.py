def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string
input_str = "hello"
output_str = reverse_string(input_str)
print("The reversed string is:", output_str)
