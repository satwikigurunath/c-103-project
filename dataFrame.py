import pandas as pd
import plotly.express as px

f=pd.read_csv("data_frame.csv")

figure=px.scatter(f,x="date",y="cases", color="country",title='Covid Cases')
figure.show()