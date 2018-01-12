## Description

Implementation and output data of "Global-Context Neural Machine Translation through Target-Side Attentive Residual Connections".

This work is based on the dl4mt-tutorial by [Kyunghyun Cho et al.](https://github.com/nyu-dl/dl4mt-tutorial).


## Test files

The output files of the 3 reported systems: baseline NMT (dl4mt-tutorial), average embeddings, and attentive residual connections are included here.
>	- en-zh: unCorpus subset (2000 sentences)
>	- es-en: newstest2013
>	- en-de: newstest2014


## Visualization:

We include visualization of the alignment matrix and the attention over previous words. For this purpose, use the following command:

```sh
python plot.py [source file] [target file] [sentence number]
```
Example:
```sh
python plot.py data/es-en/newstest2013.es data/es-en/attentive_newstest2013.en 1
```


## Reference:

>Miculicich, L., Pappas, N., Ram, D., & Popescu-Belis, A. (2017). Global-Context Neural Machine Translation through Target-Side Attentive Residual Connections. arXiv preprint arXiv:1709.04849.(https://arxiv.org/pdf/1709.04849.pdf)

```
@article{miculicich2017global,
  title={Global-Context Neural Machine Translation through Target-Side Attentive Residual Connections},
  author={Miculicich, Lesly and Pappas, Nikolaos and Ram, Dhananjay and Popescu-Belis, Andrei},
  journal={arXiv preprint arXiv:1709.04849},
  year={2017}
}
```


## Contact:

lmiculicich@idiap.ch
