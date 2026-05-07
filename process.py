import csv


def read_reviews(file_name):
    reviews = []

    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            reviews.append(row)

    return reviews


def reviews_per_park(reviews):
    parks = {}

    for review in reviews:
        park = review["Branch"]

        if park in parks:
            parks[park] += 1
        else:
            parks[park] = 1

    return parks


def reviews_by_country(reviews, park_name):
    countries = {}

    for review in reviews:
        if review["Branch"].lower() == park_name.lower():
            country = review["Reviewer_Location"]

            if country in countries:
                countries[country] += 1
            else:
                countries[country] = 1

    return countries