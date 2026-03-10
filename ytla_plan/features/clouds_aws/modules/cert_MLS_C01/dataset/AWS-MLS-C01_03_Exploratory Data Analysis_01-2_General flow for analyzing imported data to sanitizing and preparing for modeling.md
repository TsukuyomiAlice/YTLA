### General flow for analyzing imported data to sanitizing and preparing for modeling:
  * import data
  * head()
  * Does the data have column names?
  * Identify and handle missing data, corrupt data, stop words, etc.
    * Labeled data (recognizing when you have enough labeled data and identifying mitigation\[s])
    * strategies [Data labeling tools (Mechanical Turk, manual labor)])
  * Are certain rows attributes of the data type or na values?
    * Can drop rows potentially (*.dropna(inplace=True), though this might introduce bias if the missing values aren't evenly distributed
  * describe()=> are counts of all the columns equal?
  * Formatting, normalizing, augmenting, and scaling data
  * If remapping the data, it is a good idea to check the mean/std of attributes from/to via describe()
  * To convert to the numpy array=>*.values()


#### Imputing missing data
##### Mean Replacement 
  * Replace missing values with the mean value from the rest of the column (single feature)
  * Fast & easy, won't affect mean or sample size of overall data set
  * Median may be a better choice than mean when outliers are present
  * Certainly better than imputing 0
  * But it's generally pretty terrible.
    * Only works on column level, misses correlations between features
    * Can't use on categorical features (imputing, with most frequent value can work in this case, though)
    * Not very accurate
##### Dropping 
  * If not many rows contain missing Data
    * dropping those rows doesn't bias your data
    * you don't have a lot of time
  * Will never be the right answer for the "best" approach.
  * Almost anything is better. Can you substitute another similar field perhaps? (i.e., review summary vs. full text)
  * However, if generalization is the goal and leaving in outliers will have a negative impact this might be beneficial
##### KNN: Find K "nearest" (most similar) rows and average their values
  * Assumes numerical data, not categorical
  * There are ways to handle categorical data (Hamming distance)
  * KNN is a good method to produce decent imputation results for missing data
##### Deep Learning
  * Build a machine learning model to impute data for your other machine learning model(s)!
  * Works well for categorical data, though complicated.
  * One of the better methods for missing data to produce decent results
##### Regression
  * Find linear or non-linear relationships between the missing feature and other features
  * Most advanced technique: MICE (Multiple Imputation by Chained Equations) - finds relationships between features and one of the better imputation methods for missing data
##### Get more data
  * What's better than imputing data? Getting more real data!


#### Unbalanced data
  * Large discrepancy between "positive" and "negative" cases
    * i.e., fraud detection. Fraud is rare, and most rows will be not-fraud
    * "positive" doesn't mean "good" it means the thing you're testing for happened.
      * If your machine learning model is made to detect fraud, then fraud is the positive case.
  * Mainly a problem with neural networks
  * Potential Solutions:
    * Create additional "positive" cases (eg: SMOTE/GAN)
    * Optimize the cost function to penalize the model for predicting negative outcomes when the actual outcome is positive (punish false negatives, or in other words, false negatives have a larger impact than that of false positives)
  * If having to use unmodified, unbalanced data some good metrics would be F1 Score, Recall, Precision and AUROC

#### Oversampling
  * Duplicate samples from the minority class
  * Can be done at random

#### Undersampling
  * Instead of creating more positive samples, remove negative ones
  * Throwing data away is usually not the right answer
    * Unless you are specifically trying to avoid "big data" scaling issues

#### Random Sampling
  * Most popular sampling technique, though if time-series based, needs to be mindful of temporal order so as to keep the training relevant

#### Stratified Sampling
  * If some strata are unique in your data, this technique ensures proportional representation of each representational class, allowing you to understand how each group compares with each other
  * Divides data per designated column, selecting samples randomly from each strata to then combine these samples into a stratified population sample, which might be helpful to mitigate class imbalances
   
#### SMOTE 
  * Artificially generate new samples of the minority class using nearest neighbors
    * Run K-nearest-neighbors of each sample of the minority class
    * Create a new sample from the KNN result (mean of the neighbors)
  * Both generates new samples and undersamples majority class
  * Generally better than just oversampling
  * New samples are almost identical
  * Technique is expeditious, though the results aren't as useful as unique observations created by alternative techniques (eg: GAN)

#### GAN 
  * Technique generates unique observations that more closely resemble real minority observations without being almost identical. This results in more unique observations of your minority class that improves your model’s accuracy by helping to correct the imbalance in your data.


#### Adjusting thresholds
  * When making predictions about a classification (fraud / not fraud), you have some sort of threshold of probability at which point you'll flag something as the positive case (fraud)
  * If you have too many false positives, one way to fix that is to simply increase that threshold.
    * Reduces false positives but; could result in more false negatives

