print('Enter File Number from the Data Folder :')
f=input()
print("Enter the word :")
word=input()
file='data/'+f

try:
    infile = open(file,'r').read()        
except UnicodeDecodeError:
    print('exception : file corrupted unicode reading error. try another file.')

senlist=infile.split('\n')

for i in senlist:
    if(i.split(' ')[-1]=='writes:'):
        ind=senlist.index(i)
        senlist=senlist[ind+1:-1]

for i in range(senlist.count('')):
    senlist.remove('')

for i in range(len(senlist)):
    senlist[i]=senlist[i].strip('>."')

count=0
for i in senlist:
    if(word.lower()==i.split(' ')[0].lower()):
        count+=1


print('Number of sentences starting with "',word,'" is/are : ',count)


for i in senlist:
    print(i)
