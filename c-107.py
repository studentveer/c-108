import pandas as pd
import plotly.figure_factory as ff

df=pd.read_csv("C:/Users/dell/Desktop/Python/project/data.csv")

fig=ff.create_distplot([df["AvgRating"]],["AvgRating"],show_hist=False)
fig.show()