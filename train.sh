#!/usr/bin/env bash

set -e

help_message="help"
stage=0
nvectors=
epochs=30

. ./parse_options.sh

if [ $# -le 4 ]; then
  echo "Usage: $0 <model_name> <model_version> <vectors_path> <train_dir> <dev_dir> --nvectors [vector_size]"
  echo "E.g.: $0 ca_fasttext_md 1.2.0 cc.ca.300.vec.gz 20000"
  echo "Train a spacy model.";
  exit 1;
fi

model_name=$1
model_version=$2
vectors_path=$3
train_dir=$4
dev_dir=$5

prune_flag=

if [ ! -z "${nvectors}" ]; then
    prune_flag="--prune-vectors $nvectors";
fi

model_path="${model_name}_${model_version}";

if [ $stage -le 0 ]; then
    mkdir -p $model_path/vectors;
    spacy init-model ca $model_path/vectors -v $vectors_path $prune_flag;
fi

if [ $stage -le 1 ]; then
    mkdir -p $model_path/tagger;
    spacy train ca $model_path/tagger -V $model_version -v $model_path/vectors $train_dir/pos.json $dev_dir/pos.json -n $epochs -ne 5 -p 'tagger,parser';
fi

if [ $stage -le 2 ]; then
    rm -rf $model_path/vectors;
    mv $model_path/tagger/model-final $model_path/tagger/final;
    rm -rf $model_path/tagger/model*;
fi

if [ $stage -le 3 ]; then
    mkdir -p $model_path/ner;
    spacy train ca $model_path/ner -V $model_version $train_dir/ner.json $dev_dir/ner.json -b $model_path/tagger/final -n $epochs -ne 5 -p ner -R;
fi