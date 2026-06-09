"""
---------
BRONZE.Py
PURPOSE: To ingest data into the system using Databricks Autoloader
---------
"""


from pyspark import pipelines as dp
from pyspark.sql import functions as F

catalog = "main"
schema = dbName = db = "default"
volume_name = "dbsc"

# ----------------------------------
# Ingest raw claims data from CSV files
# Contains claim information: claim numbers, dates, driver details, incident information
# ----------------------------------
@dp.table(comment="The raw claims data loaded from csv files.")
def raw_claim():
return (
spark.readStream.format("cloudFiles")
.option("cloudFiles.format", "csv")
.option("cloudFiles.inferColumnTypes", "true")
.load(f"/Volumes/{catalog}/{db}/{volume_name}/DSBC_Claims"))

# ----------------------------------
# Ingest raw policy data from CSV files
# Contains policy information: policy numbers, dates, premiums, location details
# ----------------------------------
@dp.table(comment="The raw policy data loaded from csv files.")
def raw_policy():
return (
spark.readStream.format("cloudFiles")
.option("cloudFiles.format", "csv")
.option("cloudFiles.inferColumnTypes", "true")
.load(f"/Volumes/{catalog}/{db}/{volume_name}/DSBC_Policy.csv"))

# ----------------------------------
# Ingest raw telematics (IoT) streaming data from parquet files
# Contains vehicle telemetry: speed, GPS coordinates, chassis numbers
# ----------------------------------
@dp.table(comment="The raw telematics data loaded from csv files.")
def raw_telematics():
return (
spark.readStream.format("cloudFiles")
.option("cloudFiles.format", "csv")
.option("cloudFiles.inferColumnTypes", "true")
.load(f"/Volumes/{catalog}/{db}/{volume_name}/DSBC_Telematics.csv"))
  
