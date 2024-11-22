#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
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
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """    

     # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture",model.upper(), 
          "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}\n".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Print Summary Statistics Percentages on the Model run
    for key, value in results_stats_dic.items():
        if key[:3] == 'pct':
            print("Pecentage Name: {:>26}  Percentage Value:{:>17}".format(key, value))


    # IF print_incorrect_dogs == True AND there were images incorrectly 
    # classified as dogs or vice versa - print out these cases
    if(print_incorrect_dogs and ((results_stats_dic['n_correct_dogs'] +  results_stats_dic['n_correct_notdogs'])
       != results_stats_dic['n_images'] )):

       print("\nINCORRECT Dog/NOT Dog Assigments:")

       # process through results dict, printing incorrectly classified dogs
       for key in results_dic:

          if (sum(results_dic[key][3:]) == 1):
                print("Real: {:>26}  Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))


    # IF print_incorrect_breed == True AND there were dogs whose breeds 
    # were incorrectly classified - print out these cas
    if (print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']) ):
        print("\nINCORRECT Dog Breed Assignment:")

        # process through results dict, printing incorrectly classified breeds
        for key in results_dic:

            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if ( sum(results_dic[key][3:]) == 2 and
                results_dic[key][2] == 0 ):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0],
                                                          results_dic[key][1]))


    None


if __name__ == "__main__":
    results_dic = {'Boston_terrier_02285.jpg': ['boston terrier', 'basenji', 0, 1, 1], 'German_shepherd_dog_04931.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 1, 1], 'Basset_hound_01034.jpg': ['basset hound', 'basset, basset hound', 1, 1, 1], 'cat_02.jpg': ['cat', 'tiger cat, cat', 1, 0, 0], 'Great_pyrenees_05435.jpg': ['great pyrenees', 'great pyrenees', 1, 1, 1], 'Boston_terrier_02303.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'German_shorthaired_pointer_04986.jpg': ['german shorthaired pointer', 'german shorthaired pointer', 1, 1, 1], 'Golden_retriever_05195.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'Miniature_schnauzer_06884.jpg': ['miniature schnauzer', 'miniature schnauzer', 1, 1, 1], 'Collie_03797.jpg': ['collie', 'collie', 1, 1, 1], 'Golden_retriever_05223.jpg': ['golden retriever', 'golden retriever', 1, 1, 1], 'gecko_80.jpg': ['gecko', 'tailed frog, bell toad, ribbed toad, tailed toad, ascaphus trui', 0, 0, 0], 'Great_pyrenees_05367.jpg': ['great pyrenees', 'kuvasz', 0, 1, 1], 'Beagle_01125.jpg': ['beagle', 'beagle', 1, 1, 1], 'Basenji_00974.jpg': ['basenji', 'basenji', 1, 1, 1], 'Golden_retriever_05182.jpg': ['golden retriever', 'tibetan mastiff', 0, 1, 1], 'Poodle_07927.jpg': ['poodle', 'standard poodle, poodle', 1, 1, 1], 'Cocker_spaniel_03750.jpg': ['cocker spaniel', 'cocker spaniel, english cocker spaniel, cocker', 1, 1, 1], 'Dalmatian_04068.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'great_horned_owl_02.jpg': ['great horned owl', 'ruffed grouse, partridge, bonasa umbellus', 0, 0, 0], 'Golden_retriever_05257.jpg': ['golden retriever', 'afghan hound, afghan', 0, 1, 1], 'Beagle_01170.jpg': ['beagle', 'walker hound, walker foxhound', 0, 1, 1], 'cat_01.jpg': ['cat', 'african hunting dog, hyena dog, cape hunting dog, lycaon pictus', 0, 0, 0], 'Saint_bernard_08010.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 1, 1], 'Poodle_07956.jpg': ['poodle', 'standard poodle, poodle', 1, 1, 1], 'Basenji_00963.jpg': ['basenji', 'basenji', 1, 1, 1], 'fox_squirrel_01.jpg': ['fox squirrel', 'fox squirrel, eastern fox squirrel, sciurus niger', 1, 0, 0], 'Great_dane_05320.jpg': ['great dane', 'great dane', 1, 1, 1], 'Saint_bernard_08036.jpg': ['saint bernard', 'saint bernard, st bernard', 1, 1, 1], 'skunk_029.jpg': ['skunk', 'skunk, polecat, wood pussy', 1, 0, 0], 'Dalmatian_04037.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'gecko_02.jpg': ['gecko', 'alligator lizard', 0, 0, 0], 'polar_bear_04.jpg': ['polar bear', 'ice bear, polar bear, ursus maritimus, thalarctos maritimus', 1, 0, 0], 'Dalmatian_04017.jpg': ['dalmatian', 'dalmatian, coach dog, carriage dog', 1, 1, 1], 'Boston_terrier_02259.jpg': ['boston terrier', 'boston bull, boston terrier', 1, 1, 1], 'Rabbit_002.jpg': ['rabbit', 'wood rabbit, cottontail, cottontail rabbit, rabbit', 1, 0, 0], 'Beagle_01141.jpg': ['beagle', 'english foxhound', 0, 1, 1], 'Boxer_02426.jpg': ['boxer', 'boxer', 1, 1, 1], 'German_shepherd_dog_04890.jpg': ['german shepherd dog', 'german shepherd, german shepherd dog, german police dog, alsatian', 1, 1, 1], 'cat_07.jpg': ['cat', 'egyptian cat, cat', 1, 0, 0]}
    results_stats_dic ={'n_dogs_img': 30, 'n_match': 30, 'n_correct_dogs': 30, 'n_correct_notdogs': 10, 'n_correct_breed': 24, 'n_images': 40, 'n_notdogs_img': 10, 'pct_match': 75.0, 'pct_correct_dogs': 100.0, 'pct_correct_breed': 80.0, 'pct_correct_notdogs': 100.0}
    model = 'resnet'
    print_results(results_dic, results_stats_dic, model, True, True)
                
