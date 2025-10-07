from matplotlib.pylab import mean
import pandas as pd

dataframe = pd.read_csv("/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP/OpenCEP/test/EventFiles/201901-citibike-tripdata-1-fabricated-original.csv")

def get_paths(filename):
    paths = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(", Path: ")
            bike_id = int(parts[0].split(": ")[1])
            path_str = parts[1].strip("[]")
            path = [int(x) for x in path_str.split(", ")]
            paths.append((bike_id, path))
    return paths

def check_max_interval(dataframe, paths):
    time_intervals = []
    for _, path in paths:
        # print(path[0], path[-1])
        start_time = dataframe.iloc[path[0]]["starttime"]
        end_time = dataframe.iloc[path[-1]]["stoptime"]
        start_time = pd.to_datetime(start_time)
        end_time = pd.to_datetime(end_time)
        interval = ((end_time - start_time).total_seconds() / 60)
        time_intervals.append(interval)
    print(time_intervals)
    print("Max interval (minutes):", max(time_intervals) if time_intervals else "No valid intervals found")
    print(mean(time_intervals) if time_intervals else "No valid intervals found")
    print(f"Median: {pd.Series(time_intervals).median() if time_intervals else 'No valid intervals found'}")

paths = get_paths("/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP/OpenCEP/test/EventFiles/scripts/fabricated_paths.txt")
print(paths)
check_max_interval(dataframe, paths)