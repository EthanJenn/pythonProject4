def decode_password(password):
    new_password = ""
    for digit in password:
        new_password += str(int(digit-3) % 10)

    return new_password
