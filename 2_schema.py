from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType
from pyspark.sql.functions import col

Spark =SparkSession.builder.appName("Learning").getOrCreate()
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

data_repartition = data.repartition(3)
data.printSchema()
data_repartition.show(5)
us_flights= data.filter(col("DEST_COUNTRY_NAME")=="United States")
us_india_flights= us_flights.filter((col("ORIGIN_COUNTRY_NAME")=="India") | (col("ORIGIN_COUNTRY_NAME")=="Singapore"))

total_flight_ind_sing = us_india_flights.groupby("DEST_COUNTRY_NAME").sum('count')
total_flight_ind_sing.show()



