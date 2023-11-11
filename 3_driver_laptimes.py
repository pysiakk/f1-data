import fastf1 as f1
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import unicodedata
from datetime import datetime

from utils import team_color_hex

# %%
def generate_driver_laptimes_plot(year, gp, identifier):
    race = f1.get_session(year, gp, identifier)
    race.load()

    driver_performance = race.laps.copy()
    driver_performance.LapTime = (
        driver_performance["LapTime"].dt.components["seconds"]
        + (driver_performance["LapTime"].dt.components["milliseconds"] / 1000)
        + (driver_performance["LapTime"].dt.components["minutes"] * 60)
    )
    driver_performance = driver_performance.loc[driver_performance.IsAccurate]

    team_dump = []
    fig = go.Figure(
        layout=go.Layout(
            template="plotly_dark",
            width=1000,
            height=1000,
            title=dict(
                text=f"Drivers Lap Times - {race.event.Location} {race.session_info['StartDate'].year} - {race.session_info['Type']}",
                font=dict(size=30),
                automargin=False,
            ),
            yaxis_range=[
                driver_performance.LapTime.min(),
                1.10 * driver_performance.LapTime.min(),
            ],
        )
    )
    for driver in race.results.Abbreviation:
        data = driver_performance.loc[driver_performance.Driver == driver]
        if data.shape[0] == 0:
            continue
        fig.add_trace(
            go.Scatter(
                x=data.LapNumber,
                y=data.LapTime,
                name=driver,
                line=dict(
                    color=team_color_hex(data.iloc[0].Team),
                    width=2.5,
                    shape="linear",
                    dash="dash" if data.Team.iloc[0] in team_dump else "solid",
                ),
            )
        )
        team_dump.append(data.iloc[0].Team)
    fig.update_yaxes(title="Lap time")
    fig.update_xaxes(title="Lap")

    fig.write_html(
        f"figs/driver_laptimes/{unicodedata.normalize('NFD', race.event.Location).encode('ascii', 'ignore').lower().replace(b' ', b'_').decode('utf-8')}_{race.event.EventDate.year}.html"
    )

# %%
schedule = f1.get_event_schedule(2023)
schedule.loc[:,'Session5Date'] = pd.to_datetime(schedule.Session5Date, utc=True)
schedule = schedule.loc[
    (schedule.EventFormat != "testing") & (schedule.Session5Date < pd.Timestamp(datetime.now(), tz=0))
]
for event in schedule.RoundNumber:
    generate_driver_laptimes_plot(2023, event, "race")

# %%
