fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for line in fh :
    line = line.lower()
    line = line.rstrip()
    print(line)