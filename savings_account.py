"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    savings = Account(balance, 0)

    # Calculate interest earned
     # ADD YOUR CODE HERE
    interest_earned = balance * (interest_rate/100 * months/12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE
    balance += interest_earned

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings.set_balance(balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE
    savings.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return  savings # ADD YOUR CODE HERE

if __name__ == "__main__":
    valid_input = {'Initial Balance': False, 'Interest Rate': False, 'Duration': False}

    while True:
        try:
            float(initial_balance)
        except:
            try:
                initial_balance = float(input("Please input the account initial balance:\n"))
                valid_input['Initial Balance'] = True
            except:
                pass
        
        try:
            float(interest_rate)
        except:
            try:
                interest_rate = float(input("Please input the interest rate (apr):\n"))
                valid_input['Interest Rate'] = True
            except:
                pass

        try:
            int(duration)
        except:
            try:
                duration = int(input("Please input the esitmated account duration in months:\n"))
                valid_input['Duration'] = True
            except:
                pass       
        
        
        if all(valid_input.values()):
            break
        else:
            [print(f"The input for {key} was invalid.") for (key, value) in valid_input.items() if not value]
            keep_going = input("Would you like to try again? (Y/N):\n")
            if keep_going.lower() in ["y", "yes"]:
                pass
            else:
                break


    my_savings = create_savings_account(initial_balance, interest_rate, duration)

    print(f"After {duration} months, the final account balance is ${my_savings.balance:,.2f}.")
    print(f"The account earned ${my_savings.interest:,.2f} of interest over that period.")
keep_going