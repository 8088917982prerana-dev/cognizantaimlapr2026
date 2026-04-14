"""
application entry point
"""

import random


def generate_otp():
    """
    this function generates a random otp
    """
    otp = random.randint(100000, 999999)
    return otp


if __name__ == "__main__":
    otp = generate_otp()
    print("Generated OTP:", otp)
