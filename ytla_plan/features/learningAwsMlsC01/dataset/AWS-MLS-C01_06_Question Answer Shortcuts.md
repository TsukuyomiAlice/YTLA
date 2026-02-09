## Question Answer Shortcuts
  * If you see "near real time" in the question, be on the look out for the use of λ in the answer
  * If you see "real time" look for an option in the kinesis services
  * If "efficiency" is desired for the solution, kinesis services might not be best as custom coding might be necessary
  * If given a choice between a "hand rolled" service vs an AWS solution, choose the latter
  * If there is an AWS Service (excluding SageMaker Algorithms) available to do a job and minimal work is to be done, go with this (eg: Personalize for a recommendation engine would be less effort that setting up a SM Factorization Machine)
  * If classification is needed at the "pixel" level, look for a solution utilizing Semantic Segmentation
  * If metadata mentioned, Glue is likely part of the solution
  * If a fully managed (scalable) service used transfer of any data/logs/text/videos => Amazon Data Firehose
  * If anything concerning 'celebrity' detection (with minimal development), Rekognition is likely part of the solution, and if video based input => Amazon Rekognition Video
  * Built in SM algorithms are not customizable (containers, frameworks, archetecture, etc.)
  * Remember the following algorithm optimizers: Adam, AdaGrad, SGD, Rmsprop, and adadelta
  * If a question's premise specifies the prescense of labeled or unlabled data, this should grant insight into eliminating either unsupervised or supervised algorithms
  * Pronunciation=>Lexicons