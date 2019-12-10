**SNU_IDS**

[Reference Paper](https://www.aclweb.org/anthology/S18-1182.pdf)

[Source code](https://github.com/galsang/SemEval2018-task12)

It took the 12th position on the Argument Reasoning Comprehension Task with an accuracy of 0.565, which is 0.038 points above the baseline.

The reference paper included development score, score distribution and best hyper-parameters.

The system uses a neural network with GloVe word embeddings and a CoVe sentence encoder and feed-forward layers.
We encountered problems with PyTorch versioning, as we did with the NLITrans system reproduction.

The experiments were run on a Dell R740 Server with 2 Xeon Gold 6152 CPUs and 256Gb of RAM.

We used Python 3.6.2 to run the experiments, as reported in the paper.
[PyTorch version 0.3.0.post4](https://download.pytorch.org/whl/cu75/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl) was used, along with the necessary packages and respective versions provided in the requirements.txt file.

We encountered problems in downloading a required torch pre-trained model, where it raised a Runtime error due to hash value.
The solution was to simply run a wget to fetch the model from the url https://s3.amazonaws.com/research.metamind.io/cove/wmtlstm-b142a7f2.pth, saving it to the correct folder.

We ran the SECOVARC-last (w/ heuristics) model, which is the model submitted to the competition, with 840B.300d Glove pre-trained embeddings and all other hyper-parameters were kept as default.

The final reported accuracy values are an average of 20 runs.
It took one person one working day to reproduce this system.
