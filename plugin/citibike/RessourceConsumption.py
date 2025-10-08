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
        # snapshot children cpu times (pid -> cpu_times)
        try:
            children_init = {c.pid: c.cpu_times() for c in self.proc.children(recursive=True)}
        except Exception:
            children_init = {}

        result = fn(*args, **kwargs)

        #FINAL SNAPSHOT
        elapsedt_time_final = time.perf_counter()
        cpu_time_final = self.proc.cpu_times()
        try:
            children_final = {c.pid: c.cpu_times() for c in self.proc.children(recursive=True)}
        except Exception:
            children_final = {}

        elapsedt = elapsedt_time_final - elapsedt_time_init
        parent_user = cpu_time_final.user - cpu_time_init.user
        parent_system = cpu_time_final.system - cpu_time_init.system

        # helper to safely get user/system from cpu_times
        def _ts_to_us(ts):
            return (getattr(ts, 'user', 0.0), getattr(ts, 'system', 0.0))

        # sum deltas for children present in final snapshot
        child_user = 0.0
        child_system = 0.0
        # total initial and final sums (for simple delta) to tolerate pid churn
        total_children_init_user = 0.0
        total_children_init_system = 0.0
        for ts in children_init.values():
            u, s = _ts_to_us(ts)
            total_children_init_user += u
            total_children_init_system += s
        total_children_final_user = 0.0
        total_children_final_system = 0.0
        for ts in children_final.values():
            u, s = _ts_to_us(ts)
            total_children_final_user += u
            total_children_final_system += s

        # delta across all children observed between snapshots
        child_user = total_children_final_user - total_children_init_user
        child_system = total_children_final_system - total_children_init_system

        # Some children might have started and finished between snapshots; this approach can
        # slightly underestimate their contribution, but works well when children persist.

        total_cpu_user = parent_user + child_user
        total_cpu_system = parent_system + child_system

        # percent relative to a single core (matches previous behaviour)
        cpu_pct_single_core = 100.0 * (total_cpu_user + total_cpu_system) / elapsedt if elapsedt > 0 else 0.0

        # percent relative to all available logical CPUs
        cpu_count = psutil.cpu_count(logical=True) or 1
        cpu_pct_all_cores = cpu_pct_single_core / cpu_count

        # Diagnostic info
        try:
            num_children = len(children_final)
        except Exception:
            num_children = 0
        try:
            num_threads = self.proc.num_threads()
        except Exception:
            num_threads = None

        print("--- Resource consumption summary ---")
        print(f"Elapsed (s): {elapsedt:.4f}")
        print(f"Parent CPU user (s): {parent_user:.4f}, system (s): {parent_system:.4f}")
        print(f"Children CPU user (s): {child_user:.4f}, system (s): {child_system:.4f} (observed PIDs: {num_children})")
        print(f"Total CPU seconds: {(total_cpu_user + total_cpu_system):.4f}")
        print(f"CPU % (single core): {cpu_pct_single_core:.2f}%")
        print(f"CPU % (all {cpu_count} logical cores): {cpu_pct_all_cores:.2f}%")
        if num_threads is not None:
            print(f"Parent threads: {num_threads}")
        print("------------------------------------")

        return result
