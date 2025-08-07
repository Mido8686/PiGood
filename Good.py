import mpmath

class PiGood:
    def __init__(self):
        # Set up mpmath to calculate Pi to a large number of digits
        mpmath.mp.dps = 1000  # Set the precision to get a large number of digits
        self.pi = str(mpmath.pi)[2:]  # Get Pi digits as a string, remove "3."
        self.index = 0  # Start index to return the next block of 100 digits

    def get_next_100_digits(self):
        # Get the next block of 100 digits
        start = self.index
        end = start + 100
        if end <= len(self.pi):
            block = self.pi[start:end]
            self.index += 100  # Move the index forward
            return block
        else:
            return None  # If no more digits are available

# Example Usage:
pi_good = PiGood()

# Get the first 100 digits
print(pi_good.get_next_100_digits())

# Get the next 100 digits
print(pi_good.get_next_100_digits())

# Continue calling pi_good.get_next_100_digits() to get further digits
