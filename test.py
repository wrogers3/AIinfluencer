from instabot import Bot

#gotta put them somewhere safe

#pubes
#nail clipping
#bathwater
#
username = 'ivankanowak'
password = 'In270205'

gptstring = 'this summer is hot af'
hookstring = '                       #model #hot #beauty #fyp #delicious #young #18+ #sugarpie #facial #youthful #kissme #free #howto #fitness #sexy #polish #girl'

bot = Bot()


bot.login(username= username, password= password)

bot.upload_photo('test.png', caption=gptstring + hookstring)

bot.logout()
