from pyspark.sql import SparkSession
from pyspark.sql.types import * #StructField, StructType, StringType, IntegerType
from pyspark.sql.functions import *
import time

Spark =SparkSession.builder.master("local[5]").appName("Learning").getOrCreate()
            # .config("spark.hadoop.io.native.lib.available", "false") \
            # .getOrCreate()
        
myschema = StructType([StructField("DEST_COUNTRY_NAME", StringType(), True),
                       StructField("ORIGIN_COUNTRY_NAME", StringType(), True),
                       StructField("count", IntegerType(), True)])
data = Spark.read.format("csv")\
        .option("inferSchema",'false')\
        .option("header","true")\
        .schema(myschema)\
        .option("mode","FAILFAST")\
        .load("C:\\Users\\pragy\\Desktop\\spark_poc\\spark-learning\\data\\flight_data.csv")
data.show(5)
print(data.rdd.getNumPartitions())
data_repartition = data.repartition(5)
print(data_repartition.rdd.getNumPartitions())
data_repartition.withColumn("PartitionId", spark_partition_id()).groupBy("PartitionId").count().show()
# partition_on_column=data.repartition(300,"ORIGIN_COUNTRY_NAME")
# partition_on_column.withColumn("PartitionId", spark_partition_id()).groupBy("PartitionId").count().show()
data.printSchema()

data_coalesce = data_repartition.coalesce(3)
data_coalesce.withColumn("PartitionId", spark_partition_id()).groupBy("PartitionId").count().show()

data_repartition.show(5)
us_flights= data.filter(col("DEST_COUNTRY_NAME")=="United States")
us_india_flights= us_flights.filter((col("ORIGIN_COUNTRY_NAME")=="India") | (col("ORIGIN_COUNTRY_NAME")=="Singapore"))

total_flight_ind_sing = us_india_flights.groupby("DEST_COUNTRY_NAME").sum('count')
total_flight_ind_sing.show()
total_flight_ind_sing.write.mode("overwrite").option("header", "true").csv("C:\\Users\\pragy\\Desktop\\spark_poc\\spark-learning\\data\\output\\total_flight_ind_sing.csv")

time.sleep(100)

