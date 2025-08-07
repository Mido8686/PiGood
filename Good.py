import mpmath

# Set the number of digits you want to calculate
def generate_pi(digits: int):
    mpmath.mp.dps = digits + 1  # Set precision (one extra digit to ensure rounding is correct)
    pi_value = str(mpmath.mp.pi)[2:]  # Get Pi digits as a string, removing the "3."
    return pi_value

def main():
    print("PiGood: Generating Pi digits endlessly... (Ctrl+C to stop)")

    digits_per_request = 100  # Number of digits to generate per request
    
    while True:
        input(f"Press Enter to generate next {digits_per_request} digits of Pi...")
        
        # Generate the next batch of digits
        new_digits = generate_pi(digits_per_request)
        
        # Print only the newly generated digits
        print(new_digits)

if __name__ == "__main__":
    main()
