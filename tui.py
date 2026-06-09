def display_title():

    text = "Disneyland Reviews System"
    border = "*" * len(text)

    print(border)
    print(text)
    print(border)


def display_menu():

    print("\nMenu Options")
    print("A - Show parks with most reviews")
    print("B - Show reviews by country")
    print("X - Close program")


def get_choice():

    choice = input("Select an option: ")

    # Remove spaces and change to capital letters
    choice = choice.strip().upper()

    return choice
# april update
# may upadte
# june update