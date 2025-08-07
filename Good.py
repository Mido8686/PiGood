import mpmath

class PiGood:
    def __init__(self):
        # Set mpmath to a very high precision. 
        mpmath.mp.dps = 1000000  # You can set this to a very high number for indefinite generation
        # Get Pi as a string, including "3."
        self.pi = str(mpmath.pi)
        self.index = 2  # Start after the "3."

    def get_next_100_digits(self):
        # Get the next 100 digits of Pi
        start = self.index
        end = start + 100  # Extract exactly 100 digits of Pi
        block = self.pi[start:end]  # Get the next 100 digits
        self.index += 100  # Move index forward for the next call
        
        # On the first call, include "3." and the next 100 digits
        if self.index == 102:  # The first set includes "3."
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
