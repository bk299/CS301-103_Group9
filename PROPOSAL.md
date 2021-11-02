# <div align="center">Proposal</div>

## What is the problem that you will be investigating? Why is it interesting?

GeoGuessr is a web-based geographic discovery game. In this game, you are put somewhere in the world with Google Maps coverage, usually using Google Street View, and you have to figure out where in the world you are. In normal modes, the player can move around in the Google Street View and look for clues to help them figure out where they are, including architecture, language, or distinct geographical features of an area. Some people have gotten really good at the game and can pinpoint nearly exactly where they are in the world based on a static image with no moving, panning, or zooming (commonly called NMPZ).
What we plan to do is use Machine Learning to try to pinpoint the country which we are in just by feeding our algorithm a picture of wherever the game drops us in the Google Street View. This is interesting because, for the average player, it may be almost impossible to figure out which country you are in just by looking at a single picture. And our goal with this project is to end up with a product that gets trained well into guessing the correct country that the image was actually taken in.

## What reading will you examine to provide context and background?

One reading we will be using is [Google's ML Practicum for Image Classification](https://developers.google.com/machine-learning/practica/image-classification). This reading will give us a better background in image classification. Another link that may be useful is [Kaggle's Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning). This will be useful to us in order to get a solid introduction to machine learning. We are also looking into how machine learning has been used to identify other images, for example, in CAPTCHA and RECAPTCHA software, explaned in this article, [Why CAPTCHAs have gotten so difficult](https://www.theverge.com/2019/2/1/18205610/google-captcha-ai-robot-human-difficult-artificial-intelligence) from The Verge. This will give us insight into how image recognition is already being used and allow us to robustify our algorithm.

## What data will you use? If you are collecting new data, how will you do it?

The data we will use is going to be sampled from GeoGuessr. We will feed our algorithm with several pictures from each country in the game, and those will all be from spots where Google Street View is available.

## What algorithm and how to implement it

We are going to be using some sort of image classification algorithm for our project. While we are not certain yet, we may use a convolutional neural network (CNN) for this project, as that is what seems to be a popular way to implement image classification. A CNN takes an image's raw pixel data as input and "learns" how to extract features based on them, so that seems like a good tool to use for our project.

## How will we evaluate our results?

Luckily, there will always be a ground truth for our project: the actual location we are placed in GeoGuessr. We will evaluate our results by playing GeoGuessr and seeing how accurate our finished product is in guessing where we are in the world, perhaps based on the difference between the predicted location compared to the actual location.
