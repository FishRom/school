def to_hex(n):
    hex_chars = "0123456789ABCDEF"
    if n < 16:
        return hex_chars[n]
    else:
        return to_hex(n // 16) + hex_chars[n % 16]


number = int(input())
hex_number = to_hex(number)
print(hex_number)