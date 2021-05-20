import importlib
import sys


def check_packages (package):
     try:
         importlib.import_module(package)
         print ("{} available" .format (package))

     except:
        print ("{} not available!" .format (package))



packages = ['os', 'pandas', 'numpy']

for package in packages:
    check_packages (package)



# test the inported module
#pandas
#d = {'col1': [1, 2], 'col2': [3, 4]}
#df = pandas.DataFrame(data=d)

#numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)