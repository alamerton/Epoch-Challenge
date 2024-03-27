import plotly.graph_objects as go

# Read the existing HTML file
with open('challenge-figure.html', 'r') as file:
    html_content = file.read()

# Create a Figure object from the HTML content
fig = go

# Update the layout to use logarithmic scales
fig.update_layout(
    xaxis_type='log',
    yaxis_type='log'
)

# Save the updated figure as a new HTML file
fig.write_html('logarithmic_graph.html')
