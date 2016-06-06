import os

from nester import print_lol

import pickle

os.chdir('C:\Personal_Data\Temp\Python_Practice\HeadFirstPython')

man = []
other = []
new_man = []

try :
    data = open('sketch.txt')

    for each_line in data:

        try:

            (role, line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)


            #print(role, ' said: ', line_spoken)
        except ValueError:
            pass


    data.close()

except IOError as err:
    print('File error: ' + str(err))

try:
    with open('man_data_1.txt', 'wb') as man_file, open('other_data_1.txt','wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
        #print_lol(man, fn = man_file)
        #print_lol(other, fn = other_file)

except IOError as err1:
    print('File error: ' + str(err1))

except pickle.PickleError as perr:
    print('Pickle Error: ' + str(perr))

try:
    with open('man_data_1.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)

except IOError as err1:
    print('File error: ' + str(err1))

except pickle.PickleError as perr:
    print('Pickle Error: ' + str(perr))

print_lol(new_man)








