import findspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, avg
from awesome_spotify_packages.aws import SecretManager as secret_manager

bucket_secret = secret_manager('dev/awesome_api_spotify/bucket_name')
bucket_name = bucket_secret.get_secret()

conf = SparkConf()
conf.setAll([
    ("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262"),
    ("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem"),
    ("fs.s3a.aws.credentials.provider","com.amazonaws.auth.DefaultAWSCredentialsProviderChain")
])

# Creating a SparkContext object  
findspark.init()
sc = SparkContext.getOrCreate()
# Creating a SparkSession  
spark = SparkSession.builder \
    .config(conf = conf) \
    .appName("awesome-api-potify") \
    .getOrCreate()

# Tracks Processing
wildcard_path = 'User/top/tracks/*.json'
s3_path_with_wildcard = f"s3a://{bucket_name}/{wildcard_path}"

tracks = spark.read.option("multiline","true").json(s3_path_with_wildcard)
# For use later

tracks_artist = tracks.select('id', explode("artists").alias("artists"))
tracks_artist = tracks_artist.withColumn('track_id', col('id')).drop('id')
tracks_artist = tracks_artist.select('track_id', 'artists.*')
tracks_artist = tracks_artist.withColumn('artist_id', col('id')).drop('id')
tracks_artist = tracks_artist.select('track_id', 'artist_id', 'name')

duration = tracks.agg(avg('duration_ms').alias('avg_duration')).withColumn('avg_duration_min', round((col('avg_duration')/60000), 2)).drop('avg_duration').head()[0]

print(tracks_artist.show())


# Artist Processing
# wildcard_path = 'User/top/artists/*.json'
# s3_path_with_wildcard = f"s3a://{bucket_name}/{wildcard_path}"

# artist = spark.read.option("multiline","true").json(s3_path_with_wildcard)
# artist = artist.select('id', 'name', 'genres')


