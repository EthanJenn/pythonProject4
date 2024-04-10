# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def decode(password):
    new_password = ""
    for digit in password:
        new_password += (digit-3) % 10
