import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from wordcloud import STOPWORDS, WordCloud

# Set clean aesthetic plot parameters
sns.set_theme(style="whitegrid")
plt.rcParams.update({"font.size": 10, "axes.labelsize": 12, "figure.titlesize": 14})


def generate_eda_dashboard(input_file="cleaned_books.csv"):
    # 1. Load the processed dataset pipeline asset
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(
            f"Error: '{input_file}' not found. Run Task 2 preprocessing first."
        )
        return

    # Create a 2x2 grid layout window dashboard for the core plots
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # ----------------------------------------------------
    # Plot 1: Price Distribution (Histogram + KDE)
    # ----------------------------------------------------
    sns.histplot(
        data=df,
        x="price_numeric",
        kde=True,
        color="skyblue",
        bins=15,
        ax=axes[0, 0],
    )
    axes[0, 0].set_title("1. Distribution of Book Prices")
    axes[0, 0].set_xlabel("Price (£)")
    axes[0, 0].set_ylabel("Frequency Count")

    # ----------------------------------------------------
    # Plot 2: Rating Distribution (Bar Plot Count)
    # ----------------------------------------------------
    sns.countplot(
        data=df,
        x="rating_numeric",
        palette="viridis",
        hue="rating_numeric",
        legend=False,
        ax=axes[0, 1],
    )
    axes[0, 1].set_title("2. Distribution of Star Ratings")
    axes[0, 1].set_xlabel("Star Rating (1 to 5)")
    axes[0, 1].set_ylabel("Book Count")

    # ----------------------------------------------------
    # Plot 3: Average Price by Category (Horizontal Bar)
    # ----------------------------------------------------
    avg_price_cat = (
        df.groupby("category")["price_numeric"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )
    sns.barplot(
        data=avg_price_cat,
        x="price_numeric",
        y="category",
        palette="plasma",
        hue="category",
        legend=False,
        ax=axes[1, 0],
    )
    axes[1, 0].set_title("3. Average Book Price by Category Group")
    axes[1, 0].set_xlabel("Average Price (£)")
    axes[1, 0].set_ylabel("Category")

    # ----------------------------------------------------
    # Plot 4: Relationship - Category vs Stock (Box Plot)
    # ----------------------------------------------------
    sns.boxplot(
        data=df,
        x="stock_count",
        y="category",
        palette="muted",
        hue="category",
        legend=False,
        ax=axes[1, 1],
    )
    axes[1, 1].set_title("4. Stock Inventory Dispersion by Category")
    axes[1, 1].set_xlabel("Available Stock Count")
    axes[1, 1].set_ylabel("Category")

    plt.tight_layout()
    fig.savefig("books_structural_eda_dashboard.png", dpi=300)
    plt.close()
    print(
        "Dashboard plots successfully exported as 'books_structural_eda_dashboard.png'"
    )

    # ----------------------------------------------------
    # Plot 5: Word Cloud from Product Descriptions
    # ----------------------------------------------------
    raw_text = " ".join(df["product_description"].dropna().astype(str).tolist())

    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update(
        [
            "book",
            "story",
            "read",
            "author",
            "novel",
            "available",
            "description",
            "product",
        ]
    )

    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color="white",
        max_words=150,
        stopwords=custom_stopwords,
        colormap="Dark2",
        random_state=42,
    ).generate(raw_text)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Dominant Semantic Themes in Book Descriptions", fontsize=16, pad=15)
    plt.tight_layout()
    plt.savefig("descriptions_wordcloud.png", dpi=300)
    plt.close()
    print(
        "Word cloud canvas successfully exported as 'descriptions_wordcloud.png'"
    )

    # ----------------------------------------------------
    # 6. Command Console Summary Statistical Profiling
    # ----------------------------------------------------
    print("\n" + "=" * 50)
    print("             STATISTICAL SUMMARY REPORT             ")
    print("=" * 50)
    print(f"Overall Dataset Items Profiled: {len(df)}")
    print(f"Mean Market Listing Price: £{df['price_numeric'].mean():.2f}")
    print(f"Price Standard Deviation:  £{df['price_numeric'].std():.2f}")

    print("\n[Highly Rated Bargains (Rating >= 4, Price < £20)]:")
    bargains = df[(df["rating_numeric"] >= 4) & (df["price_numeric"] < 20.0)]
    if not bargains.empty:
        print(
            bargains[["title", "category", "price_numeric", "rating_numeric"]]
            .head(5)
            .to_string(index=False)
        )
    else:
        print("No low-cost high-rating items matched in this specific slice.")


if __name__ == "__main__":
    generate_eda_dashboard()
