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
    print("C - Show reviews per park chart")
    print("D - Show reviews by country chart")
    print("X - Close program")


def get_choice():

    choice = input("Select an option: ")

    # Remove spaces, change capital letters
    choice = choice.strip().upper()

    return choice


# april update
# may update
# june update
