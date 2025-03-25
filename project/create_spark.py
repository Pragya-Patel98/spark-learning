from pyspark.sql import SparkSession
import logging.config
logging.config.fileConfig('properties/configuration/logging.config')

loggers =logging.getLogger("Create_spark")

def get_spark_object(envn, appName):
    try:
        if envn == 'DEV':
            master = 'local'
        else:
            master = "Yarn"
            
        spark = SparkSession.builder.master(master).appName(appName) \
                    .config("spark.ui.enabled", "true") \
                    .config("spark.ui.port", "4040") \
                    .config("spark.driver.memory", "4g") \
                    .config("spark.executor.memory", "2g") \
                    .config("spark.sql.shuffle.partitions", "200")\
                    .config("spark.driver.maxResultSize", "1g") \
                    .config("spark.sql.execution.arrow.enabled", "true")\
                    .config("spark.default.parallelism", "100") \
                    .config("spark.sql.autoBroadcastJoinThreshold", "-1").getOrCreate()
        
        return spark

    except Exception as e:
        loggers.errorstr("Exception- {}", e)
