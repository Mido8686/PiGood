import mpmath

class PiGood:
    def __init__(self):
        # Set up mpmath to calculate Pi to a large number of digits
        mpmath.mp.dps = 10000  # Set the precision to get a large number of digits
        self.pi = str(mpmath.pi)[2:]  # Get Pi digits as a string, remove "3."
        self.index = 0  # Start index to return the next block of 100 digits

    def get_next_100_digits(self):
        # Get the next block of 100 digits
        start = self.index
        end = start + 100
        block = self.pi[start:end]
        self.index += 100  # Move the index forward
        return block

# Example Usage:
if __name__ == "__main__":
    pi_good = PiGood()
    print("PiGood: Generating Pi digits endlessly... (Ctrl+C to stop)")
    
    while True:
        input("Press Enter to generate next 100 digits of Pi...")
        next_100 = pi_good.get_next_100_digits()
        print(next_100)
