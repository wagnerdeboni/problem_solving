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


def reviews_per_park(reviews):
    total_by_park = {}

    for review in reviews:
        park = review["Branch"]

        if park not in total_by_park:
            total_by_park[park] = 1
        else:
            total_by_park[park] += 1

    return total_by_park


def reviews_by_country(reviews, park_name):
    total_by_location = {}

    park_name = park_name.strip().lower().replace(" ", "_")

    for review in reviews:
        current_park = review["Branch"].lower()

        if current_park == park_name:
            location = review["Reviewer_Location"]

            if location not in total_by_location:
                total_by_location[location] = 1
            else:
                total_by_location[location] += 1

    return total_by_location

# april update
# nmay update
# june update