import MySQLdb as mdb
import _mysql

class DataBaseCl(object):

    def __init__(self):
        try:
            self.con = mdb.connect('localhost', 'user', '123', 'my_db',use_unicode='True', charset='utf8')
            self.cursor = self.con.cursor()
        except _mysql.Error, e:
            print("Error %d: %s" % (e.args[0], e.args[1]))

    def db_insert(self,  table_name, params):
        with self.con:
            for value in params:
                print('Insert into %s set responce = "%s"' % (table_name, unicode(value)))
                self.cursor.execute('Insert into %s set responce = " %s "' % (table_name, unicode(value)))


