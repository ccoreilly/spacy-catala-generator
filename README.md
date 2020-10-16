# Training script and dataset for [spacy-catala](https://github.com/ccoreilly/spacy-catala)

> Note: this repository uses Git LFS for the files under train directory

```
$ ./train.sh
Usage: train.sh <model_name> <model_version> <vectors_path> <train_dir> <dev_dir> --nvectors [vector_size]
E.g.: train.sh ca_fasttext_md 1.2.0 cc.ca.300.vec.gz train dev --nvectors 50000
Train a spacy model.
```

`vectors_path` expects gzipped text vectors. These are not included, you can download them with:

```
$ curl -x -o cc.ca.300.vec.gz https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ca.300.vec.gz
```

In order to recreate the large model in [spacy-catala](https://github.com/ccoreilly/spacy-catala) run:

```
$ ./train.sh ca_fasttext_wiki_lg 1.0.0 cc.ca.300.vec.gz train dev
```

The medium sized model has been pruned to the most common 20000 vectors using:

```
$ ./train.sh ca_fasttext_wiki_md 1.0.0 cc.ca.300.vec.gz train dev --nvectors 20000
```
