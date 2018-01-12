import os, sys
from PIL import Image
im=Image.open('mnist.png')# hamed is a QT.pi

list=[]

pix= im.load()
for x in range(0,289):
	for y in range(0,289):
		if x==0 and y==0:
			numb = (pix[x,y])
			list.append(((numb[2]+numb[1]+numb[0])/3)/255)
		elif (x==0 and y!=0) and y%29!=0:
			numb = (pix[x,y])
			list.append(((numb[2]+numb[1]+numb[0])/3)/255)
		elif (x!=0 and y==0) and x%29!=0:
			numb = (pix[x,y])
			list.append(((numb[2]+numb[1]+numb[0])/3)/255)
		elif(x%29!=0 or y%29!=0):
			numb = (pix[x,y])
			list.append(((numb[2]+numb[1]+numb[0])/3)/255)
		#list.append(((numb[2]+numb[1]+numb[0])/3)/255)

print(list)