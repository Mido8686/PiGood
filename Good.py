import mpmath

# Set the number of digits you want to calculate
def generate_pi(digits: int):
    mpmath.mp.dps = digits + 1  # Set precision (one extra digit to ensure rounding is correct)
    pi_value = str(mpmath.mp.pi)[2:]  # Get Pi digits as a string, removing the "3."
    return pi_value

def main():
    print("PiGood: Generating Pi digits endlessly... (Ctrl+C to stop)")

    digits_per_request = 100  # Number of digits to generate per request
    total_digits_generated = 0  # Track the total number of digits generated so far

    while True:
        input(f"Press Enter to generate next {digits_per_request} digits of Pi...")
        
        # Calculate the starting point to avoid repetition
        start = total_digits_generated
        total_digits_generated += digits_per_request
        
        # Generate only the next batch of digits
        new_digits = generate_pi(total_digits_generated)[start:]
        
        # Print only the newly generated digits
        print(new_digits)

if __name__ == "__main__":
    main()
