# Reproduce the Udacity Project on Mac
I want to reproduce the Udacity bahavioral learning project on my Mac. 
Behavioral Cloning Project

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report

Full details of this project can be found here:
https://github.com/papiot/CarND-Behavioral-Cloning

Once you record a few laps of the track, you end up with a folder which contain images take from three different cameras. All of them are on the hood of the car, but one is centered, and the other two are left and right respectivelly.

There is also a CVS file which contains the following data:

|Center Image | Left Image | Right Image | Steering Angle | Throttle | Break | Speed|
|-------------|------------|-------------|---------------:|---------:|------:|-----:|
|IMG/center...|IMG/left... |IMG/right... |0               |0.23434   |   0   |   0  | 
|IMG/center...|IMG/left... |IMG/right... |0.03            |0.23434   |   0   |   0  |

There are about 14 frames per second.

For the first try I will use only center images and see what happens.
