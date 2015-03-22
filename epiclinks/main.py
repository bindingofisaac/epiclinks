import os

from fbapi import get_api
from ninegag import get_link


def main():
    cfg = {
        "page_id" : os.environ["ELPAGE"],
        "access_token": os.environ["ELACCE"]
    }
    api = get_api(cfg)
    msg = ""
    attr = {}
    attr["link"] = get_link() 
    
    new_post = False

    with open("posted_links", "r") as f:
        links = f.read().splitlines()
        if attr["link"] not in links:
            status = api.put_wall_post(msg, attr)
            new_post = True

    if new_post:
        with open("posted_links", "a") as f: f.write(attr["link"]+"\n")

if __name__ == "__main__":
    main()
