from datetime import datetime
import numpy as np
from threading import Lock
import psutil
from collections import deque
import time

from misc import DefaultConfig

class PerformanceMetrics:
    def __init__(self,recent_latencies_interval=DefaultConfig.RECENT_LATENCIES_INTERVAL):
        self.lock = Lock()
        self.latencies = []
        self.recent_latencies=deque(maxlen=recent_latencies_interval)
        self.starttime= None
        self.endtime= None
        self.event_count=0
        self.units=0

    def add_unit(self):
        with self.lock:
            # print("zad unit")
            self.units+=1
            if self.starttime== None:
                self.starttime=time.perf_counter()
                # print("starttime",self.starttime)
    def remove_unit(self):
        # print("remove unit")
        with self.lock:
            self.units-=1
            return self.units ==0

    def update_latency(self,latency):
        with self.lock:
            self.latencies.append(latency)
            self.recent_latencies.append(latency)

    def update_matches(self):
        with self.lock:
            if self.event_count % 1000 ==0:
                print("we are updating event count",self.event_count)
            self.event_count+=1
    
    def current_latency(self):
        with self.lock:
            # print("current latency")
            if self.recent_latencies:
                return float(max(self.recent_latencies))
                # return float(np.percentile(self.recent_latencies, 95))
            return None
        
    def baseline_latency(self):
            with self.lock:
                # print("baseline latency")

                if self.latencies:
                    return float(np.percentile(self.latencies, 95))
                return None
    
    def baseline_throughput(self):
        with self.lock:
                # print("baseline throughput")
                if self.starttime:
                    print("event count",self.event_count,time.perf_counter())
                    return self.event_count / max(time.perf_counter() - self.starttime, 1e-9)
                return None