import pandas as pd
from geopy.distance import geodesic
import enchant

data = pd.read_csv(r'C:\Users\AyushPatel\Downloads\Assignment_data.csv')
print(data)

# adding is_similar column into our input file and setting value to 0 as default and will change according to the problem statement.
data['is_similar']=0
# funcion for finding distance between two points (points is basically a tuple of longitude and latitude of a location.)
def geo_dist(a,b):
    return geodesic(a,b).meters


# function for finding similarity between two words.
# Here I am using enchant library to calculate levenshtein distance between two words.
def similarity(word1,word2):
    count = enchant.utils.levenshtein(word1, word2)
    # as given conditions for similarity levenshtein distance between two words must be less then 5.
    if count<5:
        return 1
    return 0

#Running loop for all the data rows in the input dataset.
for i in range(0,len(data)-1):
    point1 = (data['latitude'][i],data['longitude'][i])
    point2 = (data['latitude'][i+1],data['longitude'][i+1])
    distance = geo_dist(point1,point2)
    
    #condition loop to check both the conditions given to set is_similar value to 1.
    if distance<=200:
        is_similar = similarity(data['name'][i],data['name'][i+1])
        if(is_similar):
            data['is_similar'][i] = 1
            data['is_similar'][i+1] = 1

#saving the final output to output.csv file
data.to_csv('Output.csv')
