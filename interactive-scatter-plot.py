import plotly.express as px

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
