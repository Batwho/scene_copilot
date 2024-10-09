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

# for linux
for object in os.listdir(path):
    df.path.append(f'{path}/{object}')
    df.object.append(object.strip('.py'))

df.to_csv(path_or_buf='dataset.csv')
