import os,sys
import logging
import linkminers

from fbapi import get_api
from multiprocessing import Pool
from apscheduler.schedulers.background import BlockingScheduler

from redis import Redis
from rq import Queue

import timer

def main(links):
    global page_q
    cfg = {
            "page_id" : os.environ["ELPAGE"],
            "access_token": os.environ["ELACCE"]
            }
    api = get_api(cfg)
    attr = {}
    for link in links:
        attr["link"] = link
        new_post = False

        with open("posted_links", "r") as f:
            links = f.read().splitlines()
            if attr["link"] not in links:
                page_q.enqueue(api.put_wall_post, "", attr)
                new_post = True

        if new_post:
            with open("posted_links", "a") as f: f.write(attr["link"]+"\n")
        
        timer.timer()

def f(x):
    return x()

if __name__ == "__main__":

    scheduler = BlockingScheduler()

    page_q = Queue(connection=Redis())
    pool = Pool(8)
    main(pool.map(f, linkminers.links))
    scheduler.add_job(lambda: main(pool.map(f, linkminers.links)), 'interval', minutes=60)
    logging.basicConfig() 
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
