**NLITrans**

[Reference Paper](https://www.aclweb.org/anthology/S18-1185.pdf)

[Source Code](https://github.com/IKMLab/arct)

It was the fourth-best system on the Argument Reasoning Comprehension Task, with 0.590 accuracy, 0.014 points behind the third-best system.

Its reference paper has one of the most extensive descriptions of reproduction details.
It reports a score distribution, the search method, bounds and best settings for the hyper-parameters.

The system uses a neural network enhanced with transfer learning using the MultiNLI natural language inference data set.
The authors made available a reproduction script with a list of experimented models.

Nevertheless, the system submitted to the ARCT was not available given its large size, namely the 2048 dimensional encoder model used for weight initialization (transfer), which was too large for the GitHub repository.

The best available pre-trained models were 512-sized (encoder) models, which the authors referred to as t512fwcomp.
This is thus the model that we used for reproduction.

We could not resolve some packages libraries versions, namely torch and hsdbi.
Several packages were also required but were not reported, so the version of these was a guess.

The Python version was not documented in the paper or in the source code, so we used Python 3.6.9.
The PyTorch version used was 0.3.0.post4, as reported in the available documentation. Download for this PyTorch version is available [here](https://download.pytorch.org/whl/cu75/torch-0.3.0.post4-cp36-cp36m-linux_x86_64.whl).

Inside the file environment.yml, a list of required packages and their respective versions were declared, which we installed, however, some needed packages were not included.

A dockerized version of MongoDB was used to store experiment results, as required by the program.
The version used was bitnami/mongodb:4.2-debian-9.

The experiments were run on a GeForce GTX 1080 Ti.

The pre-trained embeddings used were 840B.300d Glove embeddings, all other hyper-parameters were kept as default, with a new seed being produced each run.
The reproduction script required a spacy English model to be loaded, which we did not have and the script did not do so.
The solution was to run ``python3 -m spacy download en``.
The reproduction script also required additional packages, namely pandas and scipy, which were not included in the environment.yml file.

As per the paper, the reported accuracy value is an average of 200 runs.
We obtained a score of 0.623, 0.033 points above that reported in the ARCT.
We hypothesize that the reason for this difference in scores is due to the fact that we did not have access to the NLI Model with a 2048 dimensional encoder size, used in the competition submission as an initialization model (Transfer). Having resorted to the available 512 dimension model, this could be the cause for the difference in scores reported in this work.
It took one person two working days to reproduce this system.

It follows the development scores for the 200 runs:

```
Model 1 - Best tuning accuracy: 0.6583
Model 2 - Best tuning accuracy: 0.6760
Model 3 - Best tuning accuracy: 0.6792
Model 4 - Best tuning accuracy: 0.6854
Model 5 - Best tuning accuracy: 0.6948
Model 6 - Best tuning accuracy: 0.6792
Model 7 - Best tuning accuracy: 0.6542
Model 8 - Best tuning accuracy: 0.6885
Model 9 - Best tuning accuracy: 0.6760
Model 10 - Best tuning accuracy: 0.6781
Model 11 - Best tuning accuracy: 0.6979
Model 12 - Best tuning accuracy: 0.6885
Model 13 - Best tuning accuracy: 0.6792
Model 14 - Best tuning accuracy: 0.6917
Model 15 - Best tuning accuracy: 0.6823
Model 16 - Best tuning accuracy: 0.6698
Model 17 - Best tuning accuracy: 0.6792
Model 18 - Best tuning accuracy: 0.6854
Model 19 - Best tuning accuracy: 0.6719
Model 20 - Best tuning accuracy: 0.6833
Model 21 - Best tuning accuracy: 0.6948
Model 22 - Best tuning accuracy: 0.6792
Model 23 - Best tuning accuracy: 0.6792
Model 24 - Best tuning accuracy: 0.6979
Model 25 - Best tuning accuracy: 0.6760
Model 26 - Best tuning accuracy: 0.6615
Model 27 - Best tuning accuracy: 0.6823
Model 28 - Best tuning accuracy: 0.6719
Model 29 - Best tuning accuracy: 0.6667
Model 30 - Best tuning accuracy: 0.6656
Model 31 - Best tuning accuracy: 0.6667
Model 32 - Best tuning accuracy: 0.6687
Model 33 - Best tuning accuracy: 0.6948
Model 34 - Best tuning accuracy: 0.6698
Model 35 - Best tuning accuracy: 0.6948
Model 36 - Best tuning accuracy: 0.6698
Model 37 - Best tuning accuracy: 0.6792
Model 38 - Best tuning accuracy: 0.6948
Model 39 - Best tuning accuracy: 0.6667
Model 40 - Best tuning accuracy: 0.6698
Model 41 - Best tuning accuracy: 0.6823
Model 42 - Best tuning accuracy: 0.6885
Model 43 - Best tuning accuracy: 0.6885
Model 44 - Best tuning accuracy: 0.6729
Model 45 - Best tuning accuracy: 0.6854
Model 46 - Best tuning accuracy: 0.6792
Model 47 - Best tuning accuracy: 0.6719
Model 48 - Best tuning accuracy: 0.6823
Model 49 - Best tuning accuracy: 0.6792
Model 50 - Best tuning accuracy: 0.6833
Model 51 - Best tuning accuracy: 0.6760
Model 52 - Best tuning accuracy: 0.6844
Model 53 - Best tuning accuracy: 0.6823
Model 54 - Best tuning accuracy: 0.6885
Model 55 - Best tuning accuracy: 0.6635
Model 56 - Best tuning accuracy: 0.6760
Model 57 - Best tuning accuracy: 0.6823
Model 58 - Best tuning accuracy: 0.6792
Model 59 - Best tuning accuracy: 0.6854
Model 60 - Best tuning accuracy: 0.6656
Model 61 - Best tuning accuracy: 0.6698
Model 62 - Best tuning accuracy: 0.6781
Model 63 - Best tuning accuracy: 0.6792
Model 64 - Best tuning accuracy: 0.6813
Model 65 - Best tuning accuracy: 0.6875
Model 66 - Best tuning accuracy: 0.6760
Model 67 - Best tuning accuracy: 0.6937
Model 68 - Best tuning accuracy: 0.6719
Model 69 - Best tuning accuracy: 0.6687
Model 70 - Best tuning accuracy: 0.6917
Model 71 - Best tuning accuracy: 0.6979
Model 72 - Best tuning accuracy: 0.6823
Model 73 - Best tuning accuracy: 0.6917
Model 74 - Best tuning accuracy: 0.6917
Model 75 - Best tuning accuracy: 0.6542
Model 76 - Best tuning accuracy: 0.6823
Model 77 - Best tuning accuracy: 0.6667
Model 78 - Best tuning accuracy: 0.6792
Model 79 - Best tuning accuracy: 0.6917
Model 80 - Best tuning accuracy: 0.6729
Model 81 - Best tuning accuracy: 0.6979
Model 82 - Best tuning accuracy: 0.6698
Model 83 - Best tuning accuracy: 0.6823
Model 84 - Best tuning accuracy: 0.6885
Model 85 - Best tuning accuracy: 0.6854
Model 86 - Best tuning accuracy: 0.6823
Model 87 - Best tuning accuracy: 0.6781
Model 88 - Best tuning accuracy: 0.6760
Model 89 - Best tuning accuracy: 0.6792
Model 90 - Best tuning accuracy: 0.6885
Model 91 - Best tuning accuracy: 0.6729
Model 92 - Best tuning accuracy: 0.6729
Model 93 - Best tuning accuracy: 0.6823
Model 94 - Best tuning accuracy: 0.6760
Model 95 - Best tuning accuracy: 0.6625
Model 96 - Best tuning accuracy: 0.6698
Model 97 - Best tuning accuracy: 0.6594
Model 98 - Best tuning accuracy: 0.6885
Model 99 - Best tuning accuracy: 0.6792
Model 100 - Best tuning accuracy: 0.6594
Model 101 - Best tuning accuracy: 0.6760
Model 102 - Best tuning accuracy: 0.6729
Model 103 - Best tuning accuracy: 0.6781
Model 104 - Best tuning accuracy: 0.6656
Model 105 - Best tuning accuracy: 0.6698
Model 106 - Best tuning accuracy: 0.6719
Model 107 - Best tuning accuracy: 0.6698
Model 108 - Best tuning accuracy: 0.6823
Model 109 - Best tuning accuracy: 0.6823
Model 110 - Best tuning accuracy: 0.6885
Model 111 - Best tuning accuracy: 0.6760
Model 112 - Best tuning accuracy: 0.6813
Model 113 - Best tuning accuracy: 0.6729
Model 114 - Best tuning accuracy: 0.6719
Model 115 - Best tuning accuracy: 0.6604
Model 116 - Best tuning accuracy: 0.6698
Model 117 - Best tuning accuracy: 0.6781
Model 118 - Best tuning accuracy: 0.6865
Model 119 - Best tuning accuracy: 0.6823
Model 120 - Best tuning accuracy: 0.6729
Model 121 - Best tuning accuracy: 0.6885
Model 122 - Best tuning accuracy: 0.6823
Model 123 - Best tuning accuracy: 0.6823
Model 124 - Best tuning accuracy: 0.6917
Model 125 - Best tuning accuracy: 0.6813
Model 126 - Best tuning accuracy: 0.6854
Model 127 - Best tuning accuracy: 0.6771
Model 128 - Best tuning accuracy: 0.6917
Model 129 - Best tuning accuracy: 0.6948
Model 130 - Best tuning accuracy: 0.6792
Model 131 - Best tuning accuracy: 0.6667
Model 132 - Best tuning accuracy: 0.6875
Model 133 - Best tuning accuracy: 0.7198
Model 134 - Best tuning accuracy: 0.6917
Model 135 - Best tuning accuracy: 0.6604
Model 136 - Best tuning accuracy: 0.6667
Model 137 - Best tuning accuracy: 0.6854
Model 138 - Best tuning accuracy: 0.6760
Model 139 - Best tuning accuracy: 0.6760
Model 140 - Best tuning accuracy: 0.6875
Model 141 - Best tuning accuracy: 0.6906
Model 142 - Best tuning accuracy: 0.6656
Model 143 - Best tuning accuracy: 0.6813
Model 144 - Best tuning accuracy: 0.6813
Model 145 - Best tuning accuracy: 0.6854
Model 146 - Best tuning accuracy: 0.6969
Model 147 - Best tuning accuracy: 0.6760
Model 148 - Best tuning accuracy: 0.6792
Model 149 - Best tuning accuracy: 0.6885
Model 150 - Best tuning accuracy: 0.6729
Model 151 - Best tuning accuracy: 0.6771
Model 152 - Best tuning accuracy: 0.6760
Model 153 - Best tuning accuracy: 0.6687
Model 154 - Best tuning accuracy: 0.6760
Model 155 - Best tuning accuracy: 0.6760
Model 156 - Best tuning accuracy: 0.6542
Model 157 - Best tuning accuracy: 0.6802
Model 158 - Best tuning accuracy: 0.6979
Model 159 - Best tuning accuracy: 0.6792
Model 160 - Best tuning accuracy: 0.6917
Model 161 - Best tuning accuracy: 0.6781
Model 162 - Best tuning accuracy: 0.6802
Model 163 - Best tuning accuracy: 0.6875
Model 164 - Best tuning accuracy: 0.6813
Model 165 - Best tuning accuracy: 0.6823
Model 166 - Best tuning accuracy: 0.6833
Model 167 - Best tuning accuracy: 0.6729
Model 168 - Best tuning accuracy: 0.6760
Model 169 - Best tuning accuracy: 0.6792
Model 170 - Best tuning accuracy: 0.6927
Model 171 - Best tuning accuracy: 0.6719
Model 172 - Best tuning accuracy: 0.6917
Model 173 - Best tuning accuracy: 0.6917
Model 174 - Best tuning accuracy: 0.6792
Model 175 - Best tuning accuracy: 0.6906
Model 176 - Best tuning accuracy: 0.6594
Model 177 - Best tuning accuracy: 0.6729
Model 178 - Best tuning accuracy: 0.6854
Model 179 - Best tuning accuracy: 0.6781
Model 180 - Best tuning accuracy: 0.6792
Model 181 - Best tuning accuracy: 0.6792
Model 182 - Best tuning accuracy: 0.6760
Model 183 - Best tuning accuracy: 0.6823
Model 184 - Best tuning accuracy: 0.6625
Model 185 - Best tuning accuracy: 0.6823
Model 186 - Best tuning accuracy: 0.6698
Model 187 - Best tuning accuracy: 0.6594
Model 188 - Best tuning accuracy: 0.6729
Model 189 - Best tuning accuracy: 0.6854
Model 190 - Best tuning accuracy: 0.6781
Model 191 - Best tuning accuracy: 0.6792
Model 192 - Best tuning accuracy: 0.6792
Model 193 - Best tuning accuracy: 0.6760
Model 194 - Best tuning accuracy: 0.6823
Model 195 - Best tuning accuracy: 0.6625
Model 196 - Best tuning accuracy: 0.6823
Model 197 - Best tuning accuracy: 0.6698
Model 198 - Best tuning accuracy: 0.6594
Model 199 - Best tuning accuracy: 0.6729
Model 200 - Best tuning accuracy: 0.6854
```
