#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
# Create List of Value by Spliting on - Character and Lower Case Word if is not Alpha Character
# Use the pet names list as input to create dictionary maping
def get_lowercase_name_with_split(animal_list):
    """Lower case name and split word list 
       only append if the first character isalpha
    """
    pet_names = []

    for name in animal_list:
        pet_name = ' '.join(item for item in name.lower().split('_') if item.isalpha())
        pet_names.append(pet_name.strip())

    return pet_names


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    WARNING_MESSAGE = "** Warning: Key={} already exists in results_dic with value={}"
    animal_list = listdir(image_dir)
    results_dic = dict()

    # Create Dictionary Value by Spliting on - and Lower Case Characters of is not Alpha Character
    # Use the pet names as input to create dictionary maping
    pet_names = get_lowercase_name_with_split(animal_list)
  

    for idx, animal in enumerate(animal_list):
        if animal not in results_dic:
            results_dic[animal] = [pet_names[idx]]
        else:
            print(WARNING_MESSAGE.format(animal, results_dic[animal]))


    for key in results_dic:
      print('Filename=:', key, "  Pet Label=", results_dic[key][0])


    return results_dic

if __name__ == '__main__':
    get_pet_labels('pet_images/')
