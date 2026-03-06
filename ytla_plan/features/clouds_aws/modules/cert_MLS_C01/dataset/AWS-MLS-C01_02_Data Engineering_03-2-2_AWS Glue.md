#### AWS Glue:
  * Managed ETL service (fully serverless) used to prepare/transform data for analysis
    * Job timeout between 1 to 10080 minutes (< 7 days)
    * Utilizes Python (PySpark) or Scala (Spark) scripts, but runs on serverless Spark platform
    * Targets: S3, JDBC (RDS, Redshift), or Glue Data Catalog
    * Jobs scheduled via Glue Scheduler
    * Jobs triggered by events=>Glue Triggers
    * Transformations:
      * Glue can't output RecordIO-protobuf format
      * Bundled Transformations
        * DropFields/DropNullFields
        * Filter records
        * Join data to make more interesting data
        * Map/Reduce
      * ML Transformations
        * FindMatches ML: identify duplicate or matching data, even when the records lack a common unique identifier, and no fields exactly match
        * K-Means
      * Format conversions: CSV, JSON, Avro, Parquet, ORC, XML
      * Need an IAM role / credentials to access the TO/FROM data stores
  * Can be event driven (eg: λ triggered by S3 put object) to call Glue ETL
  * Glue Data Catalog:
    * Uses an AWS Glue Data Crawler scanning DBs/S3/data to write associated metadata utilized by Glue ETL, or data discovery on Athena, Redshift Spectrum or EMR
    * Can issue crawlers throughout a DP to be able to know what data is where in the flow
    * Metadata repo for all tables with versioned schemas and automated schema inference
  * Glue Crawlers go through your data to infer schemas and partitions (s3 based on organization \[see S3 Data Partitioning])
    * formats supported: JSON, Parquet, CSV, relational store
    * Crawlers work for: S3, Amazon Redshift, Amazon RDS
    * Can be schedule or On-Demand
    * Need an IAM role / credentials to access the data store(s)
  * Glue Job bookmarks prevent reprocessing old data
  * Glue Studio-new GUI to create, run, and monitor ETL jobs in Glue
  * Glue Streaming ETL (built on Apache Spark Structured Streaming)-compatible with Kinesis Data Streaming, Kafka, MSK
  * Glue Elastic Views:
    * Combine and replicate data across multiple data stores using SQL (View)
    * No custom code, Glue monitors for changes in the source data, serverless
    * Leverages a "virtual table" (materialized view)

##### AWS Glue Inputs
  * Aurora
  * Postgres, Redshift, SqlServer, Oracle, MySql (JDBC datastores) (RDS based or otherwise)
  * dynamodb
  * mongodb/documentdb
  * Kinesis Data Streams
  * Kafka/Amazon Managed Streaming for Apache Kafka
  * Athena
  * Spark
  * S3
  * Files (Orc, Parquet)

##### AWS Glue Data Brew

  * Allows you to clean, normalize, and translate data without writing any code (ETL)
  * Reduces ML and analytics data preparation time by up to 80%
  * +250 ready-made transformations to automate tasks
  * Filtering anomalies, data conversion, correct invalid values...
  * Needs access to input via IAM role
  * Can conduct statistics on data for the sake of analysis
  * Can find (and remove) missing, invalid, duplicate, and outlier data
  * All conducted transformations are recorded into a recipe, from which a glue job might be created
  * Inputs:
    * File upload
    * Data lake/data store
    * Redshift
    * Aurora
    * JDBC
    * AWS Glue Data Catalog
    * Amazon Appflow
    * AWS Data Exchange
    * Snowflake