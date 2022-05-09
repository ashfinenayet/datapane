import pandas as pd
import plotly.express as px
df = pd.read_csv('updatedreport.csv')

fig = px.scatter(df, x="year", y="Happiness Score", animation_frame="year", animation_group="Country", title='Happiness Score 2015-2022',
            color="Region", hover_name="Country", hover_data=["Happiness Rank"],
           log_x=True, size_max=120, range_x=[2015,2022], range_y=[2,8])

fig.show()