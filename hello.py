import pandas as pd
from preswald import connect, get_df


connect()
df = get_df("data/mental_health_dataset.csv")

# this function was not behaving correctly
from preswald import query

sql = "SELECT * FROM df"
result = query(sql, "df")

from preswald import table, text

text("# My Data Analysis App")

# I would show the result variable here but query does
# not seem to be working correctly
table(df, title="Filtered Data")

from preswald import plotly
import plotly.express as px

fig = px.scatter(df, x="age", y="sleep_hours", color="stress_level")
plotly(fig)