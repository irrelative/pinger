import time

import icmplib
import psycopg2

HOSTS = ['boxily.com', '192.168.4.1']


def main():
    conn = psycopg2.connect('dbname=pi')
    cur = conn.cursor()
    while True:
        start = time.time()
        for host in HOSTS:
            resp = icmplib.ping(host, count=1, privileged=False)
            cur.execute("INSERT INTO pings (host, is_alive, duration) VALUES (%s, %s, %s)", (host, resp.is_alive, resp.max_rtt))
        conn.commit()
        time.sleep(max(0, 1 - (time.time() - start)))


if __name__ == '__main__':
    main()
