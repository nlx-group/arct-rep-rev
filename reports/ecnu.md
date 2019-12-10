**ECNU**

[Reference Paper](https://www.aclweb.org/anthology/S18-1184.pdf)

[Source code](https://github.com/rgtjf/SemEval2018-Task12)

It was the third-best system on the Argument Reasoning Comprehension Task, with 0.604 accuracy, only 0.002 behind the second-best system.
The system is an ensemble of several neural networks, each encoding information using LSTM and LSTM+CNN.

The reference paper included development score, score distribution and best hyper-parameters.
It included a paper and source code, however there was no helpful documentation provided with the source code. It also had no specified library requirements.

The Python source code uses Tensorflow  and Keras, along with related dependencies such as numpy, but these dependencies, and their precise versions, had to be determined by trial and error as the paper and source code documentation did not specify that information and using the most recent versions yielded errors.
After several version regressions, we settled for a working Tensorflow (1.0.0) and Keras (2.2.4) version.

The Python version was also not reported, thus we used 3.6.9 (the most recent stable version at the time of running our experiment).

The system makes use of the Stanford CoreNLP pipeline to parse its input but, again, the precise version is not specified and had to be determined (version 2015-12-09) through inspection of the source code.
This Stanford CoreNLP version yields an error when used with recent Java JDKs which can only be fixed by running with the flag --add-modules java.xml.bind.

The system relies on pre-trained Word2Vec embeddings, but their source was not described so we assumed them to be the standard GoogleNews pre-trained vectors.

The source code implements several models, but since the documentation does not specify which are used in the ensemble, these had to be determined by inspecting the source code, The models used for the ensemble are intra_attention_ii, intra_attention_cnn and intra_attention_cnn_negclaim.

The code ran with the hyper-parameters described in the paper, for 3 runs. The final reported values were the average of the ensemble of these 3 runs.
The experiments were ran on 2 Intel(R) Xeon(R) Gold 6152 CPU's.

We obtained a score of 0.583, 0.021 points below than that reported in the ARCT.
We hypothesize that the reason for the score difference may lie in the ensemble models criterion.
This criterion was not described in the paper, which could have potentially been an ensemble of the best models in the 3 runs. The criterion chosen for this work was to evaluate the ensemble system at each run and calculate the mean of the accuracy scores across the 3 runs.

We consider the ECNU system hard to reproduce due to the lack of documentation, taking one person roughly two working days to fully reproduce it.
