# Author: Lyubov Sidlinskaya
# Assignment: HW2
# Course: CSC 535 Data Mining
# Date: 03-01-2018
# Trace Location: \\trace\Class\CSC-535-635\001\Sidlinskaya\HW2

import sys
import csv
import copy
import math
import operator

# Function which calculates the distance between two points, the training sample & test sample.
def calc_euclidean(x, y):
    train_sample = x[1:] # Removes the first column label/class attribute
    test_sample = y[1:]  # Removes the first column label/class attribute
    distance = 0
    # distance2 = 0
    # Using each value of both the training and testing sample, calculate the euclidean distance
    for i in (range(len(test_sample)-1)):
        distance += (pow((float(train_sample[i]) - float(test_sample[i])),2))
    final_dist = math.sqrt(distance)
    return (final_dist)

def get_distance(item): # Returns values in index "1".
    return item[1]

def calculate_knn(T, t, K):
    training_data = T[1:] # Remove header row from training dataset.
    testing_data = t      # Test sample, received one row at a time.
    neighbor_set = []     # Set for holding the (K) closest neighbors of test sample.
    
    for train_row in training_data:
        # For each row in training data, calculate the euclidean distance to the test sample.
        train_row_dist = calc_euclidean(train_row, testing_data)
        if (len(neighbor_set)) < K:                 # If neighbor set less than K value.
            tup = [train_row, train_row_dist]      
            neighbor_set.append(tup)                # Add tuples of training data row, distance to neighbor set.
            neighbor_set = sorted(neighbor_set, key = get_distance, reverse=True) # Sort list high to low, based on distance
        else:                                       # When next training data row cannot be appended to neighbor set
            for element in neighbor_set:            # For each element in neighbor set.
                element_index = neighbor_set.index(element) # Get index of that element in neighbor set.
                if train_row_dist <= element[1]:            # If distance of current row <= any elements of neighbor set.
                    neighbor_set.pop(element_index)         # Remove that element from neighbor set.
                    tup = [train_row, train_row_dist]       # Create a tuple of current training row and its distance.
                    neighbor_set.append(tup)                # Append this closer training data row to neighbor set.

                    neighbor_set = sorted(neighbor_set, key = get_distance, reverse=True) # Sort list high to low
                    break                                   # Jump out of loop as item in neighbor set has been replaced.
    return neighbor_set                                     # Return final set of neighbors for test sample

# Function to determine class of test samples.
# Receives the neighbors (K) as an argument.
def classify_class(neighbors):
    inv_sums = []
    for k_item in neighbors:                # For item in neighbors set
        k_item.append(1/k_item[1])          # append its weighted vote.
    
    class_weight = {}
    classes = list(set([c[0][0] for c in neighbors])) # Get list of classes of the K neighbors.
    for selected_class in classes:                      # For each unique class in K neighbors.
        total_votes = 0                                 # Counter for total weighted vote.
        for elem in neighbors:                          # For each neighbor:...
            if selected_class == elem[0][0]:            # if unique class is equal to the neighbors class..
                total_votes += (elem[2])                # add the weighted vote to total for that unique class.
        class_weight[selected_class] = total_votes      # Save total weight for each unique class in dictionary. 
    # Find the class with the higher weighted vote
    max_class = max(class_weight.items(), key=operator.itemgetter(1))[0]
    return (max_class)
    
# Function to read csv input files into list.
def read_data(input_file_name):
    try:
        with open(input_file_name, newline="") as data_file:
            rows = csv.reader(data_file)
            data_set = list(rows)
        return data_set
    # Throw error if issue reading file.
    except IOError:
        print ("Error reading file.", input_file_name)
        sys.exit()

# Function which displays accuracy of KNN algorithm & additional info.
def accuracy_info(test_length, mistakes):
    rate = ((test_length - mistakes)/ test_length) * 100        # Calculates the accuracy rate.
    print ("Accuracy Rate: ", rate, "%")
    print ("Number of misclassified test samples:", mistakes)   # Displays number of missclassified samples.
    print ("Total number of test samples: ", test_length)       # Displays total  number of test samples.
  

def main():
    if len(sys.argv) > 2:
        train_file_name = sys.argv[1]                           # Accepts filename as cmd line argument.
        test_file_name = sys.argv[2]
        
        training_data = read_data(train_file_name)              # Reads csv file into list.
        testing_data = read_data(test_file_name)
        # k_squareroot = int(math.sqrt([len(training_data)]))       # K square root value.
        
        k_value = 4                                             # K value for selecting number of neighbors.
        missed_samples = 0                                      # Counter for missclassified samples.
        print ("K = ", k_value)

        for test_row in testing_data[1:]:                       # For each row in testing data minus header row
            neighbor_set = calculate_knn(training_data, test_row, k_value) # Get the neighbors for the test sample
            final_class = classify_class(neighbor_set)          # Get the computed class for the test sample
            print ("Desired Class:", test_row[0], "  Computed Class:", final_class)
            if test_row[0] != final_class:                      # If sample was missclassified, increment counter.
                missed_samples +=1
        accuracy_info((len(testing_data)-1), missed_samples)    # Displays accuracy information about algorithm and dataset.

    else:
        print ("Please enter the correct cmd line arguments in the format:")
        print ("python hw2.py train_dataFile.csv test_dataFile.csv")

main()
