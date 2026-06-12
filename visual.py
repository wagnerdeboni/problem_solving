import matplotlib.pyplot as plt


# reviews p park
def reviews_per_park_chart(reviews):

    park_total = {}

    for review in reviews:

        park = review["Branch"]

        if park not in park_total:
            park_total[park] = 1
        else:
            park_total[park] += 1

    parks = list(park_total.keys())
    totals = list(park_total.values())

    plt.pie(
        totals,
        labels=parks,
        autopct="%1.1f%%"
    )

    plt.title("Reviews per Park")
    plt.show()


# reviews by country
def reviews_by_country_chart(reviews, park_name):

    country_total = {}

    park_name = park_name.lower()

    for review in reviews:

        park = review["Branch"].lower()

        if park == park_name:

            country = review["Reviewer_Location"]

            if country not in country_total:
                country_total[country] = 1
            else:
                country_total[country] += 1

    countries = list(country_total.keys())
    totals = list(country_total.values())

    plt.bar(countries, totals)

    plt.title("Reviews by Country")
    plt.xlabel("Country")
    plt.ylabel("Reviews")

    plt.xticks(rotation=45)

    plt.show()


def top_10_locations_chart(data):

    sorted_locations = sorted(
        data.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top10 = sorted_locations[:10]

    locations = []
    ratings = []

    for location, rating in top10:
        locations.append(location)
        ratings.append(rating)

    plt.figure(figsize=(10, 5))
    plt.bar(locations, ratings)

    plt.title("Top 10 Locations by Average Rating")
    plt.xlabel("Location")
    plt.ylabel("Average Rating")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def average_rating_by_month_chart(data):

    months_order = [
        "01", "02", "03", "04",
        "05", "06", "07", "08",
        "09", "10", "11", "12"
    ]

    ratings = []

    for month in months_order:

        if month in data:
            ratings.append(data[month])
        else:
            ratings.append(0)

    plt.figure(figsize=(10, 5))
    plt.bar(months_order, ratings)

    plt.title("Average Rating by Month")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")

    plt.show()


# may update
# june update
