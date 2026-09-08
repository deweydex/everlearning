---
title: "Exploring the Galaxy with Pandas: A Star Trek Tutorial"
slug: 02-pandas-star-trek-tutorial
course: database-methods
course_title: "Database Methods"
series: core
series_title: "Notebooks"
version: 2026.09.06.1
---

# Exploring the Galaxy with Pandas: A Star Trek Tutorial

Welcome to this pandas tutorial using Star Trek-themed datasets. You'll learn the essential pandas operations for data analysis and visualization.

```python exec
id: 02-pandas-star-trek-tutorial-1
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting style
plt.style.use('ggplot')
sns.set(style="darkgrid")
```

## Creating Our Star Trek Datasets

Let's create two datasets: one for starships and another for missions.

```python exec
id: 02-pandas-star-trek-tutorial-2
# Create a DataFrame for Starfleet and other notable ships
starships_data = {
    'ship_id': range(1, 11),
    'name': ['USS Enterprise', 'USS Voyager', 'USS Defiant', 'USS Discovery',
             'USS Excelsior', 'USS Reliant', 'Klingon Bird of Prey',
             'Romulan Warbird', 'Borg Cube', 'USS Prometheus'],
    'registry': ['NCC-1701-D', 'NCC-74656', 'NX-74205', 'NCC-1031',
                 'NCC-2000', 'NCC-1864', 'IKS Rotarran', 'IRW D\'deridex',
                 'Cube 5174', 'NX-59650'],
    'class': ['Galaxy', 'Intrepid', 'Defiant', 'Crossfield',
              'Excelsior', 'Miranda', 'B\'rel', 'D\'deridex',
              'Borg Cube', 'Prometheus'],
    'crew_size': [1014, 141, 50, 136,
                  750, 35, 12, 1500,
                  129000, 4],
    'max_warp': [9.8, 9.975, 9.5, 9.9,
                 9.1, 9.0, 9.6, 9.6,
                 9.8, 9.99],
    'launch_year': [2363, 2371, 2370, 2256,
                    2285, 2270, 2340, 2360,
                    2370, 2374],
    'captain': ['Picard', 'Janeway', 'Sisko', 'Lorca/Pike',
                'Sulu', 'Terrell', "Martok", 'Toreth',
                'Collective', 'Emergency Hologram'],
    'quadrant': ['Alpha', 'Delta', 'Alpha', 'Alpha',
                 'Alpha', 'Alpha', 'Alpha', 'Beta',
                 'Delta', 'Alpha'],
}

# Create the starships DataFrame
starships_df = pd.DataFrame(starships_data)

# Create a DataFrame for space missions
missions_data = {
    'mission_id': range(101, 111),
    'mission_name': ['First Contact with Q', 'Delta Quadrant Exploration', 'Dominion War',
                     'Klingon Peace Treaty', 'Genesis Project', 'Battle of Wolf 359',
                     'Cardassian Border Conflict', 'Romulan Neutral Zone Patrol',
                     'Borg Invasion Defense', 'Voyager Rescue'],
    'ship_id': [1, 2, 3, 1, 5, 1, 3, 8, 1, 10],
    'stardate': [41153.7, 48315.6, 49011.4, 43989.1, 8130.4, 43997.0,
                 47941.7, 58105.3, 50893.5, 51462.0],
    'duration_days': [7, 2555, 548, 32, 18, 1, 124, 87, 12, 42],
    'success': [True, True, True, True, False, False, True, True, True, True],
    'casualties': [0, 17, 23, 2, 35, 39, 4, 0, 11, 0],
    'first_contact': [True, True, False, False, False, False, False, False, False, False]
}

# Create the missions DataFrame
missions_df = pd.DataFrame(missions_data)

# Display the first few rows of each DataFrame
print("Starships DataFrame:")
starships_df.head()
```

## Basic DataFrame Operations

Let's explore our starships data.

```python exec
id: 02-pandas-star-trek-tutorial-3
# Check the shape of the DataFrame (rows, columns)
print(f"The starships DataFrame has {starships_df.shape[0]} rows and {starships_df.shape[1]} columns.")

# Get a summary of the DataFrame
print("\nDataFrame Information:")
starships_df.info()

# Get basic statistics
print("\nBasic Statistics:")
starships_df.describe()
```

### Accessing Columns and Rows

```python exec
id: 02-pandas-star-trek-tutorial-4
# Get a single column
print("Ship Names:")
starships_df['name']

# Get multiple columns
print("\nShip Names and Classes:")
starships_df[['name', 'class']]

# Access a specific row by index
print("\nSecond row (index 1):")
starships_df.iloc[1]

# Access rows by a condition
print("\nFederation ships (using string matching):")
federation_ships = starships_df[starships_df['registry'].str.contains('NCC|NX')]
federation_ships
```

## Your turn 1: Basic DataFrame Exploration

Now it's your turn to explore the missions DataFrame.

```python exec
id: 02-pandas-star-trek-tutorial-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# 1. Display the first 5 rows of the missions DataFrame
# Your code here

# 2. Check the shape of the missions DataFrame
# Your code here

# 3. Get the basic statistics for the missions DataFrame
# Your code here

# 4. Display only the mission_name and duration_days columns
# Your code here
```

## Filtering and Querying Data

```python exec
id: 02-pandas-star-trek-tutorial-6
# Filter ships with a crew size greater than 500
large_crews = starships_df[starships_df['crew_size'] > 500]
print("Ships with large crews:")
large_crews

# Multiple conditions using & (and) and | (or)
# Ships with large crews that can go faster than Warp 9.5
fast_large_ships = starships_df[(starships_df['crew_size'] > 500) & (starships_df['max_warp'] > 9.5)]
print("\nLarge ships that can go faster than Warp 9.5:")
fast_large_ships

# Filter using .query() method - an alternative syntax
alpha_quadrant = starships_df.query("quadrant == 'Alpha'")
print("\nShips in the Alpha Quadrant:")
alpha_quadrant
```

## Your turn 2: Filtering Practice

Time to practice your filtering skills on the missions DataFrame.

```python exec
id: 02-pandas-star-trek-tutorial-7
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# 1. Find all successful missions
# Your code here

# 2. Find missions that lasted longer than 100 days
# Your code here

# 3. Find successful missions with no casualties
# Your code here

# 4. Find first contact missions that were successful (use the & operator)
# Your code here
```

## Adding and Modifying Columns

```python exec
id: 02-pandas-star-trek-tutorial-8
# Add a new column: years in service (as of 2380)
starships_df['years_in_service'] = 2380 - starships_df['launch_year']

# Add a categorical column: ship size based on crew
def ship_size_category(crew_size):
    if crew_size < 50:
        return 'Small'
    elif crew_size < 500:
        return 'Medium'
    else:
        return 'Large'

starships_df['ship_size'] = starships_df['crew_size'].apply(ship_size_category)

# View the updated DataFrame
starships_df.head()
```

## Your turn 3: Adding and Modifying Columns

```python exec
id: 02-pandas-star-trek-tutorial-9
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# 1. Add a column 'casualty_rate' that calculates casualties per day (casualties / duration_days)
# Your code here

# 2. Add a categorical column 'mission_length' that categorizes missions as:
#    'Short' (less than 30 days), 'Medium' (30-365 days), 'Long' (over 365 days)
# Your code here
```

## Merging DataFrames

Now, let's combine our starships and missions data.

```python exec
id: 02-pandas-star-trek-tutorial-10
# Inner join: only keep rows where the ship_id exists in both DataFrames
mission_details = pd.merge(
    missions_df,
    starships_df,
    on='ship_id',
    how='inner'
)

# Display the merged DataFrame
print("Merged mission and ship details:")
mission_details.head()

# Left join: keep all missions, even if the ship doesn't exist in the starships DataFrame
all_missions = pd.merge(
    missions_df,
    starships_df[['ship_id', 'name', 'captain']],  # Select only specific columns
    on='ship_id',
    how='left'
)

print("\nAll missions with ship details (if available):")
all_missions.head()
```

## Your turn 4: Advanced Merging

```python exec
id: 02-pandas-star-trek-tutorial-11
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# 1. Create a small DataFrame of alien species and their quadrants of origin
species_data = {
    'species': ['Human', 'Vulcan', 'Klingon', 'Romulan', 'Borg', 'Cardassian', 'Bajoran'],
    'home_quadrant': ['Alpha', 'Alpha', 'Beta', 'Beta', 'Delta', 'Alpha', 'Alpha'],
    'federation_member': [True, True, True, False, False, False, True]
}
species_df = pd.DataFrame(species_data)

# 2. Merge this with the starships DataFrame based on the 'quadrant' column
# Hint: You'll need to use 'quadrant' and 'home_quadrant' as the merge keys
# Your code here
```

## Grouping and Aggregation

Let's analyze our data in more depth.

```python exec
id: 02-pandas-star-trek-tutorial-12
# Group ships by quadrant and calculate the average crew size and max warp
quadrant_stats = starships_df.groupby('quadrant').agg({
    'crew_size': 'mean',
    'max_warp': 'mean',
    'ship_id': 'count'
}).rename(columns={'ship_id': 'ship_count'})

print("Average statistics by quadrant:")
quadrant_stats

# Group missions by ship_id and calculate mission statistics
ship_mission_stats = missions_df.groupby('ship_id').agg({
    'mission_id': 'count',
    'duration_days': 'sum',
    'casualties': 'sum',
    'success': 'mean'
}).rename(columns={
    'mission_id': 'mission_count',
    'success': 'success_rate'
})

print("\nMission statistics by ship:")
ship_mission_stats

# Now let's merge this with the ship names for better readability
ship_performance = pd.merge(
    ship_mission_stats,
    starships_df[['ship_id', 'name']],
    on='ship_id'
)

print("\nShip performance with names:")
ship_performance
```

## Your turn 5: Grouping and Aggregation Practice

```python exec
id: 02-pandas-star-trek-tutorial-13
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# 1. Group the merged mission_details by captain and calculate:
#    - Total number of missions
#    - Average mission duration
#    - Total casualties
#    - Success rate
# Your code here

# 2. Group by ship_size (the category we created) and calculate the average
#    max_warp and average number of years in service
# Your code here
```

## Data Visualization

Let's create some visualizations to better understand our data.

```python exec
id: 02-pandas-star-trek-tutorial-14
# Set a larger figure size for better visualization
plt.figure(figsize=(12, 6))

# Bar chart of ship crew sizes
plt.subplot(1, 2, 1)
sns.barplot(x='name', y='crew_size', data=starships_df)
plt.xticks(rotation=90)
plt.title('Crew Size by Ship')
plt.xlabel('Ship Name')
plt.ylabel('Crew Size')

# Scatter plot of max warp vs. launch year
plt.subplot(1, 2, 2)
sns.scatterplot(x='launch_year', y='max_warp', size='crew_size',
                hue='quadrant', data=starships_df)
plt.title('Max Warp Capability vs. Launch Year')
plt.xlabel('Launch Year')
plt.ylabel('Max Warp')

plt.tight_layout()
plt.show()
```

```python exec
id: 02-pandas-star-trek-tutorial-15
# Plot mission statistics
plt.figure(figsize=(12, 6))

# Mission duration by ship
plt.subplot(1, 2, 1)
mission_by_ship = missions_df.merge(starships_df[['ship_id', 'name']], on='ship_id')
sns.barplot(x='name', y='duration_days', data=mission_by_ship)
plt.xticks(rotation=90)
plt.title('Mission Duration by Ship')
plt.xlabel('Ship Name')
plt.ylabel('Duration (Days)')

# Success rate by quadrant
plt.subplot(1, 2, 2)
quadrant_success = mission_details.groupby('quadrant')['success'].mean().reset_index()
sns.barplot(x='quadrant', y='success', data=quadrant_success)
plt.title('Mission Success Rate by Quadrant')
plt.xlabel('Quadrant')
plt.ylabel('Success Rate')

plt.tight_layout()
plt.show()
```

## Your turn 6: Create Your Own Visualizations

```python exec
id: 02-pandas-star-trek-tutorial-16
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# 1. Create a pie chart showing the distribution of ships by quadrant
# Your code here

# 2. Create a scatter plot comparing mission duration vs. casualties,
#    with points colored by success and sized by the ship's crew size
# Your code here
```

## Creating a Mission Report

```python exec
id: 02-pandas-star-trek-tutorial-17
def generate_mission_report(mission_id):
    """Generate a report for a specific mission."""
    # Get mission data
    mission = mission_details[mission_details['mission_id'] == mission_id].iloc[0]

    # Create a figure for the report
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f"Mission Report: {mission['mission_name']}", fontsize=16)

    # Mission overview text
    overview = (
        f"Mission ID: {mission['mission_id']}\n"
        f"Ship: {mission['name']} ({mission['registry']})\n"
        f"Captain: {mission['captain']}\n"
        f"Stardate: {mission['stardate']}\n"
        f"Duration: {mission['duration_days']} days\n"
        f"Success: {'Yes' if mission['success'] else 'No'}\n"
        f"Casualties: {mission['casualties']}\n"
        f"First Contact: {'Yes' if mission['first_contact'] else 'No'}"
    )

    # Add text to the figure
    fig.text(0.1, 0.8, overview, fontsize=12, bbox=dict(facecolor='lightgray', alpha=0.5))

    # Plot 1: Compare this mission's duration to average mission duration
    avg_duration = missions_df['duration_days'].mean()
    durations = pd.DataFrame({
        'Mission': ['This Mission', 'Average Mission'],
        'Duration (Days)': [mission['duration_days'], avg_duration]
    })
    sns.barplot(x='Mission', y='Duration (Days)', data=durations, ax=axes[0, 0])
    axes[0, 0].set_title('Mission Duration Comparison')

    # Plot 2: Ship comparison to others of its class
    same_class = starships_df[starships_df['class'] == mission['class']]
    if len(same_class) > 1:
        sns.barplot(x='name', y='max_warp', data=same_class, ax=axes[0, 1])
        axes[0, 1].set_title(f'Max Warp of {mission["class"]} Class Ships')
        axes[0, 1].tick_params(axis='x', rotation=45)
    else:
        axes[0, 1].text(0.5, 0.5, f"No other {mission['class']} class ships for comparison",
                      horizontalalignment='center', verticalalignment='center')
        axes[0, 1].set_title(f'{mission["class"]} Class Comparison')

    # Plot 3: Ship's mission history
    ship_missions = mission_details[mission_details['ship_id'] == mission['ship_id']]
    if len(ship_missions) > 1:
        sns.lineplot(x='mission_id', y='casualties', data=ship_missions, ax=axes[1, 0], marker='o')
        axes[1, 0].set_title(f"Casualties Across {mission['name']}'s Missions")
    else:
        axes[1, 0].text(0.5, 0.5, f"No other missions for {mission['name']}",
                      horizontalalignment='center', verticalalignment='center')
        axes[1, 0].set_title(f"{mission['name']}'s Mission History")

    # Plot 4: Quadrant mission success rates
    quad_success = mission_details.groupby('quadrant')['success'].agg(['mean', 'count']).reset_index()
    quad_success.columns = ['Quadrant', 'Success Rate', 'Mission Count']

    bars = sns.barplot(x='Quadrant', y='Success Rate', data=quad_success, ax=axes[1, 1])
    axes[1, 1].set_title('Mission Success Rate by Quadrant')

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

    return fig

# Generate a report for Mission ID 101
report_fig = generate_mission_report(101)
```

## Your turn: Create Your Own Mission Report

Choose a mission and create your own mission report.

```python exec
id: 02-pandas-star-trek-tutorial-18
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Choose a different mission ID and create your own report
# Your code here
```

## Conclusion

You've completed your training on pandas with Star Trek data. You've learned how to:

1. Create and manipulate DataFrames
2. Filter and query data
3. Add and modify columns
4. Merge multiple DataFrames
5. Group and aggregate data
6. Create visualizations
7. Generate reports

May your data analyses live long and prosper! 

## Bonus: Saving and Loading Data

```python exec
id: 02-pandas-star-trek-tutorial-19
# Save DataFrames to CSV files
starships_df.to_csv('starships.csv', index=False)
missions_df.to_csv('missions.csv', index=False)

# Load DataFrames from CSV files
loaded_starships = pd.read_csv('starships.csv')
loaded_missions = pd.read_csv('missions.csv')

# Check that the loaded data matches the original
loaded_starships.head()
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
