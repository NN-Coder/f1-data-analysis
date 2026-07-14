import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
plt.figure(figsize=(11, 6))
sns.set_theme(style="whitegrid")
sns.scatterplot(
    data=plot_data,
    x='totalEntries',
    y='APG',
    alpha=0.7,
    edgecolor='none',
    s=80,
    color='#2b5c8f'
)
cutoff = 700
plt.axvline(x=cutoff, color='red', linestyle='--', linewidth=1.5, label=f'The Cutoff Threshold ({cutoff} entries)')
forti_row = plot_data[plot_data['name'] == 'Forti']
if not forti_row.empty:
    plt.text(
        x=forti_row['totalEntries'].values[0] + 5,
        y=forti_row['APG'].values[0] - 0.2,
        s='Forti Corse (~5.11 APG)',
        color='darkred',
        weight='bold',
        fontsize=10
    )
plt.xscale('log')
plt.title('Sample Size and Statistical Variance', fontsize=14, pad=15, weight='bold')
plt.xlabel('Total Race Entries (Log Scale)', fontsize=12)
plt.ylabel('Average Positions Gained (APG)', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
