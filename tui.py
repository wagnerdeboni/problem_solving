def display_title():

    title = "Disneyland Review Analyser"

    print("-" * len(title))
    print(title)
    print("-" * len(title))


def display_main_menu():

    print("\nPlease enter the letter which corresponds with your desired menu choice:\n")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Data")
    print("[X] Exit")


def display_view_data_menu():

    print("\nPlease enter one of the following options:\n")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per Year by Park")
    print("[D] Average Score per Park by Reviewer Location")
    print("[X] Back")


def display_visualise_menu():

    print("\nPlease enter one of the following options:\n")
    print("[A] Most reviewed Parks")
    print("[B] Park Ranking by Nationality")
    print("[C] Most Popular Month by Park")
    print("[X] Back")


def get_choice():

    choice = input("Select an option: ")

    # Remove spaces, change capital letters
    choice = choice.strip().upper()

    return choice


# april update
# may update
# june update
