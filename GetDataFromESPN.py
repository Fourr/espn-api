from espn_api.football import League

def get_scores():

	league = League(league_id= 1082411793, year=2021, espn_s2 = 'AEBFYq2%2Bcr45uiDMebG2kPfWoI0QmsEEF66soC1%2FWQ%2FuA4j2LpOPLZDZNpbHmkAa44Es296hMr4pjbdf0Rx0NcLtc%2FhSlo8a%2B528y8QBOrUer5esCRJr00U84jMawcTgb1OFDng1Rzq7z6THAQz620%2FYoDvCPZcOxlqGtDBOM7sx0zXAVgrjfMmdU7al7m2HFRoK2SdIASD9WFObY1rm5vFnndeMSjCKWJJmli6Qx2Qkk%2FvpV%2FwzpoTE9tyfIvpM2JlUf4ZOSI2El9U72QzUW0xn0lYOcVPw9uIN1sOrmKXh5GU2mxeT%2F0HnvXwIKpt5QPfbR8R7Vuj1fMKJF6BgeIBX', swid = '{34271226-9219-4E25-AA2B-EB4F06085729}' )
	scores = league.box_scores()
	boxscores = "```Score Update: \n"

	for x in scores:
		teamOne = x.home_team.team_name
		teamTwo = x.away_team.team_name
		teamOneScore = x.home_score
		teamTwoScore = x.away_score

		if teamTwoScore > teamOneScore:
			teamThree = teamOne
			teamOne = teamTwo
			teamTwo = teamThree

			teamThreeScore = teamOneScore
			teamOneScore = teamTwoScore
			teamTwoScore = teamThreeScore

		boxscores = boxscores + teamOne + " **" + str(teamOneScore) + "** vs " + teamTwo + " **" + str(teamTwoScore) + "**"+ "\n" #bold on scores

	boxscores = boxscores + "```"
	return boxscores
def get_scores_projections():

	projection = get_scores()
	league = League(league_id= 1082411793, year=2021, espn_s2 = 'AEBFYq2%2Bcr45uiDMebG2kPfWoI0QmsEEF66soC1%2FWQ%2FuA4j2LpOPLZDZNpbHmkAa44Es296hMr4pjbdf0Rx0NcLtc%2FhSlo8a%2B528y8QBOrUer5esCRJr00U84jMawcTgb1OFDng1Rzq7z6THAQz620%2FYoDvCPZcOxlqGtDBOM7sx0zXAVgrjfMmdU7al7m2HFRoK2SdIASD9WFObY1rm5vFnndeMSjCKWJJmli6Qx2Qkk%2FvpV%2FwzpoTE9tyfIvpM2JlUf4ZOSI2El9U72QzUW0xn0lYOcVPw9uIN1sOrmKXh5GU2mxeT%2F0HnvXwIKpt5QPfbR8R7Vuj1fMKJF6BgeIBX', swid = '{34271226-9219-4E25-AA2B-EB4F06085729}' )
	scores = league.box_scores()
	projection = projection + "```\nProjections:\n"

	for x in scores:
		teamOne = x.home_team.team_name
		teamTwo = x.away_team.team_name
		teamOneProj = x.home_projected
		teamTwoProj = x.away_projected

		if teamTwoProj > teamOneProj:
			teamThree = teamOne
			teamOne = teamTwo
			teamTwo = teamThree

			teamThreeProj = teamOneProj
			teamOneProj = teamTwoProj
			teamTwoProj = teamThreeProj

		projection = projection + teamOne + " **" + str(teamOneProj) + "** vs " + teamTwo + " **" + str(teamTwoProj) + "**"+ "\n" #bold on scores

	projection = projection + "```"
	return projection

def close_scores():
	league = League(league_id= 1082411793, year=2021, espn_s2 = 'AEBFYq2%2Bcr45uiDMebG2kPfWoI0QmsEEF66soC1%2FWQ%2FuA4j2LpOPLZDZNpbHmkAa44Es296hMr4pjbdf0Rx0NcLtc%2FhSlo8a%2B528y8QBOrUer5esCRJr00U84jMawcTgb1OFDng1Rzq7z6THAQz620%2FYoDvCPZcOxlqGtDBOM7sx0zXAVgrjfMmdU7al7m2HFRoK2SdIASD9WFObY1rm5vFnndeMSjCKWJJmli6Qx2Qkk%2FvpV%2FwzpoTE9tyfIvpM2JlUf4ZOSI2El9U72QzUW0xn0lYOcVPw9uIN1sOrmKXh5GU2mxeT%2F0HnvXwIKpt5QPfbR8R7Vuj1fMKJF6BgeIBX', swid = '{34271226-9219-4E25-AA2B-EB4F06085729}' )

	scores = league.box_scores()
	boxscores = "```Close Scores: \n"
	for x in scores:
		teamOne = x.home_team.team_name
		teamTwo = x.away_team.team_name
		teamOneScore = x.home_score
		teamTwoScore = x.away_score

		if teamTwoScore > teamOneScore:
			teamThree = teamOne
			teamOne = teamTwo
			teamTwo = teamThree

			teamThreeScore = teamOneScore
			teamOneScore = teamTwoScore
			teamTwoScore = teamThreeScore

		if abs(teamOneScore - teamTwoScore) <=16:
			boxscores = boxscores + teamOne + " **" + str(teamOneScore) + "** vs " + teamTwo + " **" + str(teamTwoScore) + "**"+ "\n"
	boxscores = boxscores + "```"

def trophies():
	league = League(league_id= 1082411793, year=2021, espn_s2 = 'AEBFYq2%2Bcr45uiDMebG2kPfWoI0QmsEEF66soC1%2FWQ%2FuA4j2LpOPLZDZNpbHmkAa44Es296hMr4pjbdf0Rx0NcLtc%2FhSlo8a%2B528y8QBOrUer5esCRJr00U84jMawcTgb1OFDng1Rzq7z6THAQz620%2FYoDvCPZcOxlqGtDBOM7sx0zXAVgrjfMmdU7al7m2HFRoK2SdIASD9WFObY1rm5vFnndeMSjCKWJJmli6Qx2Qkk%2FvpV%2FwzpoTE9tyfIvpM2JlUf4ZOSI2El9U72QzUW0xn0lYOcVPw9uIN1sOrmKXh5GU2mxeT%2F0HnvXwIKpt5QPfbR8R7Vuj1fMKJF6BgeIBX', swid = '{34271226-9219-4E25-AA2B-EB4F06085729}' )

	scores = league.box_scores()
	finalscores = "```Final Score Update: \n"
	for x in scores:
		teamOne = x.home_team.team_name
		teamTwo = x.away_team.team_name
		teamOneScore = x.home_score
		teamTwoScore = x.away_score

		if teamTwoScore > teamOneScore:
			teamThree = teamOne
			teamOne = teamTwo
			teamTwo = teamThree

			teamThreeScore = teamOneScore
			teamOneScore = teamTwoScore
			teamTwoScore = teamThreeScore

		finalscores = finalscores + teamOne + " **" + str(teamOneScore) + "** vs " + teamTwo + " **" + str(teamTwoScore) + "**"+ "\n" #bold on scores

	finalscores = finalscores + "\nTrophies:\n"
	low_score = "Lowest Score: " + " " + " "


	finalscores = finalscores + "```"

