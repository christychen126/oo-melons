"""This file should have our order classes in it."""

from random import randint
from datetime import datetime


class AbstractMelonOrder(object):
    """Abstract melon order parent class"""

    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

        if self.qty > 100:
            raise TooManyMelonsError("Too many melons!")

        try:
            if self.qty > 100:
                raise TooManyMelonsError("Too many melons!")
        except TooManyMelonsError:
            print "booooooo too many melons"

    def get_base_price(self):
        """Return base price"""

        # Choose random baseprice
        base_price = randint(5,9)
        
        # Initialize current hour and day of week
        now = datetime.now()
        hour = now.hour
        day = now.weekday()

        # weekday list is Monday -> Sunday = [0,1,2,3,4,5,6]
        monday = 0
        friday = 4

        # if time between 8am - 11am and M-F, adjust base_price for rush hour
        if 8 <= hour < 11 and  monday <= day <= friday: 
            base_price += 4
            print base_price

        return base_price


    def get_total(self):
        """Calculate price."""

        # Call get_base_price method
        base_price = self.get_base_price()

        # Adjust base_price if Christmas Melon
        if self.species == "Christmas Melon":
            base_price = base_price * 1.5

        # Add $3 if international order under 10 melons
        if self.country_code and self.qty < 10:
            total = (1 + self.tax) * self.qty * base_price + 3

        else:
            total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class TooManyMelonsError(ValueError):
    """Error handling for TooManyMelonsError"""


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A Government melon order"""

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_insepection = False
        self.tax = 0


    def mark_inspection(self, passed):
        """ Check if passed inspection """

        self.passed = passed

        if self.passed:
            self.passed_insepection = True
        else:
            self.passed_insepection = False

        return self.passed_insepection
