#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # change intended inner list into dictionary 
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

print('The Magic CD Inventory\n')
while True:
    print('[a] Add CD\n[i] Display Current Inventory\n[l] load Inventory from file')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        break
    if strChoice == 'a':  
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        print(dicRow)
    elif strChoice == 'i':
        #print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'l': #modification of read and display functions
        lstTbl.clear()
        dicRow.clear() #clean up required for both list and inner list(dictionary) when loading?
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': lstRow[0], 'Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
            print(dicRow) #checking and printing the expected results 
        objFile.close()
    elif strChoice == 'd':
	#initially mistook objective as deleting selected entries loaded from the file
        delChoice = input('Enter the CD title or Artist name to be deleted:')
        for i in range(len(lstTbl)):
            # if lstTbl[i].get('Title') or lstTbl[i].get('Artist') == delChoice: #boolean logic issue with the first part of the if statement when not fully separating two statements
            #     del lstTbl[i]
            #     break                   #break once the entry is found and deleted
            if lstTbl[i].get('Title') == delChoice or lstTbl[i].get('Artist') == delChoice:
                del lstTbl[i]
                print("Entry deleted!")
                break
            else:
                print('Not in our inventory!') #primitive way to reject failed deletion?
                break
        #if delChoice in lstTbl:
            #print('Yes')
        #print(dicRow) #dictionary row does not update properly, only shows the latest additional entry I add?
    elif strChoice == 's':
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

