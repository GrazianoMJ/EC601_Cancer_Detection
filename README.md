# EC601_Cancer_Detection

<<<<<<< Arjun
Worked on the webpage for the project. Index.html is the homepage of the site. Only an user can upload/download text files. 
=======
Jingjun Wang:
For the machine learning part: 
- The preprocess file is to use nltk(natural language toolkit) to process the original text file, which is also known as clinical data, to get a cleaner version of text file. The object is to get exclude the influence of those unrelated words, such as "a, the", those common english words.
- The run_modle file is to fit our data into sikit learn model, and test the accuracy of different model.

## Text_Processing Folder Description:
This folder contains folders devoted to the preprocessing of our Kaggle provided data. Two sets of data were provided (training and test) and these two sets are broken down further into text files and variants.
- Text contains all of our clinical documents in a delimitted file (the delimitting character is "||"). Each line of the file is a ID number and the full text of the clinical document.
- Variants are .csv files that indicate the associated text's identification number, the gene being discussed in the clinical document, the mutation of the gene that causes cancer, and its classification number.
Within the folder, two python codes are provided that do the following:
- Create cleaner text files by removing unnecessary words and symbols
- Makes a better set of test data by using a provided solution file from Kaggle to extract the known classification/clinical document pairs.

## AWS_Lambda Folder Description:
This folder contains all the work associated with the automation of the AWS Services used for this project. *This is not a comprehensive folder due to the fact that some aspects of the automation are communication functions or settings directly controlled in the AWS Service account* Within this folder you will find files that handle the following:
- A directory and zip file that demonstrate how to perform communication between AWS S3 and AWS Lambda.
- Our current AWS Lambda code that performs functions based on the addition of a new file to the S3 "bucket".
- A test code used to determine if our communication between our S3, Lambda, SQS Queue and EC2 Instance was working correctly.

Currently work is being done to complete the communication between our EC2 Instance and our RDS Database (see the Database folder for code).

>>>>>>> master
