![gla university logo](/logo.png)

# GLA University Mathura, 2019  

## Mini Project Synopsis  

## Face Expression Recognition (FER) 

## Team Members  

1. [Shubham Sinha](https://github.com/shubhamsinha0001) 
2. [Sitanshu Tripathi](https://github.com/sitanshu-cse10) 
3. [Shobhit Dixit](https://github.com/shobhit00dixit)
4. [Vivek Vikram Singh](https://github.com/vivek-777) 


#### REASON FOR SELECTING THE TOPIC

```
Problems faced by any company or institute during conducting their online examination that whether valid candidate or not. 
Our system  will provide them a solution to validate that whether a valid candidate is giving the examination or not, it will authenticate that only valid candidate can give the examination.

Facial expressions and related changes in facial patterns give us information about the emotional state of the person and help to regulate conversations with the person. 
Moreover, these expressions help in understanding the overall mood of the person in a better way.

```

___

#### OBJECTIVES OF THE PROJECT

```
Human Face expression Recognition is one of the most powerful and challenging tasks in social communication. Generally, facial expressions are natural and direct means for human beings to communicate their emotions and intentions. 
Face expressions are the key characteristics of non-verbal communication.

Facial image based mood detection techniques may provide a fast and practical approach for non-invasive mood detection. 
This project is based on Face Expression Recognition (FER) techniques which include the three major stages such as pre-processing, feature extraction and classification. 
The purpose of the project is to develop an intelligent system for facial image based expression classification using neural networks.

Facial expressions and related changes in facial patterns give us information about the emotional state of the person and help to regulate conversations with the person. 
Moreover, these expressions help in understanding the overall mood of the person in a better way.

Our second objective of the project is to provide valid user authentication to an online test conducted by several platforms like AMCAT, CO-CUBES in this we will authenticate that whether the valid candidate is giving the paper or not.


```

___

#### LITERATURE SURVEY / FEASIBILITY STUDY

```
Facial expressions play an important role in human interactions and non-verbal communication. 
Classification of facial expressions could be used as an effective tool in behavioral studies and in medical rehabilitation. Facial expression analysis deals with visually recognizing and analyzing different facial motions and facial feature changes.

Numerous investigators have used neural networks for facial expression classification. 
The performance of a neural network depends on several factors including the initial random weights, the training data, the activation function used, and the structure of the network including the number of hidden layer neurons.

A smile on human face shows their happiness and it expresses an eye with a curved shape. 
The sad expression is the feeling of looseness which is normally expressed as rising skewed eyebrows and frown. The anger on a human face is related to unpleasant and irritating conditions. The expression of anger is expressed with squeezed eyebrows, slender and stretched eyelids. 
The disgust expressions are expressed with pull down eyebrows and creased nose. The surprise or shock expression is expressed when some unpredicted happens. 
This is expressed with eye-widening and mouth gaping and this expression is an easily identified one. The expression of fear is related with surprise expression which is expressed as growing skewed eyebrows.

FER has an important stage is feature extraction and classification. Feature extraction includes two types and they are geometric based and appearance based. 
The classification is also one of the important processes in which the above-mentioned expressions such as smile, sad, anger, disgust, surprise, and fear are categorized. The geometrically based feature extraction comprises eye, mouth, nose, eyebrow, other facial components and the appearance based feature extraction comprises the exact section of the face

Two types of parameters were extracted from the facial image: real-valued and binary. A total of 15 parameters consisting of eight real-valued parameters and seven binary parameters were extracted from each facial image. The real-valued parameters were normalized. Generalized neural networks were trained with all fifteen parameters as inputs. There were seven output nodes corresponding to the five facial expressions (neutral, angry, happy, sad and surprised).

```

___  

#### FUTURE SCOPE

```
Facial expressions are important in facilitating human communication and interactions. Also, they are used as an important tool in behavioral studies and medical rehabilitation. Facial image based mood detection techniques may provide a fast and practical approach for non-invasive mood detection.

Facial classification can be used in future as emotion detector of any meeting or seminar in detecting the impact of speech or meeting on the people through their facial detection, it can be used as recommendation system based on the mood of the person. It can be also used in playing music or suggesting songs to a person based on his mood. The face for real-time applications. FER is used in real-time applications such as driver sate surveillance, medical, robotics interaction, forensic section, detecting deceptions.

Secondly, it can be used as authentication for a valid candidate in any online examination by checking a candidate in a particular instance of time. It will reduce cheating chance in examinations.


```

___  

#### METHODOLOGY

```
Two types of parameters were extracted from the facial image: real-valued and binary. A total of 15 parameters consisting of eight real-valued parameters and seven binary parameters were extracted from each facial image. The real-valued parameters were normalized. Generalized neural networks were trained with all fifteen parameters as inputs. There were seven output nodes corresponding to the five facial expressions (neutral, angry, happy, sad and surprised).

Based on initial testing, the best performing neural networks were recruited to form a generalized committee for expression classification. Due to a number of ambiguous and no-classification cases during the initial testing, specialized neural networks were trained for angry, disgust, fear and sad expression. Then, the best performing neural networks were recruited into a specialized committee to perform specialized classification. A final integrated committee neural network classification system was built utilizing both generalized committee networks and specialized committee networks. Then, the integrated committee neural network classification system was evaluated with an independent expression dataset not used in training or in initial testing. 

A number of parameters, both real-valued and binary, were extracted and analyzed to decide their effectiveness in identifying a certain facial expression. The features which did not provide any effective information of the facial expression portrayed in the image were eliminated and were not used in the final study.

Each network had fifteen input nodes, each corresponding to the fifteen input parameters. Each of these networks had seven output nodes, each corresponding to one of the five expressions (neutral, angry, happy, sad and surprised). Since the normalized input data was in the range of -1 to 1, the "tensing" function was used for the hidden layer neurons. The output of the neural network has to be in the 0 to 1 range. Thus, the "logging" function was used as the transfer function for the output layer neurons. The output of each node was converted to a binary number (either 0 or 1). An output of 0.6 or more was forced to 1 and an output of less than 0.6 was forced to 0. An output of 1 indicated that particular expression was a present output of 0 indicated that particular expression was absent. We have varied the threshold from 0.55 to 0.9 and found that a threshold of 0.6 gave better results.


```

___  

#### HARDWARE & SOFTWARE TO BE USED FOR DEVELOPMENT

```
8GB RAM system or more
Intel Core i5 processor or more
128GB Hard Disk storage or more
A webcam
Python 3.x 
Anaconda (Jupyter Notebook)


```

___  

#### TESTING TECHNOLOGIES TO BE USED  

```
Unit Testing (Selenium)
```

___  

#### WHAT CONTRIBUTION WOULD THE PROJECT MAKE AND WHERE?

```
It will enhance the amcat the way of taking exams. 
```

___
#### CONCLUSION

```
Eight real-valued and five binary parameters were successfully extracted from 97 subjects (467 facial images) for five different expressions (neutral, angry, sad, happy and surprised). An integrated committee neural network system was developed incorporating a generalized neural network committee and a specialized neural network committee.

Several (105) generalized neural networks (with different initial weights, structure, etc.) were trained to classify the image into seven different expressions (neutral, angry, sad, happy and surprised). Similarly, several (20) specialized neural networks were trained to classify the image into four different expressions (angry and sad). All of the networks were tested with initial testing data derived from subjects not used in training. The best performing networks were recruited into a generalized committee and a specialized committee. If the generalized committee gave an ambiguous output or no-classification, then, the data was fed to a specialized committee. The integrated committee system was evaluated with data not used in training or in initial testing.

```

___  
