from flask import Flask, g
import sqlite3

from flask import Flask
app=Flask(__name__)
db_location='var/test.db'

def get_db():
		db=getattr(g,'db',None
		if db is None:
			db=sqlite3.connect(db_location)
			g.db=db
		return db)

@app.teardown_appcontext
def.close_