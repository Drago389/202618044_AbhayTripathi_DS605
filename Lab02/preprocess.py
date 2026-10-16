import numpy as np
import pandas as pd


def preprocess_book_data(input_file="raw_books.csv", output_file="cleaned_books.csv"):
    # 1. Load the raw scraped dataset
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: {input_file} not found. please check the file path.")
        return

    print(f"Initial raw records: {len(df)}")

    # ----------------------------------------------------
    # 2. Text Cleaning and Missing Value Handling
    # ----------------------------------------------------
    # Strip whitespace from string columns
    string_cols = ["title", "category", "availability", "product_description", "UPC"]
    for col in string_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # Deduplicate dataset using the unique UPC field
    df = df.drop_duplicates(subset=["UPC"], keep="first")
    print(f"Records after removing duplicate UPCs: {len(df)}")

    # Handle missing values in product descriptions
    df["product_description"] = df["product_description"].replace(
        ["nan", "None", ""], np.nan
    )
    df["product_description"] = df["product_description"].fillna(
        "No description available."
    )

    # ----------------------------------------------------
    # 3. Numeric Extractions and Data Type Conversions
    # ----------------------------------------------------
    # Clean price column: Remove currency symbols (£) and convert to float
    df["price_numeric"] = (
        df["price"].str.replace("£", "", regex=False).astype(float)
    )

    # Map text ratings (One to Five) to integers (1 to 5)
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    df["rating_numeric"] = df["rating"].map(rating_map).fillna(0).astype(int)

    # Extract numeric stock counts out of text strings (e.g., "In stock (19 available)")
    # Defaults to 0 if the book is completely out of stock
    df["stock_count"] = (
        df["availability"]
        .str.extract(r"(\d+)")
        .fillna(0)
        .astype(int)
    )

    # ----------------------------------------------------
    # 4. Feature Engineering
    # ----------------------------------------------------
    # Feature 1: Word Count of the product description
    df["description_word_count"] = df["product_description"].apply(
        lambda x: 0 if x == "No description available." else len(str(x).split())
    )

    # Feature 2: Price Band categorisation based on dataset distribution
    # Low: under £20, Medium: £20 to £40, High: over £40
    def assign_price_band(price):
        if price < 20.0:
            return "Low"
        elif price <= 40.0:
            return "Medium"
        else:
            return "High"

    df["price_band"] = df["price_numeric"].apply(assign_price_band)

    # Feature 3: Value Score (Ratio of rating performance to its numeric cost)
    # Higher value score = better rating bang-for-your-buck
    df["value_score"] = round(df["rating_numeric"] / df["price_numeric"], 4)

    # Feature 4: Recommendation Flag (Boolean)
    # True if the item holds a high rating (4+) and is actively in stock
    df["recommended"] = (df["rating_numeric"] >= 4) & (df["stock_count"] > 0)

    # ----------------------------------------------------
    # 5. Export Cleaned Pipeline Output
    # ----------------------------------------------------
    df.to_csv(output_file, index=False)
    print(f"Preprocessing successfully saved to: '{output_file}'")

    # Display a sneak peek of the newly created features
    print("\nSample Preview of Processed Feature Set:")
    preview_cols = [
        "title",
        "price_numeric",
        "rating_numeric",
        "stock_count",
        "description_word_count",
        "price_band",
        "value_score",
        "recommended",
    ]
    print(df[preview_cols].head(3).to_string())


if __name__ == "__main__":
    preprocess_book_data()
