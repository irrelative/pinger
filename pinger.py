import logging
import time

import icmplib
import psycopg2

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


HOSTS = ['boxily.com', '192.168.4.1']

def main():
    conn = psycopg2.connect('dbname=pi')
    cur = conn.cursor()
    while True:
        start = time.time()
        for host in HOSTS:
            try:
                resp = icmplib.ping(host, count=1, privileged=False)
            except Exception as ex:
                logger.error("Error: %s", ex)
            else:
                logger.info("%s %s %s", host, resp.is_alive, resp.max_rtt)
                cur.execute("INSERT INTO pings (host, is_alive, duration) VALUES (%s, %s, %s)", (host, resp.is_alive, resp.max_rtt))
        conn.commit()
        time.sleep(max(0, 1 - (time.time() - start)))


if __name__ == '__main__':
    main()
