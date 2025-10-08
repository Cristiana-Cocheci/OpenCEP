# replace dataset with half

import pandas as pd
dataframe = pd.read_csv("/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP/OpenCEP/test/EventFiles/201901-citibike-tripdata-1-fabricated-original.csv")
new_dataframe = dataframe[dataframe['eventid'] < 500000]
new_dataframe.to_csv("/Users/cricoche/Desktop/aalto_master/SSDM/OpenCEP/OpenCEP/test/EventFiles/201901-citibike-tripdata-1-fabricated-original-half.csv", index=False)