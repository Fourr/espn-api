from espn_api.football import League
from decimal import *
from typing import List

def RetrieveData(msg: str):
	league = League(league_id= 1082411793, year=2022, espn_s2 = 'AEBFYq2%2Bcr45uiDMebG2kPfWoI0QmsEEF66soC1%2FWQ%2FuA4j2LpOPLZDZNpbHmkAa44Es296hMr4pjbdf0Rx0NcLtc%2FhSlo8a%2B528y8QBOrUer5esCRJr00U84jMawcTgb1OFDng1Rzq7z6THAQz620%2FYoDvCPZcOxlqGtDBOM7sx0zXAVgrjfMmdU7al7m2HFRoK2SdIASD9WFObY1rm5vFnndeMSjCKWJJmli6Qx2Qkk%2FvpV%2FwzpoTE9tyfIvpM2JlUf4ZOSI2El9U72QzUW0xn0lYOcVPw9uIN1sOrmKXh5GU2mxeT%2F0HnvXwIKpt5QPfbR8R7Vuj1fMKJF6BgeIBX', swid = '{34271226-9219-4E25-AA2B-EB4F06085729}' )

	if msg == "Final Scores" or msg == "Trophies":
		league_scores = league.box_scores(week = league.current_week - 1)

	else:
		league_scores = league.box_scores()
	message = "```" + msg + ":\n"

	if msg == "Power Rankings":
		power_rankings = league.power_rankings()

		printable_pr = "```Power Rankings:\n" 
		for x in power_rankings:
			printable_pr +=  str(x[0]) + " - " + x[1].team_name + "\n"
		printable_pr += "```"
		return printable_pr

	if msg == "Current Standings":
		standings = league.standings()
		y = 1
		printable_standings = "```Current Standings:\n" 
		for x in standings:

			printable_standings += str(y) + ": " + x.team_name +  " (" + str(x.wins) +  " - " + str(x.losses) + ") " + "Streak: " + x.streak_type + " " + str(x.streak_length) + "\n"
			y += 1
		printable_standings += "```"
		return printable_standings

	if msg == "Match Ups":
		scoreboard = league.scoreboard()
		printable_scoreboard = "```This Week's Match Ups:\n"
		for x in scoreboard:
			printable_scoreboard += x.home_team.team_name +  " (" + str(x.home_team.wins) +  " - " + str(x.home_team.losses) + ") vs " + x.away_team.team_name +  " (" + str(x.away_team.wins) +  " - " + str(x.away_team.losses) + ")\n"
		printable_scoreboard += "```"
		return printable_scoreboard
	teams = {}
	closescore = blowoutscore = 0
	for x in league_scores:

		teamOneLineUp = x.home_lineup
		teamTwoLineUp = x.away_lineup

		teamOne = x.home_team.team_name
		teamTwo = x.away_team.team_name

		if msg == "Projections" or msg == "Close Scores":
			teamOneScore = x.home_projected
			teamTwoScore = x.away_projected
		else:
			teamOneScore = x.home_score
			teamTwoScore = x.away_score

		if teamTwoScore > teamOneScore:
			teamThree = teamOne
			teamOne = teamTwo
			teamTwo = teamThree

			teamThreeScore = teamOneScore
			teamOneScore = teamTwoScore
			teamTwoScore = teamThreeScore


		if msg == "Close Scores":
			if abs(teamOneScore - teamTwoScore) <= 16 and (NotEveryonePlayed(teamTwoLineUp) or NotEveryonePlayed(teamOneLineUp)):
				message += teamOne + " (" + str(teamOneScore) + ") vs " + teamTwo + " (" + str(teamTwoScore) + ") \n"
		elif msg == "Trophies": 
			teams[teamOne] = teamOneScore
			teams[teamTwo] = teamTwoScore
			scorediff = Decimal(str(teamOneScore)) - Decimal(str(teamTwoScore))
			if closescore == 0 and blowoutscore == 0:
				closewinner = blowoutwinner = teamOne
				closeloser = blowoutloser = teamTwo
				closescore = blowoutscore = scorediff 

			elif closescore > scorediff:
				closewinner = teamOne
				closeloser = teamTwo
				closescore = scorediff

			elif blowoutscore < scorediff:
				blowoutwinner = teamOne
				blowoutloser = teamTwo
				blowoutscore = scorediff 

		else:
			message += teamOne + " (" + str(teamOneScore) + ") vs " + teamTwo + " (" + str(teamTwoScore) + ") \n"

	if msg == "Trophies":

		lowestpoints = min(teams.values())
		highestpoints = max(teams.values())

		lowestname = (list(teams.keys())[list(teams.values()).index(lowestpoints)])
		highestname = (list(teams.keys())[list(teams.values()).index(highestpoints)])


		message += "Lowest Score: " + lowestname + " with " + str(lowestpoints) + " points\n"
		message += "Highest Score: " + highestname + " with " + str(highestpoints) + " points\n"
		message += closewinner + " barely beat " + closeloser + " by a margin of " + str(closescore) + " points\n"
		message += blowoutwinner + " destroyed " + blowoutloser + " by " + str(blowoutscore) + " points\n"

	message = message + "```"


	return message



def NotEveryonePlayed(team: List):
	for x in team:
		if(x.slot_position != "BE" and x.slot_position != "IR" and x.game_played == 0):	
			return True
	return False

