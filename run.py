#!flask/bin/python
from app import app
#from logging.config import dictConfig
import logging

#app.run(debug = True)
if __name__ == '__main__':
    app.debug = True
    #日志记录到文件
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    #logging的级别主要有NOTSET、DEBUG、INFO、WARNING、ERROR和CRITICAL
    handler.setLevel(logging.DEBUG)
    #日志格式
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run()