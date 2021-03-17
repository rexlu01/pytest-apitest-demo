"""确定当前位置"""
import os, sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pymysql
from pymysql.cursors import DictCursor
from utils.config_data import GetData

class ConnDataBase():

    def __init__(self):
        self.landir = GetData().get_config_data("micsdatabase")

    def connMysql(self):
        conn = pymysql.connect(host= self.landir.get("hostname"), port = self.landir.get("post"), user = self.landir.get("user"), passwd = self.landir.get("password"), db = self.landir.get("database"),charset="utf8")
        return conn
    
    def execSelectSQL(self,sql):
        try:
            conn = self.connMysql()
            cursor = conn.cursor(DictCursor)
            cursor.execute(sql)
            rows = cursor.fetchall()
            conn.commit()
            return rows
        except Exception as e:
            print(str(e))
        finally:
            cursor.close()

