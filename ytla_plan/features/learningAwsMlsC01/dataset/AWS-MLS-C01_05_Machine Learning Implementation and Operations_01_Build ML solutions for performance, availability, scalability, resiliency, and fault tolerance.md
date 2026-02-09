## Machine Learning Implementation and Operations

### Build ML solutions for performance, availability, scalability, resiliency, and fault tolerance. 
#### AWS environment logging and (error) monitoring

##### AWS CloudTrail:
  * Service that monitors and records account activity across AWS infrastructure (history of events/API calls)
  * Provides governance, compliance and audit for your AWS account:
    * Enabled by default
    * Trail can be applied to all regions (default) or a single region
    * Doen't monitor SM InvokeEndpoint calls

##### CloudTrail Events:
  * Able to be separated into read/write events
  * Management events (default on)
  * Data events (default off due to volume, though can be turned on to trigger/invoke)
  
##### CloudTrail Insights:
  * Used to detect unusual activity in an account (if enabled):
   * Inaccurate resource provisioning
   * Hitting service limits
   * Bursts of AWS IAM actions
   * Gaps in periodic maintenance
   * Analyzes normal management events to create a baseline to then continuosly analyze write events to detect unusual patterns (S3/CloudTrail console/EventBridge events)
   * Cloudtrail Events are stored for 90 days, though can be sent to S3 and analyzed by Athena

##### Amazon EventBridge (aka Cloudwatch Events):
  * Service to provide connectivity between certain events and resultant services such as
    * CRON job triggering (via EventBridge) a λ 
    * λ triggering (via EventBridge) SNS/SQS messages
    * S3 Event Notifications (via EventBridge) to trigger whatever service is required (eg: trigger SM Pipeline)
    * SNS topics
    * SM endpoint change in status due to drift
    * Event Pattern: rules specified in AWS JSON rule configs react (eg: filter) to certain service action(s) (eg: check for external generated certs that are n days away from expiration, metadata, object sizes, names, etc.)
    * When an EventBridge rule runs, it needs permission on the target (eg: \[λ, SNS, SQS, Cloudwatch Logs, API GW, etc.] resource based policy or \[Kinesis Streams, Sys Mgr Run Command, ECS tasks etc.] IAM Role must allow EventBridge)
    * Externally available to 3rd party SAAS partners
    * Can analyze events and infer an associated schema (capable of versioning).  This registered schema allows code generation for applications to know the structure of the data in coming into the event bus
    * EventBridge Event Buses Types:
      * Default (receive events from AWS services)
      * Partner (receive events from SAAS)
      * Custom (recieve from Custom Applications)
    * EventBridge Event Buses:
      * Are accessible to other AWS accounts/Regions via Resource based policies
      * Events can be archived/filtered sent to it (time based or forever) and even replayed
      * Multiple destinations at one time is possible

##### Cloudwatch vs Cloudtrail:
  * Cloudwatch:
    * Cloudwatch Contributor Insight=>helps analyze (VPC) logs
    * Performance monitoring and dashboards (metrics, CPU, network, etc.)
    * Events and Alerting
    * Log aggregation and analysis
    * Cloudwatch metric=>Amazon Data Firehose to S3 or 3rd parties in near real time
    * Captures SM monitoring metrics at a 1 minute frequency
  * CloudTrail: 
    * Record API calls made within Account by everyone
    * Can define trails for specific resources
    * Global service

#### Multiple regions, Multiple AZs
#### AMI/golden image
#### Docker containers
#### Auto Scaling groups
#### Rightsizing
  * Instances
  * Provisioned IOPS
  * Volumes
  * Load balancing
  * AWS best practices

