from pyspark.sql import DataFrame
import pyspark.sql.functions as F
from pyspark.sql.window import Window
from pyspark.sql import SparkSession 


def get_nth_highest_salary(employee_df: DataFrame, n: int):
    """
    Finds the nth highest distinct salary.
    Returns the value or None if not found.
    """
    # Step 1: Filter for distinct salaries only
    df = employee_df.select("salary").distinct()
    
    # Step 2: Use a Window function to rank them in descending order
    # Hint: Use Window.orderBy(F.desc("salary"))
    window = Window.orderBy(F.col("salary").desc())
    # Step 3: Apply a ranking function (row_number or dense_rank)
    df =df.withColumn("rank",F.dense_rank().over(window))
    # Step 4: Filter for the row where rank == n
    result_df = df.filter(F.col("rank")==n)
    # Step 5: Extract the value or return None if the DataFrame is empty
    row = result_df.first()
    return row["salary"] if row else None 

spark = SparkSession.builder.appName("Nth Highest Salary").getOrCreate()
data = [(1, 100), (2, 200), (3, 300), (4, 300)]
columns = ["id", "salary"]
employee_df = spark.createDataFrame(data, columns)

print(f"2nd Highest: {get_nth_highest_salary(employee_df, 2)}") 
print(f"5th Highest: {get_nth_highest_salary(employee_df, 5)}") 