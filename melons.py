"""This file should have our order classes in it."""
from random import randint
from datetime import datetime


class AbstractMelonOrder(object):

    def __init__(self, species, qty, country_code = None):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_base_price(self):

        base_price = randint(5,9)
        return base_price

    def get_total(self):
        """Calculate price."""
        base_price = self.get_base_price()

        if self.species == "Christmas Melon":
            base_price = base_price * 1.5

        if self.country_code and self.qty < 10:
            total = (1 + self.tax) * self.qty * base_price + 3

        else:
            total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.order_type = "international"
        self.tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.passed_insepection = False
        self.tax = 0


    def mark_inspection(self, passed):
        self.passed = passed
        if self.passed:
            self.passed_insepection = True
        else:
            self.passed_insepection = False


        return self.passed_insepection


# class DomesticMelonOrder(object):
#     """A domestic (in the US) melon order."""

#     def __init__(self, species, qty):
#         """Initialize melon order attributes"""

#         self.species = species
#         self.qty = qty
#         self.shipped = False
#         self.order_type = "domestic"
#         self.tax = 0.08

#     def get_total(self):
#         """Calculate price."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price
#         return total

#     def mark_shipped(self):
#         """Set shipped to true."""

#         self.shipped = True


# class InternationalMelonOrder(object):
#     """An international (non-US) melon order."""

#     def __init__(self, species, qty, country_code):
#         """Initialize melon order attributes"""

#         self.species = species
#         self.qty = qty
#         self.country_code = country_code
#         self.shipped = False
#         self.order_type = "international"
#         self.tax = 0.17

#     def get_total(self):
#         """Calculate price."""

#         base_price = 5
#         total = (1 + self.tax) * self.qty * base_price
#         return total

#     def mark_shipped(self):
#         """Set shipped to true."""

#         self.shipped = True

#     def get_country_code(self):
#         """Return the country code."""

#         return self.country_code
