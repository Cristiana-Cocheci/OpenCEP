from numpy import dtype, floor
import pandas as pd
from datetime import datetime
from typing import Optional, Callable
from stream.Stream import InputStream

def citibike_preprocessor(dataframe: pd.DataFrame):
    result = dataframe.copy()  
    CITIBIKE_COLUMNS = [
            'tripduration', 'starttime', 'stoptime', 'startstationid', 'endstationid', 'bikeid'
    ]
    result = result[CITIBIKE_COLUMNS]
    timestamp_format = "%Y-%m-%d %H:%M:%S.%f" 
    for col in ['starttime', 'stoptime']:
        result[col] = pd.to_datetime(result[col], format=timestamp_format)

    for col in ['startstationid', 'endstationid', 'bikeid', 'tripduration']:
        result[col] = result[col].apply(lambda x: str(int(floor(x))) if pd.notnull(x) else None)
    return result

class CitiBikeDataFrameInputStream(InputStream):
    def __init__(self, 
                 filename: str, 
                 timestamp_column: str,
                 sort_by_timestamp: bool = True,
                 preprocessor: Optional[Callable[[pd.DataFrame], pd.DataFrame]] = None):
        """
        Initialize the DataFrame input stream.
        
        Args:
            filename: The path to the CSV file containing the data
            timestamp_column: Name of the column containing timestamps
            sort_by_timestamp: Whether to sort the DataFrame by timestamp (recommended for CEP)
            preprocessor: Optional function to preprocess the DataFrame before streaming
        """
        super().__init__()

        # Load and preprocess the dataframe
        self.dataframe = pd.read_csv(filename)
        
        self.dataframe = citibike_preprocessor(self.dataframe)

        if preprocessor:
            self.dataframe = preprocessor(self.dataframe)
            
        
        if sort_by_timestamp:
            self.dataframe = self.dataframe.sort_values(by=timestamp_column)
        
        #write processed dataframe to a new csv file for verification
        self.dataframe.to_csv(filename, index=False)

        for _, row in self.dataframe.iterrows():
            self._stream.put(row.to_dict())

        self.close()
        
    @staticmethod
    def create_citibike_preprocessor(
        bike_ids_filter: Optional[set] = None
    ) -> Callable[[pd.DataFrame], pd.DataFrame]:
        """
        Create a preprocessing function for CitiBike data filtering.
        
        Args:
            bike_ids_filter: Set of allowed bike IDs
        """
        def preprocessor(df: pd.DataFrame) -> pd.DataFrame:
            result = df.copy()

            # Filter by bike IDs
            if bike_ids_filter is not None:
                result = result[result['bikeid'].isin(bike_ids_filter)]
            return result
        
        return preprocessor

