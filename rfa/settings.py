
BOT_NAME = 'rfa'

SPIDER_MODULES = ['rfa.spiders']
NEWSPIDER_MODULE = 'rfa.spiders'

ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'

ITEM_PIPELINES = {
    'rfa.pipelines.MySQLPipeline': 2
}

DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWD = 'helloworld'
DB_DB = 'khmergoo_sequelize'
