import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import hashlib


def create_database():
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()

    cursor.execute("""
       CREATE TABLE IF NOT EXISTS registrations(
           user_id INTEGER PRIMARY KEY AUTHENTICATION,
           name TEXT NOT NULL,
           email TEXT UNIQUE NOT NULL,
           phone TEXT,
           create_at TEXT
        )    
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login (
            login_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES registrationa (user_id)
         )
    """)

    conn.commit()
    conn.close(

        
    )