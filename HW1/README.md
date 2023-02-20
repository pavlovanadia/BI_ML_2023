## KNN method ##

#### K-neariest neighbours method implementation ####

You can find all files of interest in the *code* directory. It contains files: *KNN.ipynb*, *knn.py*, *metrics.py*.

*KNN.ipynb* is a notebook with KNN classification of clothes dataset (binary and multiclass) and KNN regression of the diabetes dataset. The notebook mostly focuses on choosing the best neighbour number for each task.

**knn.py** contains a class KNNClassifier where the following methods are realised:

- **fit** - for model fitting on train features and target

- **predict** - predicting target

- **compute_distances_two_loops** - computes L1 distance from every sample of X to every training sample; uses simplest implementation with 2 Python loops

- **compute_distances_one_loop** - Computes L1 distance from every sample of X to every training sample vectorizes some of the calculations, so only 1 loop is used

- **compute_distances_no_loops** - computes L1 distance from every sample of X to every training sample fully vectorizes the calculations using numpy

- **predict_labels_binary** - returns model predictions for binary classification case

- **predict_labels_multiclass** - returns model predictions for multi-class classification case

**metrics.py** contains several functions with metrics for evaluating predictions quality:

- **binary_classification_metrics** - computes metrics for binary classification

- **multiclass_accuracy** - computes metrics for multiclass classification

- **r_squared** - computes r-squared for regression

- **mse** - computes mean squared error

- **mae** - computes mean absolute error

### Running the code on your mahine locally ###

**This code was performed with VSCode using Python 3.9.12 on Ubuntu 22.04.1 LTS**

For the best performance I reccommend you installing requirements.txt to avoid the packages version conflict.

- clone the repository to your local machine with

`git clone git@github.com:pavlovanadia/BI_ML_2023.git`

- checkout to the homework_1 branch with

`git checkout homework_1`

- create and activate the virtual environment with

`python3 -m venv environment`

`source environment/bin/activate`

- (if using VSCode) upload kernel to your virtual environment with

`pip3 install ipykernel`

`python3 -m ipykernel install --user --name=projectname`

 then reload VSCode

- upload requirements.txt with

`pip install -r requirements.txt`