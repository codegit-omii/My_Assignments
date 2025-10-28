"""
This module provides a function to calculate the compound interest
on a given principal amount over a specified number of years at a given
annual interest rate. The interest is compounded annually. 
The result is rounded to two decimal places.
Amount = Principal * (1 + Rate/100) ^ Years
Compound Interest = Amount - Principal
"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): ")) 
years = int(input("Enter the number of years: "))
amount = principal * (1 + rate / 100) ** years
compound_interest = amount - principal
print(f"The compound interest after {years} years is: {compound_interest:.2f}")
print(f"The total amount after {years} years is: {amount:.2f}")    