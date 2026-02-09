### Select and express intuition behind the appropriate model(s) for a given machine learning problem

#### [Xgboost](https://github.com/LongBu/AWS-MLS-C01-Study-Guide#xgboost-extreme-gradient-boosting)
    * Observations are weighted
    * Some will take part in new training sets more often
    * Training is sequential; each classifier takes into account the previous one's success.
    * Boosting generally yields better accuracy than Bagging
    
#### logistic regression - supervised model dealing with classification and probability outcomes, though the former is more prevalent
  * multinomial logistic regression - used to predict categorical placement in or the probability of category membership on a dependent variable based on multiple independent variables.  It is a simple extension of (binary) logistic regression that allows for more than two categories of the dependent or outcome variable. 

#### K-means - unsupervised cluster analysis on unlabeled data where the aim is to partition a set of objects into K clusters in such a way to understand what types of groups exist or to identify unknown groups in complex data sets

#### linear regression - useful in predicting a variable based on the value of another variable, a supervised model curvature, if you will, in a n-space dimensional plane 

#### decision trees - a supervised model based on a set of decision rules for prediction analysis, data classification, and regression. May possibly overfit training data.

#### [RNN](https://github.com/LongBu/AWS-MLS-C01-Study-Guide#rnn)

#### [CNN](https://github.com/LongBu/AWS-MLS-C01-Study-Guide#cnn)

#### Ensemble-supervised, multiple models that are combined to improve the overall performance and accuracy.  An excellent example being Random Cut Forests, as decision trees are prone to overfitting, where lots of decision trees are modeled and let them all vote on the result.  

#### [Transfer learning](https://github.com/LongBu/AWS-MLS-C01-Study-Guide#transfer-learning)

#### Bagging - generate N new training sets by random sampling with replacement.  Each resampled model can be trained in parallel
    * Bagging avoids overfitting over boost
    * Bagging is easier to parallelize over boost

#### Support Vector Machine (SVM)
    * a supervised ML algorithm that can be used for either classification or regression
    * can solve linear and nonlinear problems
    * SVM classification creates a line or hyperplane to separate data into classes 
    * can be used for text classification such as categories, detecting spam and sentiment analysis
    * commonly used for image recognition (performs particularly well in aspect-based recognition and color-based classification)
    * outlier detection

#### t-SNE or t-distributed stochastic neighbor embedding - utilized for reducing high dimensional data usually to two to three dimensions with the intent of visualization
