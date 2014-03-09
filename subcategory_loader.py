# -*- coding: utf-8 -*-
import MySQLdb
import os

class SubcategoryLoader():
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='', db='kerengga', host='localhost', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def load(self):
        try:
            self.cursor.execute('select * from category where parent_id is null')
            rows = self.cursor.fetchall()

            for row in rows:
                command = 'scrapy crawl gpa_subcategory -a url=' + str(row[3]) + ' -a pid=' + str(row[0])
                print command

            self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

def main():
  loader = SubcategoryLoader()
  loader.load()

if  __name__ =='__main__':
   main()
