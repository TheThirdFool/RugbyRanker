
import csv

a_rank = []
f_rank = []
aa_rank = []
af_rank = []

teama_rank = []
teamf_rank = []
teamaa_rank = []
teamaf_rank = []

def getrank(team):

	switcher = {
	 "IRE": 1,
	 "NZL": 2,
	 "ENG": 3,
	 "RSA": 4,
	 "WAL": 5,
	 "AUS": 6,
	 "SCO": 7,
	 "FRA": 8,
	 "FIJ": 9,
	 "JAP": 10,
	 "ARG": 11,
	 "GEO": 12,
	 "USA": 13,
	 "ITA": 14,
	 "TON": 15,
	 "SAM": 16,
	 "URU": 19,
	 "RUS": 20,
	 "CAN": 22,
	 "NAM": 23,
	}

	return float(switcher.get(team, "-1"))

def getstats(team):
	print("")
	print("")
	print(team, " ----------------")
	teamrank = getrank(team)
	print("Team rank = ", teamrank)

	pointsfor = 0
	pointsagainst = 0
	gamesplayed = 0
	scaled_for = 0
	scaled_against = 0

	with open("RWCScores.txt") as csv_file:
		csvreader = csv.reader(csv_file, delimiter=',')
		for row in csvreader:
			team1 = row[0]
			team2 = row[3]
			score1 = float(row[1])
			score2 = float(row[2])

			if(team1 == team):
				pointsfor = pointsfor + score1
				pointsagainst = pointsagainst + score2
				gamesplayed = gamesplayed + 1
				scaled_for = score1 * (teamrank / getrank(team2)) 
				scaled_against = score2 * (getrank(team2) / teamrank)

			if(team2 == team):
				pointsfor = pointsfor + score2
				pointsagainst = pointsagainst + score1
				gamesplayed = gamesplayed + 1
				scaled_for = score2 * (teamrank / getrank(team1)) 
				scaled_against = score1 * (getrank(team1) / teamrank)

	check = True

	for x in a_rank:
		if (pointsagainst/gamesplayed) < x:
			a_rank.insert(a_rank.index(x), (pointsagainst/gamesplayed))
			teama_rank.insert(a_rank.index(x) -1, team)
			check = False
			break
	if(check):	
		a_rank.append(pointsagainst/gamesplayed)
		teama_rank.append(team)

	check = True
	for x in f_rank:
		if (pointsfor/gamesplayed) > x:
			f_rank.insert(f_rank.index(x), (pointsfor/gamesplayed))
			teamf_rank.insert(f_rank.index(x) -1, team)
			check = False
			break
	if(check):
		f_rank.append(pointsfor/gamesplayed)
		teamf_rank.append(team)

	check = True
	for x in aa_rank:
		if (scaled_against/gamesplayed) < x:
			aa_rank.insert(aa_rank.index(x), (scaled_against/gamesplayed))
			teamaa_rank.insert(aa_rank.index(x) -1, team)
			check = False
			break
	if(check):
		aa_rank.append(scaled_against/gamesplayed)
		teamaa_rank.append(team)

	check = True
	for x in af_rank:
		if (scaled_for/gamesplayed) > x:
			af_rank.insert(af_rank.index(x), (scaled_for/gamesplayed))
			teamaf_rank.insert(af_rank.index(x) -1, team)
			check = False
			break
	if(check):
		af_rank.append(scaled_for/gamesplayed)
		teamaf_rank.append(team)

	print("Points for = ", pointsfor)
	print("  Per game = %1.2f" % (pointsfor/gamesplayed))
	print("  adjusted = %1.2f" % (scaled_for/gamesplayed))
	print("")
	print("Points against = ", pointsagainst)
	print("      Per game = %1.2f" % (pointsagainst/gamesplayed))
	print("      adjusted = %1.2f" % (scaled_against/gamesplayed))
#	print("")
	print("Games played = ", gamesplayed)
	#print("")
	#print("")

def main():

	print("")
	print("What team?")
	team = input("Team = ")

	allteams = [
	 "IRE",
	 "NZL",
	 "ENG",
	 "RSA",
	 "WAL",
	 "AUS",
	 "SCO",
	 "FRA",
	 "FIJ",
	 "JAP",
	 "ARG",
	 "GEO",
	 "USA",
	 "ITA",
	 "TON",
	 "SAM",
	 "URU",
	 "RUS",
	 "CAN",
	 "NAM"
	]

	if(team == "ALL"):
		for x in allteams:
			getstats(x)
	else:
		getstats(team)

	print("")
	print("")

	i = 0
	print("Points against")
	while i < len(a_rank):
		print(i, "\t : ", teama_rank[i], " : %1.2f" % a_rank[i])
		i = i + 1

	print("")
	print("")

	i = 0
	print("Points for")
	while i < len(f_rank):
		print(i, "\t : ", teamf_rank[i], " : %1.2f" % f_rank[i])
		i = i + 1

	print("")
	print("")

	i = 0
	print("Points against ajusted")
	while i < len(aa_rank):
		print(i, "\t : ", teamaa_rank[i], " : %1.2f" % aa_rank[i])
		i = i + 1

	print("")
	print("")

	i = 0
	print("Points for ajusted")
	while i < len(af_rank):
		print(i, "\t : ", teamaf_rank[i], " : %1.2f" % af_rank[i])
		i = i + 1

	print("")
	print("")



main()



