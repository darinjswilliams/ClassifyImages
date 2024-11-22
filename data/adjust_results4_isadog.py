#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """    

    dogname_dic = {}

    with open(dogfile, 'r') as data:
        line = data.readline()
        while line != '':
            name = line.rstrip()

            if name not in dogname_dic:
                dogname_dic[name] = 1 

            line = data.readline()

    
    for key in results_dic:
        
        if results_dic[key][0] in dogname_dic:
        
            if results_dic[key][1] in dogname_dic:
                results_dic[key].extend((1,1))
            else:
                results_dic[key].extend((1,0))
        else:
            
            if results_dic[key][1] in dogname_dic:
                results_dic[key].extend((0,1))
            else:
                results_dic[key].extend((0,0))
    
   
    None

if __name__ == '__main__':
    results_dic = {'Boston_terrier_02285.jpg': ['boston terrier', 'basenji', 0], 'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1], 
    'Basset_hound_01034.jpg': ['basset hound', 'basset, basset hound', 1], 'cat_02.jpg': ['cat', 'tiger cat, cat', 1], 
    'Great_pyrenees_05435.jpg': ['great pyrenees', 'great pyrenees', 1], 'Boston_terrier_02303.jpg': ['boston terrier', 'boston bull, boston terrier', 1],
    'German_shorthaired_pointer_04986.jpg': ['german shorthaired pointer', 'german shorthaired pointer', 1], 'Golden_retriever_05195.jpg': ['golden retriever', 'golden retriever', 1], 
    'Miniature_schnauzer_06884.jpg': ['miniature schnauzer', 'miniature schnauzer', 1], 'Collie_03797.jpg': ['collie', 'collie', 1], 'Golden_retriever_05223.jpg': ['golden retriever', 'golden retriever', 1],
    'gecko_80.jpg': ['gecko', 'tailed frog, bell toad, ribbed toad, tailed toad, ascaphus trui', 0], 'Great_pyrenees_05367.jpg': ['great pyrenees', 'kuvasz', 0], 'Beagle_01125.jpg': ['beagle', 'beagle', 1],
    'Basenji_00974.jpg': ['basenji', 'basenji', 1], 'Golden_retriever_05182.jpg': ['golden retriever', 'tibetan mastiff', 0], 'Poodle_07927.jpg': ['poodle', 'standard poodle, poodle', 1], 
    'Cocker_spaniel_03750.jpg': ['cocker spaniel', 'cocker spaniel, english cocker spaniel, cocker', 1], 'Dalmatian_04068.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1], 
    'great_horned_owl_02.jpg': ['great horned owl', 'ruffed grouse, partridge, bonasa umbellus', 0], 'Golden_retriever_05257.jpg': ['golden retriever', 'afghan hound, afghan', 0],
    'Beagle_01170.jpg': ['beagle', 'walker hound, walker foxhound', 0], 'cat_01.jpg': ['cat', 'african hunting dog, hyena dog, cape hunting dog, lycaon pictus', 0], 'Saint_bernard_08010.jpg': ['saint bernard', 'saint bernard, st bernard', 1],
    'Poodle_07956.jpg': ['poodle', 'standard poodle, poodle', 1], 'Basenji_00963.jpg': ['basenji', 'basenji', 1], 'fox_squirrel_01.jpg': ['fox squirrel', 'fox squirrel, eastern fox squirrel, sciurus niger', 1], 
    'Great_dane_05320.jpg': ['great dane', 'great dane', 1], 'Saint_bernard_08036.jpg': ['saint bernard', 'saint bernard, st bernard', 1], 'skunk_029.jpg': ['skunk', 'skunk, polecat, wood pussy', 1], 'Dalmatian_04037.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1],
    'gecko_02.jpg': ['gecko', 'alligator lizard', 0], 'polar_bear_04.jpg': ['polar bear', 'ice bear, polar bear, ursus maritimus, thalarctos maritimus', 1], 'Dalmatian_04017.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1], 
    'Boston_terrier_02259.jpg': ['boston terrier', 'boston bull, boston terrier', 1], 'Rabbit_002.jpg': ['rabbit', 'wood rabbit, cottontail, cottontail rabbit, rabbit', 1], 'Beagle_01141.jpg': ['beagle', 'english foxhound', 0], 'Boxer_02426.jpg': ['boxer', 'boxer', 1], 
    'German_shepherd_dog_04890.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1], 'cat_07.jpg': ['cat', 'egyptian cat, cat', 1]}

    dogfile = 'dognames.txt'

    adjust_results4_isadog(results_dic, dogfile)
    