from tui import display_title, display_menu, get_choice

from process import (
    read_reviews,
    reviews_per_park,
    reviews_by_country
)

from visual import (
    reviews_per_park_chart,
    reviews_by_country_chart
)


def main():

    # title
    display_title()

    # rev file
    reviews = read_reviews("disneyland_reviews.csv")

    print("\nData loaded successfully")
    print("Number of reviews:", len(reviews))

    while True:

        # menu
        display_menu()

        # op user
        option = get_choice()

        # op A
        if option == "A":

            print("\nParks with most reviews:\n")

            park_info = reviews_per_park(reviews)

            for park in park_info:
                print(park, "-", park_info[park], "reviews")

        # op B
        elif option == "B":

            park = input("\nType the park name: ")

            location_info = reviews_by_country(reviews, park)

            if len(location_info) == 0:
                print("No reviews found.")

            else:
                print("\nReviews by country for", park)

                for country in location_info:
                    print(country, "-", location_info[country], "reviews")

        # op C
        elif option == "C":

            reviews_per_park_chart(reviews)

        # op D
        elif option == "D":

            park = input("\nType the park name: ")

            reviews_by_country_chart(reviews, park)

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
