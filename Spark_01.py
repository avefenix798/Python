# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 08:50:57 2024

@author: Usuario
"""


from pyspark.sql import SparkSession
spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()

df=spark.range(100)
df.show()


