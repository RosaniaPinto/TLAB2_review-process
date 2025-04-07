import matplotlib.pyplot as plt
from collections import Counter
import os

def make_plot(sentiments: list) -> None:
    """
    Generates and saves a bar chart showing the count of each sentiment category 
    (positive, neutral, negative, and irrelevant) from the provided list.

    Parameters:
        sentiments (list): A list of sentiment strings. Valid sentiments include 
                           'positive', 'neutral', 'negative', and 'irrelevant'.

    This function does not return any value. The plot is saved in the 'images/' folder.
    """
    # Count the occurrences of each sentiment
    sentiment_counts = Counter(sentiments)

    # Ensure all categories are represented, even if count is 0
    categories = ['positive', 'neutral', 'negative', 'irrelevant']
    counts = [sentiment_counts.get(category, 0) for category in categories]

    # Create the bar plot
    plt.figure(figsize=(8, 6))
    plt.bar(categories, counts, color=['green', 'blue', 'red', 'gray'])
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()

    # Create the images folder if it doesn't exist
    os.makedirs("images", exist_ok=True)

    # Save the plot
    plt.savefig("images/sentiment_distribution.png")
    plt.close()
