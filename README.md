
# Movie Theater Box Office & Concession Analysis

## Project Overview

This project focuses on analyzing movie theater ticket sales and concession purchases. It helps understand movie performance, customer attendance, revenue generation, and food and beverage sales.

The analysis is performed using Python, Pandas, and NumPy.

## Student Details

- **Name:** Harshit Kaushik
- **Roll Number:** 2026B15410204
- **Course:** B.Tech CSE DS

## Project Objectives

- Analyze movie ticket sales and revenue.
- Identify the top-performing movies.
- Compare weekday and weekend sales.
- Study screen format performance.
- Analyze showtime attendance.
- Understand concession spending.
- Identify large group bookings.
- Provide business recommendations.

## Technologies Used

- Python
- Pandas
- NumPy
- Visual Studio Code

## Dataset Information

The project uses a CSV dataset containing movie theater transaction records.

The dataset includes:
- Transaction ID
- Movie
- Genre
- Show Date
- Showtime Slot
- Screen Format
- Ticket Quantity
- Ticket Price
- Occupancy Percentage
- Concession Spend

## Tasks Performed

1. Load and inspect the dataset.
2. Identify missing values and duplicate records.
3. Clean missing values and remove duplicates.
4. Convert dates and identify weekdays and weekends.
5. Calculate ticket, concession, and total revenue.
6. Identify the top 10 movies.
7. Analyze screen format performance.
8. Compare weekday and weekend sales.
9. Analyze attendance by showtime.
10. Calculate concession attach rate.
11. Analyze spending by movie genre.
12. Calculate mean, median, and standard deviation using NumPy.
13. Identify potential large group bookings using IQR.
14. Categorize transactions by ticket quantity.
15. Provide business recommendations.

## Project Structure

```text
Movie-theatre-analysis/
│
├── Data/
│   └── Cinema_sales_data.csv
│
├── Output/
│   ├── Cleaned_Cinema_Sales.csv
│   ├── Top_10_Movies.csv
│   ├── Screen_Format_Analysis.csv
│   ├── Weekday_Weekend_Analysis.csv
│   ├── Showtime_Analysis.csv
│   ├── Genre_Analysis.csv
│   └── Large_Group_Bookings.csv
│
├── src/
│   └── Movie_theatre_analysis.py
│
├── SRS.docx
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Install the required libraries using:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command from the main project folder:

```bash
python src/Movie_theatre_analysis.py
```

## Output

The program displays the results of all 15 tasks in the terminal and saves the analysis results as CSV files in the Output folder.

The project uses text-based output and does not include data visualizations.

## Conclusion

This project provides a basic analysis of movie theater operations using transaction data. The results help understand ticket sales, concession revenue, customer attendance, and movie performance.

It also provides recommendations that can help improve theater operations and business decisions.
