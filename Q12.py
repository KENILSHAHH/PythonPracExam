string='thequickbrownfoxjumpsoverthelazydog'
dictionary={}
for i in string:
    if string.count(i)>1 :
        dictionary[i]=string.count(i)
print(dictionary)