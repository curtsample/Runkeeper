import pandas as pd
import time

def get_friendly_time(time_struct):
    if not(isinstance(time_struct, time.struct_time)):
        time_struct = time.strptime(time_struct, "%M:%S")

    secs = time_struct.tm_sec if time_struct.tm_sec >= 10 else "0{0}".format(time_struct.tm_sec)
    return "{0}:{1}".format(time_struct.tm_min, secs)


def print_quick_runs(data_frame, use_friendly_time=True):
    data_frame = data_frame.sort('Average Pace', ascending=True).head()[['Average Pace', 'Notes']]

    if (use_friendly_time):
        for index, row in data_frame.iterrows():
            row['Average Pace'] = get_friendly_time(row['Average Pace'])

    print(data_frame)


parser = lambda x: time.strptime(x, "%M:%S")
df = pd.read_csv('2015.csv', header=0, parse_dates=['Average Pace'], date_parser=parser)

# TOTALS
number_of_runs = len(df)
total_miles = df['Distance'].sum()
total_calories = int(df['Calories Burned'].sum())

print("I have been on {0} runs totalling {1} miles which burnt {2:,} calories".format(number_of_runs, total_miles, total_calories))

# AVERAGES
avg_miles = df['Distance'].mean()
avg_calories = df['Calories Burned'].mean()

print("The average distance is {0:.2f} miles which burns {1:.1f} calories".format(avg_miles, avg_calories))

print("\nFURTHEST RUNS")
print(df.sort('Distance', ascending=False).head()[['Distance', 'Notes']])

print("\nQUICKEST RUNS")
print_quick_runs(df)

print("\nQUICKEST SHORT RUNS")
print_quick_runs(df[(df['Distance'] > 3) & (df['Distance'] < 5)])

print("\nQUICKEST LONG RUNS")
print_quick_runs(df[df['Distance'] > 5])