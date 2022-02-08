from turtle import color
from django.template import base
import greenlet
import plotly.graph_objects as go
import pandas as pd
import numpy as np

s = pd.read_csv(r"C:\Users\sr528\OneDrive\Desktop\bar graph\xymo.csv")


fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=s["date"],
        y=s["AUTOMOTIVE"]
    ))

fig.add_trace(
    go.Bar(
        x=s["date"],
        y=s["AUTOMOTIVE"]
    ))

fig.show()