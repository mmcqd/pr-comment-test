import shelve
import shelve as pickle

from shelve import open

import flask

@app.route("/a/rout")
def insert_person():

    tainted = flask.request.get_json()
    tainted2 = flask.request.cookies("taint")
    tainted3 = flask.request.headers.get("taint")

    s = "not tainted"
    b = bytearray().extend(map(ord,string))

    # ruleid: tainted-shelve-flask 
    shelve.open(tainted)
    # ruleid: tainted-shelve-flask 
    shelve.open(tainted, protocol=pickle.DEFAULT_PROTOCOL)
    # ruleid: tainted-shelve-flask 
    shelve.open(tainted, protocol=pickle.DEFAULT_PROTOCOL, writeback=False)

    # ruleid: tainted-shelve-flask 
    dbshelf = shelve.DbfilenameShelf(tainted)
    dbshelf.open()

    # ok: tainted-shelve-flask 
    shelve.open(s)
    # ok: tainted-shelve-flask 
    shelve.open(s, protocol=pickle.DEFAULT_PROTOCOL)
    # ok: tainted-shelve-flask 
    shelve.open(s, protocol=pickle.DEFAULT_PROTOCOL, writeback=False)

    # ok: tainted-shelve-flask 
    dbshelf = shelve.DbfilenameShelf(s)
    dbshelf.open()

    # ruleid: tainted-shelve-flask 
    pickle.open(tainted)
    # ruleid: tainted-shelve-flask 
    pickle.open(tainted, protocol=pickle.DEFAULT_PROTOCOL)
    # ruleid: tainted-shelve-flask 
    pickle.open(tainted, protocol=pickle.DEFAULT_PROTOCOL, writeback=False)

    # ok: tainted-shelve-flask 
    dbshelf = pickle.DbfilenameShelf(s)
    dbshelf.open()

    # ok: tainted-shelve-flask 
    pickle.open(s)
    # ok: tainted-shelve-flask 
    pickle.open(s, protocol=pickle.DEFAULT_PROTOCOL)
    # ok: tainted-shelve-flask 
    pickle.open(s, protocol=pickle.DEFAULT_PROTOCOL, writeback=False)

    # ruleid: tainted-shelve-flask 
    dbshelf = pickle.DbfilenameShelf(tainted)
    dbshelf.open()

    # ruleid: tainted-shelve-flask 
    open(tainted)
    # ruleid: tainted-shelve-flask 
    open(tainted, protocol=pickle.DEFAULT_PROTOCOL)
    # ruleid: tainted-shelve-flask 
    open(tainted, protocol=pickle.DEFAULT_PROTOCOL, writeback=False)

    # ok: tainted-shelve-flask 
    open(s)
    # ok: tainted-shelve-flask 
    open(s, protocol=pickle.DEFAULT_PROTOCOL)
    # ok: tainted-shelve-flask 
    open(s, protocol=pickle.DEFAULT_PROTOCOL, writeback=False)

