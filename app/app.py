import logging

import requests
import yaml
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.netutil import bind_sockets
from tornado.process import fork_processes
from tornado.web import Application
from tornado.web import RequestHandler


class DB(object):
    def __init__(self, entries=None):
        self.entries = [] if entries is None else entries

    def add(self, entry):
        """An entry is a tuple of (id, datetime, text)."""
        self.entries.append(entry)

    def search(self, query_string):
        """
        >>> DB([(1, "", "tour city",), (2, "", "some other",)]).search("city tour")
        [(1, '', 'tour city')]
        """
        result = self.entries
        for item in set(query_string.split()):
            result = filter(lambda x: item in x[2], result)
        return list(result)


def init_db(data_source):
    raw_data = requests.get(data_source).json()['data']
    data = list(map(lambda x: (x['review_id'], x['date'], x['message']), raw_data))
    return DB(data)


class ReqHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    def get(self, query_string):
        r = self.db.search(query_string)
        self.write({'size': len(r), 'entries': r})


def make_app(db):
    return Application(
        [('/s/(.+)', ReqHandler, dict(db=db))])


def load_config(config_file="config.yml"):
    with open(config_file, 'r') as config:
        return yaml.load(config)


if __name__ == '__main__':
    cfg = load_config()
    db = init_db(cfg['database']['DATA_SOURCE'])
    app = make_app(db)
    sockets = bind_sockets(cfg['server']['PORT'])
    fork_processes(0)
    server = HTTPServer(app)
    server.add_sockets(sockets)
    logging.info("Server are listening in %d port ", cfg['server']['PORT'])
    IOLoop.current().start()
