from instabot import Bot
import gptstring

#gotta put them somewhere safe

gptstring = ''
def post(username, password, folder, caption):
    #with the given folder, go and post every picture there is
    hookstring = '#model #hot #beauty #fyp #delicious #young #18+ #sugarpie #facial #youthful #kissme #free #howto #fitness #sexy #teen #girl'
    bot = Bot()
    bot.login(username= username, password= password)
    bot.upload_photo('test.png', caption=caption + hookstring)
    #move the pic from this folder to the uploaded repo which is inside the models main repo
    bot.logout()
