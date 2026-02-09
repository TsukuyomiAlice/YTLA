#### Data ingestion pipelines (Batch-based ML workloads and streaming-based ML workloads)

##### Example Full Data Engineering Analytics pipeline

 ```mermaid
graph LR
    A[S3]-->B[AWS Glue Data Catalog]
    B---|Schema|C[Athena]
    A-->E["Redshift /(Redshift Spectrum)"]
    A-->D["EMR (Hadoop/Spark/Hive)"]
    E-->C
    E-->F[QuickSight]
    C-->F
```

##### AWS Data Pipeline (DP)
  * Data sources can be on-prem or AWS (Can be integrated with EMR and EMR Spark Streaming for processing and transformation of data)
  * Destinations: S3, RDS, DynamoDB, Redshift, EMR
  * Conducted with EC2 or EMR instances managed by DP
  * Manages task dependencies
  * Retries and notifies upon failure(s)
  * HA

##### AWS DP vs. Glue:
  * Glue: 
    * focused on ETL
    * resources all managed by AWS
    * Data Catalog is there to make the data available to Athena or Redshift Spectrum
    * Lambda based
  * DP:
    * Move data from one location to another
    * More control over environment, compute resources that run code and the code itself
    * EC2 or EMR instance based

##### API Gateway:
  * Essentially a front door to AWS resources (λ/EC2/Dynamodb/etc.)
  * Can cache for increased performance
  * Able to throttle
  * Low cost
  * Scales
  * Can enable/disable CORS
  * Handle security (Authentication [*Integrates with Cognito User Pools*]/Authorization[IAM-internal AWS]) 
  * Create API keys
  * Swagger/Open API import to define APIs
  * Custom Domain name HTTPS security integration with ACM
    * If Edge-Optimized=>certificate in US-East-1
    * If Regional=>certificate in API Gateway region
    * Must setup CNAME or A-Alias record in Route 53
  * Endpoints:
    * Edge-Optimized: Cloudfront Edge Locations (API GW 1 region)
    * Regional: clients/API GW in the same region
    * Private: VPC accessible via VPC endpoint with resource policy

##### λ:
  * Serverless backend capable of supporting container image (must implement λ Runtime API)
  * Free tier => 1,000,000 requests and 400,000 GBs of compute time
  * Pay .20 per 1,000,000 requests after free threshold
  * Pay per duration of memory (in increments of 1 ms) after the free threshold ($1.00 for 600,000 GBs)
  * Up to 10 GB of RAM, minimum 128 MB
  * More RAM improves CPU and network capabilities
  * Environment variables (< 4KB)
  * Does not have out-of-the box caching
  * Regionally based
  * Disk capacity in function container (/tmp) 512 MB to 10 GB
  * Can use /tmp to load other files at startup
  * Concurrency executions: 1000, but can be increased
  * Deployment size: uncompressed 250 MB, compressed 50 MB
  * Can run via CloudFront as CloudFront functions and λ@edge
  * Can create λ layers (up to 5) to reuse code, making deployment smaller
  * Timeout is the maximum amount of time in seconds a λ can run (default 3). This can be adjusted from 1 to 900 seconds (15 minutes).  A low timeout value has increased risk of unexpected timeout due to external service lag, downloads or long(er) computational executions.  




##### Amazon Kinesis Video Streams 
  * Producers
    * used to capture, process and store video streams in real-time such as smartphone/security/body camera(s), AWS DeepLens, audio feeds, images, RADAR data; RTSP camera.
    * One producer per video streams
    * Video playback capability
    * RTSP-proxy based cameras will work for a small load (~100), but if scaling is necessary utilize AWS DeepLens cameras 
  * Consumers
    * custom build server (MXNet, Tensorflow, etc.)
      * This may pass on the data to db (checkpoint stream per processing status), decode the input frames and pass onto SageMaker, or even inference results to Kinesis Streams=>λ for downstream notifications
    * EC2 instances
    * AWS SageMaker
    * Amazon Rekognition Video
  * retention between 1 hr to 10 years

##### MQTT
  * An IoT Standard messaging protocol
  * Sensor data transferred to your model
  * The AWS loT Device SDK can connect via MQTT

##### AWS IoT
  * AWS IoT Rules listen for MQTT messages so as to match and execute a range of actions \[eg: send SNS notification(s)]
  * IoT Core utilized to conduct sensor data
  * IoT Analytics is built for analyzing highly unstructured IoT data
  * IoT Greengrass is built for local inference on deployed devices