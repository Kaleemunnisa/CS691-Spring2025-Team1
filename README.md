  
# Sports Analysis 

## Introduction
This project analyzes Tennis players in a video to measure their speed, ball shot speed and number of shots. This project will detect players and the tennis ball using YOLO and also utilizes CNNs to extract court keypoints. This hands on project is perfect for polishing your machine learning, and computer vision skills. 

## Output Videos
Here are a few screenshots from as output video:

![op1](https://github.com/user-attachments/assets/736ba556-28f4-4c5d-9942-b2fac8617b72)
![op3](https://github.com/user-attachments/assets/5e4d5e08-b0a1-4931-8dc9-c0af0bc03664)
![op2](https://github.com/user-attachments/assets/076df51b-8925-4c50-be45-5bebb49f7ebf)

## Models Used
* YOLO v8 for player detection
* Fine Tuned YOLO for tennis ball detection
* Court Key point extraction

* Trained YOLOV5 model: https://drive.google.com/file/d/1UZwiG1jkWgce9lNhxJ2L0NVjX1vGM05U/view?usp=sharing
* Trained tennis court key point model: https://drive.google.com/file/d/1QrTOF1ToQ4plsSZbkBs3zOLkVt3MBlta/view?usp=sharing

## Training
* Tennis ball detector with YOLO: training/tennis_ball_detector_training.ipynb
* Tennis court keypoint with Pytorch: training/tennis_court_keypoints_training.ipynb

## Requirements
* python3.8
* ultralytics
* pytorch
* pandas
* numpy 
* opencv
