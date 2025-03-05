from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("TestSpark").getOrCreate()

# Print Spark version
print("Spark Version:", spark.version)

# Create a simple DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

# Stop Spark session
spark.stop()
