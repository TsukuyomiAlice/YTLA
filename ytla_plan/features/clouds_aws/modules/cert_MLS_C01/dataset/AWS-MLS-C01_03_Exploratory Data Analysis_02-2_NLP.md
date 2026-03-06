### NLP

#### Term Frequency and Inverse Document Frequency (TF-IDF)
  * Important data for search - figures out what terms are most relevant for a document
    * Compute TF-IDF for every word/n-gram in a corpus
    * For a given search word/n-gram, sort the documents by their TF-IDF score accordingly 
    * Display the results
  * Term Frequency just measures how often/relevancy of a word occurs in a document
  * Document Frequency is how often a word occurs or not (this is either 0 or 1 per document) in an entire set of documents, i.e., all of Wikipedia or every web page (predicts common words).  The test appears to use the formula tf/log(document frequency)
  * Equal to: Term Frequency/Document Frequency or Term Frequency * Inverse Document Frequency
    * We actually use the log of the TF-IDF (sometimes depending on magnitudes), since word frequencies are distributed exponentially. That gives us a better weighting of a words overall popularity
  * TF-IDF assumes a document is a "bag of words"
    * Parsing documents into a bag of words can be most of the work
    * Bag of words can be used to show the statistics/occurence of individual words in a document
    * Words can be represented as a hash value (number) for efficiency
    * What about synonyms? Various tenses? Abbreviations? Capitalizations? Misspellings?
  * Doing this at scale is the hard part (Spark can help here)

#### NLP Preprocessing/Cleaning Techniques for scalability:
  * lowercase characters
  * punctuation removal
  * word tokenization
  * stop word removal
  * html tag removal
  * stemming
  * lemmatization

#### Unigrams, bigrams, etc.
  * An extension of TF-IDF is to not only compute relevancy for individual words (terms) but also for bi-grams or, more generally, n-grams.
  * "I love certification exams"
    * Unigrams: "l", "love", "certification", "exams"
    * Bi-grams: "I love", "love certification", "certification exams"
    * Tri-grams: "I love certification", "love certification exams"
  * The TF-IDF matrix will consist of the documents as rows and the selection of n-grams as columns

#### Modern Natural Language Processing
  * ﻿﻿Transformer deep learning architectures are currently state of the art utilizing a mechanism of "self-attention"
    * ﻿﻿Weighs significance of each part of the input data
    * ﻿﻿Processes sequential data (like words, like an RNN), but processes entire input all at once.
    * ﻿﻿The attention mechanism provides context, so no need to process one word at a time.
  * ﻿﻿BERT, RoBERTa, T5, GPT-2, DistilBERT
  * ﻿﻿DistilBERT: uses knowledge distillation to reduce model size by 40%

#### Transfer Learning
  * fine-tuning and transfer learning are the same thing
  * ﻿﻿NLP models (and others) are too big and complex to build from scratch and re-train every time
    * ﻿﻿The latest may have hundreds of billions of parameters!
  * use a pre-trained model to further train for specific task(s)
  * ﻿﻿Model zoos such as Hugging Face offer pre-trained models to start from
    * ﻿﻿Integrated with Sagemaker via Hugging Face Deep Learning Containers
    * Hugging face is essentially a giant repo of pre-trained models (eg: GPT2, GPTJ, llama, stable-diffusion)
  * ﻿﻿You can fine-tune these models for your own use cases
  * If fine-tuning a model, need to install the source version of the model
  * ﻿﻿BERT transfer learning example:
    * ﻿﻿Hugging Face offers a Deep Learning Container (DLC) for BERT
    * ﻿﻿It's pre-trained on BookCorpus and Wikipedia
    * ﻿﻿You can fine-tune BERT (or DistilBERT etc) with your own additional training data through transfer learning
      * ﻿﻿Tokenize your own training data to be of the same format
      * ﻿﻿Just start training it further with your data, with a low learning rate.

##### Transfer Learning approaches 
  * ﻿﻿Continue training a pre-trained model (fine-tuning)
    * ﻿﻿Use for fine-tuning a model that has way more training data than you ever have
    * ﻿﻿Use a low learning rate to ensure you are just incrementally improving the model
  * ﻿﻿Add new trainable layers to the top of a frozen model
    * ﻿﻿Learns to turn old features into predictions on new data
    * Can freeze certain layers, re-train others (NN based)
      * Train a new tokenizer to learn a new Fine-tuning NN language per additional training data
    * ﻿﻿Can do both: add new layers, then fine tune as well
  * ﻿﻿Retrain from scratch
    * ﻿﻿If you have a large amount of training data and it's fundamentally different from what the model was pre-trained with
    * ﻿﻿And you have the computing capacity for it!
  * ﻿﻿Use it as-is
    * ﻿﻿When the model's training data is what you want already
  * Adapt it to other tasks (eg: classification, etc.)

