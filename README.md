# Zomato-Data-Analysis
Project Overview
This project involves analyzing a dataset of Zomato restaurants to gain insights into the restaurant industry. The dataset includes information on various aspects of restaurants, including their ratings, types, votes, cost for two people, and whether they accept online orders.

Technologies Used
Python: The programming language used for data manipulation and analysis.
Pandas: A powerful data manipulation library used for reading and processing the dataset.
NumPy: Used for numerical computations.
Matplotlib: A plotting library used for creating visualizations.
Seaborn: An enhanced data visualization library built on Matplotlib, used for creating more advanced visualizations.
Dataset
The dataset used in this project is a CSV file named Zomato data.csv. It contains information about various restaurants listed on Zomato. The key columns used in this analysis include:

rate: The rating of the restaurant.
listed_in(type): The type/category of the restaurant.
votes: The number of votes received by the restaurant.
approx_cost(for two people): The approximate cost for two people.
online_order: Indicates whether the restaurant accepts online orders.
Data Processing
Handling Ratings: The ratings are originally stored as strings in the format X.X/5. A function handleRate was implemented to extract the numerical rating and convert it to a float.
Grouping Data: The data was grouped by restaurant type to calculate the total votes each type received.
Visualizations
Restaurant Types Count Plot:

A count plot of the different restaurant types (listed_in(type)).

Votes by Restaurant Type:

A line plot showing the total number of votes for each type of restaurant.

Ratings Distribution:

A histogram showing the distribution of ratings.

Cost for Two People:

A count plot of the approximate cost for two people.

Online Order vs. Rating:

A box plot showing the relationship between online orders and ratings.

Heatmap:

A heatmap of the number of restaurants that accept online orders, grouped by restaurant type.

Conclusion
The analysis provides insights into the Zomato restaurant dataset, including the distribution of restaurant ratings, the types of restaurants that receive the most votes, and the relationship between online orders and ratings.

How to Run
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/zomato-data-analysis.git
Install Dependencies:

Copy code
pip install numpy pandas matplotlib seaborn
Run the Analysis:

Copy code
python zomato_analysis.py

