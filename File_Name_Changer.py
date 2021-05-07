import os

print('This python script will change the names of files in any directory.\nPlease answer the following questions knowing that case and spelling matter.\n')

dirName = input('In what folder are the files?\n')

fileExt = input('\nWhat is the file ext of the files (.mp3, .text, .doc, etc...)?\n')

fileExtLength = len(fileExt)

removeOrAdd = input('\nWould you like to add a common phrase to the file or remove a common phrase? (Type: Add or Remove)\n')

fileAddOn = input('\nWhat would you like to add to or remove from the file names?\n')

os.chdir(dirName)

files = os.listdir()

for filename in files:
	lengthOfFile = len(filename)
	rmExtFilename = filename[0:lengthOfFile - fileExtLength]
	lenRmExtFilename = len(rmExtFilename)
	if (removeOrAdd == 'Remove'):
		lengthOfRemoval = len(fileAddOn)
		newFilename = rmExtFilename[0:lenRmExtFilename - lengthOfRemoval]
		newFilename = newFilename + fileExt
	elif (removeOrAdd == 'Add'):
		newFilename = rmExtFilename + fileAddOn + fileExt
	os.rename(filename, newFilename)
	print(f'Changed file name to: {newFilename}')


