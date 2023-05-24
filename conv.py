notes=[]
duration=[]
delaynotes=[]
delayprev=False
tonecounter=0
delaycounter=0
def sumforcheck(name):
	sum=0
	for i in name:
		sum+=float(i)
	return(sum/1000)

def parsenotes():
	global delaycounter
	global tonecounter
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
			tonecounter+=1
		elif parslin=="delay":
			if delayprev==True:
				#print(line[10:24])
				delaynotes[-1]=str(float(delaynotes[-1])+float(str(line[10:24]).replace(');','',1).replace(')','',1).replace('\n','')))
			if delayprev==False:
				#print("duration",line[10:22])
				delaynotes.append(str(line[10:24]).replace(');','',1).replace(')','',1).replace('\n',''))
				delayprev=True
			delaycounter+=1
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

print("Конвертер tone-duration-delay спагетти в отдельные массивы")
while(1):
	print("")
	if (tonecounter>0 and delaycounter>0):
		print("Статус: Массив загружен, ожидание вывода...")
		print("Размер массивов в памяти: "+str(2*tonecounter+4*tonecounter+4*delaycounter)+"KB")
		if(sumforcheck(duration)>sumforcheck(delaynotes)):
			if round(sumforcheck(duration))>60:
				print("Длительность мелодии: "+str(round(sumforcheck(duration))/60)+" минут "+str(round(sumforcheck(duration))%60)+" секунд")
			else:
				print("Длительность мелодии: "+str(round(sumforcheck(duration)))+" секунд")
		else:
			if round(sumforcheck(delaynotes))>60:
				print("Длительность мелодии: "+str(round(sumforcheck(delaynotes))/60)+" минут "+str(round(sumforcheck(delaynotes))%60)+" секунд")
			else:
				print("Длительность мелодии: "+str(round(sumforcheck(delaynotes)))+" секунд") 
	else:
		print("Статус: Массив ещё не загружен. Выполните ввод файла.")
	print("")
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

