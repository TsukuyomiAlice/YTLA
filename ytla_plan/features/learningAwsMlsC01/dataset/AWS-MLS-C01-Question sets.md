## question 1

#### A large mobile network operating company is building a machine learning model to predict customers who are likely to unsubscribe from the service. The company plans to offer an incentive for these customers as the cost of churn is far greater than the cost of the incentive.
#### The mode produces the following confusion matrix after evaluating on a test dataset of 100 customers:
| n = 100          | PREDICTED CHURN Yes | PREDICTED CHURN No |
|------------------|---------------------|--------------------|
| ACTUAL CHURN Yes | 10                  | 4                  |
| ACTUAL CHURN No  | 10                  | 76                 |
#### Based on the model evaluation results, why is this a viable model for production?

* The model is 86% accurate and the cost incurred by the company as a result of false negatives is less than the false positives

## question 2

#### A Machine Learning Specialist is designing a system for improving sales for a company. The objective is to use the large amount of information the company has on users' behavior and product preferences to predict which products users would like based on the users' similarity to other users.
#### What should the Specialist do to meet this objective?

* Build a collaborative filtering recommendation engine with Apache Spark ML on Amazon EMR.

## question 3

#### A Mobile Network Operator is building an analytics platform to analyze and optimize a company's operations using Amazon Athena and Amazon S3.
#### The source systems send data in .CSV format in real time. The Data Engineering team wants to transform the data to the Apache Parquet format before storing it on Amazon S3.
#### Which solution takes the LEAST effort to implement?

* Ingest .CSV data from Amazon Kinesis Data Streams and use Amazon Glue to convert data into Parquet.

## question 4

#### A city wants to monitor its air quality to address the consequences of air pollution. A Machine Learning Specialist needs to forecast the air quality in parts per million of contaminates for the next 2 days in the city. As this is a prototype, only daily data from the last year is available.
#### Which model is MOST likely to provide the best results in Amazon SageMaker?

* Use the Amazon SageMaker Linear Learner algorithm on the single time series consisting of the full year of data with a predictor_type of regressor.

## question 5

#### A Data Engineer needs to build a model using a dataset containing customer credit card information.
#### How can the Data Engineer ensure the data remains encrypted and the credit card information is secure?

* Use AWS KMS to encrypt the data on Amazon S3 and Amazon SageMaker, and redact the credit card numbers from the customer data with AWS Glue.

## question 6

#### A Machine Learning Specialist is using an Amazon SageMaker notebook instance in a private subnet of a corporate VPC. The ML Specialist has important data stored on the Amazon SageMaker notebook instance's Amazon EBS volume, and needs to take a snapshot of that EBS volume. However, the ML Specialist cannot nd the Amazon SageMaker notebook instance's EBS volume or Amazon EC2 instance within the VPC.
#### Why is the ML Specialist not seeing the instance visible in the VPC?

* Amazon SageMaker notebook instances are based on EC2 instances running within AWS service accounts.

## question 7

#### A Machine Learning Specialist is building a model that will perform time series forecasting using Amazon SageMaker. The Specialist has finished training the model and is now planning to perform load testing on the endpoint so they can configure Auto Scaling for the model variant.
#### Which approach will allow the Specialist to review the latency, memory utilization, and CPU utilization during the load test?

* Generate an Amazon CloudWatch dashboard to create a single view for the latency, memory utilization, and CPU utilization metrics that are outputted by Amazon SageMaker.

## question 8

#### A manufacturing company has structured and unstructured data stored in an Amazon S3 bucket. A Machine Learning Specialist wants to use SQL to run queries on this data.
#### Which solution requires the LEAST effort to be able to query this data?

* Use AWS Glue to catalogue the data and Amazon Athena to run queries.

## question 9

#### A Machine Learning Specialist is developing a custom video recommendation model for an application. The dataset used to train this model is very large with millions of data points and is hosted in an Amazon S3 bucket. The Specialist wants to avoid loading all of this data onto an Amazon SageMaker notebook instance because it would take hours to move and will exceed the attached 5 GB Amazon EBS volume on the notebook instance.
#### Which approach allows the Specialist to use all the data to train the model?

* Load a smaller subset of the data into the SageMaker notebook and train locally. Confirm that the training code is executing and the model parameters seem reasonable. Initiate a SageMaker training job using the full dataset from the S3 bucket using Pipe input mode.

## question 10

#### A Machine Learning Specialist has completed a proof of concept for a company using a small data sample, and now the Specialist is ready to implement an end- to-end solution in AWS using Amazon SageMaker. The historical training data is stored in Amazon RDS.
#### Which approach should the Specialist use for training a model using that data?

* Push the data from Microsoft SQL Server to Amazon S3 using an AWS Data Pipeline and provide the S3 location within the notebook.

## question 11

#### A Machine Learning Specialist receives customer data for an online shopping website. The data includes demographics, past visits, and locality information. The Specialist must develop a machine learning approach to identify the customer shopping patterns, preferences, and trends to enhance the website for better service and smart recommendations.
#### Which solution should the Specialist recommend?

* Collaborative filtering based on user interactions and correlations to identify patterns in the customer database.

## question 12

#### A Machine Learning Specialist is working with a large company to leverage machine learning within its products. The company wants to group its customers into categories based on which customers will and will not churn within the next 6 months. The company has labeled the data available to the Specialist.
#### Which machine learning model type should the Specialist use to accomplish this task?

* Classification

## question 13

#### The displayed graph is from a forecasting model for testing a time series.
![](/pics/q13.png)
#### Considering the graph only, which conclusion should a Machine Learning Specialist make about the behavior of the model?

*  The model predicts both the trend and the seasonality well

## question 14

#### A company wants to classify user behavior as either fraudulent or normal. Based on internal research, a Machine Learning Specialist would like to build a binary classier based on two features: age of account and transaction month. The class distribution for these features is illustrated in the figure provided.
![](/pics/q14.png)
#### Based on this information, which model would have the HIGHEST accuracy?

* Support vector machine (SVM) with non-linear kernel

#### Based on this information, which model would have the HIGHEST recall with respect to the fraudulent class?

* Naive Bayesian classier

## question 15

#### A Machine Learning Specialist at a company sensitive to security is preparing a dataset for model training. The dataset is stored in Amazon S3 and contains Personally Identifiable Information (PII).
#### The dataset:
#### ✑ Must be accessible from a VPC only.
#### ✑ Must not traverse the public internet.
#### How can these requirements be satisfied?

* Create a VPC endpoint and apply a bucket access policy that restricts access to the given VPC endpoint and the VPC.

## question 16

#### During mini-batch training of a neural network for a classification problem, a Data Scientist notices that training accuracy oscillates.
#### What is the MOST likely cause of this issue?

* The learning rate is very high.

## question 17

#### An employee found a video clip with audio on a company's social media feed. The language used in the video is Spanish. English is the employee's rst language, and they do not understand Spanish. The employee wants to do a sentiment analysis.
#### What combination of services is the MOST efficient to accomplish the task?

* Amazon Transcribe, Amazon Translate, and Amazon Comprehend

## question 18

#### A Machine Learning Specialist is packaging a custom ResNet model into a Docker container so the company can leverage Amazon SageMaker for training. 
#### The Specialist is using Amazon EC2 P3 instances to train the model and needs to properly configure the Docker container to leverage the NVIDIA GPUs.
#### What does the Specialist need to do?

* Bundle the NVIDIA drivers with the Docker image.

## question 19

#### A Machine Learning Specialist is building a logistic regression model that will predict whether or not a person will order a pizza. The Specialist is trying to build the optimal model with an ideal classification threshold.
#### What model evaluation technique should the Specialist use to understand how different classification thresholds will impact the model's performance?

* Receiver operating characteristic (ROC) curve

## question 20

#### An interactive online dictionary wants to add a widget that displays words used in similar contexts. A Machine Learning Specialist is asked to provide word features for the downstream nearest neighbor model powering the widget.
#### What should the Specialist do to meet these requirements?

* Create one-hot word encoding vectors.

## question 21

#### A Machine Learning Specialist is configuring Amazon SageMaker so multiple Data Scientists can access notebooks, train models, and deploy endpoints. To ensure the best operational performance, the Specialist needs to be able to track how often the Scientists are deploying models, GPU and CPU utilization on the deployed SageMaker endpoints, and all errors that are generated when an endpoint is invoked.
#### Which services are integrated with Amazon SageMaker to track this information? (Choose two.)

* AWS CloudTrail
* Amazon CloudWatch

## question 22

#### A retail chain has been ingesting purchasing records from its network of 20,000 stores to Amazon S3 using Amazon Kinesis Data Firehose. To support training an improved machine learning model, training records will require new but simple transformations, and some attributes will be combined. The model needs to be retrained daily.
#### Given the large number of stores and the legacy data ingestion, which change will require the LEAST amount of development effort?

* Insert an Amazon Kinesis Data Analytics stream downstream of the Kinesis Data Firehose stream that transforms raw record attributes into simple transformed values using SQL.

## question 23

#### A Machine Learning Specialist is building a convolutional neural network (CNN) that will classify 10 types of animals. The Specialist has built a series of layers in a neural network that will take an input image of an animal, pass it through a series of convolutional and pooling layers, and then finally pass it through a dense and fully connected layer with 10 nodes. The Specialist would like to get an output from the neural network that is a probability distribution of how likely it is that the input image belongs to each of the 10 classes.
#### Which function will produce the desired output?

* Softmax

## question 24

#### A Machine Learning Specialist trained a regression model, but the rst iteration needs optimizing. The Specialist needs to understand whether the model is more frequently overestimating or underestimating the target.
#### What option can the Specialist use to determine whether it is overestimating or underestimating the target value?

* Residual plots

## question 25

#### A Machine Learning Specialist kicks off a hyperparameter tuning job for a tree-based ensemble model using Amazon SageMaker with Area Under the ROC Curve(AUC) as the objective metric. This workflow will eventually be deployed in a pipeline that retrains and tunes hyperparameters each night to model click-through on data that goes stale every 24 hours.
#### With the goal of decreasing the amount of time it takes to train these models, and ultimately to decrease costs, the Specialist wants to reconfigure the input hyperparameter range(s).
#### Which visualization will accomplish this?

* A scatter plot with points colored by target variable that uses t-Distributed Stochastic Neighbor Embedding (t-SNE) to visualize the large number of input variables in an easier-to-read dimension.

## question 26

#### A Machine Learning Specialist is creating a new natural language processing application that processes a dataset comprised of 1 million sentences. The aim is to then run Word2Vec to generate embeddings of the sentences and enable different types of predictions.
#### Here is an example from the dataset:
#### "The quick BROWN FOX jumps over the lazy dog.`
#### Which of the following are the operations the Specialist needs to perform to correctly sanitize and prepare the data in a repeatable manner? (Choose three.)

* Normalize all words by making the sentence lowercase.
* Remove stop words using an English stopword dictionary.
* Tokenize the sentence into words.

## question 27

#### A company is using Amazon Polly to translate plaintext documents to speech for automated company announcements. However, company acronyms are being mispronounced in the current documents.
#### How should a Machine Learning Specialist address this issue for future documents?

* Convert current documents to SSML with pronunciation tags.

## question 28

#### An insurance company is developing a new device for vehicles that uses a camera to observe drivers' behavior and alert them when they appear distracted. The company created approximately 10,000 training images in a controlled environment that a Machine Learning Specialist will use to train and evaluate machine learning models.
#### During the model evaluation, the Specialist notices that the training error rate diminishes faster as the number of epochs increases and the model is not accurately inferring on the unseen test images.
#### Which of the following should be used to resolve this issue? (Choose two.)

* Perform data augmentation on the training data.
* Add L2 regularization to the model.

## question 29

#### When submitting Amazon SageMaker training jobs using one of the built-in algorithms, which common parameters MUST be specified? (Choose three.)

* The training channel identifying the location of training data on an Amazon S3 bucket.
* The Amazon EC2 instance class specifying whether training will be run using CPU or GPU.
* The output path specifying where on an Amazon S3 bucket the trained model will persist.

## question 30

#### A monitoring service generates 1 TB of scale metrics record data every minute. A Research team performs queries on this data using Amazon Athena. The queries run slowly due to the large volume of data, and the team requires better performance.
#### How should the records be stored in Amazon S3 to improve query performance?

* Parquet files

