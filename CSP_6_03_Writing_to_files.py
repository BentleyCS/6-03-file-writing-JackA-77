
#You need to create your own test file for this assignment.
#Because we are dealing with both reading and writing to files. Your test file will be more complicated than it has been.

def writeFile(inputList, fileName):
    #Creates a file of the given name and adds each value from the list to said file with each line being an index from the list.
    f = open(fileName, 'w')
    for item in inputList:
        f.write(item)
        f.write('\n')
    out = ""
    f = open(fileName)
    for line in f:
        out += line
    return out

def sortNames(fileName, targetFile):
    #Modify the below function such that it takes in source file and a target file.
    #Sort all of the values from the source file and write them to the target file
    #I recommend using .sort() for this. You do not need to write the sorting algorithm yourself.
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    names = out.split()
    names.sort()
    g = open(targetFile, 'w')
    for name in names:
        g.write(name)
        g.write('\n')
    g = open(targetFile)
    out = g.read()
    return out

def highScore( newScore: int):
    #Modify the function such that it adds a new score to the file scores.txt
    #Then return the average score from all of the scores in scores.txt
    average = 0
    with open('scores.txt', 'a+') as f:
        f.write('\n')
        f.write(str(newScore))
        f.write('\n')
    with open('scores.txt') as f:
        out = f.read()
        print(out)
        nums = out.split()
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        print(nums)
        print(len(nums))
        print(sum(nums))
        average = sum(nums) / len(nums)
    return average
