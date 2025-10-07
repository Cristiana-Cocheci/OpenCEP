# add a match every 20 datapoints

import pandas as pd
import random

dataframe = pd.read_csv("/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP/OpenCEP/test/EventFiles/201901-citibike-tripdata-1.csv")
output_file = "/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP/OpenCEP/test/EventFiles/201901-citibike-tripdata-1-fabricated-original.csv"

def is_valid_pair(row1, row2):
    # return True when the first row's stoptime is strictly before the second row's starttime
    return row1["stoptime"] < row2["starttime"]

STOP_STATION = 111111
fabricated_start_ids = []
for i in range(0, len(dataframe)):
    if i % 50 == 0:
        row1 = dataframe.iloc[i]
        bike_id = row1["bikeid"]
        current_path = [i]

        path_len = random.randint(2, 5)
        # print(path_len)
        for j in range(1, path_len):
            found = False
            for k in range(current_path[-1] + 1, min(current_path[-1] + 100, len(dataframe))):
                next_row = dataframe.iloc[k]
                if is_valid_pair(row1, next_row):
                    dataframe.at[k, "bikeid"] = bike_id
                    dataframe.at[k, "startstationid"] = dataframe.at[current_path[-1], "endstationid"]
                    current_path.append(k)
                    # print(k)
                    row1 = next_row
                    found = True
                    break
        
        # print(current_path)
        if len(current_path) > 1:
            dataframe.at[current_path[-1], "endstationid"] = STOP_STATION
            fabricated_start_ids.append((int(bike_id), current_path))

event_ids = range(len(dataframe))
dataframe["eventid"] = event_ids
dataframe.to_csv(output_file, index=False)
with open("/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP/OpenCEP/test/EventFiles/fabricated_paths.txt", "w") as f:
    for tuple in fabricated_start_ids:
        bike_id, path = tuple
        f.write(f"Bike ID: {bike_id}, Path: {path}\n")

        