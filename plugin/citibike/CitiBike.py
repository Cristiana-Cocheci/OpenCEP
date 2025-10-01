from datetime import datetime

from base.DataFormatter import DataFormatter, EventTypeClassifier

# CitiBike CSV column keys (based on typical CitiBike data format)
CITIBIKE_TRIP_DURATION_KEY = "tripduration"
CITIBIKE_START_TIME_KEY = "starttime"
CITIBIKE_END_TIME_KEY = "stoptime"
CITIBIKE_START_STATION_ID_KEY = "startstationid"
CITIBIKE_START_STATION_NAME_KEY = "startstationname"
CITIBIKE_END_STATION_ID_KEY = "endstationid"
CITIBIKE_END_STATION_NAME_KEY = "endstationname"
CITIBIKE_BIKE_ID_KEY = "bike_id"



# Standard CitiBike CSV column order
CITIBIKE_COLUMN_KEYS = [
    CITIBIKE_TRIP_DURATION_KEY,
    CITIBIKE_START_TIME_KEY,
    CITIBIKE_END_TIME_KEY,
    CITIBIKE_START_STATION_ID_KEY,
    CITIBIKE_START_STATION_NAME_KEY,
    CITIBIKE_END_STATION_ID_KEY,
    CITIBIKE_END_STATION_NAME_KEY,
    CITIBIKE_BIKE_ID_KEY,
    ]


class CitiBikeStartStationEventTypeClassifier(EventTypeClassifier):
    """
    This type classifier assigns event types based on start station ID.
    Each station becomes a different event type for pattern matching.
    """
    def get_event_type(self, event_payload: dict):
        """
        The type of a CitiBike event is the start station ID.
        """
        return f"START_Station_{event_payload[CITIBIKE_START_STATION_ID_KEY]}"
    
class CitiBikeEndStationEventTypeClassifier(EventTypeClassifier):
    """
    This type classifier assigns event types based on end station ID.
    Each station becomes a different event type for pattern matching.
    """
    def get_event_type(self, event_payload: dict):
        """
        The type of a CitiBike event is the end station ID.
        """
        return f"END_Station_{event_payload[CITIBIKE_END_STATION_ID_KEY]}"



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

    def parse_event(self, raw_data: str):
        """
        Expected format: tripduration,starttime,stoptime,startstationid,startstationname,endstationid,endstationname,bikeid


        Example: 320,2019-01-01 00:01:47.4010,2019-01-01 00:07:07.5810,3160.0,Central Park West & W 76 St,3283.0,W 89 St & Columbus Ave,15839
        """
        print(f"Parsing raw data: {raw_data}")
        event_attributes = raw_data.replace("\n", "").replace("\r", "").split(",")
        if len(event_attributes) != len(CITIBIKE_COLUMN_KEYS):
            raise ValueError(f"Malformed event: {raw_data} (expected {len(CITIBIKE_COLUMN_KEYS)} fields, got {len(event_attributes)})")

        timestamp_format = "%Y-%m-%d %H:%M:%S.%f" 
        event_payload=dict(zip(CITIBIKE_COLUMN_KEYS, event_attributes))
        
        try:
            event_payload[CITIBIKE_START_TIME_KEY]=datetime.strptime(event_payload[CITIBIKE_START_TIME_KEY], timestamp_format)
            event_payload[CITIBIKE_END_TIME_KEY]=datetime.strptime(event_payload[CITIBIKE_END_TIME_KEY], timestamp_format)
            return event_payload
        except ValueError:
            raise ValueError(f"Unable to parse timestamp in event: {raw_data}")

    def get_event_timestamp(self, event_payload: dict):
        """
        The event timestamp uses the start time of the trip. it sets min and max_time in event.py consequently in the rets of teh file
        """
        return event_payload[CITIBIKE_START_TIME_KEY]
