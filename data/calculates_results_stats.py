#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 

def get_calcualted_counts(results_dic, results_stats_dic):
    """Calculate the counts for image classifiercation
    
    Results_dic Keys
        n_match
        n_dogs_img
        n_correct_dogs
        n_notdogs_img
        n_correct_breed
        n_correct_notdogs  
    """
    for key in results_dic:
    
        #Number of Label Matches Increment n_match - Y
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1

        #Number of Correct Breeds Increment n_correct_breed - E
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1

        #Number of Dog Images Increment n_dogs_img - B
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1

            #Number of Correct Dog Matches Increment n_correct_dogs  A
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
        
        #Number of Correct Non-Dog Matches Increment n_corrent - C
        if results_dic[key][3] == 0 and results_dic[key][4] == 0:
            results_stats_dic['n_correct_notdogs'] += 1
        
        elif results_dic[key][3] == 0:
            results_stats_dic['n_correct_notdogs'] += 1


def get_summary_of_percentages(results_dic, results_stats_dic):
    """Calculate summary of percentages and store value is results_stats_dic

      Results_stats_dic  Keys:
        Images Keys
        n_images
        n_match
        n_dogs_img
        n_correct_dogs
        n_notdogs_img
        n_correct_breed
        n_correct_notdogs

        Percentage Keys
        pct_match
        pct_correct_dogs
        pct_correct_breed
        pct_correct_notdogs
    """
    #calculates number of total images
    results_stats_dic['n_images'] = len(results_dic)

    # calculates number of not-a-dog images using - images & dog images counts
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                      results_stats_dic['n_dogs_img']) 

    # Calculates % correct for matches - A
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] /  results_stats_dic['n_images']) * 100 

    # Calculates % correct dogs - B
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100  

    # Calculates % correct breed of dog
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100

    # Calculates % correct not-a-dog images
    # Uses conditional statement for when no 'not a dog' images were submitted 
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                results_stats_dic['n_notdogs_img'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0


def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 
    #return None

    results_stats_dic = dict()

    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0 

    #Calculate Counts
    get_calcualted_counts(results_dic, results_stats_dic)

    #Compute Summary of Percentages
    get_summary_of_percentages(results_dic, results_stats_dic)

    return results_stats_dic


if __name__ == '__main__':
    results_dic = {'Boston_terrier_02285.jpg': ['boston terrier', 'basenji', 0, 1, 1], 'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 1, 1], 'Basset_hound_01034.jpg': ['basset hound', 'basset, basset hound', 1, 1, 1], 'cat_02.jpg': ['cat', 'tiger cat, cat', 1, 0, 0], 'Great_pyrenees_05435.jpg': ['great pyrenees', 'great pyrenees', 1, 1, 1], 'Boston_terrier_02303.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'German_shorthaired_pointer_04986.jpg': ['german shorthaired pointer', 'german shorthaired pointer', 1, 1, 1], 'Golden_retriever_05195.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'Miniature_schnauzer_06884.jpg': ['miniature schnauzer', 'miniature schnauzer', 1, 1, 1], 'Collie_03797.jpg': ['collie', 'collie', 1, 1, 1], 'Golden_retriever_05223.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'gecko_80.jpg': ['gecko', 'tailed frog, bell toad, ribbed toad, tailed toad, ascaphus trui', 0, 0, 0], 'Great_pyrenees_05367.jpg': ['great pyrenees', 'kuvasz', 0, 1, 1], 'Beagle_01125.jpg': ['beagle', 'beagle', 1, 1, 1], 'Basenji_00974.jpg': ['basenji', 'basenji', 1, 1, 1], 'Golden_retriever_05182.jpg': ['golden retriever', 'tibetan mastiff', 0, 1, 1], 'Poodle_07927.jpg': ['poodle', 'standard poodle, poodle', 1, 1, 1], 'Cocker_spaniel_03750.jpg': ['cocker spaniel', 'cocker spaniel, english cocker spaniel, cocker', 1, 1, 1], 'Dalmatian_04068.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'great_horned_owl_02.jpg': ['great horned owl', 'ruffed grouse, partridge, bonasa umbellus', 0, 0, 0], 'Golden_retriever_05257.jpg': ['golden retriever', 'afghan hound, afghan', 0, 1, 1], 'Beagle_01170.jpg': ['beagle', 'walker hound, walker foxhound', 0, 1, 1], 'cat_01.jpg': ['cat', 'african hunting dog, hyena dog, cape hunting dog, lycaon pictus', 0, 0, 0], 'Saint_bernard_08010.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 1, 1], 'Poodle_07956.jpg': ['poodle', 'standard poodle, poodle', 1, 1, 1], 'Basenji_00963.jpg': ['basenji', 'basenji', 1, 1, 1], 'fox_squirrel_01.jpg': ['fox squirrel', 'fox squirrel, eastern fox squirrel, sciurus niger', 1, 0, 0], 'Great_dane_05320.jpg': ['great dane', 'great dane', 1, 1, 1], 'Saint_bernard_08036.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 1, 1], 'skunk_029.jpg': ['skunk', 'skunk, polecat, wood pussy', 1, 0, 0], 'Dalmatian_04037.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'gecko_02.jpg': ['gecko', 'alligator lizard', 0, 0, 0], 'polar_bear_04.jpg': ['polar bear', 'ice bear, polar bear, ursus maritimus, thalarctos maritimus', 1, 0, 0], 'Dalmatian_04017.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'Boston_terrier_02259.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'Rabbit_002.jpg': ['rabbit', 'wood rabbit, cottontail, cottontail rabbit, rabbit', 1, 0, 0], 'Beagle_01141.jpg': ['beagle', 'english foxhound', 0, 1, 1], 'Boxer_02426.jpg': ['boxer', 'boxer', 1, 1, 1], 'German_shepherd_dog_04890.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 1, 1], 'cat_07.jpg': ['cat', 'egyptian cat, cat', 1, 0, 0]}

    calculates_results_stats(results_dic)