# / sandbox

## The (Data) Scientific Method
### 0. Framing the Problem

 - Here is the data, what can be done?
 - Here is the problem, what data is needed to solve?

### 1. Data Wrangling

 - Accquistion
    - Must consider elevancy, privacy, security and bias of data, whilst sourcing.
 - Formatting, etc.

## An Artificial Intelligence Model
### 2. Data <u>Pre-Processing</u>

 Preperation of the data for use in the model.

#### <u>Handling Bias</u>

 ##### 1. Oversampling the Minority Class

 - Cloning data (weighting)
 - Synthetic data generation
    - Synthetic Minority Over-sampling TEchnique (SMOTE)

 ##### 2. Undersampling the Majority Class

#### <u>Tokenisation</u>
 Preperation of input data, by:
 1. Breaking down of data into chunks.
 2. Numericalising the chunks to integers (e.g. `a` --> `1`, `b` --> `2`). These values will later be used for indexing.

 ##### 1. Basic Character Tokenisation
  For a string text input, create a set of all occuring characters (the vocabularly). For the input data, convert each character to its index in the vocabulary.

 ##### 2. Basic Word Toeknisation
  Same as above, but on a word-by-word basis, instead of characters.

#### <u>Vectorisation</u>
 Conversion of the input dataset (text, images, etc.) into a matrix of numerical values, using some method or metric. This matrix can be processed by the model.

 ##### 1. Bag of Words

  Count the number of occurences of each entity (word, character, bigram, etc.), and use these frequencies to determine a probability table.

  Can be used to determine the classification of data based off of the presence of the input.

 ##### 2. TF-IDF

 ##### 3. Word Embeddings

 ##### 4. Document Embeddings

 ##### 5. One-Hot Encoding

### 3. The Algorithm (<u>Processing</u>)
 Calculation of output

#### <u>Classification</u>

 ##### 1. Naive Bayes
  Calculates the probability of a data point belonging to each possible class based on the features it has, assuming that these features are independent of each other, and then assigns the data point to the class with the highest probability.

  Uses Bayes' theorem.

 ##### 2. Nearest Neighbour (k-NN)

#### <u>TODO</u>

 ##### 3. Decision Trees

 ##### 4. Random Forests

 ##### 5. Gradient Boosted Trees

 ##### 6. Gradient Boosted Machines

### 4. <u>Post-Processing</u>

Interpretation

Evaluate the performance of the model using a metric:
- Precision-Recall AUC
- Balanced Accuracy
- Matthew Correlation Coefficient
