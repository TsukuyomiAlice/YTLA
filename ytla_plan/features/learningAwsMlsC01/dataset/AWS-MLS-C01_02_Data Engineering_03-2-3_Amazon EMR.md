#### EMR:
  * Service to create a managed Hadoop framework clusters (Big Data) to analyze/process lots of data using (many) instances
  * Supports Apache Spark, HBase, Presto, Flink, Hive, etc.
  * Takes care of provisioning and configuration
  * Autoscaling and integrated with Spot Instances for cost savings
  * Use cases: Data processing, ML, Web Indexing, BigData
  * Can have long-running cluster or transient (temporary) cluster
  * At installation of the cluster you need to select frameworks and applications to install
  * Connect to the master node through an EC2 instance and run jobs from the terminal or via ordered steps submitted via the console

##### EMR Node types
  * Master Node:
    * single EC2 instance to manage the cluster
    * coordinates distribution of data and tasks
    * manages health-long running process
  * Core Node:
    * Hosts HDFS data and runs tasks and stores data-long running process
    * can spin up/down as needed
  * Task Node (optional):
    * only to run tasks-usually Spot Instances are a best option
    * no hosted data, so no risk of data loss upon removal
    * can spin up/down as needed

##### EMR Purchasing options: 
  * On-demand: reliable, predictable, won't be terminated, good for long running cluster(s) \[though you need to manually delete]
  * Reserved: cost savings (EMR will use if available), good for long running cluster(s) \[though you need to manually delete]
  * Spot instances: 
    * cheaper, can be terminated, less reliable
    * Good choice for task nodes (temporary capacity)
    * Only use on core & master if you're testing only (not production) or very cost-sensitive; you're risking partial data loss
   
##### EMR Instance Type(s) selection
  * Master node:
    * m4.large if < 50 nodes, m4.xlarge if > 50 nodes
  * Core & task nodes:
    * m4.large is usually good
    * If cluster waits a lot on external dependencies (i.e. a web crawler), t2.medium
    * Improved performance: m4.xlarge
    * Computation-intensive applications: high CPU instances
    * Database, memory-caching applications: high memory instances
    * Network / CPU-intensive (NLP, ML) - cluster computer instances
    * Accelerated Computing / AI - GPU instances (g3, g4, p2, p3)

##### EMR promises
  * EMR charges by the hour
    * Plus EC2 charges
  * Provisions new nodes if a core node fails
  * Can add and remove tasks nodes on the fly
  * Can resize a running cluster's core nodes

##### EMR AWS Integration
  * Amazon EC2 for the instances that comprise the nodes in the cluster
  * Amazon VPC to configure the virtual network in which you launch your instances
  * Amazon S3 to store input and output data or HDFS (default)
  * Amazon CloudWatch to monitor cluster performance and configure alarms
  * AWS IAM to configure permissions
  * AWS CloudTrail to audit requests made to the service
  * AWS Data Pipeline to schedule and start your clusters

##### EMR Storage
  * HDFS (distributed scalable file system for Hadoop)
    * distributes data that it stores across every instance in a cluster, as well as multiple copies of data on different instances to ensure no data is lost if instance(s) fail
    * each file stored as blocks
    * default block size is 128 MB
    * storage is ephemeral and is lost upon termination
    * performance benefit of processing data where stored to avoid latency
    * EBS serves as a backup for HDFS
  * EMRFS: access S3 as if it were HDFS
    * EMRFS Consistent View - Optional for S3 consistency
    * Uses DynamoDB to track consistency
  * Local file system

##### EMR Notebook
  * Similar concept to Zeppelin, with more AWS integration
  * Notebooks backed up to S3 only (not in within the cluster)
  * Provision clusters from the notebook!
  * Able to use multiple Notebooks to share the multi-tenant EMR clusters
  * Hosted inside a VPC
  * Accessed only via AWS console
  * build Apache Spark Apps and run queries against the cluster (python, pyspark, spark sql, spark r, scala, and/or anaconda based open source graphical libs)

##### Deep Learning on EC2 / EMR
  * EMR supports Apache MXNet and GPU instance types
  * Appropriate instance types for deep learning:
    * P3: 8 Tesla V100 GPUs
    * P2: 16 K80 GPUs
    * G3: 4 M60 GPUs (all Nvidia chips)
    * G5g : AWS Graviton 2 processors / Nvidia T4G Tensor Core GPUs
      * Not (yet) available in EMR
      * Also used for Android game streaming
    * P4d - A100 "UltraClusters" for supercomputing
  * Deep Learning AMIs
    * Preloaded with all Deep Learning frameworks
    * Can perform Multi-GPU training
    * Three styles available: conda, base AMI and AMI with source code
  * Sagemaker can deploy a cluster using whatever architecture you want
  * Trn1 instances
    * "Powered by Trainium"
    * Optimized for training NN/LLM (50% savings)
    * 800 Gbps of Elastic Fabric Adapter (EFA) networking for fast clusters
  * Trn1n instances
    * Even more bandwidth (1600 Gbps)
  * Inf2 instances
    * "Powered by AWS Inferentia2"
    * Optimized for inference
    
##### EMR Security
  * IAM policies: can be combined with tagging to control access on a cluster-by-cluster basis 
  * Kerberos
  * SSH can use kerberos or EC2 key pairs for client authentication
  * IAM roles:
    * Every cluster in EMR must have a service role and a role for EC2 instance profile(s).  These roles, attached via policies, will provide permission(s) to interact with other AWS Services
    * If a cluster uses automatic scaling, an autoscaling role is necessary
    * Service linked roles can be used if service for EMR has lost ability to clean up EC2 resources
    * IAM roles can also be used for EMRFS requests to S3 to control user access to files with in EMR based on users, groups, or location(s) within S3
  * Security configurations may be specified for Lake Formation (JSON)
  * Native integration with Apache Ranger to provide security for Hive data metastore and Hive instance(s) on EMR
    * For data security on Hadoop/Hive

##### How to use EMR
  * Within EMR, select Create studio instance, which is your environment for running workspaces/notebooks
  * Requires:
    * VPC access
    * 1-5 subnets
    * SG(s)
    * Service role (IAM/IAM Identity Center)
    * S3 bucket
  * Within the studio instance, create workspaces.  The workspace will need to create/attach an EMR cluster
  * A notebook must select a kernel at initialization (relative to the tech stack used)
  * Good practice delete your cluster if not using so it's not billed, though good to have a safeguard of the cluster shutting down, automatically to avoid paying for it
  