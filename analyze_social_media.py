import csv

filename = "social-media-analytics.csv"

total_reach = 0
total_likes = 0
total_comments = 0
total_shares = 0
post_count = 0

with open(filename, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_reach += int(row["Reach"])
        total_likes += int(row["Likes"])
        total_comments += int(row["Comments"])
        total_shares += int(row["Shares"])
        post_count += 1

print("Social Media Performance Report")
print("--------------------------------")

print(f"Posts analyzed: {post_count}")
print(f"Total reach: {total_reach}")
print(f"Total likes: {total_likes}")
print(f"Total comments: {total_comments}")
print(f"Total shares: {total_shares}")

if total_reach > 0:
    engagement = (
        (total_likes + total_comments + total_shares)
        / total_reach
    ) * 100

    print(f"Overall engagement rate: {engagement:.2f}%")
