**BLCU_NLP**

[Reference Paper](https://www.aclweb.org/anthology/S18-1186/)

[Source code](https://github.com/blcunlp/SemEval2018--argument_reasoning_comprehension)

The BLCU_NLP system was the second-best system on the Argument Reasoning Comprehension Task, with 0.606 accuracy, 0.106 points below the first system.
The reference paper reported the development score, the score distribution and the best hyper-parameters.
The system is an ensemble of ESIM models, which are enhanced LSTM networks that incorporate syntactic information.
Source code was made available through a public code [repository](https://github.com/blcunlp/SemEval2018--argument_reasoning_comprehension).
Although the source code contained a minor problem in its instructions (pointing to a different script for execution) no other problems occur regarding running the source code.

The reference paper mentions the use of the best five models for an ensemble majority vote, however, it does not mention the total number of models from which the five best models were selected.
We decided to run the system ten times and choose the best five models to reproduce the ensemble.

It took one person less than one working day to reproduce this system.
Obtaining ten models took less than two hours.

We obtained a score of 0.642, 0.036 points higher than that reported in the Argument Reasoning Comprehension Task.
We hypothesize that the number of total models, from which the best five models were selected, is the reason for the difference from the original score and the one we obtained.
A possibility is that the authors picked five models from a larger set than ours and the models had higher overfitting to the development set than ours.
Some details were missing from the reference paper but that did not prevent us from reproducing the system using the provided source code.
As such, we consider the BLCU_NLP system to be reproducible.

It follows the development scores for the ten models obtained:
```
----model 0
dev_acc = 0.6677215189873418 (selected for ensemble)
----model 1
dev_acc = 0.6613924050632911
----model 2
dev_acc = 0.6867088607594937 (selected for ensemble)
----model 3
dev_acc = 0.6518987341772152
----model 4
dev_acc = 0.6392405063291139
----model 5
dev_acc = 0.6487341772151899
----model 6
dev_acc = 0.6772151898734177 (selected for ensemble)
----model 7
dev_acc = 0.6708860759493671 (selected for ensemble)
----model 8
dev_acc = 0.6993670886075949 (selected for ensemble)
----model 9
dev_acc = 0.6455696202531646
```
The resulting test answers for the selected models for the ensemble are available at:

[model 0](test_answer_0)

[model 2](test_answer_2)

[model 6](test_answer_6)

[model 7](test_answer_7)

[model 8](test_answer_8)

