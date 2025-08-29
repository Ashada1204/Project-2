import pandas as pd

def clean_csv(input_file, output_file):
    # Load CSV
    df = pd.read_csv(input_file)

    print("Columns in CSV:", df.columns)  # Debugging step

    # Handle Age column → fill missing with mean, round to nearest int
    if "Age" in df.columns:
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")  # convert all to numbers
        if df["Age"].notna().sum() > 0:  # only if valid values exist
            mean_age = df["Age"].mean()
            df["Age"] = df["Age"].fillna(mean_age).round().astype(int)

    # Handle Fare column → fill missing with mean (keep numeric)
    if "Fare" in df.columns:
        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")
        if df["Fare"].notna().sum() > 0:
            mean_fare = df["Fare"].mean()
            df["Fare"] = df["Fare"].fillna(mean_fare)

    # For other columns → replace missing values with "Missing"
    for col in df.columns:
        if col not in ["Age", "Fare"]:
            df[col] = df[col].fillna("Missing")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Export cleaned CSV
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned dataset saved to {output_file}")


# Example usage
input_file = "Titanic_Dataset.csv"
output_file = "Titanic_Dataset_Cleaned.csv"
clean_csv(input_file, output_file)
