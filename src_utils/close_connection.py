import sys


# close database connection
def close_connection(self):
    self.curs.close()
    del self.curs
    self.conn.close()
    sys.exit()
