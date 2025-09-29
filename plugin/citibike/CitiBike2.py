from base.DataFormatter import DataFormatter, EventTypeClassifier
import pandas as pd

# CitiBike CSV column keys (based on typical CitiBike data format)
CITIBIKE_TRIP_DURATION_KEY = "tripduration"
CITIBIKE_START_TIME_KEY = "starttime"
CITIBIKE_END_TIME_KEY = "stoptime"
CITIBIKE_START_STATION_ID_KEY = "startstationid"
CITIBIKE_END_STATION_ID_KEY = "endstationid"
CITIBIKE_BIKE_ID_KEY = "bikeid"



# Standard CitiBike CSV column order
CITIBIKE_COLUMN_KEYS = [
    CITIBIKE_TRIP_DURATION_KEY,
    CITIBIKE_START_TIME_KEY,
    CITIBIKE_END_TIME_KEY,
    CITIBIKE_START_STATION_ID_KEY,
    CITIBIKE_END_STATION_ID_KEY,
    CITIBIKE_BIKE_ID_KEY,
    ]

class CitiBikeTripEventTypeClassifier(EventTypeClassifier):
    """
    Assigns a single event type to all trip events.
    """
    TRIP_TYPE = "CitiBikeTrip"

    def get_event_type(self, event_payload: dict):
        return self.TRIP_TYPE

class CitiBikeDataFormatter(DataFormatter):
    """
    A data formatter implementation for CitiBike trip data in CSV format.
    Supports different event type classification strategies.
    """
    def __init__(self, event_type_classifier: EventTypeClassifier = CitiBikeTripEventTypeClassifier()):
        super().__init__(event_type_classifier)

    def parse_event(self, raw_data: dict) -> dict:
        """
        Expected format: tripduration,starttime,stoptime,startstationid,endstationid,bikeid
        """
        if isinstance(raw_data, dict):
            return raw_data
        else:
            raise ValueError("Unsupported raw_data type. Expected dict or pd.Series.")
        
        

    def get_event_timestamp(self, event_payload: dict):
        """
        The event timestamp uses the start time of the trip.
        """
        return event_payload[CITIBIKE_START_TIME_KEY]