from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Load JSON data
    json_file = './LebronData/lebron_james_processed.json'
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Convert JSON to DataFrame (if applicable)
    df = pd.DataFrame(data)
    df = df.sort_values(by=["Minutes", "FG"])

    # Create plot
    fig = px.scatter(df, x="Minutes", y="FG")  # Customize as needed
    graph_html = fig.to_html(full_html=False)

    return render_template('index.html', plot=graph_html)

if __name__ == '__main__':
    app.run(debug=True)
