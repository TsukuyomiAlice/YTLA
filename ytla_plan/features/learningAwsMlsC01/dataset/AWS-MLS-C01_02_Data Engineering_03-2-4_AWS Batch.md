#### AWS Batch:
  * Fully managed (serverless) batch processing at any scale using dynamically launched *EC2 instances (spot or on-demand)* managed by AWS for which you pay
  * Job with a start and an end (not continuous)
  * Can run 100,000s of computing batch jobs
  * You submit/schedule batch jobs and AWS Batch handles it
    * Can be scheduled using CloudWatch Events 
    * Can also be orchestrated using step functions 
  * Provisions optimal amount/type of compute/memory based on volume and requirements
  * Batch jobs are defined as *docker images and run on ECS*
  * Helpful for cost optimization and focusing less on infrastructure
  * No time limit
  * Any run time packaged in docker image
  * Rely on EBS/instance store for disk space
  * Advantage over λ=>time limit, limited runtimes, limited disk space
  * Good for any compute based job (must harness docker) and for any non-ETL based work, batch is likely best (eg: periodically cleaning up s3 buckets)
  * Using spot instances to train deep learning models