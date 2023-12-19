# customer_banking

Homework assignment for Module 3 of AI Bootcamp.

## Module 3 Challenge: Customer Banking

This challenge had us mimic basic banking algorithms. We were given a class 'Account.py' 
and asked to create and instance of that account in two seperate functions. Those functions
also did some basic interest calculations.

Once the functions, functioned (ha) we wrote a main script that prompts the user to
input initial values for account balance, interest rate, and intended account duration.
After error checking the input, the results of the interest earned and final balance
calculations are printed to std.out.

## Input Error handling

The prompt suggested checking the input for correct type without much requirement
for *how* to do this. I took some liberties and played with a dictionary, infinite loops,
and some try/except statements to create an interface that waits for the user to input all
three variables for a specific account before reporting if any of the inputs are incorrect
and then allowing them the choice to try inputing just the failed inputs again. 

Overboard, I'm sure but it was fun trying to put into practice some of the tools we've
learned the passed couple weeks.
