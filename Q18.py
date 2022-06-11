fname = input("Enter file name: ")
try :
    fh = open(fname)
except:
    print('Cannot open the file ',fname ,'please try again')
    quit()

for i,line in enumerate(fh) :
    if i>=10:
        break
    line = line.lower()
    line = line.rstrip()
    print(line)