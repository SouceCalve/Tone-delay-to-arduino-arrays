notes=[]
duration=[]
delaynotes=[]
delayprev=False
def parsenotes():
	inputfile="./"+input("Вход:")
	f = open(inputfile)
	for line in f:
		parslin=line[4:9]
		#print(parslin)
		if parslin=="tone(":
			#print("note!",line[18:21])
			notes.append(line[18:21])
			duration.append(str(line[23:29]).replace(');','',1).replace(')','',1))
			delayprev=False
		elif parslin=="delay":
			if delayprev==True:
				#print(line[10:24])
				delaynotes[-1]=str(float(delaynotes[-1])+float(str(line[10:24]).replace(');','',1).replace(')','',1).replace('\n','')))
			if delayprev==False:
				#print("duration",line[10:22])
				delaynotes.append(str(line[10:24]).replace(');','',1).replace(')','',1).replace('\n','')) #добавить проверку множественых delay'в
				delayprev=True
	f.close()
	print("Готово!")
	return

def output():
        outputfile="./"+input("Выход:")
        f=open(outputfile,"w")
        f.write(str(notes).replace("'","").replace("[","{").replace("]","}")+'\n')
        f.write(str(duration).replace("'","").replace("[","{").replace("]","}")+'\n')
        f.write(str(delaynotes).replace("'","").replace("[","{").replace("]","}")+'\n')
        print("Готово!")
        return

print("Конвертер tone-duration-delay спагетити в отдельные массивы")
while(1):
	print("Выберите режим:")
	print("1:Ввод txt с tone-delay конструкциями")
	print("2:Вывод массивов в файл")
	print("3:Выход")
	choice=int(input(":"))
	if choice==1:
		parsenotes()
	elif choice==2:
		output()
	elif choice==3:
		break
	else:
		print("Фигня какая-то, вводи по новой")
print("Давай!")

