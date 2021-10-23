"""Wait for the databasae to come online."""
import random
import time

import psycopg2 as pg  # type: ignore

from app.core.config import settings


def wait_for_db(tries: int):
    """Try and connect to the database `tries` times."""
    print("Trying to connect to database...")
    for _ in range(tries):
        try:
            pg.connect(settings.SQLALCHEMY_DATABASE_URI)
            print("Connected to database.")
            return
        except Exception as e:
            # Wait ~5 seconds, with added jitter to avoid spamming port
            print(e)
            time.sleep(3 + random.random())

    print("Could not connect to database, giving up.")
    exit(1)


if __name__ == "__main__":
    wait_for_db(100)
