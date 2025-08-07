import mpmath

class PiGood:
    def __init__(self):
        # Start with a small precision (you can increase it further if needed)
        self.dps = 100000  # Starting with 100,000 digits
        mpmath.mp.dps = self.dps  # Set initial precision
        self.pi = str(mpmath.pi)  # Get Pi as a string
        self.index = 2  # Start after the "3."

    def get_next_100_digits(self):
        # Get the next 100 digits of Pi
        start = self.index
        end = start + 100  # Extract exactly 100 digits of Pi
        block = self.pi[start:end]
        self.index += 100

        # If the current precision is insufficient, dynamically increase it
        if self.index >= len(self.pi) - 100:
            self.dps += 100000  # Increase precision by 100,000 digits each time
            mpmath.mp.dps = self.dps  # Update the precision
            self.pi = str(mpmath.pi)  # Recalculate Pi with the updated precision

        # Return Pi digits with "3." on the first call, no "3." afterward
        if self.index == 102:  # For the first call, include "3."
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
