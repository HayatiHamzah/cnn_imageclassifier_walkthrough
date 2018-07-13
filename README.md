# cnn_imageclassifier_walkthrough

## Overview

A Simple Deep Neural Network to classify images made with Keras. This supports binary and multiclass classification.

## Requirements

  * Keras = 2.x (TensorFlow backend)
  * Numpy = 1.x

## Usage

First, collect training and validation data and deploy it like this(for multiclass classification),
```
./data/
  train/
    Celine/
      Celine1.jpg
      Celine2.jpg
      ...
    Chanel/
      Chanel1.jpg
      Chanel2.jpg
      ...
    Givenchy/
      Givenchy1.jpg
      Givenchy2.jpg
      ...
  validation/
    Celine/
      Celine1.jpg
      Celine2.jpg
      ...
    Chanel/
      Chanel1.jpg
      Chanel2.jpg
      ...
    Givenchy/
      Givenchy1.jpg
      Givenchy2.jpg
      ...
```

and then run train script.

```
python src/train-multiclass.py
```

Train script makes model and weights file to `./output/`.

To test another images, run

```
python src/predict-multiclass.py
```

After training, you'll have tensorboard log in `./tf-log/`
So you can see the result

```
tensorboard --logdir=./tf-log
```
