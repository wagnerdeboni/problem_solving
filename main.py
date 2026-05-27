from tui import show_title, show_menu, user_choice
from process import (
    read_reviews,
    reviews_per_park,
    reviews_by_country
)

def main():

    #title
    show_title()

    #rev file
    reviews = read_reviews("data/disneyland_reviews.csv")

    print("\nData loaded successfully")
    print("Number of reviews:", len(reviews))

    #running until user exits
    while True:

        #menu
        show_menu()

        #option user
        option = user_choice()

        #op A
        if option == "A":

            print("\nParks with most reviews:\n")

            park_info = reviews_per_park(reviews)

            for park in park_info:
                print(park, "-", park_info[park], "reviews")

        #op B
        elif option == "B":

            park = input("\nType the park name: ")

            location_info = reviews_by_country(reviews, park)

            #check if results exist
            if len(location_info) == 0:
                print("No reviews found.")

            else:
                print("\nReviews by country for", park)

                for country in location_info:
                    print(country, "-", location_info[country], "reviews")

        #exit
        elif option == "X":

            print("Program closed.")
            break

        #wrong op
        else:
            print("Please enter a valid option.")


#run
main ()