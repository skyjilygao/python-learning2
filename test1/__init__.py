from datetime import datetime
import os
from apscheduler.schedulers.blocking import BlockingScheduler

import traceback

tt = 0
scheduler = BlockingScheduler()
# scheduler.add_job(tick_interval,'cron', seconds=3)

@scheduler.scheduled_job('interval', seconds=3)
def tick_interval():
    global tt
    tt += 1
    print(tt,'Tick! The time is : %s' % datetime.now())

scheduler.add_job(tick_interval,'interval', seconds=3)

if __name__ == "__main__":
    print(1+3)
    print('111sd')
    print("你好")
    # scheduler = BlockingScheduler()
    # scheduler.add_job(tick_interval, 'cron', seconds=3)
    try:
        # raise Exception('hello,终于出错了')
        scheduler.start()
    except Exception as e:
        print('repr:',repr(e))
        pass
    finally:
        print('program end...')