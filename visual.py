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

    plt.bar(parks, totals)

    plt.title("Reviews per Park")
    plt.xlabel("Park")
    plt.ylabel("Reviews")

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


# may update
# june update
