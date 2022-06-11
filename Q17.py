fname = input("Enter file name: ")
try :
    fk = open(fname)
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for line in fk :
    line = line.upper()
    line = line.rstrip()
    print(line)