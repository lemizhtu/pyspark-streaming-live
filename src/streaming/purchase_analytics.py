from pyspark.sql.functions import *


class PurchaseAnalytics:

    @staticmethod
    def product_total_spend(purchase_df: DataFrame):
        return purchase_df \
            .groupBy("productId") \
            .agg(sum(col("quantity") * col("pricePerUnit")).alias("productTotalSpend"))
