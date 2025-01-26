import pandas as pd
import plotly.express as px

# Step 1: Load the CSV file into a DataFrame
file_path = './LebronData/lebron_james_2025_gamelog.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Step 2: Create an interactive graph (e.g., line chart)
fig = px.scatter(data, x='FG%', y='FT', title='Interactive Graph')

# Step 3: Show the graph
fig.show()