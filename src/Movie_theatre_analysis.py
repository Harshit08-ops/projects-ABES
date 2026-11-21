
import pandas as pd
import numpy as np
import os

# ============================================================
# MOVIE THEATER BOX OFFICE & CONCESSION ANALYSIS
# ============================================================

# PROJECT FOLDER PATHS
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "Data", "Cinema_sales_data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "Output")

os.makedirs(OUTPUT_DIR, exist_ok=True)


# FUNCTION TO DISPLAY TASK HEADINGS
def heading(title):
    print("\n" + "=" * 65)
    print(title)
    print("=" * 65)


# FUNCTION TO DISPLAY TABLES
def show_table(data):
    if data.empty:
        print("No records found.")
    else:
        print(data.to_string(index=False))


print("\n")
print("=" * 65)
print("       MOVIE THEATER BOX OFFICE & CONCESSION ANALYSIS")
print("=" * 65)


# ============================================================
# TASK 1: LOAD AND INSPECT DATASET
# ============================================================

heading("TASK 1: LOAD AND INSPECT DATASET")

if not os.path.exists(DATA_PATH):
    print("ERROR: Dataset file not found!")
    print("Please check the Data folder.")
    raise SystemExit

df = pd.read_csv(DATA_PATH)

required_columns = [
    "Transaction_ID",
    "Movie",
    "Genre",
    "Show_Date",
    "Showtime_Slot",
    "Screen_Format",
    "Ticket_Quantity",
    "Ticket_Price",
    "Occupancy_Percentage",
    "Concession_Spend"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    print("ERROR: Required columns are missing:", missing_columns)
    raise SystemExit

print("Dataset loaded successfully!")

print("\nFirst 5 Records:")
print(df.head().to_string(index=False))

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include="all").to_string())


# ============================================================
# TASK 2: MISSING VALUES AND DUPLICATES
# ============================================================

heading("TASK 2: MISSING VALUES AND DUPLICATES")

print("Missing Values:")
print(df.isnull().sum().to_string())

duplicates = df["Transaction_ID"].duplicated().sum()

print("\nDuplicate Transaction IDs:", duplicates)


# ============================================================
# TASK 3: DATA CLEANING
# ============================================================

heading("TASK 3: DATA CLEANING")

missing_before = df["Concession_Spend"].isnull().sum()

median_value = df["Concession_Spend"].median()

df["Concession_Spend"] = df["Concession_Spend"].fillna(
    median_value
)

df = df.drop_duplicates(
    subset="Transaction_ID",
    keep="first"
).copy()

print("Missing values before cleaning:", missing_before)
print("Median concession spending:", median_value)
print(
    "Missing values after cleaning:",
    df["Concession_Spend"].isnull().sum()
)
print("Duplicate records removed:", duplicates)
print("Records after cleaning:", len(df))


# ============================================================
# TASK 4: DATE CONVERSION
# ============================================================

heading("TASK 4: DATE CONVERSION")

df["Show_Date"] = pd.to_datetime(
    df["Show_Date"],
    errors="coerce"
)

invalid_dates = df["Show_Date"].isnull().sum()

df = df.dropna(subset=["Show_Date"]).copy()

df["Day_Type"] = np.where(
    df["Show_Date"].dt.day_of_week >= 5,
    "Weekend",
    "Weekday"
)

print("Date conversion completed!")
print("Invalid dates removed:", invalid_dates)

print("\nDate and Day Type:")
show_table(df[["Show_Date", "Day_Type"]].head())


# ============================================================
# TASK 5: REVENUE CALCULATION
# ============================================================

heading("TASK 5: REVENUE CALCULATION")

df["Ticket_Revenue"] = (
    df["Ticket_Quantity"] * df["Ticket_Price"]
)

df["Total_Revenue"] = (
    df["Ticket_Revenue"] + df["Concession_Spend"]
)

print("First 5 Revenue Records:")
show_table(
    df[
        [
            "Ticket_Revenue",
            "Concession_Spend",
            "Total_Revenue"
        ]
    ].head()
)

total_ticket_revenue = df["Ticket_Revenue"].sum()
total_concession_revenue = df["Concession_Spend"].sum()
total_combined_revenue = df["Total_Revenue"].sum()

print("\nTotal Ticket Revenue:", round(total_ticket_revenue, 2))
print("Total Concession Revenue:", round(total_concession_revenue, 2))
print("Total Combined Revenue:", round(total_combined_revenue, 2))


# ============================================================
# TASK 6: TOP 10 MOVIES
# ============================================================

heading("TASK 6: TOP 10 MOVIES")

movie_analysis = df.groupby("Movie").agg(
    Total_Tickets=("Ticket_Quantity", "sum"),
    Ticket_Revenue=("Ticket_Revenue", "sum")
).reset_index()

top_movies = movie_analysis.sort_values(
    by="Ticket_Revenue",
    ascending=False
).head(10)

print("Top 10 Movies by Ticket Revenue:")
show_table(top_movies)

top_movies.to_csv(
    os.path.join(OUTPUT_DIR, "Top_10_Movies.csv"),
    index=False
)

print("\nTop 10 Movies saved successfully.")


# ============================================================
# TASK 7: SCREEN FORMAT ANALYSIS
# ============================================================

heading("TASK 7: SCREEN FORMAT ANALYSIS")

screen_analysis = df.groupby("Screen_Format").agg(
    Average_Occupancy=("Occupancy_Percentage", "mean"),
    Total_Tickets=("Ticket_Quantity", "sum"),
    Total_Revenue=("Total_Revenue", "sum")
).reset_index()

print("Screen Format Performance:")
show_table(screen_analysis)

screen_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "Screen_Format_Analysis.csv"),
    index=False
)

print("\nScreen Format Analysis saved successfully.")


# ============================================================
# TASK 8: WEEKDAY AND WEEKEND ANALYSIS
# ============================================================

heading("TASK 8: WEEKDAY AND WEEKEND ANALYSIS")

day_analysis = df.groupby("Day_Type").agg(
    Total_Ticket_Sales=("Ticket_Revenue", "sum"),
    Total_Concession_Spending=("Concession_Spend", "sum"),
    Total_Attendance=("Ticket_Quantity", "sum")
).reset_index()

print("Weekday and Weekend Comparison:")
show_table(day_analysis)

day_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "Weekday_Weekend_Analysis.csv"),
    index=False
)

print("\nWeekday Weekend Analysis saved successfully.")


# ============================================================
# TASK 9: SHOWTIME ANALYSIS
# ============================================================

heading("TASK 9: SHOWTIME ANALYSIS")

showtime_analysis = df.groupby("Showtime_Slot").agg(
    Total_Attendance=("Ticket_Quantity", "sum"),
    Total_Revenue=("Total_Revenue", "sum")
).reset_index()

print("Showtime Performance:")
show_table(showtime_analysis)

showtime_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "Showtime_Analysis.csv"),
    index=False
)

print("\nShowtime Analysis saved successfully.")


# ============================================================
# TASK 10: CONCESSION ATTACH RATE
# ============================================================

heading("TASK 10: CONCESSION ATTACH RATE")

total_transactions = len(df)

concession_transactions = (
    df["Concession_Spend"] > 0
).sum()

if total_transactions > 0:
    attach_rate = (
        concession_transactions / total_transactions
    ) * 100
else:
    attach_rate = 0

print("Total Transactions:", total_transactions)

print(
    "Transactions with Concession Purchases:",
    concession_transactions
)

print("Concession Attach Rate:", round(attach_rate, 2), "%")


# ============================================================
# TASK 11: GENRE-WISE SPENDING ANALYSIS
# ============================================================

heading("TASK 11: GENRE-WISE SPENDING ANALYSIS")

genre_analysis = df.groupby("Genre").agg(
    Average_Ticket_Spending=("Ticket_Revenue", "mean"),
    Average_Snack_Spending=("Concession_Spend", "mean"),
    Total_Attendance=("Ticket_Quantity", "sum")
).reset_index()

print("Genre Analysis:")
show_table(genre_analysis)

genre_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "Genre_Analysis.csv"),
    index=False
)

print("\nGenre Analysis saved successfully.")


# ============================================================
# TASK 12: NUMPY STATISTICAL ANALYSIS
# ============================================================

heading("TASK 12: NUMPY STATISTICAL ANALYSIS")

total_spending = df["Total_Revenue"].to_numpy()

print(
    "Mean Total Spending:",
    round(np.mean(total_spending), 2)
)

print(
    "Median Total Spending:",
    round(np.median(total_spending), 2)
)

print(
    "Standard Deviation:",
    round(np.std(total_spending), 2)
)


# ============================================================
# TASK 13: LARGE GROUP BOOKINGS USING IQR
# ============================================================

heading("TASK 13: LARGE GROUP BOOKINGS USING IQR")

q1 = df["Ticket_Quantity"].quantile(0.25)
q3 = df["Ticket_Quantity"].quantile(0.75)

iqr = q3 - q1

upper_limit = q3 + (1.5 * iqr)

large_groups = df[
    df["Ticket_Quantity"] > upper_limit
].copy()

print("First Quartile (Q1):", q1)
print("Third Quartile (Q3):", q3)
print("Interquartile Range (IQR):", iqr)
print("Upper Limit:", upper_limit)

print(
    "Potential Large Group Bookings:",
    len(large_groups)
)

print("\nLarge Group Booking Records:")

show_table(
    large_groups[
        [
            "Transaction_ID",
            "Movie",
            "Ticket_Quantity"
        ]
    ]
)

large_groups.to_csv(
    os.path.join(OUTPUT_DIR, "Large_Group_Bookings.csv"),
    index=False
)

print("\nLarge Group Bookings saved successfully.")


# ============================================================
# TASK 14: TICKET QUANTITY CATEGORIES
# ============================================================

heading("TASK 14: TICKET QUANTITY CATEGORIES")

bins = [0, 1, 2, 5, np.inf]

labels = [
    "Solo",
    "Couple",
    "Small Group",
    "Large Group"
]

df["Group_Category"] = pd.cut(
    df["Ticket_Quantity"],
    bins=bins,
    labels=labels
)

print("Ticket Quantity Category Counts:")

print(
    df["Group_Category"]
    .value_counts()
    .reindex(labels, fill_value=0)
    .to_string()
)


# ============================================================
# TASK 15: BUSINESS RECOMMENDATIONS
# ============================================================

heading("TASK 15: BUSINESS RECOMMENDATIONS")

if not top_movies.empty:
    top_movie = top_movies.iloc[0]["Movie"]
else:
    top_movie = "No data available"

if not screen_analysis.empty:
    best_screen = screen_analysis.loc[
        screen_analysis["Average_Occupancy"].idxmax(),
        "Screen_Format"
    ]
else:
    best_screen = "No data available"

if not showtime_analysis.empty:
    best_showtime = showtime_analysis.loc[
        showtime_analysis["Total_Attendance"].idxmax(),
        "Showtime_Slot"
    ]
else:
    best_showtime = "No data available"

if not day_analysis.empty:
    best_day = day_analysis.loc[
        day_analysis["Total_Ticket_Sales"].idxmax(),
        "Day_Type"
    ]
else:
    best_day = "No data available"

if not genre_analysis.empty:
    best_genre = genre_analysis.loc[
        genre_analysis["Total_Attendance"].idxmax(),
        "Genre"
    ]
else:
    best_genre = "No data available"

print("1. Promote the movie with the highest ticket revenue:", top_movie)

print(
    "2. Focus on the screen format with highest average occupancy:",
    best_screen
)

print(
    "3. Consider more shows during the busiest showtime:",
    best_showtime
)

print(
    "4. Plan suitable offers for the stronger ticket sales period:",
    best_day
)

print(
    "5. Focus marketing on the genre with highest attendance:",
    best_genre
)


# ============================================================
# SAVE CLEANED DATASET
# ============================================================

df.to_csv(
    os.path.join(OUTPUT_DIR, "Cleaned_Cinema_Sales.csv"),
    index=False
)

print("\nCleaned dataset saved successfully.")

print("\nAll output files are stored in the Output folder.")


# ============================================================
# PROJECT COMPLETION
# ============================================================

heading("PROJECT COMPLETED SUCCESSFULLY")

print("All 15 Tasks Completed Successfully!")
print("Thank You!")

print("=" * 65)
