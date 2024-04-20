import requests
import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.express as px

def dashboard():
    # Using latitude and longitude of Kansas City
    latitude = "39.09973000"
    longitude = "-94.57857000"

    api_key = "0b6f74926bf66f0ff55d68e7d8aed37d"

    weather_api_url = "https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&appid={}".format(latitude, longitude, api_key)

    response = requests.get(weather_api_url)

    # Save the response into a variable
    weather_data = response.json()

    # selecting hourly data for dashboard
    hourly_data = weather_data["hourly"]

    df = pd.DataFrame(hourly_data)

    # Select the desired columns
    df = df[["dt", "temp", "feels_like", "pressure", "humidity", "uvi", "dew_point", "clouds", "wind_speed", "pop", "weather"]]

    # Convert timestamps to datetime objects
    df["dt"] = pd.to_datetime(df["dt"], unit="s")

    df['weather'] = df['weather'].apply(lambda x: x[0]['main'])

    # create dashboard
    app = dash.Dash(__name__)

    app.layout = html.Div(children=[
        html.H1(children='Weather Dashboard'),

        dcc.Graph(
            id='temp_vs_feels_like',
            figure={
                'data': [
                    {'x': df['dt'], 'y': df['temp'], 'type': 'line', 'name': 'Temperature'},
                    {'x': df['dt'], 'y': df['feels_like'], 'type': 'line', 'name': 'Feels Like'},
                ],
                'layout': {
                    'title': 'Temperature Vs Feels Like',
                    'xaxis': {
                        'title': 'Time',
                        'tickformat': '%d/%m/%Y %H:%M'
                    },
                    'yaxis': {
                        'title': 'Value'
                    }
                }
            }
        ),
        dcc.Graph(
            id='clouds_vs_temperature',
            figure=px.scatter(df, x=df["temp"], y=df["clouds"], title="Clouds VS Temperature")
        )
    ])

    # the dashboard will be accessible through http://127.0.0.1:8050/ after running the server. the screenshot of the dashboard is provided in the result folder.
    app.run_server(debug=True)




dashboard()
