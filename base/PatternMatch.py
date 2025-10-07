from base.Event import Event
from typing import List


class PatternMatch:
    """
    Represents a set of primitive events satisfying one or more patterns.
    An instance of this class could correspond either to a full pattern match, or to any intermediate result
    created during the evaluation process.
    """
    def __init__(self, events: List[Event], probability: float = None):
        self.events = events
        self.last_timestamp = max(events, key=lambda x: x.max_timestamp).max_timestamp
        self.first_timestamp = min(events, key=lambda x: x.min_timestamp).min_timestamp
        # this field is only used for full pattern matches
        self.pattern_ids = []
        self.probability = probability
        self.t_emit = None

    def __eq__(self, other):
        return isinstance(other, PatternMatch) and set(self.events) == set(other.events) and \
               self.pattern_ids == other.pattern_ids

    def __str__(self):
        result = ""
        match = ""
        for event in self.events:
            match += "%s\n" % event
        if len(self.pattern_ids) == 0:
            result += match
            result += "\n"
        else:
            for idx in self.pattern_ids:
                result += "%s: " % idx
                result += match
                result += "\n"
        return result
    
    def pretty_print(self):
        # Bike ID: 34051, Path: [967250, 967257]

        def _get_attr_from_event(ev, key):
            # ev may be an Event or AggregatedEvent
            try:
                if hasattr(ev, "payload") and key in ev.payload:
                    return ev.payload.get(key)
            except Exception:
                pass

            # events from a Kleene closure are aggregated events
            if hasattr(ev, "primitive_events"):
                for pe in ev.primitive_events:
                    try:
                        if hasattr(pe, "payload") and key in pe.payload:
                            return pe.payload.get(key)
                    except Exception:
                        continue
            return None

        bike_id = _get_attr_from_event(self.events[0], "bikeid")

        path = []
        for ev in self.events:
            if hasattr(ev, "primitive_events"):
                for pe in ev.primitive_events:
                    if hasattr(pe, "payload"):
                        eid = pe.payload.get("eventid")
                        if eid is None:
                            eid = pe.payload.get(Event.INDEX_ATTRIBUTE_NAME)
                        path.append(eid)
            else:
                if hasattr(ev, "payload"):
                    eid = ev.payload.get("eventid")
                    if eid is None:
                        eid = ev.payload.get(Event.INDEX_ATTRIBUTE_NAME)
                    path.append(eid)

        formatted_item = f"Bike ID: {bike_id}, Path: {str(path)}\n"
        return formatted_item

    def add_pattern_id(self, pattern_id: int):
        """
        Adds a new pattern ID corresponding to this pattern,
        """
        if pattern_id not in self.pattern_ids:
            self.pattern_ids.append(pattern_id)
