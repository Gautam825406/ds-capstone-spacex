# SpaceX Falcon 9 Launch Dashboard
# Author: Gautam825406
# Run: python spacex_dash_app.py

import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
spacex_df = pd.read_csv(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
    'IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv'
)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Initialize app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div(children=[
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
    ),

    # Dropdown for launch site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40',  'value': 'CCAFS LC-40'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
            {'label': 'KSC LC-39A',   'value': 'KSC LC-39A'},
            {'label': 'VAFB SLC-4E',  'value': 'VAFB SLC-4E'},
        ],
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True
    ),

    html.Br(),

    # Pie chart
    html.Div(dcc.Graph(id='success-pie-chart')),

    html.Br(),
    html.P("Payload range (Kg):"),

    # Payload slider
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: f'{i} kg' for i in range(0, 10001, 2000)},
        value=[min_payload, max_payload]
    ),

    html.Br(),

    # Scatter chart
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# Callback 1: Pie chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(
            spacex_df,
            values='class',
            names='Launch Site',
            title='Total Successful Launches by Site'
        )
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        filtered_df = filtered_df.groupby(['class'])['class'].count().reset_index(name='count')
        filtered_df['Outcome'] = filtered_df['class'].map({0: 'Failure', 1: 'Success'})
        fig = px.pie(
            filtered_df,
            values='count',
            names='Outcome',
            title=f'Launch Success vs Failure for {entered_site}',
            color='Outcome',
            color_discrete_map={'Success': 'green', 'Failure': 'red'}
        )
    return fig


# Callback 2: Scatter chart
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown',   component_property='value'),
     Input(component_id='payload-slider',  component_property='value')]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    mask = (
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    )
    filtered_df = spacex_df[mask]

    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]

    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title=f'Payload vs Launch Outcome — {entered_site}',
        labels={'class': 'Launch Outcome (1=Success, 0=Failure)'},
        hover_data=['Launch Site']
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True, port=8050)
