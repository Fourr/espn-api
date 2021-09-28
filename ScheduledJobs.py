import schedule
import time
import SendMessage
import GetDataFromESPN

def scores(func):

    SendMessage.send_discord_message(GetDataFromESPN.get_scores(),'889659224500609067')

def projections():
    SendMessage.send_discord_message(GetDataFromESPN.get_scores_projections(),'889659224500609067')


schedule.every(10).seconds.do(projections)

schedule.every().sunday.at("16:00").do(projections)
schedule.every().sunday.at("20:00").do(projections)
schedule.every().monday.at("07:30").do(projections)
schedule.every().friday.at("07:30").do(projections)

schedule.every().tuesday.at("7:30").do(scores)


while True:
    schedule.run_pending()
    time.sleep(1)
