**GIST**

[Reference Paper](https://www.aclweb.org/anthology/S18-1122/)

[Source code](https://github.com/hongking9/SemEval-2018-task12)

The GIST system was the best system on the Argument Reasoning Comprehension Task, with 0.712 accuracy, 0.175 over the baseline.
The reference paper described the development score, the use of a distributed score and the best hyper-parameters.
The system consists of LSTMs neural networks and makes use of transfer learning from the natural language inference corpora SNLI and MultiNLI.

The source code was made available through a public code [repository](https://github.com/hongking9/SemEval-2018-task12).
Although the supporting library requirements were described in the repository, the specific versions of the libraries were not reported.
This made the reproduction difficult, due to conflicts with the Theano GPU library.
which forced us to resort to a CPU-compatible library instead, with which we were able to run the system (though certainly taking much longer than it would have on a GPU).

It took one person less than one working day to reproduce this system.
Running the system with the default 10 epochs took around 64 minutes.

It follows the output obtained from the system:

```
data processing...
build ESIM...
build GIST team system network...
Compile the theano function...
lamda : 0.0005   decay: 0.9   init_lr: 0.0002
init_dev_accuracy :  0.5537974683544303
init_tst_accuracy :  0.49099099099099097
epoch: 1   trn: 0.7099   dev: 0.6804   tst: 0.6509   lr: 0.0002
epoch: 2   trn: 0.7463   dev: 0.6994   tst: 0.6847   lr: 0.00018
epoch: 3   trn: 0.7835   dev: 0.6994   tst: 0.7095   lr: 0.000162
epoch: 4   trn: 0.8132   dev: 0.7025   tst: 0.6959   lr: 0.000146
epoch: 5   trn: 0.8355   dev: 0.7025   tst: 0.7072   lr: 0.000131
epoch: 6   trn: 0.843   dev: 0.7057   tst: 0.7095   lr: 0.000118
epoch: 7   trn: 0.8504   dev: 0.7152   tst: 0.714   lr: 0.000106
epoch: 8   trn: 0.8645   dev: 0.7057   tst: 0.7117   lr: 9.6e-05
epoch: 9   trn: 0.8818   dev: 0.7089   tst: 0.7162   lr: 8.6e-05
epoch: 10   trn: 0.9033   dev: 0.7057   tst: 0.7185   lr: 7.7e-05
time :  64.171 m
```
