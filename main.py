import requests
import pandas as pd

# APG - average positions gained
f1 = pd.read_csv('results.csv') # reading results csv file into Pandas dataframe
f1 = f1[['constructorId', 'grid', 'positionOrder']] # only using the three columns we need
f1.columns = ['teamId', 'startPos', 'endPos'] # renaming columns
f1['positionsGained'] = f1['startPos'] - f1['endPos'] # creating new column with positions gained
total_teams = f1.groupby('teamId')['positionsGained'].mean().reset_index() # creating new dataframe with each team and its APG
total_teams.columns = ['teamId', 'APG'] # renaming columns
team_entries = f1['teamId'].value_counts().reset_index() # creating new dataframe with each team and its total entries
team_entries.columns = ['teamId', 'totalEntries'] # renaming columns
total_teams = pd.merge(total_teams, team_entries, on = 'teamId', how = 'left') # combining the total entries and APG dataframes

# IMPORTANT
min_entries_required = 150 # increase this value to get data for more prevalent teams and vice versa; note that changing it too much can lead to skewed results.

if min_entries_required <= total_teams['totalEntries'].max(): # checking that the requirement is within limits
  sat_teams = total_teams[total_teams['totalEntries'] >= min_entries_required].reset_index(drop = True) # creating new dataframe with only teams that satisfy the entries requirement
  team_names = pd.read_csv('constructors.csv') # reading constructors csv file into Pandas dataframe
  sat_teams = pd.merge(sat_teams, team_names[['constructorId', 'name', 'nationality']], left_on = 'teamId', right_on = 'constructorId', how = 'left') # combining team names and nationalities with the main dataframe
  sat_teams = sat_teams[['teamId', 'name', 'nationality', 'APG', 'totalEntries']] # selecting and reordering columns
  ht_apg = round(sat_teams['APG'].max(), 2) # finding the APG of the team with the highest APG and rounding for ease of viewing
  ht_id = sat_teams.loc[sat_teams['APG'].idxmax(), 'teamId'] # finding the team ID of the team with the highest APG
  ht_name = sat_teams.loc[sat_teams['teamId'] == ht_id, 'name'].iloc[0] # finding the name of the team with the highest APG
  ht_nationality = sat_teams.loc[sat_teams['teamId'] == ht_id, 'nationality'].iloc[0] # finding the nationality of the team with the highest APG

  # Printing final results
  print(f"The team with the highest APG, being ~{ht_apg}, is {ht_nationality} {ht_name}.")
  print(f"Note that this calculation only uses teams with more than or equal to {min_entries_required} entries (this requirement can be changed on line 16).")
  print()
  # Printing top teams' APGs (top 10 if the total amount of teams is 10 or more, otherwise the total amount of teams)
  top_teams = sat_teams.sort_values(by = 'APG', ascending = False).head(10).reset_index(drop = True)
  print("Top Teams by Average Positions Gained (APG):")
  print(top_teams.to_string())
else: # Notify user of invalid entry requirement rather than throwing an error
  print(f"Your chosen minimum team entry requirement, {min_entries_required}, exceeds the top entry limit. Please decrease it to avoid errors.")
