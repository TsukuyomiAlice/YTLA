### Evaluate machine learning models.
  * Avoid overfitting/underfitting (detect and handle bias and variance)
  * Metrics (AUC-ROC, RMSE)
  * Outliers
    * Variance measures how "spread-out" the data is.
      * Variance (σ^2) is simply the average of the squared differences from the mean
      * Example: What is the variance of the data set (1, 4, 5, 4, 8)?
        * First find the mean: (1+4+5+4+8)/5 = 4.4
        * Now find the differences from the mean: (-3.4, -0.4, 0.6, -0.4, 3.6)
        * Find the squared differences: (11.56, 0.16, 0.36, 0.16, 12.96)
        * Find the average of the squared differences:
          * σ^2= (11.56 + 0.16 + 0.36 + 0.16 + 12.96) / 5 = 5.04

    * Standard Deviation σ is just the square root of the variance.
      * σ^2 = 5.04
      * σ = (5.04)^.5 = 2.24
      * So the standard deviation of (1, 4, 5, 4, 8) is 2.24.
      * This is usually used as a way to identify outliers. Data points that lie more than one standard deviation from the mean can be considered unusual.
      * You can tell how extreme a data point is by asking about "how many sigmas" away from the mean it is?
    * Correlation Types
      * Covariance correlation coefficient: used when you have a Gaussian relationship between your variables.
      * Pearson’s correlation coefficient: used when you have a Gaussian relationship between your variables.
      * Spearman’s correlation coefficient: used when you have a non-Gaussian relationship between your variables.
      * Polychoric correlation coefficient:  used to understand relationships of variables gathered via surveys (such as personality tests) that use rating scales.
    * Dealing with Outliers
      * Sometimes it's appropriate to remove outliers from your training data
      * Do this responsibly! Understand why you are doing this.
      * For example: in collaborative filtering a single user who rates thousands of movies could have a big effect on everyone else's ratings. That may not be desirable.
      * Another example: in web log data, outliers may represent bots or other agents that should be discarded.
      * But if someone really wants the mean income of US citizens for example, don't toss out billionaires just because you want to.
      * Our old friend standard deviation provides a principled way to classify outliers.
      * Find data points more than some multiple of a standard deviation in your training data.
      * What multiple? Use common sense.
      * Remember AWS's Random Cut Forest algorithm creeps into many of its services - it is made for outlier detection, eg: QuickSight, Kinesis Analytics, SageMaker, and more
      * Tranformation options:
        * Logarithm Transformation: decreases the effect of the outliers, due to the normalization of magnitude differences and the model become more robust.
        * Robust Standardization: Standardization (or z-score normalization) scales the values while taking into account standard deviation. If the standard deviation of features is different, their range also would differ from each other. This reduces the effect of the outliers in the features.  A better approach to standardizing input variables in the presence of outliers is to ignore the outliers from the calculation of the mean and standard deviation, then use the calculated values to scale the variable (eg: robust standardization).
        * Standard Scaler is also an option if dealing with large weights for some features, though it is sensitive to outliers
      * Incorrect option:
        * Normalization:  scales all values in a fixed range between 0 and 1. This transformation does not change the distribution of the feature and due to the decreased standard deviations, the effects of the outliers increases. 

    * Binning
      * Bucket observations together based on ranges of values.
      * Example: estimated ages of people
        * Put all 20-somethings in one classification, 30-somethings in another, etc.
      * Interval binning groups categories into discrete interval bins that may or may not have equal counts
      * Quantile binning, a type of interval binning, categorizes data by their place in the data distribution
        * Ensures fixed number of observations within a fixed number of bins
      * Transforms numeric data to ordinal data
      * Especially useful when there is uncertainty in the measurements
      * Helps to cover up imprecision in data collection(s)

    * Transforming
      * Applying some function to a feature to make it better suited for training
      * Feature data with an exponential trend may benefit from a logarithmic transform
      * Example: YouTube recommendations
        * A numeric feature x is also represented by x^.5 and X^2
        * This allows learning of super and sub-linear functions

    * Encoding
      * Transforming data into some new representation required by the model
      * One-hot encoding
        * Create "buckets" for every category
        * The bucket for your category has a 1, all others have a 0
        * Very common in deep learning, where categories are represented by individual output "neurons"

    * Scaling / Normalization
      * Some models prefer feature data to be normally distributed around 0 (most neural nets)
      * Most models require feature data to at least be scaled to comparable values
      * Otherwise features with larger magnitudes will have more weight than they should
        * Example: modeling age and income as features - incomes will be much higher values than ages
        * Normalization of numeric variables can help the learning process if are very large range differences between numeric variables as those with the highest magnitude could dominate the ML model, no matter if the feature is correlated with the target or not
        * Normalization isn't a good solution to deal with outliers, but is so for dealing with large magnitudes.  
        * Scikit_learn has a preprocessor module that helps (especially outliers)
          * MinMaxScaler \[vars => 0 to 1] column-wise, if features within columns
          * MaxAbsScaler \[vars => -1 to 1]
          * RobustScaler (x - xmedian)/(Range between 1st \[25%] and 3rd \[75%] quartiles)
          * StandardScaler (x - xmean)/σ aka mean/variance standardization, or z-score normalization
          * Normalizer \[vars => 0 to 1] rows-wise, if features within rows
      * Remember to scale your results back up
    * Shuffling
      * Many algorithms benefit from shuffling their training data
        * Shuffling should be conducted prior to uploading to S3
      * Otherwise they may learn from residual signals in the training data resulting from the order in which it was collected
  * Binary confusion matrix (classification metrics):
    | | Actual Yes | Actual No |
    | --- | --- | ---|
    | Predicted Yes | true positives | false positives |
    | Predicted No | false negatives| true negatives |

  * Multi-class confusion matrix + heat map, where heat map shows how the classifications or misclassifications happened (note true positives would be on the diagonal)
  * Confusion Matrix Measurements:
    | Measure | Abbreviation | Formula |
    | ------------- | ------------- | ------------- |
    | Error Rate | ERR | (FP + FN)/(TP + TN + FN + FP) = (FP + FN)/(P + N) |
    | Root Mean Square | RMSE | square root of the mean of the sum of all squared errors of each prediction from the actual true value |
    | Accuracy | ACC | (TP + TN)/(TP + FP + TN + FN) |
    | Sensitivity, True positive rate, Recall, Completeness| SN, TPR, REC | TP/(TP + FN) = TP/P = 1 - FNR |
    | Precision, Positive predictive value, Correct Positives| PREC, PPV | TP/(TP + FP) |
    | Specificity, True negative rate | SP, TNR | TN/(TN + FP) = TN/N |
    | False positive rate | FPR | FP/(FP + TN) = 1 - SP = 1 - TNR |
    | False negative rate | FNR | FN/(TP + FN) = FN/P = 1 - REC |
    | F1 Score (harmonic mean of precision and recall) | F1 | 2TP/(2TP + FP + FN) = 2 * (Precision * Recall)/(Precision+Recall) |
   
  * Recall is a good choice of metric when you care a lot about false negatives (eg: fraud detection).
  * Recall and FPR prioritize the identification of True cases, though recall of course prioritizes higher (eg: TPR > FPR)
  * Precision is a good choice of metric when you care a lot about false positives (eg: medical screening, drug testing).  In the event that precision is not available for such a scenario, specificity is a good choice, too, as this indicates how well the test indicates true negatives.  Specificity is effectively precision in the negative sense.
  * Be sure to read the question(s) to understand the goal, regardless of the test type
    * If they mention not wanting True cases going undetected=>recall
      * eg:The cost of not catching a fraudulent claim is higher than the cost of investigating a claim that is suspected to be fraudulent=>recall
    * If they mention not wanting False cases being detected=>precision
      * eg:The cost of paying a fraudulent claim is higher than the cost of investigating a claim that is suspected to be fraudulent=>precision
  * F1 is a good choice when you care about precision AND recall
  * Precision-Recall Area-Under-Curve (PR AUC) > recall if trying to improve positive case results
  * RMSE, an accuracy measurement, is a good choice when you only care about right & wrong answers
  * Offline and online model evaluation, A/B testing
  * Compare models using metrics (time to train a model, quality of model, engineering costs)
  * Cross validation (eg: from sklearn.model_selection import cross_val_score)
    * choose many (k-folds)=>train
    * choose remaining holdouts to validate against
    * average out the validation step results
    * good if lacking data
    * stratified k-folds is good to use when dealing with a classifier with imbalanced class data distribution input (training/validation)
  * Sometimes accuracy isn't everything:
    * A test for a rare disease can be 99.9% accurate by just guessing "no" all the time
    * We need to understand true positives and true negative, as well as false positives and false negatives.
    * A confusion matrix shows this.

![Heat-Confusion to know](https://docs.aws.amazon.com/images/machine-learning/latest/dg/images/mlconcepts_image3.png)


  * Number of correct and incorrect predictions per class (infer from colors of each cell)
  * F1 scores per class
  * True class frequencies: the "total" column to the left of F1
  * Predicted class frequencies: the "total" on the bottom row

#### ROC Curve
![ROC Curve](https://upload.wikimedia.org/wikipedia/commons/6/6b/Roccurves.png)
  * Receiver Operating Characteristic Curve
  * Plot of true positive rate (recall) vs. false positive rate at various threshold settings.
  * Points above the diagonal represent good classification (better than random)
  * Ideal curve would just be a point in the upper-left corner
  * The more it's "bent" toward the upper-left, the better

#### AUC Curve
  * Area Under the Curve (AUC) is the area under an ROC curve
  * Equal to probability that a classifier will rank a randomly chosen positive instance higher than a randomly chosen negative one
  * ROC AUC of 0.5 is a useless classifier, 1.0 is perfect
  * Commonly used metric for comparing classifiers
