from datetime import datetime

from base.DataFormatter import DataFormatter, EventTypeClassifier

# CitiBike CSV column keys (based on typical CitiBike data format)
CITIBIKE_RIDE_ID_KEY = "ride_id"
CITIBIKE_RIDEABLE_KEY = "rideable_type"
CITIBIKE_START_TIME_KEY = "started_at"
CITIBIKE_END_TIME_KEY = "ended_at"
CITIBIKE_START_STATION_NAME_KEY = "start_station_name"
CITIBIKE_START_STATION_ID_KEY = "start_station_id"
CITIBIKE_END_STATION_NAME_KEY = "end_station_name"
CITIBIKE_END_STATION_ID_KEY = "end_station_id"

# Standard CitiBike CSV column order
CITIBIKE_COLUMN_KEYS = [
    CITIBIKE_RIDE_ID_KEY,
    CITIBIKE_RIDEABLE_KEY,
    CITIBIKE_START_TIME_KEY,
    CITIBIKE_END_TIME_KEY,
    CITIBIKE_START_STATION_ID_KEY,
    CITIBIKE_START_STATION_NAME_KEY,
    CITIBIKE_END_STATION_ID_KEY,
    CITIBIKE_END_STATION_NAME_KEY,
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
        Expected format: ride_id,rideable_type,started_at,ended_at,start_station_name,start_station_id,end_station_name,end_station_id
        Example: AABD1C039D2D622D,electric_bike,2025-08-18 09:02:16.100,2025-08-18 09:07:45.510,City Hall - Washington St & 1 St,HB105,14 St Ferry - 14 St & Shipyard Ln,HB202
        """
        event_attributes = raw_data.replace("\n", "").replace("\r", "").split(",")
        return dict(zip(CITIBIKE_COLUMN_KEYS, event_attributes))

    def get_event_timestamp(self, event_payload: dict):
        """
        The event timestamp uses the start time of the trip.
        """
        timestamp_str = str(event_payload[CITIBIKE_START_TIME_KEY])
        timestamp_format = "%Y-%m-%d %H:%M:%S.%f" 

        try:
            return datetime.strptime(timestamp_str, timestamp_format)
        except ValueError:
            raise ValueError(f"Unable to parse timestamp: {timestamp_str}")

