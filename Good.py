import mpmath

class PiGood:
    def __init__(self):
        # Set initial precision
        self.dps = 100000  # Starting with 100,000 digits
        mpmath.mp.dps = self.dps  # Set precision
        self.pi = str(mpmath.pi)
        self.index = 2  # Start after the "3."

    def get_next_100_digits(self):
        # Get the next 100 digits of Pi
        start = self.index
        end = start + 100
        block = self.pi[start:end]
        self.index += 100

        # If precision is too low, increase it for next digits
        if self.index > len(self.pi) - 100:
            self.dps += 100000  # Increase precision in steps of 100,000
            mpmath.mp.dps = self.dps
            self.pi = str(mpmath.pi)  # Recalculate Pi with new precision

        # On the first call, include "3." and the next 100 digits
        if self.index == 102:
            return f"3.{block}"
        else:
            return block

# Example Usage:
if __name__ == "__main__":
    pi_good = PiGood()
    print("PiGood: Generating Pi digits endlessly... (Ctrl+C to stop)")
    
    while True:
        input("Press Enter to generate next 100 digits of Pi...")
        next_100 = pi_good.get_next_100_digits()
        print(next_100)
