import schedule
import time
import SendMessage
import GetDataFromESPN
import GetESPNData

def postdata(msg: str):
    SendMessage.send_discord_message(GetESPNData.RetrieveData(msg),'889659224500609067')

schedule.every().sunday.at("16:00:00").do(postdata, msg = "Scores")
schedule.every().sunday.at("16:00:01").do(postdata, msg = "Projections")

schedule.every().sunday.at("20:00:00").do(postdata, msg = "Scores")
schedule.every().sunday.at("20:00:01").do(postdata, msg = "Projections")

schedule.every().monday.at("07:30:00").do(postdata, msg = "Scores")
schedule.every().monday.at("07:30:01").do(postdata, msg = "Projections")
schedule.every().monday.at("18:30").do(postdata, msg = "Close Scores")

schedule.every().tuesday.at("07:30:00").do(postdata, msg = "Final Scores")
schedule.every().tuesday.at("07:30:01").do(postdata, msg = "Trophies")
schedule.every().tuesday.at("18:30").do(postdata, msg = "Power Rankings")

schedule.every().wednesday.at("07:30").do(postdata, msg = "Current Standings")

schedule.every().thursday.at("19:30:00").do(postdata, msg = "Match Ups")
schedule.every().thursday.at("19:30:01").do(postdata, msg = "Projections")

schedule.every().friday.at("07:30:00").do(postdata, msg = "Scores")
schedule.every().friday.at("07:30:01").do(postdata, msg = "Projections")

while True:
    schedule.run_pending()
    time.sleep(1)
