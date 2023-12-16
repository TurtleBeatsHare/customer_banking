# Import the create_cd_account and create_savings_account functions
import sys
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("-" * 72)
    valid_input = {'Savings Balance': False, 'Savings Interest': False, 'Savings Maturity': False}

    while True:
        try:
            float(savings_balance)
        except:
            try:
                savings_balance = float(input("Please input the savings account initial balance:  "))
                valid_input['Savings Balance'] = True
            except:
                pass
        
        try:
            float(savings_interest)
        except:
            try:
                savings_interest = float(input("Please input the savings account interest rate (apr):  "))
                valid_input['Savings Interest'] = True
            except:
                pass

        try:
            int(savings_maturity)
        except:
            try:
                savings_maturity = int(input("Please input the esitmated savings account duration in months:  "))
                valid_input['Savings Maturity'] = True
            except:
                pass       
        
        
        if all(valid_input.values()):
            break
        else:
            print("\n")
            [print(f"The input for {key} was invalid.") for (key, value) in valid_input.items() if not value]
            if input("Would you like to try again? (Y/N):  ").lower() in ["y", "yes"]:
                print("\n")
            else:
                sys.exit("Better luck next time :)")


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("\n")
    print(f"After {savings_maturity} months, the final savings account balance is ${updated_savings_balance:,.2f}.")
    print(f"The account earned ${interest_earned:,.2f} of interest over that period.")
    print("-" * 72)
    print("\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    valid_input = {'CD Balance': False, 'CD Interest': False, 'CD Maturity': False}

    while True:
        try:
            float(cd_balance)
        except:
            try:
                cd_balance = float(input("Please input the cd account initial balance:  "))
                valid_input['CD Balance'] = True
            except:
                pass
        
        try:
            float(cd_interest)
        except:
            try:
                cd_interest = float(input("Please input the cd account interest rate (apr):  "))
                valid_input['CD Interest'] = True
            except:
                pass

        try:
            int(cd_maturity)
        except:
            try:
                cd_maturity = int(input("Please input the esitmated cd account duration in months:  "))
                valid_input['CD Maturity'] = True
            except:
                pass       
        
        
        if all(valid_input.values()):
            break
        else:
            print("\n")
            [print(f"The input for {key} was invalid.") for (key, value) in valid_input.items() if not value]
            if input("Would you like to try again? (Y/N):  ").lower() in ["y", "yes"]:
                print("\n")
            else:
                sys.exit("Better luck next time :)")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("\n")
    print(f"After {cd_maturity} months, the final CD account balance is ${updated_cd_balance:,.2f}.")
    print(f"The account earned ${interest_earned:,.2f} of interest over that period.")

if __name__ == "__main__":
    # Call the main function.
    main()