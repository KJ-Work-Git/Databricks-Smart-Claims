
from pyspark import pipelines as dp
from pyspark.sql import functions as F

catalog = "main__build"
schema = dbName = db = "dbdemos_fsi_smart_claims"
volume_name = "volume_claims"

# ----------------------------------
# Ingest raw claims data from CSV files
# Contains claim information: claim numbers, dates, driver details, incident information
# ----------------------------------
@dp.table(comment="The raw claims data loaded from json files.")
def Load_Raw_Claims():
    path_to_load = f"/Volumes/main/default/dbsc/DBSC_Claims.csv"

    # Load the data using the CSV format options
    sdf = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(path_to_load)
        
    return sdf

# ----------------------------------
# Ingest raw policy data from CSV files
# Contains policy information: policy numbers, dates, premiums, location details
# ----------------------------------
@dp.table(comment="Policy data loaded from csv files.")
def Load_Raw_Policy():
    path_to_load = f"/Volumes/main/default/dbsc/DBSC_Policy.csv"

    # Load the data using the CSV format options
    sdf = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(path_to_load)
        
    return sdf

# ----------------------------------
# Ingest raw telematics (IoT) streaming data from parquet files
# Contains vehicle telemetry: speed, GPS coordinates, chassis numbers
# ----------------------------------
@dp.table(comment="Load Telematics (IoT) streaming data")
def Load_Raw_Tele():
    path_to_load = f"/Volumes/main/default/dbsc/DBSC_Telematics.csv"

    # Load the data using the CSV format options
    sdf = spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load(path_to_load)
        
    return sdf
  


