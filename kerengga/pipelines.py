# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import os

class MysqlStorePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='root', passwd='', db='kerengga', host='localhost', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()
        os.system("rm -rf items.json; touch items.json")

    def process_item(self, item, spider):
        try:
            if(spider.name is "gpa_category"):
                self.cursor.execute('INSERT INTO category (player_id, url, description) VALUES (%s, %s, %s)',
                                   (item['player_id'], item['url'].encode('utf-8'), item['description'].encode('utf-8')))
                self.conn.commit()

            elif(spider.name is "gpa_subcategory"):
                self.cursor.execute('INSERT INTO category (player_id, url, description, parent_id) VALUES (%s, %s, %s, %s)',
                                   (item['player_id'], item['url'].encode('utf-8'), item['description'].encode('utf-8'), item['parent_id']))
                self.conn.commit()
            else:
                price = item['price'].replace(".","").replace(",",".")
                self.cursor.execute('INSERT INTO product (url, ean, name, price) VALUES (%s, %s, %s, %s)',
                                   (item['url'].encode('utf-8'), item["ean"], item['name'], price))
                self.conn.commit()

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])

        return item
