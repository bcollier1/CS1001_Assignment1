# File name: Funds.py
# Created by: Brady Collier
# Date created: 01/13/19
# Description: Artists in the city have organized a concert to raise funds for a local charity, with an agreement from
# a local business owner to match a portion of the gross concert proceeds. (Cited from Question 1 on D2L)

# Main function


def funds():
    # Prices for adults and children
    adults = 20
    child = 15

    # Asks user for input for adult tickets and child tickets.
    adult_tickets = int(input("Hello user, please enter the amount of adult tickets sold: "))
    child_tickets = int(input("Please enter the amount of child tickets sold: "))

    # Asks user for input for Percentage of the gross concert proceeds to be matched.
    percent_match = float(input("Please enter the percentage that will be matched (as a decimal number): "))

    # Calculates the gross amount by multiplying adult tickets and child tickets to its fixed price.
    gross_amount = ((adult_tickets * adults) + (child_tickets * child))

    # Calculates the match amount by multiplying the gross amount to the percent provided by the user.
    match_amount = (gross_amount * percent_match)

    # Prints all the amounts that were calculated
    print("Gross concert proceeds: $%.2f" % gross_amount)
    print("Matched proceeds: $%.2f" % match_amount)
    print("Total funds raised: $%.2f" % (gross_amount + match_amount))


funds()
