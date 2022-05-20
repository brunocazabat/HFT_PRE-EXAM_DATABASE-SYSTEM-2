# close database connection
def close_connection(self, window):
    self.curs.close()
    del self.curs
    self.conn.close()
    window.destroy()
