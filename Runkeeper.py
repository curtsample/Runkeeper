import csv
import datetime
import time

class Run:
    def __init__(self, date, distance, duration, avg_pace, avg_speed, calories_burned, notes):
        self.date = date
        self.distance = float(distance)
        self.duration = duration
        self.avg_pace = avg_pace
        self.avg_speed = avg_speed
        self.calories_burned = int(float(calories_burned))
        self.notes = notes

    def format_date(self, date_format="%d %B %Y"):
        return datetime.datetime.strptime(self.date, "%Y-%m-%d %H:%M:%S").strftime(date_format)

    def __str__(self):
        return "Ran {0:.2f} miles on {1} at a pace of {2} burning {3:,} calories".format(self.distance, self.format_date(), str(self.avg_pace), self.calories_burned)


def get_furthest_runs(runs, limit=None):
    longest_runs = sorted(runs, key=lambda x: x.distance, reverse=True)
    return longest_runs[:limit] if limit else longest_runs


def get_runs_by_time(runs, longest=False, limit=None):
    time_format = "%M:%S"
    quickest_runs = sorted(runs, key=lambda x: time.strptime(x.avg_pace, time_format), reverse=longest)
    
    return quickest_runs[:limit] if limit else quickest_runs    


def print_runs(runs):
    print("\n".join(str(r) for r in runs))


with open("2015.csv", "rt") as csvfile:
    csvreader = csv.DictReader(csvfile)
    runs = []
    for line in csvreader:
        runs.append(Run(line['Date'], line['Distance'], line['Duration'], line['Average Pace'], line['Average Speed'], line['Calories Burned'], line['Notes']))

parse_file()

number_of_runs = len(runs)
miles = map(lambda x: x.distance, runs)
calories = map(lambda x: x.calories_burned, runs)
    
total_miles = sum(miles)
total_calories = sum(calories)
print("I have been on {0} runs totalling {1} miles which burnt {2:,} calories".format(number_of_runs, total_miles, total_calories))

avg_miles = float(total_miles) / number_of_runs
avg_calories = float(total_calories) / number_of_runs
print("The average distance is {0:.2f} miles which burns {1:.1f} calories".format(avg_miles, avg_calories))
    
print("\nFURTHEST RUNS")
print_runs(get_furthest_runs(runs, limit=5))
    
print("\nQUICKEST RUNS")
print_runs(get_runs_by_time(runs, limit=5))
    
print("\nQUICKEST SHORT RUNS")
shorter_runs = [r for r in runs if 3 < r.distance < 5]
print_runs(get_runs_by_time(shorter_runs, limit=5))

print("\nQUICKEST LONG RUNS")
longer_runs = [r for r in runs if r.distance > 5]
print_runs(get_runs_by_time(longer_runs, limit=5))