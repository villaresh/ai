import os
path = 'C:/Users/USER/Downloads/CRC-VAL-HE-7K/ADI’
files = os.listdir(path)
for index, file in enumerate(files):
   os.rename(os.path.join(path, file), os.path.join(path, ''.join([‘adi’,str(index), '.tif'])))
