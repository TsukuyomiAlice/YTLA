##### Amazon Data Firehose (formerly Amazon Kinesis Data Firehose):
  * Fully Managed (serverless) service, no administration, automatic scaling
  * Allows for custom code to be written for producer/consumer
  * Can use λ to filter/transform data prior to output (Better to use if filter/tranform with a λ to S3 over Kinesis Data Streams)
  * Near real time: 60 seconds latency minimum for non-full batches
  * Minimum 1 MB of data at a time
  * Pay only for the data going through
  * Can subscribe to SNS
  * No data persistence and must be immediately consumed/processed
  * Sent to (S3 as a backup \[of source records] or failed \[transformations or delivery] case[s]):
    * S3
    * Amazon Redshift (copy through S3)
    * Amazon Elasticsearch
    * 3rd party partners (datadog/splunk/etc.)
    * Custom destination (http[s] endpoint)
  * S3 Destination(s) (Error and/or output) allow for bucket prefixes:
    * output/year=!{timestamp:yyyy}/month=!{timestamp:MM}/
    * error/!{firehose:random-string}/!{firehose:error-output-type}/!{timestamp:yyyy/MM/dd}/
  * Data Conversion from csv/json to Parquet/ORC using AWS Glue (only for S3)
  * Data Transformation through λ (eg: csv=>json)
  * Can't write output as RecordIO-protobuf
  * Supports compression if target is S3 (GZIP/ZIP/SNAPPY)