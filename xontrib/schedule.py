import builtins
import threading
import sched
import time
import schedule as _schedule

__all__ = ()
__version__ = '0.0.1'


class ScheduleThread(threading.Thread):
    def __init__(self, *pargs, **kwargs):
        super().__init__(*pargs, daemon=True, name="scheduler", **kwargs)
        self.sched = sched.scheduler(time.time, time.sleep)

    def run(self):
        while True:
            _schedule.run_pending()

            nextsched = self.sched.run(False)
            if nextsched is None:
                nextsched = float('inf')

            try:
                nextschedule = _schedule.idle_seconds()
            except Exception:
                nextschedule = float('inf')

            if nextsched == nextschedule == float('inf'):
                time.sleep(1)  # Finish init
            else:
                time.sleep(max(min(nextsched, nextschedule), self.MAX_WAIT))

    def every(self):
        return _schedule.every()

    def when(self, time, callable, *pargs, **kwargs):
        self.sched.enterabs(time, 0, callable, pargs, kwargs)

    def delay(self, delay, callable, *pargs, **kwargs):
        self.sched.enter(delay, 0, callable, pargs, kwargs)


builtins.schedule = ScheduleThread()
builtins.schedule.start()
