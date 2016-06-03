#Dropbox Sample code challenge

def say_what_you_see(input_strings):
	retarr=[]
	for strings in input_strings:
		count=1
		prevnum=strings[0]
		opstr=''
		for i in range(1,len(strings)):
			if prevnum==strings[i]:
				count+=1
			else:
				opstr+=`count`
				opstr+=prevnum
				prevnum=strings[i]
				count=1
		else:
			opstr+=`count`
			opstr+=prevnum
		retarr.append(opstr)

	return retarr



if __name__ == '__main__':
	print say_what_you_see(["11","22"])