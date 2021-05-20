import os

directory = r"\\fileserver1.nrscloud.bcgov\bcts\RemoteSensing\TKO\LASZ\FTEK\EK17_LAZ"

files_in_directory = os.listdir(directory)
filtered_files = [file for file in files_in_directory if file.endswith('.laz')]

print ('there are {} files in this folder' .format (len(filtered_files)))
print (filtered_files)



for file in filtered_files:
    path_to_file = os.path.join(directory, file)
    os.remove(path_to_file)

print ("Files deleted!")

