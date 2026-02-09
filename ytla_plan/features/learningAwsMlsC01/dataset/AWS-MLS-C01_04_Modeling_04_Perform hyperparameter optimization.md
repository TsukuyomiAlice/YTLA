### Perform hyperparameter optimization
  * Preventing Underfitting
    * If your model peforms poorly on the training, as well as evalution data=>underfitting
    * Solutions:
      * Add more features to the model
      * Remove regularization
  * Preventing overfitting
    * Models that are good at making predictions on the data they were trained on, but not on new data it hasn’t seen before
    * Overfitted models have learned patterns in the training data that don't generalize to the real world
    * Often seen as high accuracy on training data set, but lower accuracy on test or evaluation data set.
    * Batch sizes that are larger can increase chances of becoming stuck in a local minima
    * Solutions (in decreasing order)
      * More training data might help
      * Add weight regularization
      * Reduce the capacity of the network (memorize a finite number of patterns to drive focus on the most prominent pattersns, which will likely generalize well
      * Use of less features might help
      * dropout (specific to NN)
    * Higher learning rates run the risk of overshooting an optimal solution or causing oscillation of accurate results
    * Generally good to pair a small batch size and a small learning rate
    * If seeing such a graph as either, overfitting is usually the case (blue is training, red is validation and the dashed line is the target):
      ![Classic signs of overfitting](https://img-b.udemycdn.com/redactor/raw/2020-10-03_10-38-36-1360ed7c3e1b03e7028e82140947f65a.png)
    * Specific to NN:
      * Dropout: Remove some neurons at each Epoch During training, which forces the model to learn/spread out learning among other neurons Preventing individual neurons from overfitting specific data point(s)
      * Early stopping is breaking early training from Epochs as accuracy levels out, preventing overfitting
      * Too wide/deep of a neural layer(s) ending in overfitting=> simpler model might be better
    * L1 (LASSO) / L2 (Ridge) Regularization
      * Preventing overfitting in ML in general
      * A regularization term is added as weights are learned
      * L1 term is the sum of the weights absolute weights
        * Performs feature selection - entire features go to O
        * Computationally inefficient
        * Sparse output
        * Good to avoid curse of dimensionality
        * When to use L1
          * Feature selection can reduce dimensionality
          * Out of 100 features, maybe only 10 end up with non-zero coefficients!
          * The resulting sparsity can make up for its computational inefficiency
          * But, if you think all of your features are important, L2 is probably a better choice.
      * L2 term is the sum of the square of the weights
        * All features remain considered, just weighted
        * Computationally efficient
        * Dense output
      * Same idea can be applied to loss functions and/or weights as learned
  * Training data vs Validation data vs Test data
    * 80/20 (Training/Validation) rule if data is largely available
    * Cross validation - usually done if data is in short supply
    * Validation set used to get the error rate (aka generalization or out of sample error)
    * If you training error is low and the generalization error is high=>overfitting
    * If you'd like to validate which algorithm is best, harness the training data on them and then validate against test set
    * If also validating multiple hyperparameters, a holdout, validation set, might be decent to validate following the training set=>validation set (select best model and hyperparameters that perform best), and then testing against the holdout set to avoid selecting a model that performs best on the test set data
    * Alternatively there is cross validation too, to avoid wasting too much training data on validation sets.  This involves splitting the training set into complementary subsets and the model is trained against a different combination of the subsets and tested against the remaining data subset(s).  Once the model/hyperparameters are finalized they are then trained on the complete training data to then measure the generalized error against the test set.
  
  * Model initialization
  * Neural network architecture (layers/nodes)
    * NN Learning Rate
      * Neural networks are trained by gradient descent (or some similar flavor)
      * We start at some random point, and sample different solutions (weights) seeking to minimize some cost function, over many epochs
        * Epochs – iterations at which we train, and attempt a different set of weights, looking to minimize the cost/loss function
      * How far apart these samples are is the learning rate
      * *Too high a learning rate means you might overshoot the optimal solution or oscillate on accuracy!*
      * *Too small a learning rate will take too long to train/find the optimal solution*
      * Learning rate is an example of a hyperparameter
    * NN Batch Size
      * How many training samples are used within each batch of each epoch
      * Somewhat counter-intuitively:
        * *Smaller batch sizes tend to work their way out of "local minima" more easily*
        * *Batch sizes that are too large can end up getting stuck in the wrong solution*
        * Random shuffling at each epoch can make for very inconsistent results from run to run
    * NN activation functions
  * Tree-based models (# of trees, # of levels)
  * Linear models (learning rate)
  * Note there is a time/cost consideration with iterations of training, so understand costs vs requirements up front 

#### Neural Network (NN)
  * Deep Learning Network is the case where there are multiple layers of neurons in a NN
  * Training involves learning the appropriate weights and biases throughout the network to generate classifications
  * Great for parallelization (GPU)
  * Deep Learning Frameworks (AWS supports both, but tend to build using MXNet):
    * TensorFlow/Keras
    * MXNet
  * Types:
    * Feedforward Neural Network
    * Convolutional Neural Network (CNN)
      * Image classification
    * Recurrent Neural Network (RNN)
      * Deal with Time series data or words in a sentence
      * RNN types:
        * Long Short Term Memory (LSTM), Gated Recurrent Unit (GRU)
       
##### NN on EC2
  * within EC2 instance-AMI can search for applicable image (Quickstart AMI is usually a good choice), thereafter, selecting the appropriate instance type for the AMI
  * can ssh into the instance from your local system
    * paste given host name
    * Auth=>ppk or pem file
    * Tunnel=>localhost:8888
    * after running/tunneling into the instance=> 'jupyter notebook' to then run in the browser
  * NN
    * data should be re-shaped/scaled appropriately between values of zero to one => Label should ideally be one-hot encoded
    * Other types of data matrices (eg: reviews or any given sentence) row's length (aka columns) need to be of equal count, otherwise they need to be truncated or padded before batch processing

##### CNN

Usage:
  * When you have data that doesn't neatly align into columns
    * Images Analysis that you want to find features or patterns within (eg: feature-location invariant)
    * Machine translation (eg: English to French)
    * Sentence classification
    * Sentiment analysis (can pick out sentences that flag the certain sentiment, this is more appropriate for CNN variants with attention)
  * They can find features that aren't in a specific spot
    * Like a stop sign in a picture
    * Or words within a sentence
    * Primarily used to work with image data

How do they work?
  * ﻿﻿Inspired by the biology of the visual cortex
    * Local receptive fields are groups of neurons that only respond to a part of what your eyes see (subsampling)
    * ﻿﻿They overlap each other to cover the entire visual field (convolutions)
    * They feed into higher layers that identify increasingly complex Images
      * Some receptive fields identify horizontal lines, lines at different angles, etc. (filters)
      * These would feed into a layer that identifies shapes
      * Which might feed into a layer that indentifies objects
  * For color images, extra layers for red, green, and blue

How do we "know" what we're seeing is what we're seeing?
  * Individual local receptive fields scan the image looking for edges, and pick up the edges of an object in a layer
  * The edges of the object get picked up by a higher level convolution that identifies the object's shape (and letters, too)
  * This shape then gets matched against your pattern of what your desired object looks like, also using the color layers to help narrow it down
  * The information continues to be processed upward until you are aware of what the object is

CNNs using Keras / Tensorflow
  * ﻿﻿Source data must be of appropriate dimensions
    * ﻿﻿ie width x length x color channels
  * ﻿﻿Conv2D layer type does the actual convolution on a 2D image
    * ﻿﻿Conv1D and Conv3D also available - doesn't have to be image data
  * ﻿﻿MaxPooling2D layers can be used to reduce a 2D layer (data) down by taking the maximum value in a given block reducing processing load on the CNN
  * ﻿﻿Flatten layers will convert the 2D layer to a 1D layer for passing into a flat hidden layer of neurons
  * ﻿﻿Typical usage:
    * ﻿﻿Conv2D=>MaxPooling2D=>Dropout=>Flatten=>Dense=>Dropout=>Softmax

CNN training isn't easy
  * ﻿﻿Very resource-intensive (CPU, GPU, and RAM)
  * ﻿﻿Lots of hyperparameters
    * ﻿﻿Kernel sizes, many layers with different numbers of units, amount of pooling, number of layers, choice of optimizer, etc.
  * ﻿﻿Getting the training data is often the hardest part! (As well as storing and accessing it)

CNN example architectures
  * ﻿﻿Defines specific arrangement of layers, padding, and hyperparameters
  * ﻿﻿LeNet-5
    * ﻿﻿Good for handwriting recognition
  * ﻿﻿AlexNet
    * ﻿﻿Image classification, deeper than LeNet
  * ﻿﻿GoogLeNet
    * ﻿﻿Even deeper, but with better performance
    * ﻿﻿Introduces inception modules (groups of convolution layers)
  * ﻿﻿ResNet (Residual Network)
    * ﻿﻿Even deeper - maintains performance via skip connections.

##### RNN
Usage:
  * Time-series data
    * When you want to predict future behavior based on past behavior
    * Web logs, sensor logs, stock trades
    * Where to drive your self-driving car based on past trajectories
  * Data that consists of sequences of arbitrary length
    * Machine translation
    * Image captions
    * Machine-generated music
   
Types:
  * Sequence to sequence (e.g. time series)
    * such as predict stock prices based on series of historical data
  * Sequence to vector
    * such as words in a sentence to sentiment
    * matching sequences to a vector state via multi layer perceptrons
  * Vector to sequence
    * such as create captions from an image
  * Encoder -> Decoder
    * Sequence -> vector -> sequence
    * such as machine translation

Training:
  * Backpropagation through time
    * Just like backpropagation on MLPs, but applied to each time step.
    * Back propagation must take into account nn topology as well as the time steps taken
  * All those time steps add up fast
    * Ends up looking like a really, really deep neural network.
    * Can limit backpropagation to a limited number of time steps (truncated backpropagation through time)
  * State from earlier time steps get diluted over time
    * This can be a problem (State Dilution), for example when learning sentence structures
    * Older behavior doesn't matter more than new behavior (eg: first words in a sentence, might be more important); understanding, relationships between words to derive sentiment, meaning, etc.=>LSTM or GRU
  * Layer of rnn with feedback scales horizontally, and can learn more complicated patterns as results
  * RNN neurons have a training feedback loop:
    * training data is fed to its input during training, step and/or, perhaps from the loop input from a previous layer (can be a layer or a single neuron) or step to be summed up-> activation function (eg: tanh)
    * over time during training is "memory cell" as it maintains memories of previous steps
  * LSTM Cell
    * Long Short-Term Memory Cell
    * Maintains separate short-term and long-term states
    * Can work with sequences of spoken language to then be used to generate sequenced output (eg: written text)
  * GRU Cell
    * Gated Recurrent Unit
    * Simplified LSTM Cell that performs about as well, but shorter to train
  * RNN isn't easy to train
    * Very sensitive to topologies, choice of hyperparameters
    * Very resource intensive
    * A wrong choice can lead to a RNN that doesn't converge at all.

##### Transformers

The Evolution of Transformers
  * Prior to Transformers, there were RNNs, LSTMs
  * Introduced a feedback loop for propagating information forward
  * Useful for modeling sequential things
    * Time series
    * Language! A sequence of words (or tokens)
  * Machine translation
  * Encoder / Decoder architecture
  * Encoders and Decoders are RNNs
  * But, the one vector tying them together creates an information bottleneck
    * Information from the start of the sequence may be lost

 
Attention
  * A hidden state for each step (token)
  * Deals better with differences in word order
  * Starts to have a concept of relationships between words
  * But RNNs are still sequential in nature, can't parallelize it

 What are Transformers
  * Ditch RNNs for feed-forward neural networks (FFNNs)
  * Use "self-attention"
  * This makes it parallelizable (so can train on much more data)
  * Attention-as a token is translated in a sentence, what other token(s) in said sentence, should attention be paid, potentially extracting meaning
  * Attention weights-certain weighting applied as sequential tokens are processed

Self-Attention (in more depth)
  * Each encoder or decoder has a list of embeddings (vectors) for each token that are the token's numerical translation placed in an embedding layer which is a multi dimensional vector.  Space between vectors represents similarity of tokens
  * Self-attention produces a weighted average of all token embeddings.  The magic is in computing the attention weights.
  * This results in tokens being tied to other tokens that are important for its context, and a new embedding that captures its "meaning" in context.
  * Three matrices of weights are learned through back-propagation
    * Query (Wq)
    * Key (Wk)
    * Value (Wv)
  * Every token gets a query (q), key (k), and value (v) vector by multiplying its embedding for a token against these matrices
  * Compute a score for each token by multiplying dotproduct its query with each key
  * "Scaled dot-product attention"
  * Dot product is just one similarity function we can use.
  * In practice, softmax is then applied to the scores to normalize them.

 
Masked Self-Attention
  * A mask can be applied to prevent tokens from "peeking" into future tokens (words)
  * GPT does this, but BERT does something else (masked language modeling)
  * In a sentence "A good novel", "good" wouldn't be affected by "novel", but "novel" could by "good"
  * This is just the concept... actual implementation details will vary.
  * Multiply values by scores (after masking, softmax), and sum them up.
  * Repeat entire process for each token (in parallel)
  * Now we have updated embeddings for each token!
  * These weight each token embedding as it's passed into the feed-forward NN.

 
Multi-Headed Self-Attention
  * The q, k, and v vectors are reshaped into matrices
  * Then each row of the matrix can be processed in parallel
  * The number of rows are the number of "heads"
  * Transformer Encoder-designed to learn embeddings that can be used for predictive modeling
    * BERt=> Composed of stacks of encoders
  * Transformer Decoder-designed to generate new text per query
    * GPT=> composed entirely of decoders
  * embeddings fed into an embedding layer

Applications of Transformers 
  * Chat!
  * Question answering
  * Text classification
    * eg: sentiment analysis
  * Named entity recognition
  * Summarization • Translation
  * Code generation
  * Text generation
    * eg: automated customer service 

##### GPT
  * Generative Pre-Trained Transformer (eg: GPT-2)
  * Decoder-only - stacks of decoder blocks
    * Each consisting of a masked self-attention layer, and a feed-forward neural network
    * As an aside, BERT consists only of encoders. T5 is an example of a model that uses both encoders and decoders.
  * No concept of input, all it does is generate the next token over and over
    * Using attention to maintain relationships to previous words / tokens
    * You "prompt" it with the tokens of your question
    * It then generates given the previous tokens
  * Getting rid of the idea of inputs and outputs is what allows us to train it on unlabeled piles of text
    * It's "learning a language" rather than optimizing for some specific task
  * Hundreds of billions of parameters
  * GPT output isn't based on finding true or correct results, but results generated based upon the input it was trained on

 
GPT Input processing
  * Tokenization, token encoding
  * Token embedding
    * Captures semantic relationships between tokens, token similarities
  * Positional encoding
    * Captures the position of the token in the input relative to other nearby tokens
    * Creates a (scalable \[works on any length]) matrix of vectors with overlayed sine and cosine functions interwoven, where words are within a period relative to other words to derive meaning


GPT Output processing
  * The stack of decoders outputs a vector at the end
  * Multiply this with the token embeddings
  * This gives you probabilities (logits) of each token being the right next token (word) in the sequence
  * You can randomize things a bit here ("temperature") instead of always picking the highest probability.  Setting the temperature to 0 picks the highest probability.  
  * can import GPT-2 into AWS via hugging face
  * Stacking up decoder blocks with own self attention increases the complexity of the model
  * The stack of decoder blocks is conducting masked self-attention and outputting into a feed forward NN to finally produce an output, vector of what the next token is, this output vector is then multiplied back into the embedding matrix to give us probabilities of what the next token is
  * NN work on numbers only, not words, pictures, etc.
  * Token embedding => Convert tokens to vectors in a multi dimensional space; space–distance correlating similarity of meeting
  * positional encoding-process all tokens in parallel

##### Foundation Models (Generative AI via AWS)
  * The giant, pre-trained transformer models we are fine tuning for specific tasks, or applying to new applications
  * GPT-n (OpenAl, Microsoft)
  * BERT (Google)
  * DALL-E (OpenAl, Microsoft)
  * LLaMa (Meta)
  * Segment Anything (Meta)
    
###### AWS Foundation Models
  * Jurassic-2 (Al21labs)
    * Multilingual LLMs for text generation
    * Spanish, French, German, Portuguese, Italian, Dutch
  * Claude (Anthropic)
    * LLMs for conversations
    * Question answering
    * Workflow automation
  * Stable Diffusion (stability.ai)
    * Image, art, logo, design generation
  * Amazon Titan
    * Text summarization
    * Text generation
    * Q&A
    * Embeddings
      * Personalization
      * Search
      * Converting input to a vector, which can then be used as a similar to comparison for another import, or even a listing of similar results

###### Amazon SM Jumpstart with Generative AI
  * SageMaker Studio has a "JumpStart" feature
  * Lets you quickly open up a notebook with a given model loaded up and ready to go
  * Current foundation models
    * Hugging race models (text generation)
      * Falcon, Flan, BloomZ, GPT-J
    * Stabile Diffusion (image generation)
    * Amazon Alexa (encoder/decoder multilingual LLM)
    * Google, and Microsoft models aren't supported on AWS as they are direct competitors

###### Amazon SM Jumpstart How-To
  * launch NB within SM, with pre-populated foundation models (internal, hugging face, etc.)
  * create a domain
    * A unique domain name
    * The user profile (eg: execution role)
    * IAM/identity center
    * SM studio integrations
    * SM canvas
    * fine-tuned network security settings
    * fine-tuned encryption settings
    * VPC associated with an account
  * deploys actual hardware, though you are also given the opportunity to change instance type(s) or potentially changing the use/# of GPUs
  * Can fine-tune the model through direct input within the NB or S3
    * if input is large, it will train it many times trying to optimally tune hyperparameters
 
#### Activation functions

A gated function that verifies how an incoming value to a node/neuron is higher than a threshold value to prevent linearity to define the output, used within internal/output layer cells in neural networks

Linear activation function (eg: y=x)
  * ﻿﻿It doesn't really *do* anything
  * ﻿﻿Can't do backpropagation

![Linear activation function](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tldIgyDQWqm-sMwP7m3Bww.png)

 
Binary step function
  * ﻿﻿It's on or off
  * ﻿﻿Can't handle multiple classification - it's binary after all
  * ﻿﻿Vertical slopes don't work well with calculus!

![Binary step function](https://raw.githubusercontent.com/Codecademy/docs/main/media/binary-step-plot.png)

Non-linear activation functions
  * ﻿﻿These can create complex mappings between inputs and outputs
  * ﻿﻿Allow backpropagation (because they have a useful derivative)
  * ﻿﻿Allow for multiple layers (linear functions degenerate to a single layer)

Sigmoid / Logistic / TanH
  * ﻿﻿Nice & smooth
  * ﻿﻿Scales everything from 0-1 (Sigmoid AKA Logistic) or -1 to 1 (tanh / hyperbolic tangent)
  * However, changes slowly for high or low values
    * The "Vanishing Gradient" problem exists for both when getting toward extremes in +/-, output changes very slowly, where numerical precision can become an issue
      * When the slope of the learning curve approaches zero, things can get stuck
      * We end up working with very small numbers that slow down training, or even introduce numerical errors
      * Becomes a problem with deeper networks and RNNs as these "vanishing gradients" propagate to deeper layers
      * Opposite problem: "exploding gradients"
    * Fixing the Vanishing Gradient Problem
      * Multi-level heirarchy
        * Break up levels into their own sub-networks trained individually
      * Long short-term memory (LSTM)
      * Residual Networks
        * eg: ResNet [a CNN based object recognition]
        * Ensemble of shorter networks
      * Better choice of activation function
        * ReLU is a good choice
    * Gradient checking:
      * A debugging technique
      * Numerically check the derivatives of the learning curve computed during training
      * Useful for validating code of NN training, though it's likely you're probably not gonna write this code
  * ﻿﻿Computationally expensive
  * ﻿﻿Tanh generally preferred over sigmoid
  * Tanh well suited for RNN
  * sigmoid appropriate for more than one classification

![Sigmoid vs tanh](https://miro.medium.com/v2/resize:fit:1190/format:webp/1*f9erByySVjTjohfFdNkJYQ.jpeg)


Rectified Linear Unit (ReLU)
  * If using slower neural network convergence
    * ReLU - solution to sigmoid and tanh 
  * ﻿﻿Very popular choice
  * ﻿﻿Easy & fast to compute
  * ﻿﻿However, when inputs are zero or negative, we have a linear function and all of it's associated problems
    * ﻿﻿The "Dying ReLU problem", where input is <= 0

![ReLU](https://machinelearningmastery.com/wp-content/uploads/2018/10/Line-Plot-of-Rectified-Linear-Activation-for-Negative-and-Positive-Inputs.png)

Leaky ReLU
* Solves "dying ReLU" by introducing a negative slope below 0

![Leaky ReLU](https://production-media.paperswithcode.com/methods/Screen_Shot_2020-05-25_at_3.09.45_PM.png)

Parametric ReLU (PReLU)
  * ﻿﻿ReLU, but the slope in the negative part is learned via backpropagation
  * ﻿﻿Complicated and YMMV (your mileage may vary)


Other ReLU variants
  * ﻿﻿Exponential Linear Unit (ELU)
  * ﻿﻿Swish
    * ﻿﻿From Google, performs really well
    * ﻿﻿Mostly a benefit with very deep networks (40+ layers)
  * ﻿﻿Maxout
    * ﻿﻿Outputs the max of the inputs
    * ﻿﻿Technically ReLU is a special case ot maxout
    * ﻿﻿But doubles parameters that need to be trained, not often practical.

Softmax
  * ﻿﻿Used on the final output layer of a multiple classification problem
  * ﻿﻿Basically converts outputs to probabilities of each classification
  * ﻿﻿Can't produce more than one label for something (sigmoid can)
  * ﻿﻿Don't worry about the actual function for the exam, just know what it's used for 

How to choose an activation function
  * ﻿﻿For multiple classification, use softmax on the output layer
  * ﻿﻿RNNs do well with Tanh
  * ﻿﻿For everything else
    * ﻿﻿Start with ReLU
    * ﻿﻿If performance needs to do better, try Leaky ReLU
    * ﻿﻿Last resort: PReLU, Maxout
    * ﻿﻿Swish for really deep networks
  * Leaky ReLU or PReLU are the answer to dying ReLU, while the latter has computationally expensive slope calculations along with the weights in said NN
