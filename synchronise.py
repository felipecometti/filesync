import os
from shutil import copyfile

import datetime
timestart = datetime.datetime.now()

#===================================================================#
#   Synchronisation block for files already available on dirs       #
#   Doesn't work as a connector (I don't know why I made this note) #
#===================================================================#

def subs(name, src, dst):
	# Runs shutil.copyfile
	# Erros aren't treated. If it runs into one, the program ends
	# The 'name' variable is largely cosmetic
	print ("Copying: " + name)
	try:
		copyfile(src, dst)
	except:
		print("There was an error")
		return 1
	print("OK.")
	

def sync(name, src, dst):
	# Compares the to files
	# If os.path.getmtime(src) > os.path.getmtime(dst), dst gets replaced by src
	# If os.path.getmtime(src) <= os.path.getmtime(dst), nothing happens
	# If os.path.getmtime(dst) returns OSError, it tries to run the replacement
	# If the replacement throws any error, the program ends

	timestart = datetime.datetime.now()
	
	try:
		os.path.getmtime(dst)
	except OSError:
		print(name + " wasn't found in the destination, or had it's access denied.")
		print("Trying to send the file to the destination...")
		subs(name, src, dst)
		
		timeend = datetime.datetime.now()
		deltatime = timeend - timestart
		print("Elapsed time: [" + str(deltatime) + "]")
		
		return 2
		
	try:
		os.path.getmtime(src)
	except OSError:
		print(name + " wasn't found on the origin.")
		return 3
	
	srcmtime = os.path.getmtime(src)
	dstmtime = os.path.getmtime(dst)
	
	if(srcmtime > dstmtime):
		subs(name, src, dst)
	else:
		print("Copying: " + name)
		print(name + " is already up to date.")
		return 4

	timeend = datetime.datetime.now()
	deltatime = timeend - timestart
	print("Elapsed time: [" + str(deltatime) + "]")

#===================================================================#
#   End of the block                                                #
#   --------------------                                            #
#   Start of the call routines                                      #
#===================================================================#

name = "Test"
src = "C:/Users/John Doe/Desktop/test/test1/updatedtest.txt"
dst = "C:/Users/John Doe/Desktop/test/test2/mytest.txt"
sync(name, src, dst)

# Copy and paste as many as you want

#===================================================================#
#   End of the call routine                                         #
#   --------------------                                            #
#   THE END                                                         #
#===================================================================#

timeend = datetime.datetime.now()
deltatime = timeend - timestart

print("\nFinished.")
print("Total time: [" + str(deltatime) + "]")
input("\nPress enter to continue...")