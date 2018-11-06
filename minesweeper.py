

##############################################

##ACADEMY OF TECHNOLOGY
##COPY RIGHT:-ACADEMY OF TECHNOLOGY
##PROGRAM DEVELOPED BY SOUVIK GHOSH

##############################################

import sys

level=1
def printmine(l):
	print "  ",
	for i in range(0,9):
		print i,"\t",
	print
	for i in range(0,9):
		print i,
		for j in range(0,9):
			print "| ",
			if l[i][j]>0 and l[i][j]<=8 or l[i][j]==99:
				print " ",l[i][j]," ","|",
			elif l[i][j]==10:
				print " ","."," ","|",
			else:
				print " "," "," ","|",
		print "\n\n"

def isWin(l):
	f=0
	for i in range(0,9):
		for j in range(0,9):
			if (l[i][j]>0 and l[i][j]<=8) or l[i][j]==10 :
				f+=1

	if f==(81-9):
		return 1
	else:
		return 0
	

def printt(l):
	print "     ",
	for i in range(0,9):
		print i,"        ",
	print
	for i in range(0,9):
		print i,
		for j in range(0,9):
			print "| ",
			if l[i][j]>0 and l[i][j]<=8 :
				print " ",l[i][j]," ","|",
			elif l[i][j]==10:
				print " ","."," ","|",
			else:
				print " "," "," ","|",
		print "\n\n"

def setmine(l,level):
	if level==1:
		l[0][8],l[2][6],l[2][4],l[3][7],l[4][5],l[5][3],l[6][3],l[6][8],l[7][3],l[0][0]=99,99,99,99,99,99,99,99,99,99
		level+=1
	elif level==2:
		l[1][7],l[2][5],l[4][1],l[4][8],l[5][8],l[6][7],l[7][7],l[8][0],l[8][2],l[8][5]=99,99,99,99,99,99,99,99,99,99
		level+=1
	elif level==3:
		l[0][3],l[2][7],l[4][2],l[4][8],l[5][8],l[6][8],l[6][5],l[7][3],l[7][4],l[7][5]=99,99,99,99,99,99,99,99,99,99
		level+=1
	elif level==4:
		l[1][1],l[3][2],l[3][8],l[4][1],l[5][1],l[5][2],l[6][6],l[7][5],l[8][8],l[8][7]=99,99,99,99,99,99,99,99,99,99
		level+=1
	elif level==5:
		l[0][6],l[2][0],l[2][5],l[3][4],l[3][6],l[4][8],l[5][2],l[5][5],l[6][4],l[7][4]=99,99,99,99,99,99,99,99,99,99
		level+=1
	elif level==6:
		l[0][3],l[0][7],l[1][4],l[1][6],l[2][2],l[4][5],l[5][4],l[7][8],l[8][3],l[8][4]=99,99,99,99,99,99,99,99,99,99
		level+=1
	elif level==7:
		l[8][6],l[1][6],l[3][0],l[3][4],l[3][7],l[5][5],l[6][2],l[7][1],l[7][8],l[8][7]=99,99,99,99,99,99,99,99,99,99
		level+=1
	elif level==8:
		l[0][0],l[0][3],l[1][6],l[2][0],l[2][5],l[5][7],l[6][2],l[7][4],l[8][3],l[8][5]=99,99,99,99,99,99,99,99,99,99
		level+=1
	elif level==9:
		l[1][1],l[2][0],l[1][4],l[3][2],l[4][0],l[6][6],l[6][7],l[7][8],l[8][6],l[7][7]=99,99,99,99,99,99,99,99,99,99
		level+=1
	elif level==10:
		l[0][0],l[2][6],l[4][7],l[3][6],l[4][8],l[5][1],l[6][3],l[7][7],l[7][2],l[8][5]=99,99,99,99,99,99,99,99,99,99
		level+=1
	else:
		print "\n\n\tYou cleared all the level"




	return l


def check(l,r,c):
	count =0
	
	if l[r][c]==99:
		return l
	if r-1>=0 and c-1>=0:
		if l[r-1][c-1]==99:
			count+=1
	if r-1>=0 and c>=0:
		if l[r-1][c]==99:
			count+=1
	if r-1>=0 and c+1<9:
		if l[r-1][c+1]==99:
			count+=1
	if  c-1>=0:
		if l[r][c-1]==99:
			count+=1
	
	if c+1<9:
		if l[r][c+1]==99:
			count+=1
	if r+1<9 and c-1>=0:
		if l[r+1][c-1]==99:
			count+=1
	if r+1<9:
		if l[r+1][c]==99:
			count+=1
	if r+1<9 and c+1<9:
		if l[r+1][c+1]==99:
			count+=1
	if count!=0:
		l[r][c]=count
		return l
	else:
		l[r][c]=10

	if r-1>=0 and c-1>=0:
		if l[r-1][c-1]==0:
			l=check(l,r-1,c-1)
	if r-1>=0 and c>=0:
		if l[r-1][c]==0:
			l=check(l,r-1,c)
		
	if r-1>=0 and c+1<9:
		if l[r-1][c+1]==0:
			l=check(l,r-1,c+1)
	if  c-1>=0:
		if l[r][c-1]==0:
			l=check(l,r,c-1)
	if c+1<9:
		if l[r][c+1]==0:
			l=check(l,r,c+1)
			
	if r+1<9 and c-1>=0:
		if l[r+1][c-1]==0:
			l=check(l,r+1,c-1)
			
	if r+1<9:
		if l[r+1][c]==0:
			l=check(l,r+1,c)
			
	if r+1<9 and c+1<9:
		if l[r+1][c+1]==0:
			l=check(l,r+1,c+1)
	return l	
	

def play(l):
	while True:
		printt(l)
		r=eval(raw_input("Row:"))
		c=eval(raw_input("Column:"))
		if l[r][c]==99:
			print "Game Over"
			printmine(l)
			break	
		l=check(l,r,c)	
		if isWin(l)==1:
			print "\n\n\tYou Win"
			break
	








print "	WELCOME"
l=[[0 for i in range(9)]for i in range(9)]

while True:
	print "1.Play\n4.High Score\n5.Exit: ",
	n=eval(raw_input(" "))
	if n==1:
		l=setmine(l,level)
		play(l)
		l=[[0 for i in range(9)]for i in range(9)]
	elif n==4:
		print level-1," Cleared"
	elif n==5:
		sys.exit()

	else:
		print "Wrong Input"



