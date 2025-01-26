from flask import Flask, render_template, url_for
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


@app.route('/GOAT')
def goat():
    image_url = url_for('static', filename='lebonbon.jpeg')
    return render_template('goat.html', image_url=image_url)

@app.route('/heatmap')
def heatmap():
    # Load JSON data
    json_file = './LebronData/lebron_james_processed.json'
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Convert JSON to DataFrame (if applicable)

    df = pd.DataFrame(data)
    df[['Points', 'Assists', 'Rebounds']] = df[['Points', 'Assists', 'Rebounds']].replace('', pd.NA)

    # Convert columns to numeric, coercing errors to NaN
    df['Points'] = pd.to_numeric(df['Points'], errors='coerce')
    df['Assists'] = pd.to_numeric(df['Assists'], errors='coerce')
    df['Rebounds'] = pd.to_numeric(df['Rebounds'], errors='coerce')

    # Drop rows with NaN values in the relevant columns (optional, based on your preference)
    df = df.dropna(subset=['Points', 'Assists', 'Rebounds'])
    heatmap_data = df[['Points', 'Assists', 'Rebounds']].corr()  # Example correlation matrix
    fig = px.imshow(heatmap_data, 
                    labels=dict(x="Stats", y="Stats"),
                    title="Correlation Heatmap of NBA Stats")

    # Convert the Plotly figure to HTML
    graph_html = fig.to_html(full_html=False)

    return render_template('heatmap.html', plot=graph_html)

# @app.route('/')
# def index():
#     # Load JSON data
#     json_file = './LebronData/lebron_james_processed.json'
#     with open(json_file, 'r') as file:
#         data = json.load(file)

#     # Convert JSON to DataFrame (if applicable)
#     df = pd.DataFrame(data)
#     df = df.sort_values(by=["Minutes", "FG"])

#     # Create plot
#     fig = px.scatter(df, x="Minutes", y="FG")  # Customize as needed
#     graph_html = fig.to_html(full_html=False)

#     return render_template('index.html', plot=graph_html)

@app.route('/LebronVSJordan')
def lvj():
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
