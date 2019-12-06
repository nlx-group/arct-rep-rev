**GIST** (TODO)

[Reference Paper](https://www.aclweb.org/anthology/S18-1122/)


The GIST system was the best system on the Argument Reasoning Comprehension Task, with 0.712 accuracy, 0.175 over the baseline.
The reference paper described the development score, the use of a distributed score and the best hyper-parameters.
The system consists of LSTMs neural networks and makes use of transfer learning from the natural language inference corpora SNLI \cite{snli:emnlp2015} and MultiNLI \cite{N18-1101}.
The source code was made available through a public code repository (GitHub).
Although the supporting library requirements were described in the repository, the specific versions of the libraries were not reported.
This made the reproduction difficult, due to conflicts with the Theano GPU library \cite{2016arXiv160502688short} 
%\footnote{Theano is a Python library to define, optimize, and evaluate mathematical expressions involving multi-dimensional arrays efficiently.}  
which forced us to resort to a CPU-compatible library instead, with which we were able to run the system (though certainly taking much longer than it would have on a GPU).
It took one person less than one working day to reproduce this system.
Running the system with the default 10 epochs took around 64 minutes.
