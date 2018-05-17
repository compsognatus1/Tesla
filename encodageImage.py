#coding: utf8
import os
path =  '/data/Bureau/sacrifice/'
inc = 0
alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for folder in os.listdir(path):
	inc += 1
	folder_old = str(inc) + '_' + folder	
	folder += '/export'
	path_new=path+'out/'
	if os.path.exists(path+folder):
		for file in os.listdir(path+folder):
			os.rename(path+folder + '/' + file, path+folder + '/' + file.replace(".",""))
			newfile = file.replace('.','')
			if not os.path.exists(path_new + folder_old):
				os.mkdir(path_new + folder_old)
			os.rename(path + folder + '/' + newfile, path_new+folder_old + '/' + ((newfile.replace("png",".png")).lower()).replace("é","e"))
		if not os.path.exists(path_new+folder_old):
			os.mkdir(path_new+folder_old)
		for file in os.listdir(path_new+folder_old):
			file_new=file
			for letter in alph:
				file_new = file_new.replace(letter,"")
			if file_new!="." and file_new!="":
				os.rename(path_new+folder_old+'/'+file,path_new+folder_old+'/'+str(int(file_new.replace(".","")))+".png")		
	if os.path.exists(path_new+folder_old+'/1.png'):
		cmd = 'convert '+path_new + folder_old + '/1.png -resize 150x84 ' + path_new+folder_old + '/vignette.png';
        	os.system(cmd)
	#print cmd

