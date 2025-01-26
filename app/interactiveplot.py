from flask import Flask, render_template
from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)

@app.route('/')
def home():
    # Create a Bokeh plot
    plot = figure(title="Example Bokeh Plot", x_axis_label='X-Axis', y_axis_label='Y-Axis')
    plot.line([1, 2, 3, 4], [4, 3, 2, 1], legend_label="Line", line_width=2)

    # Get the plot components
    script, div = components(plot)

    # Return the plot in the template
    return render_template('index.html', script=script, div=div)

if __name__ == '__main__':
    app.run(debug=True)
