class Estate:
    # Class variable
    council_tax_rate = 0.02

    def __init__(self, address, price):
        # Instance variables
        self.address = address
        self.price = price
        self.tax = self.calculate_tax()
        print("Estate.council_tax_rate", Estate.council_tax_rate)

    # Instance method
    def calculate_tax(self):
        return self.price * Estate.council_tax_rate

    # Class method
    @classmethod
    def set_tax_rate(cls, rate):
        cls.council_tax_rate = rate
        print("Class name", cls.__name__)
        return cls.council_tax_rate

    # Static method
    @staticmethod
    def validate_price(price):
        return price > 0 and isinstance(price, (int, float))

# Example usage:

# Instantiate when council_tax_rate is 0.02 which computes tax based on existing council_tax_rate
house1 = Estate("123 Main St", 250000)
print(house1.council_tax_rate, house1.tax)

# Set council_tax_rate to 0.03 which computes tax based on new council_tax_rate
Estate.set_tax_rate(0.03)
house2 = Estate("123 Main St", 250000)
print(house2.council_tax_rate, house2.tax)

# Previously instantiated house1 still has the computed tax based on the old council_tax_rate
print(house1.council_tax_rate, house1.tax)

#is_valid = Estate.validate_price(250000)