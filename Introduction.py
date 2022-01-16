# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 17:01:08 2022

@author: Venkatesan
"""
from PIL import Image
import os



def app():
    absFilePath = os.path.abspath(__file__)                # Absolute Path of the module
    st.write(absFilePath)
    import streamlit as st
    pweb = """<a href='https://www.youtube.com/channel/UCespXFy72CY6ok9l4V6WJcw' target="_blank">https://www.youtube.com/channel/UCespXFy72CY6ok9l4V6WJcw</a>"""
    sm_li = """<a href='https://www.linkedin.com/in/andymcdonaldgeo/' target="_blank"><img src='https://cdn.exclaimer.com/Handbook%20Images/linkedin-icon_32x32.png'></a>"""
    sm_tw = """<a href='https://twitter.com/geoandymcd' target="_blank"><img src='https://cdn.exclaimer.com/Handbook%20Images/twitter-icon_32x32.png'></a>"""
    sm_med = """<a href='https://medium.com/@andymcdonaldgeo/' target="_blank"><img src='https://cdn.exclaimer.com/Handbook%20Images/Medium_32.png'></a>"""
    
    st.title('Artificial Intelligence - Toolkit')
    # st.write('## Welcome to the LAS Data Explorer')
    st.write('### Created by Venkatesan Paramasivam')
    st.write(''' About 7 years of working experience as a Software Developer in Aritificial Intelligence and Python Development for various projects 
Performed Data Analysis and built Prediction Models using Supervised Machine Learning Algorithms
Have experience in R Programming and built Predictive Models using Linear & Logistic Regression, Random Forest, SVM, Naïve Bayes etc.
Self-learnt Python Programming and Machine Learning packages scikit Learn, NLTK, pandas, NumPy etc.
Have experience in Text Mining and Sentiment Analysis using NLTK package in Python
Have used Visualization packages in R for visualizing and trends
Have good knowledge on Statistics, Predictive Modelling and Data Mining Techniques using R and Python
Good understanding in Image Processing 
Strong technical experience in OCR
Quick learner, Flexible, Ability to understand concepts quickly, Eager to learn new things
''')
    st.write('\n')
    st.write('## Get in Touch')
    st.write(f'\nIf you want to get in touch, you can find me on Social Media at the links below or visit my website at: {pweb}.', unsafe_allow_html=True)
    
    st.write('## AI')
    st.write("""
             The Artificial Intelligence tutorial provides an introduction to AI which will help you to understand the concepts behind Artificial Intelligence. In this tutorial, we have also discussed various popular topics such as History of AI, applications of AI, deep learning, machine learning, natural language processing, Reinforcement learning, Q-learning, Intelligent agents, Various search algorithms, etc.

Our AI tutorial is prepared from an elementary level so you can easily understand the complete tutorial from basic concepts to the high-level concepts.""")
    image = Image.open('Images/AI.jpg')

    st.image(image, caption='What is AI')
    
    st.write('''**Machine Learning:** Machine Learning tutorial provides basic and advanced concepts of machine learning. Our machine learning tutorial is designed for students and working professionals.

Machine learning is a growing technology which enables computers to learn automatically from past data. Machine learning uses various algorithms for building mathematical models and making predictions using historical data or information. Currently, it is being used for various tasks such as image recognition, speech recognition, email filtering, Facebook auto-tagging, recommender system, and many more.

This machine learning tutorial gives you an introduction to machine learning along with the wide range of machine learning techniques such as Supervised, Unsupervised, and Reinforcement learning. You will learn about regression and classification models, clustering methods, hidden Markov models, and various sequential models.

What is Machine Learning
In the real world, we are surrounded by humans who can learn everything from their experiences with their learning capability, and we have computers or machines which work on our instructions. But can a machine also learn from experiences or past data like a human does? So here comes the role of Machine Learning.''')
    image = Image.open(r'Images/ML.jpg')
    st.image(image, caption='Machine Learning')
    st.write('''**Natural Language Processing:** NLP stands for Natural Language Processing, which is a part of Computer Science, Human language, and Artificial Intelligence. It is the technology that is used by machines to understand, analyse, manipulate, and interpret human's languages. It helps developers to organize knowledge for performing tasks such as translation, automatic summarization, Named Entity Recognition (NER), speech recognition, relationship extraction, and topic segmentation.''')
    image = Image.open(r'Images/NLP.jpg')
    st.image(image, caption='Natural Language Processing')
    st.write('''**Deep Learning:** Deep learning is based on the branch of machine learning, which is a subset of artificial intelligence. Since neural networks imitate the human brain and so deep learning will do. In deep learning, nothing is programmed explicitly. Basically, it is a machine learning class that makes use of numerous nonlinear processing units so as to perform feature extraction as well as transformation. The output from each preceding layer is taken as input by each one of the successive layers.''')
    
    st.write('''**Computer Vision:** Computer vision is a scientific field which deals with how computers can be made as high level devices which understand digital images and videos. In terms of engineering, it is an automate task that the human visual system can do. Computer vision has methods for acquiring, processing, analyzing and understanding the digital image. The most important task is to extract high dimensional data from the real world which can produce numerical or symbolic information.

As a scientific discipline, computer vision is related to the theory of artificial system which can extract information from images. The image data is used in the form of video sequences which can be seen by a human.''')
    image = Image.open(r'Images/CV.jpg')
    st.image(image, caption='Computer Vision')    
    st.write('''**Speech to text / Text to speech:** Have you ever thought about how Google Assistant or Amazon Alexa recognizes whatever you say? You must be thinking about some complex smart technologies working behind bars. Apart from a massive hit in the market of tremendous technological growth of recognition systems, the majority of the cellular device has the feature of speech recognition all through some inbuilt applications or third party applications. Not necessarily; most such speech recognition systems are built and deployed with the help of python packages and libraries. To a certain level, Python has proven that it is an essential aspect of the foreseeable future. The reason is pretty obvious. To incorporate speech recognition in Python, you need a certain level of interactivity and accessibility to match technologies.''')
    image = Image.open(r'Images/speech_text.jpg')
    st.image(image, caption='Speech to Text')
    st.write('''**Information Retrieval:** Information Retrieval (IR) can be defined as a software program that deals with the organization, storage, retrieval, and evaluation of information from document repositories, particularly textual information. Information Retrieval is the activity of obtaining material that can usually be documented on an unstructured nature i.e. usually text which satisfies an information need from within large collections which is stored on computers. For example, Information Retrieval can be when a user enters a query into the system. 

Not only librarians, professional searchers, etc engage themselves in the activity of information retrieval but nowadays hundreds of millions of people engage in IR every day when they use web search engines. Information Retrieval is believed to be the dominant form of Information access. The IR system assists the users in finding the information they require but it does not explicitly return the answers to the question. It notifies regarding the existence and location of documents that might consist of the required information. Information retrieval also extends support to users in browsing or filtering document collection or processing a set of retrieved documents. The system searches over billions of documents stored on millions of computers. A spam filter, manual or automatic means are provided by Email program for classifying the mails so that it can be placed directly into particular folders. ''')
    image = Image.open(r'Images/IR.jpg')
    st.image(image, caption='Information Retrieval')

    # st.write('## Get in Touch')
    # st.write(f'\nIf you want to get in touch, you can find me on Social Media at the links below or visit my website at: {pweb}.', unsafe_allow_html=True)
    
    # st.write(f'{sm_li}  {sm_med}  {sm_tw}', unsafe_allow_html=True)
    
    # st.write('## Source Code, Bugs, Feature Requests')
    # githublink = """<a href='https://github.com/andymcdgeo/las_explorer' target="_blank">https://github.com/andymcdgeo/las_explorer</a>"""
