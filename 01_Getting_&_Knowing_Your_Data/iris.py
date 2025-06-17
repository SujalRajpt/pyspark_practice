from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, DoubleType, StringType


def main():
    spark = (
        SparkSession.builder.appName("IrisSchema")
        .master(
            "local[*]"
        )  # use local mode instead of connecting to spark://localhost:7077
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("ERROR")  # or "WARN"

    df = spark.read.csv("/workspace/data/iris.data", inferSchema=True, header=False)

    # Show schema
    df.printSchema()

    # Optional: show first few rows
    df.show(5)

    spark.stop()


if __name__ == "__main__":
    main()
