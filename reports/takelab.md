**Takelab**

[Reference Paper](https://www.aclweb.org/anthology/S18-1192/)

```
No Source code was made available from the authors.
```


TakeLab took the 16th place in the Argument Reasoning Comprehension Task with an accuracy of 0.541, which is 0.014 points above the baseline.
Although no source code was provided, we decided to replicate this system given that is was the only one that used a non-neural approach, namely a Support Vector Machine (SVM).
The model was created by converting the data set to a sentence encoded vector using the [Skip-thought vectors](https://arxiv.org/abs/1506.06726) and training a SVM to predict the best warrant.

We implemented the system from scratch given the descriptions provided in the reference paper, including the text normalization and feature extraction functionality.

We faced challenges using the original Skip-thought vectors which are provided by an independent library.
Without knowing the specific version of Python used in the original Skip-thought implementation we tried running the library with several Python versions, however, unsuccessfully.

As a solution we installed a version of [Skip-thought](ttps://pypi.org/project/skipthoughts/) pre-trained models for Pytorch, which uses the original Skip-tough models.
Given that no description was given for the number of words from each sentence that were converted to a vectorized representation, we experimented with the length of the maximum tokens and also with a 20 and 50 units length.

The exact SVM library used was not specified, so we experimented with Weka and the SVM provided in the Scikit-learn package, with the hyper-parameters described in the reference paper.
The data set was normalized as described and the reported complement solution was implemented.  
We also used the uni-skip model and the bi-skip model, totaling a 9,600 unit vector as a feature.

It took one person working around two days to replicate this system.
Since we obtained an accuracy score equal to the one reported on the reference paper, we consider this system to have been successfully replicated.

The **replication source code** can be found at:

* [Skip-though vectors](takelab_vectors/)

* [SVM classifier](takelab_svm.py)

For running the Python (3.5) code the following packages are required:
* `Numpy`
