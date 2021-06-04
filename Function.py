def fileReader():
    fileName= input("Enter the file name ")
    file=open(fileName,'r')
    wordcount = 0

    for i in file:
        words=i.split(" ")
        wordcount = len(words)+wordcount
    print(wordcount)
        
fileReader()