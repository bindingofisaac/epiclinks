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
    status = api.put_wall_post(msg, attr)

if __name__ == "__main__":
    main()
