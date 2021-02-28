import matplotlib.pyplot as plt
import sys
if __name__ == "__main__":

	# aus Text-Datei lesen
	try:
		file = open("data.txt", "r")
		lines = file.readlines()
	except:
		print("Keine Dabei gefunden!")
		sys.exit(0)

	# save lines to list
	avg_fit_list = list()
	best_fit_list = list()
	worst_fit_list = list()
	time_list = list()

	for line in lines:
		line = line.split(",")
		avg_fit_list.append(float(line[0]))
		best_fit_list.append(float(line[1]))
		worst_fit_list.append(float(line[2]))
		time_list.append(float(line[3]))

	fig = plt.figure(figsize=(6, 4))
	# avg fitness
	sub1 = fig.add_subplot(221) # statt plt.subplot(2, 2, 1)
	sub1.set_title('Durchschnittl. Fitness') 
	sub1.plot(avg_fit_list)
	sub1.set_ylabel('Durchschnittliche Fitness')
	sub1.set_xlabel('Generation')
	# beste fitness
	sub2 = fig.add_subplot(222)
	sub2.set_title('Beste Fitness')
	sub2.plot(best_fit_list)
	sub2.set_ylabel('Beste Fitness')
	sub2.set_xlabel('Generation')
	# worst fitness
	sub3 = fig.add_subplot(223)
	sub3.set_title('Schlechteste Fitness')
	sub3.plot(worst_fit_list)
	sub3.set_ylabel('Schlechteste Fitness')
	sub3.set_xlabel('Generation')
	# time
	sub4 = fig.add_subplot(224)
	sub4.set_title('Zeit')
	sub4.plot(time_list)
	sub4.set_ylabel('Zeit')
	sub4.set_xlabel('Generation')
	#plt.plot(t, g(t))
	plt.tight_layout()
	plt.show()


	"""
	# Graphen ausgeben
	for werte in ([avg_fit_list, 'Durchschnittliche Fitness', "Entwicklung der Fitness"], [best_fit_list, 'Beste Fitness', "Entwicklung der besten Fitness"], [worst_fit_list, 'Schlechteste Fitness', "Entwicklung der Schlechtesten Fitness"],
	 [time_list, 'Zeit', "Entwicklung der benoetigten Zeit für die Generation"]):
		plt.plot(werte[0])
		plt.ylabel(werte[1])
		plt.xlabel('Generation')
		plt.title(werte[2])
		plt.show()"""
