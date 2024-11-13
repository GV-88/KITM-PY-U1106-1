import random

kiekGalimaPaimtiMin = 1
kiekGalimaPaimtiMax = 3

zaidziam = True
while zaidziam:
	print('Pradėkime žaidimą!')
	kiekLiko = input('Kiek akmenų maiše? (jei nepateiksit skaičiaus, aš sugalvosiu)...')
	if(kiekLiko.isnumeric()):
		kiekLiko = int(kiekLiko)
	else:
		kiekLiko = random.randint(15, 30)
	
	print(f'Maiše yra {kiekLiko} akmenys.')
	zaidejoEile = True
	while kiekLiko > 0:
		# print(f'Maiše yra {kiekLiko} akmenys.')
		traukiam = ''
		if (zaidejoEile):
			while not (traukiam.isnumeric() and kiekGalimaPaimtiMin <= int(traukiam) <= kiekGalimaPaimtiMax):
				traukiam = input(f'Įveskite, kiek akmenų norite paimti ({kiekGalimaPaimtiMin}–{kiekGalimaPaimtiMax}):...')
			traukiam = int(traukiam)
		else:
			traukiam = random.randint(kiekGalimaPaimtiMin, kiekGalimaPaimtiMax)
		kiekLiko -= traukiam
		print(f'{"Jūs paėmėte" if zaidejoEile else "Kompiuteris paėmė"} {traukiam} akmenis. Liko {kiekLiko} akmenų.')
		zaidejoEile = not zaidejoEile
	print(not zaidejoEile)
	zaidziam = input('Ar norėtumėte žaisti dar kartą? (taip/ne)').lower() in (['t', 'taip'])
print('viso gero')
