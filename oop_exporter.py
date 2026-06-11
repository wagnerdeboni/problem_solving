import json
import csv


class ParkAnalyzer:

    def __init__(self, reviews):
        self.reviews = reviews
        self.park_data = self.create_summary()

    def create_summary(self):
        summary = {}

        for review in self.reviews:
            park = review["Branch"]
            rating = review["Rating"]
            country = review["Reviewer_Location"]

            if park not in summary:
                summary[park] = {
                    "reviews": 0,
                    "positive": 0,
                    "rating_total": 0,
                    "countries": []
                }

            summary[park]["reviews"] += 1
            summary[park]["rating_total"] += rating

            if rating >= 4:
                summary[park]["positive"] += 1

            if country not in summary[park]["countries"]:
                summary[park]["countries"].append(country)

        final_data = []

        for park in summary:
            average = summary[park]["rating_total"] / summary[park]["reviews"]

            final_data.append({
                "ParkName": park,
                "NumberOfReviews": summary[park]["reviews"],
                "NumberOfPositiveReviews": summary[park]["positive"],
                "AverageReviewScore": round(average, 2),
                "NumberOfUniqueCountries": len(summary[park]["countries"])
            })

        return final_data

    def get_aggregated_data(self):
        return self.park_data

    def export_to_txt(self, filename):
        if not filename.endswith(".txt"):
            filename = filename + ".txt"

        file = open(filename, "w", encoding="utf-8")

        file.write("Disneyland Park Report\n")
        file.write("======================\n\n")

        for park in self.park_data:
            file.write("Park Name: " + str(park["ParkName"]) + "\n")
            file.write("Number of Reviews: " + str(park["NumberOfReviews"]) + "\n")
            file.write("Positive Reviews: " + str(park["NumberOfPositiveReviews"]) + "\n")
            file.write("Average Score: " + str(park["AverageReviewScore"]) + "\n")
            file.write("Unique Countries: " + str(park["NumberOfUniqueCountries"]) + "\n")
            file.write("----------------------\n")

        file.close()

    def export_to_csv(self, filename):
        if not filename.endswith(".csv"):
            filename = filename + ".csv"

        file = open(filename, "w", newline="", encoding="utf-8")

        headings = [
            "ParkName",
            "NumberOfReviews",
            "NumberOfPositiveReviews",
            "AverageReviewScore",
            "NumberOfUniqueCountries"
        ]

        writer = csv.DictWriter(file, fieldnames=headings)
        writer.writeheader()
        writer.writerows(self.park_data)

        file.close()

    def export_to_json(self, filename):
        if not filename.endswith(".json"):
            filename = filename + ".json"

        file = open(filename, "w", encoding="utf-8")
        json.dump(self.park_data, file, indent=4)
        file.close()

# update april
# update may
# update june