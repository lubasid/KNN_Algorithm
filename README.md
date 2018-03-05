# KNN_Algorithm
KNN algorithm for machine learning.

CSC 535/635 – HW 2
Due Date: Tuesday, March 6, 2018

Instructions: Students are required to work alone on this assignment. Please turn in a hard copy of your solution at the beginning of class on the due date. Please upload your files to your CSC 535-635 TRACE folder in a subfolder named HW2 and turn in a hard copy in class on the due date. 

For this assignment, you will implement the KNN algorithm as given in the book on page 92. The only difference is that while the book uses simple unweighted voting, you will use weighted voting in your implementation. In simple unweighted voting, once the k nearest neighbors are found, their distances from the test sample do not matter. One neighbor is one vote. In weighted voting, the vote of a neighbor is inversely proportional to its distance to the test sample. You must use Python for your implementation.

Use the given MNIST_train.cvs as your training data set and MNIST_test.csv as the test data set. There are 10 classes, with labels 0, 1, 2, …, 9, for this data set. The first attribute/column is the class label. Also notice that the first line/row in both data sets is a headers line. Do not modify the given data sets in any way because your code will be graded using them. In your code, you can just skip over the header lines. A description of the MNIST data is available at https://www.kaggle.com/c/digit-recognizer/data 

The output from your program will display the following:
•	value of K 
•	for each test sample, print both the desired class and the computed class, where desired class, is the class label as given in the data set, and computed class, is what your code produces as the output for the sample. 
•	the accuracy rate
•	number of misclassified test samples, and 
•	total number of test samples 
Sample output is as follows. Notice that, this sample output does not show the best value of K:
```
K = 4
...
Desired Class: 9   Computed Class: 9
Desired Class: 9   Computed Class: 7
Desired Class: 9   Computed Class: 9
Desired Class: 9   Computed Class: 9
Desired Class: 9   Computed Class: 9
Accuracy Rate:  86.0 %
Number of misclassified test samples: 7
Total number of test samples:  50
```

Remarks:
•	Use Euclidean distance measure to compute distances.
•	You may use a random sample of the training data to decide on the value of K to use for the algorithm.
•	Make sure to use the data sets from the course web site and not any other instance of MNIST
•	You need to use basic Python for implementation. You are not allowed to use IPython  (no pandas, numpy, or scikit-learn) 

What to turn in?
Upload to trace copies of your source code and a report (preferably) in MS word describing how you choose k, the accuracy of the algorithm, and any comments about this homework assignment you may want to share. Constructive feedback will be appreciated. If you did the extra credit part, then add a separate section in the report to describe what you did and the improvement you got. 
Please make sure that your Python code is well organized and properly documented and commented.


2) Extra Credit: [up to 20 points]: Think about innovative way(s) to improve the performance of KNN. Implement your approach and report on the improvement. 
