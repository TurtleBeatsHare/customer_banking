# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    valid_input = {'Savings Balance': False, 'Savings Interest': False, 'Savings Maturity': False}

    while True:
        try:
            float(savings_balance)
        except:
            try:
                savings_balance = float(input("Please input the savings account initial balance:\n"))
                valid_input['Savings Balance'] = True
            except:
                pass
        
        try:
            float(savings_interest)
        except:
            try:
                savings_interest = float(input("Please input the savings account interest rate (apr):\n"))
                valid_input['Savings Interest'] = True
            except:
                pass

        try:
            int(savings_maturity)
        except:
            try:
                savings_maturity = int(input("Please input the esitmated savings account duration in months:\n"))
                valid_input['Savings Maturity'] = True
            except:
                pass       
        
        
        if all(valid_input.values()):
            break
        else:
            [print(f"The input for {key} was invalid.") for (key, value) in valid_input.items() if not value]
            keep_going = input("Would you like to correct these? (Y/N):\n")
            if keep_going.lower() in ["y", "yes"]:
                pass
            else:
                break

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"After {duration} months, the final account balance is ${updated_savings_balance:,.2f}.")
    print(f"The account earned ${interest_earned:,.2f} of interest over that period.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

if __name__ == "__main__":
    # Call the main function.
    main()