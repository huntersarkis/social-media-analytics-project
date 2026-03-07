import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/raw/social_media_engagement.csv")

# Create engagement column
df["engagement"] = df["likes"] + df["comments"] + df["shares"]

# Average engagement by platform
platform_engagement = df.groupby("platform")["engagement"].mean()

# Create bar chart
platform_engagement.plot(kind="bar")

plt.title("Average Engagement by Platform")
plt.ylabel("Average Engagement")
plt.xlabel("Platform")

plt.tight_layout()

plt.savefig("visuals/engagement_by_platform.png")

plt.show()

# Average engagement by post type
post_type_engagement = df.groupby("post_type")["engagement"].mean()

post_type_engagement.plot(kind="bar")

plt.title("Average Engagement by Post Type")
plt.ylabel("Average Engagement")
plt.xlabel("Post Type")

plt.tight_layout()

plt.savefig("visuals/engagement_by_post_type.png")

plt.show()