import schedule
import time
import os, sys
from datetime import date

def job():
    if date.today().day != 1:
        return
    else:
        with open(os.path.join(sys.path[0], "main.py"), "r") as f:
            exec(f.read())

#schedule.every(5).seconds.do(job)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
schedule.every().day.at('11:02').do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)