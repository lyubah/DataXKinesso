# DataXKinesso

Welcome to the KinessoX Github. 

# About: 
Systemic bias is present in marketing audience-building. Companies seek to be socially conscious in their marketing and advertising efforts; however, they are unaware of implicit biases in the process of building target audiences. In partnership with Kinesso, a marketing intelligence agency, our team of Data Science Students have created a tool that seeks to shed light on those biases and hopefully help companies realize the vast and unrealized benefits of diverse audiences. 

In this repository, you'll find documentation of our workflow (such as EDA), details about the tool, demo of interface, and codes for reproducability. 

All of our EDA and primary visualizations were done in IPython Notebooks. There is a description of each notebook below. The final deliverable of our tool is in a Streamlit app and method file which contains all code used in our process. 

# Statistical Computation Methods
## Chi_square_exploration_V2_draft.ipynb
- Exploration of data using the chi squared metric
- Exploration of different chi squared methods and formats to determine the best one for our product


## Correlation_matrix_V2.ipynb
- The code for our V2 Demo
- EDA
- Methods for binning data and one hot encoding data
- Methods to create a correlation matrix out of clean data

#  EDA: 
## EDA_basic_bar_graphs_cleaning_for_V1_Demo.ipynb
- EDA in preperation for V1 Demo
- Creation of several bar charts and other graphs, which were refined and used in the V1 demo

## EDA_Cond_Entropy_draft_V1_Demo.ipynb

- Exploration of conditional entropy within data
- Refinement of contitional entropy methods for use in V1 Demo
## V1_Demo.ipynb

- Code and write up used in V1 Demp
- Contains discussion and exploration of persona

# Vizualizations and UI: 

## Generate_Bar_Charts.ipynb

- Methond generates set of bar charts displaying change in chosen demographic after slicing dataset
- Also displays chi squared statistic with each graph
- Bar charts and contitional entropy help audience get familiar with data

## bar.py:
Interactive UI that allows user to select column and value to filter by, generating bar charts and chi square values 
for comparison. requires Audience_DE.csv as demo data, but is flexible to other 
data files with minor changes to code. (i.e. changing name of data imported at the beginning of script).

# Code for reproducibility : 
##  **methods.py.zip**
### Contains all codes nessesary for integrating vizualizations into company's current, audience building application. 

This includes codes for: 
- cleaning
- processing 
- statistical computations 
- visualizations









