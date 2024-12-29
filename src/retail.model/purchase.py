from pyspark.sql.types import *


class Purchase:
    schema: StructType = StructType([
        StructField("purchaseId", StringType(), nullable=False),
        StructField("customerId", StringType(), nullable=False),
        StructField("productId", StringType(), nullable=False),
        StructField("quantity", IntegerType(), nullable=False),
        StructField("pricePerUnit", DoubleType(), nullable=False),
        StructField("purchaseTimestamp", TimestampType(), nullable=False),
    ])
