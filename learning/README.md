# / learning

Directory for learning. Mostly Jupyter notebooks.

## The (Data) Scientific Process

### 1. Frame Problem

- Here is the data, what can be done?
- Here is the problem, what data is needed to solve?

### 2. Get Raw Data

Consider the relevancy, privacy, security and bias whilst sourcing.

### 3. Pre-Process / Clean Data

1. Remove inconsistencies (`United Kingdom` == `UK`, etc.)
2. Remove duplicates, errors, irrelevants.
3. Address missing data.

    Can invalidate or cause bias:
    
    - Missing completly at random - independent of both observed and unobserved data
    - Missing at random - independent of only observed data
    - Missing not at random - dmissing ata is related to reason it is missing

4. Data wrangling - converting data to a more amenable form (scaling, centering, etc.) (i.e. categorical --> numerical)

### 4. Data Exploration (Exploratory Data Analysis)

- Gain insisght and intuition.
- Explore aspects.

    Measures of central tendency: mean, median, mode
    Measure of variability: variance, standard deviation
    Correlatons: graphs

### 5. Analyse and/or Model

- Build probability model.
- Build model that simulates a process to produce the data.

### 6. Evaluate / Validate Results

- Provide evidence.
Does it fit / predict?
Are they valid and unbiased?

### 7. Use / Communicate Results

- Documentation
- Write for non-technicals
- Share