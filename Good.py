import mpmath

# Set the number of digits you want to calculate
def generate_pi(digits: int):
    mpmath.mp.dps = digits + 1  # Set precision (1 extra digit to ensure rounding is handled correctly)
    pi_value = str(mpmath.mp.pi)[2:]  # Get the value of Pi to the specified precision, removing the '3.'
    return pi_value

def main():
    print("PiGood: Generating Pi digits endlessly... (Ctrl+C to stop)")

    digits_per_request = 100  # Number of digits to generate per request
    generated_digits = ""  # Initialize to store generated digits
    
    while True:
        input(f"Press Enter to generate next {digits_per_request} digits of Pi...")
        # Append the next batch of digits to the generated digits
        generated_digits += generate_pi(digits_per_request)
        
        # Print only the newly generated digits
        print(generated_digits[-digits_per_request:])  # This will print only the most recent 100 digits

if __name__ == "__main__":
    main()
