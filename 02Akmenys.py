import random

def pritaikytiLinksni(skaicius, vienas, keli, daug):
	skaicius = abs(skaicius)
	if skaicius != 11 and skaicius % 10 == 1:
		return vienas
	elif (11 <= skaicius <= 19) or skaicius % 10 == 0:
		return daug
	return keli

def traukimas(tmin, tmax, paskutinisLaimi, kiekLiko):
	# galima dar tobulinti algoritmą...
	if(paskutinisLaimi and kiekLiko <= tmax):
		return kiekLiko # stveriu paskutinius kada tik galiu
	if(paskutinisLaimi and kiekLiko - (tmin + tmax * 1) <= tmax):
		return max(kiekLiko - (tmin + tmax * 1), tmin) # stengiuosi palikti tmin + tmax * 1
	if(paskutinisLaimi and kiekLiko - (tmin + tmax * 2) <= tmax):
		while True:
			t = random.randint(tmin, tmax)
			if (t != kiekLiko - (tmin + tmax * 2)): # stengiuosi nepalikti tmin + tmax * 2
				break
		return t
	if(paskutinisLaimi and kiekLiko - (tmin + tmax * 3) <= tmax):
		return max(kiekLiko - (tmin + tmax * 3), tmin) # stengiuosi palikti tmin + tmax * 3 (kad paskui man paliktų tmin + tmax * 2)
	return random.randint(tmin, tmax)

taisykles = {
	'kiekGalimaPaimtiMin': 1,
	'kiekGalimaPaimtiMax': 3,
	'paskutinisLaimi': True
}

zaidziam = True
while zaidziam:
	print('Pradėkime žaidimą!')
	kiekLiko = input('Kiek akmenų maiše? (jei nepateiksit skaičiaus, aš sugalvosiu)...')
	if(kiekLiko.isnumeric()):
		kiekLiko = int(kiekLiko)
	else:
		kiekLiko = random.randint(15, 30)
	
	print(f"Maiše yra {kiekLiko} {pritaikytiLinksni(kiekLiko, 'akmuo','akmenys','akmenų')}.")
	zaidejoEile = True
	while kiekLiko > 0:
		# print(f"Maiše yra {kiekLiko} {pritaikytiLinksni(kiekLiko, 'akmuo','akmenys','akmenų')}.")
		traukiam = ''
		if (zaidejoEile):
			while not (traukiam.isnumeric() and taisykles['kiekGalimaPaimtiMin'] <= int(traukiam) <= taisykles['kiekGalimaPaimtiMax']):
				traukiam = input(f"Įveskite, kiek akmenų norite paimti ({taisykles['kiekGalimaPaimtiMin']}–{taisykles['kiekGalimaPaimtiMax']}):...")
			traukiam = int(traukiam)
		else:
			traukiam = traukimas(taisykles['kiekGalimaPaimtiMin'], taisykles['kiekGalimaPaimtiMax'], taisykles['paskutinisLaimi'], kiekLiko)
		kiekLiko -= traukiam
		print(f"{'Jūs paėmėte' if zaidejoEile else 'Kompiuteris paėmė'} {traukiam} {pritaikytiLinksni(traukiam, 'akmenį','akmenis','akmenų')}.", end=' ')
		print(f"Liko {kiekLiko} {pritaikytiLinksni(kiekLiko, 'akmuo','akmenys','akmenų')}.")
		zaidejoEile = not zaidejoEile
	# kadangi zaidejoEile pasikeičia ėjimo pabaigoje ciklo viduje, tai po paskutinio ciklo tenka tikrinti kieno eilė buvo prieš pasikeitimą;
	# šito būtų galima išvengti keitimą darant ėjimo pradžioje, bet tada klaidinančiai atrodytų pradinis nustatymas kas pradeda žaidimą;
	print('Jūs paėmėte paskutinį akmenį!' if (not zaidejoEile) else 'Kompiuteris paėmė paskutinį akmenį!', end=' ')
	print('Jūs laimėjote!' if ((not zaidejoEile) == taisykles['paskutinisLaimi']) else 'Jūs pralaimėjote!')
	zaidziam = input('Ar norėtumėte žaisti dar kartą? (taip/ne)').lower() in (['t', 'taip'])
print('viso gero')
