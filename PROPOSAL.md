# <div align="center">Proposal</div>

## What is the problem that you will be investigating? Why is it interesting?

For our project, we will be collecting our own data, based on the Kaggle dataset found [here](https://www.kaggle.com/alyeasin/predict-pizza-price?select=Pizza-Price.csv). We will be investigating pizza prices in Newark, Elizabeth, and Union, New Jersey and predicting the price of pizza given an input of desired toppings and size.  This project is interesting because of its relevance to the NJIT student body, as most students on campus consider cost when ordering food.

## What reading will you examine to provide context and background?
We will be using [Predicting House Price Using Regression Algorithm for Machine Learning](https://yalantis.com/blog/predictive-algorithm-for-house-price/) and [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) as references to see how machine learning and regression can be used to predict prices. [FOOD PREFERENCES OF COLLEGE STUDENTS AND NUTRITIONAL IMPLICATIONS](https://ift.onlinelibrary.wiley.com/doi/abs/10.1111/j.1365-2621.1970.tb00950.x) will be used to compare how the price of food in general can have an effect on the health and nutrition of students.

## What data will you use? If you are collecting new data, how will you do it?

In order to collect our own data, we will use tools such as Yelp and Google Maps to find information on pizza restaurants in the locations mentioned above. We will use the restaurant website to look up prices or call the restaurant ourselves. We will investigate the cost  of one small cheese pizza, one small pepperoni pizza, and one small "specialty" pizza. A specialty pizza is a pizza with four or more toppings and is associated with the particular restaurant. We will also record the diameter of the pizza, which we will use to help find which pizza is the most cost-efficient. We will repeat this for the other locations as well. 

## What algorithm and how to implement it
As previously stated, we will be using linear regression. There are a multitude of example regression problems, and we will be using those as reference. To fine-tune our model, we will only be feeding data regarding cheese, pepperoni, and specialty pizzas.

## How will we evaluate our results?
To evaluate our resulst we will be checking the accuracy of our model given the data we feed it. To do so, we will find the $r^2$ difference between the actual and predicted value.\
$r^2_{actual} - r^2_{predicted}$
