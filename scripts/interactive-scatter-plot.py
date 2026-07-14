import plotly.express as px
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

f1 = pd.read_csv(DATA_DIR / 'results.csv')
f1 = f1[['constructorId', 'grid', 'positionOrder']].copy()
f1.columns = ['teamId', 'startPos', 'endPos']
f1['positionsGained'] = f1['startPos'] - f1['endPos']
total_teams = f1.groupby('teamId')['positionsGained'].mean().reset_index()
total_teams.columns = ['teamId', 'APG']
team_entries = f1['teamId'].value_counts().reset_index()
team_entries.columns = ['teamId', 'totalEntries']
plot_data = pd.merge(total_teams, team_entries, on='teamId', how='left')
team_names = pd.read_csv(DATA_DIR / 'constructors.csv')
plot_data = pd.merge(plot_data, team_names[['constructorId', 'name']], left_on='teamId', right_on='constructorId', how='left')

fig = px.scatter(
    plot_data,
    x='totalEntries',
    y='APG',
    hover_name='name',
    log_x=True,
    title='Interactive Analysis: Sample Size vs. Statistical Variance',
    labels={'totalEntries': 'Total Race Entries (Log Scale)', 'APG': 'Average Positions Gained (APG)'},
    template='plotly_white',
    hover_data={'totalEntries': True, 'APG': ':.2f', 'teamId': False}
)

fig.add_hline(y=0, line_dash="dot", line_color="black", line_width=1)

fig.show()
