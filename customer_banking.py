# Import the create_cd_account and create_savings_account functions
from sys import exit
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    print("-" * 72)
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    input_validation = {'Savings Balance': False, 'Savings Interest': False, 'Savings Maturity': False}

    while True:
        try:
            # Check if variable exists and is a float if so, set input_validation True
            savings_balance = float(savings_balance)
            # The next line only runs if the previous line executes correctly
            # suggesting that the input has been received and is valid.
            input_validation['Savings Balance'] = True
        except:
            try:
                # If previous check does not pass acquire input and convert to float
                savings_balance = float(input("Please input the savings account initial balance:  "))
                # If previous executes correctly, input has been received and is a float
                input_validation['Savings Balance'] = True
            except:
                # If the input above produced error, leave input_validation False and pass
                # Option to retry is offered after all three inputs for this section
                pass
        
        try:
            savings_interest = float(savings_interest)
            input_validation['Savings Interest'] = True
        except:
            try:
                savings_interest = float(input("Please input the savings account interest rate (apr):  "))
                input_validation['Savings Interest'] = True
            except:
                pass

        try:
            savings_maturity = int(savings_maturity)
            input_validation['Savings Maturity'] = True
        except:
            try:
                savings_maturity = int(input("Please input the esitmated savings account duration in months:  "))
                input_validation['Savings Maturity'] = True
            except:
                pass       
        
        
        if all(input_validation.values()):
            break
        else:
            print("\n")
            [print(f"The input for {input_key} was invalid.") for (input_key, valid_input) in input_validation.items() if not valid_input]
            if input("Would you like to try again? (Y/N):  ").lower() in ["y", "yes"]:
                print("\n")
            else:
                exit("Better luck next time :)")


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nAfter {savings_maturity} months, the final savings account balance is ${updated_savings_balance:,.2f}.")
    print(f"The account earned ${interest_earned:,.2f} of interest over that period.\n{'-' * 72}\n")


    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    input_validation = {'CD Balance': False, 'CD Interest': False, 'CD Maturity': False}

    while True:
        try:
            cd_balance = float(cd_balance)
            input_validation['CD Balance'] = True
        except:
            try:
                cd_balance = float(input("Please input the cd account initial balance:  "))
                input_validation['CD Balance'] = True
            except:
                pass
        
        try:
            cd_interest = float(cd_interest)
            input_validation['CD Interest'] = True
        except:
            try:
                cd_interest = float(input("Please input the cd account interest rate (apr):  "))
                input_validation['CD Interest'] = True
            except:
                pass

        try:
            cd_maturity = int(cd_maturity)
            input_validation['CD Maturity'] = True
        except:
            try:
                cd_maturity = int(input("Please input the esitmated cd account duration in months:  "))
                input_validation['CD Maturity'] = True
            except:
                pass       
        
        
        if all(input_validation.values()):
            break
        else:
            print("\n")
            [print(f"The input for {input_key} was invalid.") for (input_key, valid_input) in input_validation.items() if not valid_input]
            if input("Would you like to try again? (Y/N):  ").lower() in ["y", "yes"]:
                print("\n")
            else:
                exit("Better luck next time :)")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\nAfter {cd_maturity} months, the final CD account balance is ${updated_cd_balance:,.2f}.")
    print(f"The account earned ${interest_earned:,.2f} of interest over that period.\n{'-' * 72}\n")

if __name__ == "__main__":
    # Call the main function.
    main()