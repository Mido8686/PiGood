import mpmath

# Set the number of digits you want to calculate
def generate_pi(digits: int):
    mpmath.mp.dps = digits  # set precision (decimal places)
    pi_value = str(mpmath.pi)  # get the value of Pi to the specified precision
    return pi_value

def main():
    print("PiGood: Generating Pi digits endlessly... (Ctrl+C to stop)")
    
    digits_per_request = 100  # Number of digits to generate per request

    while True:
        input(f"Press Enter to generate next {digits_per_request} digits of Pi...")
        pi_digits = generate_pi(mpmath.mp.dps + digits_per_request)
        print(pi_digits[-digits_per_request:])  # Print only the newly generated digits

if __name__ == "__main__":
    main()
