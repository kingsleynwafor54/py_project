# import the neccessary modules
from pyspark.sql import SparkSession

# create a SparkSession
spark=SparkSession.builder\
        .appName('Write to Hdfs')\
        .getOrCreate()
# create dataframe or rdd with the data you want to store

data=[('Alice',20),('Bob',30),('charlie',35)]
df=spark.createDataFrame(data,['Name','Age'])
df.show()
# df=spark.read.csv('hdfs://localhost:9000/path/to/output.csv',header=True, inferSchema=True)
# df.write\
# .format('csv')\
# .mode('overwrite')\
# .save('hdfs://localhost:9000/path/to/output')
# df.show()
# import pyarrow.hdfs as hdfs

# #Connect to HDFS
# fs=hdfs.connect()

# #Get the NameNode hostname
# namenode=fs.infor('/')
# print(namenode['name'])

# spark.stop()

