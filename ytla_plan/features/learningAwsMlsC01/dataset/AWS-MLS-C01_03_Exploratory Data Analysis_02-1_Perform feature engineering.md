### Perform feature engineering

  * Applying your knowledge of the data - and the model you're using - to identify and extract useful features to train your model with.
  * Analyze/evaluate feature engineering concepts (binning, tokenization, outliers, synthetic features, 1 hot encoding, reducing dimensionality of data) to understand what features one should use
    * Do I need to transform these features in some way?
    * How do I handle missing data?
    * Should I create new features from the existing ones?
    * You can't just throw in raw data and expect good results
    * Expertise in the applied field helps
    * Trim down feature data or create and combine new ones
    * Normalize or encode data
    * Handle missing data
   
### The Curse of Dimensionality
  * Too many features can be a problem - leads to sparse data
  * Every feature is a new dimension
  * Much of feature engineering is selecting the features most relevant to the problem at hand
    * This often is where domain knowledge comes into play
  * Unsupervised dimensionality reduction techniques can also be employed to distill many features into fewer features to provide insights
    * РСА
    * K-Means
   
### Feature Dependencies:
  * Features that are perfectly linearly dependent=>leads to a singular matrix=>infinity solutions
  * Vectors are linearly dependent if at least one vector of the set can be expressed as a linear combination of the other vectors, which equates to a homogenous system having a non-zero solution
  * Highly correlated features can be alleviated by Lasso Regularization and PCA, K-Means, an autoencoder, which otherwise can cause trouble for models to arrive at solution(s)

### Time Series Analysis:
  * Discrete samples taken over a period of time
  * trends
    * slope slant
    * can be seasonal, can superimpose curves vs the trends to decipher if a pattern is exhibited in variations (eg: month to month)
    * can both be seasonal and have an overall trend, too.  To get the overall trend, subtract out noise and seasonality 
  * Noise: random variations
    * Additive model
      * Seasonal variation is constant => seasonality + trends + noise = TS model
    * Multiplicative model
      * seasonal variation increases as the trend increases => seasonality * trends * noise = TS model
  * If developing a model, avoid harnessing static attributes, or limited data in favor of data detailing correlational activity
     
