def binary_to_hex(binary_str):
    # Convert binary string to integer
    decimal_num = int(binary_str, 2)
    # Convert integer to hexadecimal string
    hex_str = hex(decimal_num)[2:]  # [2:] removes the '0x' prefix from hex()
    return hex_str.upper()  # Convert to uppercase for standard hexadecimal format

# Example usage:
binary_number = "101101"
hexadecimal_number = binary_to_hex(binary_number)
print(f"The hexadecimal equivalent of binary {binary_number} is {hexadecimal_number}")
