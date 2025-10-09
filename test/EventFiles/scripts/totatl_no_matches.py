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

def max_no_paths(dataframe, paths):
    max_no_paths = 0
    for _, path in paths:
        max_no_paths+= (len(path) - 1)
    return max_no_paths

print("Max no paths:",max_no_paths(dataframe, get_paths("/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP/OpenCEP/test/EventFiles/scripts/fabricated_paths.txt")))