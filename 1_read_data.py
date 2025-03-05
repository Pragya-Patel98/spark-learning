from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("TestSpark").getOrCreate()
data= spark.read.format("csv")\
        .option("inferschema","true")\
        .option("header", "true")\
        .option("mode","FAILFAST")\
        .load("C:\\Users\\pragy\\Desktop\\spark_poc\\spark-learning\\data\\flight_data.csv")
data.show(5)
print(data.printSchema())