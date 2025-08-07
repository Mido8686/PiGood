import mpmath

class PiGood:
    def __init__(self):
        # Set mpmath precision to a large number (10000 decimal places)
        mpmath.mp.dps = 10000
        # Get Pi as a string and include "3."
        self.pi = str(mpmath.pi)
        self.index = 2  # Start from the first digit after the decimal point

    def get_next_100_digits(self):
        # Get the next 100 digits of Pi, including "3."
        start = self.index
        end = start + 100
        block = self.pi[start:end]  # Get the substring of 100 digits
        self.index += 100  # Move index forward for the next call
        return block

# Example Usage:
if __name__ == "__main__":
    pi_good = PiGood()
    print("PiGood: Generating Pi digits endlessly... (Ctrl+C to stop)")
    
    while True:
        input("Press Enter to generate next 100 digits of Pi...")
        next_100 = pi_good.get_next_100_digits()
        print(next_100)
