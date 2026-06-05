"""
-------------------
SAMPLE EXPLORATION

PURPOSE: Each function loads and displays a .CSV file containing data on Insurance Claims, Policies and Telematic Data respectively.
-------------------
"""

def Load_Claims():
    path_to_load = f"/Volumes/main/default/dbsc/DBSC_Claims.csv"

    # Load the data using the CSV format options
    sdf = spark.read.format("csv") \
     .option("header", "true") \
     .option("inferSchema", "true") \
     .load(path_to_load)

    display(sdf)

def Load_Policy():
    path_to_load = f"/Volumes/main/default/dbsc/DBSC_Policy.csv"

    # Load the data using the CSV format options
    sdf = spark.read.format("csv") \
     .option("header", "true") \
     .option("inferSchema", "true") \
     .load(path_to_load)

    display(sdf)

def Load_Tele():
    path_to_load = f"/Volumes/main/default/dbsc/DBSC_Telematics.csv"

    # Load the data using the CSV format options
    sdf = spark.read.format("csv") \
     .option("header", "true") \
     .option("inferSchema", "true") \
     .load(path_to_load)

    display(sdf)


Load_Claims()
Load_Policy()
Load_Tele()
