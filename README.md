# Install img2emoji

#### Membre: Yutong YAN, Sixiang XU, Heng ZHANG

## Introduction

This project aims to **detect objects in an image** and **match detected objects with emojis**.

## Interface

![](doc/img/interface.png) 

## Steps

- Install `PyQt`;
- Modify the `Makefile` file according to your environment.
```
GPU=1		# 0 if your pc doesn't support CUDA
CUDNN=1		# 0 if your pc doesn't support CUDNN
OPENCV=1	# 0 if your pc doesn't support OPENCV
```
- `make` the project;
- Download `yolo.weights` and `tiny-yolo.weights` by running:
```bash
wget https://pjreddie.com/media/files/yolo.weights
wget https://pjreddie.com/media/files/tiny-yolo-voc.weights
```
- If you want to detect one image, run:
```bash
python yolo_detection.py filename
```
for exemple:
```bash
python yolo_detection.py data/dog.jpg
```
- If you want to detect more than one images, run:
```bash
python yolo_detection.py filename1 filename2 filename3 ...
```

## For more information(in french)

- [Cahier de charge](https://github.com/ZHANGHeng19931123/img2emoji/blob/master/doc/Cahier_de_charge.md) 

## Reference

This project is based on [darknet](https://github.com/pjreddie/darknet).