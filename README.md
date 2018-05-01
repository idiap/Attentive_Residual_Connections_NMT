## Description

Implementation and output data of "Self-Attentive Residual Decoder for Neural Machine Translation".

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

>Miculicich, L., Pappas, N., Ram, D., & Popescu-Belis, A. (2018). [Self-Attentive Residual Decoder for Neural Machine Translation](http://publications.idiap.ch/downloads/papers/2018/MiculicichWerlen_NAACL_2018.pdf). NAACL-HLT 2018

```
@inproceedings{werlenself,
  title={Self-Attentive Residual Decoder for Neural Machine Translation},
  author={Werlen, Lesly Miculicich and Pappas, Nikolaos and Ram, Dhananjay and Popescu-Belis, Andrei}
  booktitle={Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics}
  year={2018}
}
```


## Contact:

lmiculicich@idiap.ch
