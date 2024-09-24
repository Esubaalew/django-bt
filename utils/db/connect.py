#connect.py

"""Yess database connection code"""

import sqlite3
from sqlite3 import Connection


def connect() -> Connection:
    """Connect to the database"""
    conn = sqlite3.connect(r'utils/db/yess.sqlite')
    return conn
