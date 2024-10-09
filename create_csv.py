import os
import sys
import pandas as pd

curpath = os.getcwd()
df = pd.DataFrame(columns=['object', 'code'])

n = len(sys.argv)
if n is not 2:
    print("Please use the format: 'python create_csv.py [DIRECTORY OF PYTHON OBJECTS]")
    exit()

path = sys.argv[1]
paths = []
objects = []

# for linux
for object in os.listdir(path):
    paths.append(f'{path}/{object}')
    objects.append(object.strip('.py'))

addtodf = dict({'object': objects, 'path': paths})

df = pd.DataFrame(addtodf)

df.to_csv(path_or_buf='dataset.csv')
