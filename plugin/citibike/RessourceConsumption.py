import psutil
import time

class RessourceConsumption:
    def __init__(self):
        self.proc = psutil.Process()
        self.proc.cpu_percent(None)

    def run(self, fn, *args, **kwargs):
        #INITIAL SNAPSHOT
        elapsedt_time_init = time.perf_counter()
        cpu_time_init = self.proc.cpu_times()

        result = fn(*args, **kwargs)

        #FINAL SNAPSHOT
        elapsedt_time_final = time.perf_counter()
        cpu_time_final = self.proc.cpu_times()

        elapsedt = elapsedt_time_final - elapsedt_time_init
        cpu_user = cpu_time_final.user - cpu_time_init.user
        cpu_kernel = cpu_time_final.system - cpu_time_init.system

        cpu_pct_avg = 100.0 * (cpu_user + cpu_kernel) / elapsedt

        print(f"CPU %: {cpu_pct_avg:.2f}%")

        return result
