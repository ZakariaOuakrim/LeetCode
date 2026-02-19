from pyspark.sql import SparkSession 
from pyspark.sql import functions as sf 
from pyspark.sql import Window 

spark = SparkSession.builder.appName("Rank Scores").getOrCreate()
data = [(1, 3.50), (2, 3.65), (3, 4.00), (4, 3.85), (5, 4.00), (6, 3.65)]
df_scores = spark.createDataFrame(data, ["id", "score"])

df_scores.show()

window = Window.orderBy(sf.col("score").desc())

dfResult= df_scores.withColumn("rank",sf.dense_rank().over(window))
print("-----------result--------------")
dfResult.select("score","rank").show()

