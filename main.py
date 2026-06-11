from tui import (
display_title,
display_main_menu,
display_view_data_menu,
display_visualise_menu,
get_choice
)

from process import (
    read_reviews,
    reviews_for_park,
    reviews_by_park_and_location,
    average_score_by_year,
    average_rating_by_location,
    average_rating_by_month,
    average_score_per_park_by_location
)

from visual import (
    reviews_per_park_chart,
    reviews_by_country_chart,
    top_10_locations_chart,
    average_rating_by_month_chart
)

from oop_exporter import ParkAnalyzer

def get_park_choice():
    print("\nSelect a park:")
    print("1 - Disneyland California")
    print("2 - Disneyland Paris")
    print("3 - Disneyland HongKong")

    choice = input("Option: ")

    if choice == "1":
        return "Disneyland_California"
    elif choice == "2":
        return "Disneyland_Paris"
    elif choice == "3":
        return "Disneyland_HongKong"
    else:
        print("Invalid option.")
        return None


def main():

    # title
    display_title()

    # rev file
    reviews = read_reviews("disneyland_reviews.csv")

    print("\nData loaded successfully")
    print("Number of reviews:", len(reviews))

    while True:

        display_main_menu()

        option = get_choice()

        if option == "A":
            print("\nYou have chosen option A - View Data")

        elif option == "B":
            print("\nYou have chosen option B - Visualise Data")

        elif option == "X":
            print("\nYou have chosen option X - Exit")

        # View Data
        if option == "A":

            while True:

                display_view_data_menu()

                sub_option = get_choice()

                # op A
                if sub_option == "A":

                    park = get_park_choice()

                    if park is None:
                        continue

                    park_reviews = reviews_for_park(reviews, park)

                    print("\nReviews for", park, "\n")

                    for review in park_reviews:
                        print(review)

                # op B
                elif sub_option == "B":

                    park = get_park_choice()

                    if park is None:
                        continue

                    location = input("Enter reviewer location: ")

                    total_reviews = reviews_by_park_and_location(
                        reviews,
                        park,
                        location
                    )

                    print(
                        "\nNumber of reviews from",
                        location,
                        "for",
                        park,
                        "=",
                        total_reviews
                    )

                # op C
                elif sub_option == "C":

                    park = get_park_choice()

                    if park is None:
                        continue

                    year = input("Enter year: ")

                    average = average_score_by_year(
                        reviews,
                        park,
                        year
                    )

                    print(
                        "\nAverage rating for",
                        park,
                        "in",
                        year,
                        "=",
                        round(average, 2)
                    )

                # op D
                elif sub_option == "D":

                    results = average_score_per_park_by_location(
                        reviews
                    )

                    for park in results:

                        print("\n" + park)

                        for location in results[park]:
                            print(
                                location,
                                "-",
                                results[park][location]
                            )

                # back
                elif sub_option == "X":
                    break

                else:
                    print("Please enter a valid option.")

        # Visualise Data
        elif option == "B":

            while True:

                display_visualise_menu()

                sub_option = get_choice()

                # chart A - Most reviewed Parks
                if sub_option == "A":

                    reviews_per_park_chart(reviews)

                # chart B - Park Ranking by Nationality
                elif sub_option == "B":

                    park = get_park_choice()

                    if park is None:
                        continue

                    data = average_rating_by_location(
                        reviews,
                        park
                    )

                    top_10_locations_chart(data)

                # chart C - Most Popular Month by Park
                elif sub_option == "C":

                    park = get_park_choice()

                    if park is None:
                        continue

                    data = average_rating_by_month(
                        reviews,
                        park
                    )

                    average_rating_by_month_chart(data)

                # back
                elif sub_option == "X":
                    break

                else:
                    print("Please enter a valid option.")

        # Export Data
        elif option == "C":

            analyzer = ParkAnalyzer(reviews)

            print("\nChoose export format:")
            print("1 - TXT")
            print("2 - CSV")
            print("3 - JSON")

            export_choice = input("Option: ")

            if export_choice == "1":
                analyzer.export_to_txt("park_report")
                print("TXT file exported.")

            elif export_choice == "2":
                analyzer.export_to_csv("park_report")
                print("CSV file exported.")

            elif export_choice == "3":
                analyzer.export_to_json("park_report")
                print("JSON file exported.")

            else:
                print("Invalid option.")

        # exit
        elif option == "X":

            print("Program closed.")
            break

        # invalid op
        else:
            print("Please enter a valid option.")


    # run

    # march update

    # april update

    # may update

    # june update

main()
