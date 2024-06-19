def iterate(iterator=-1, reverse=0, notFirstRun=0):
    notFirstRun=1
    if (reverse == 1 and (iterator == 1 or iterator == 2 or iterator == 3)):
        iterator-=1
        return iterator, reverse, notFirstRun
    elif (reverse == 0 and (iterator == 0 or iterator == 1 or iterator == 2)):
        iterator+=1
        return iterator, reverse, notFirstRun
    elif (iterator == 3):
        iterator = 2
        reverse = 1
        return iterator, reverse, notFirstRun
    else:
        iterator=0
        return iterator, reverse, notFirstRun


def compareArrays(a1, a2):
    traverseSequence=[4,3,3,2]

    a1Len=len(a1)
    a2Len=len(a2)

    if (a1Len!=a2Len):
        return False
    
    else:
        [iterator, reverse, notFirstRun]=iterate()
        i=iterator
        
        while (i<a1Len):
            [iterator, reverse, notFirstRun]=iterate(iterator, reverse, notFirstRun)
            if (a1[i]!=a2[i]):
                print("iterator:", iterator)
                print("travSeq:", traverseSequence[iterator])
                return False
            i+=iterator
            
    if a1!=a2:
        return False
    return True


print(compareArrays([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]))
