from json import load, dump
from os import system
from getpass import getpass
from time import sleep

fileUser = 'user.json'
fileGrade = 'grade.json'

user = {}
grade = {}

def loadData():
		global user, grade

		with open(fileUser) as f:
				user = load(f)

		with open(fileGrade) as f:
				grade = load(f)

		return True

def saveData():
		global user, grade

		with open(fileUser, 'w') as f:
				dump(user, f)

		with open(fileGrade, 'w') as f:
				dump(grade, f)

		return True

def login():
		counter = 1
		Username = input('Enter Username : ')
		Password = getpass('Enter Password : ')
		dataCheck = False
		passLogin = False
		if Username in user:
				dataCheck = True
				passLogin = (user[Username] == Password)

		while (not dataCheck) or (not passLogin):
				counter += 1
				if counter > 3:
						return False
				print('Combination Username and Password is Wrong')
				Username = input('Enter Username : ')
				Password = getpass('Enter Password : ')
				if Username in user :
						dataCheck = True
						passLogin = (user[Username] == Password)
		else:
				print('Login Pass')
				return True

def print_menu():
		print('Welcome to Grade Apps')
		print('1. Print grade')
		print('2. Add A grade')
		print('3. Remove A grade')
		print('4. Lookup A grade')
		print('5. Change A grade')
		print('Q. Quit')

def print_grade():
	if len(grade) > 0:
		for info in grade:
				print(f'Name \t: {info}| UH\t: {grade[info][0]} | PTS\t: {grade[info][1]} | PAS\t: {grade[info][2]}')
	else:
		print('There is no grade available right now.')

def add_grade():
	list_grade = []
	print('Add your grade\n')

	name = input('Name \t:')
	exam = input('Score UH \t:')
	list_grade.append(exam)
	exam = input('Score PTS \t:')
	list_grade.append(exam)
	exam = input('Score PAS \t:')
	list_grade.append(exam)
	grade[name] = list_grade
	saveData()
	print('Saving Data ...')
	sleep(1.5)
	print('Data Saved.')

def remove_grade():
	print('Remove a fileGrade\n')

	name = input('Name \t:')

	if name in grade:
		del grade[name]
		saveData()
		print('Removing Data ...')
		sleep(1.5)
		print('Data Saved.')
	else:
		print(f'{name} doesnot exists in contact')

def lookup_grade():
	print('Lookingup a grade\n')

	name = input('Name \t:')

	if name in grade:
		print(f'Name \t: {name}\t Exam \t:{grade[name]}')

	else:
		print(f'{name} doesnot exists in contact')

def change_grade():
	print('Changing a grade\n')

	name = input('Name \t:')
	
	if name in grade:
		pilihanGrade = input("What grade do you want to change : ")
		if(pilihanGrade == "UH"):
			print(f'old grade = {grade[name][0]}')
			exam = input('New grade = ')
		
			grade[name][0] = exam
		
			saveData()
			print('Saving Data ...')
			sleep(1.5)
			print('Data Saved.')
		elif(pilihanGrade == "PTS"):
			print(f'old grade = {grade[name][1]}')
			exam = input('New grade = ')
		
			grade[name][1] = exam
		
			saveData()
			print('Saving Data ...')
			sleep(1.5)
			print('Data Saved.')
		elif(pilihanGrade == "PAS"):
			print(f'old grade = {grade[name][2]}')
			exam = input('New grade = ')
		
			grade[name][2] = exam
		
			saveData()
			print('Saving Data ...')
			sleep(1.5)
			print('Data Saved.')
		else:
			print(f'{pilihanGrade} doesnot exists')
	else:
		print(f'{name} doesnot exists in contact')
