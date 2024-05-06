
<!-- README.md is generated from README.Rmd. Please edit that file -->

# Data Poisoning Project

## By: Caitlyn Crow and Saul Varshavsky






<!-- badges: start -->
<!-- badges: end -->

### Sources Used for Assistance:

https://youtu.be/1ILVm4IeNY8?si=6o8lhKgUquMHfECH

https://github.com/AIAnytime/Training-Small-Language-Model/blob/main/Training_a_Small_Language_Model.ipynb

https://youtu.be/5L6h_MrNvsk?si=4uDbgWpGHCEpTEEG

https://youtu.be/y62Dvo2Ml7o?si=_T4yD_ihGXFhokYS

https://getbootstrap.com/docs/5.3/getting-started/introduction/

https://www.geeksforgeeks.org/navigation-bars-in-flask/


### Objective

This project aimed to gain an in-depth understanding of data poisoning. With that understanding, we then investigated ways in which various data poisoning attacks can be used to attack Natural Language Processing (NLP) models, thereby revealing their vulnerabilities along the way.


### Motivation

Data poisoning is a huge issue for LLM models and machine learning models in general nowadays. A data poisoning attack in an LLM model can lead to serious problems, such as misinformation, bias, and the spread of hateful behaviors. These serious problems can be devastating to social dynamics and can lead to division in society. Considering that data poisoning is a serious issue that needs to be addressed, this project serves as a gateway towards dealing with and diagonosing this issue.


### Code Used

First, we created a website that is designed to present and educate others about data poisoning as well as what solutions may be implemented to help address
data poisoning. The code pertaining to the website can be found inside the folder titled "web-design-code".

Then, we implemented a series of data poisoning attacks on a couple of NLP models, in order to help diagnose how data poisoning can penetrate a model. The code pertaining to implementing
data poisoning attacks can be found inside the folder titled "data-poisoning-code".


### Requirements to Use the Web Design Code

1. pip install flask


### Requirements to Use the Data Poisoning Code

1. pip install datasets
2. pip install transformers
3. pip install torch
4. pip install torchtext
5. pip install sentencepiece
6. pip install pandas
7. pip install tqdm



### Data Used

Here are the links to the datasets we used for the Data Poisoning Code:

1. Disease Symptoms (https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms)
2. News Classification (https://huggingface.co/datasets/janani4office2/connl_rlhf)
