def read_reviews(file_path):
    reviews = []

    file = open(file_path, "r", encoding="utf-8")
    all_lines = file.readlines()
    file.close()

    for line in all_lines[1:]:
        values = line.strip().split(",")

        review = {
            "Review_ID": int(values[0]),
            "Rating": int(values[1]),
            "Year_Month": values[2],
            "Reviewer_Location": values[3],
            "Branch": values[4]
        }

        reviews.append(review)

    return reviews


def reviews_for_park(reviews, park_name):

    park_reviews = []

    park_name = park_name.strip().lower().replace(" ", "_")

    for review in reviews:

        if review["Branch"].lower() == park_name:
            park_reviews.append(review)

    return park_reviews


def reviews_by_park_and_location(
        reviews,
        park_name,
        location_name):

    total_reviews = 0

    park_name = park_name.strip().lower().replace(" ", "_")
    location_name = location_name.strip().lower()

    for review in reviews:

        if (
            review["Branch"].lower() == park_name
            and review["Reviewer_Location"].lower() == location_name
        ):
            total_reviews += 1

    return total_reviews

def average_score_by_year(reviews, park_name, year):

    total_rating = 0
    review_count = 0

    park_name = park_name.strip().lower().replace(" ", "_")

    for review in reviews:

        review_year = review["Year_Month"][:4]

        if (
            review["Branch"].lower() == park_name
            and review_year == str(year)
        ):
            total_rating += review["Rating"]
            review_count += 1

    if review_count == 0:
        return 0

    return total_rating / review_count

def average_rating_by_location(reviews, park_name):

    totals = {}
    counts = {}

    park_name = park_name.strip().lower().replace(" ", "_")

    for review in reviews:

        if review["Branch"].lower() == park_name:

            location = review["Reviewer_Location"]

            if location not in totals:
                totals[location] = review["Rating"]
                counts[location] = 1
            else:
                totals[location] += review["Rating"]
                counts[location] += 1

    averages = {}

    for location in totals:
        averages[location] = totals[location] / counts[location]

    return averages

def average_rating_by_month(reviews, park_name):

    totals = {}
    counts = {}

    park_name = park_name.strip().lower().replace(" ", "_")

    for review in reviews:

        if review["Branch"].lower() == park_name:

            month = review["Year_Month"][5:7]

            if month not in totals:
                totals[month] = review["Rating"]
                counts[month] = 1
            else:
                totals[month] += review["Rating"]
                counts[month] += 1

    averages = {}

    for month in totals:
        averages[month] = totals[month] / counts[month]

    return averages

def average_score_per_park_by_location(reviews):

    parks = {}

    for review in reviews:

        park = review["Branch"]
        location = review["Reviewer_Location"]
        rating = review["Rating"]

        if park not in parks:
            parks[park] = {}

        if location not in parks[park]:
            parks[park][location] = {
                "total": rating,
                "count": 1
            }
        else:
            parks[park][location]["total"] += rating
            parks[park][location]["count"] += 1

    results = {}

    for park in parks:

        results[park] = {}

        for location in parks[park]:

            average = (
                parks[park][location]["total"]
                /
                parks[park][location]["count"]
            )

            results[park][location] = round(
                average,
                2
            )

    return results

# april update
# may update
# june update