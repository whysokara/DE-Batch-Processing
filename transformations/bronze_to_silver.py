from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("bronze-to-silver")
    .config(
        "spark.jars.packages",
        "org.apache.hadoop:hadoop-aws:3.3.1,"
        "com.amazonaws:aws-java-sdk-bundle:1.11.1026"
    )
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")




bronze_path = "s3a://s3kara-batch/bronze/behaviour_metrics.csv"
silver_path = "s3a://s3kara-batch/silver/behaviour_metrics/"

df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv(bronze_path)

df_clean = (
    df
    .dropna(how="all")
    .dropDuplicates()
)

df_clean.write \
    .mode("overwrite") \
    .parquet(silver_path)
