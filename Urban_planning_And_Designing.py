import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Sample dataset
data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01'],
    'WQI_Phase_4': [53.35, 60.0, 58.5],
    'pH_Phase_4': [7.6, 7.9, 7.4],
    'DO_Phase_4': [7.8, 8.1, 8.0],
    'Turbidity_Phase_4': [12.10, 9.8, 10.5]
}

# Create DataFrame
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Create figures
fig_wqi = px.line(df, x='Date', y='WQI_Phase_4', title='Water Quality Index Comparison')
fig_ph = px.line(df, x='Date', y='pH_Phase_4', title='pH Comparison')
fig_do = px.line(df, x='Date', y='DO_Phase_4', title='Dissolved Oxygen Comparison')
fig_turbidity = px.line(df, x='Date', y='Turbidity_Phase_4', title='Turbidity Comparison')

# Dash app
app = Dash(__name__)
app.layout = html.Div([
    html.H1('Urban Lake Monitoring System'),
    html.Div([html.Label('Water Quality Index'), dcc.Graph(figure=fig_wqi)]),
    html.Div([html.Label('pH Levels'), dcc.Graph(figure=fig_ph)]),
    html.Div([html.Label('Dissolved Oxygen'), dcc.Graph(figure=fig_do)]),
    html.Div([html.Label('Turbidity'), dcc.Graph(figure=fig_turbidity)])
])

if __name__ == '__main__':
    app.run(debug=True)

