# -*- coding: UTF-8 -*-
import re
import json
from flask import Flask, request
from pymessenger.bot import Bot

from Action import Action
from setting import ACCESS_TOKEN
from MsgParser import MsgParser

app = Flask(__name__)
dndbot = Bot(ACCESS_TOKEN)

# 20170525 Y.D.: User's game state.
USER_STATE = 'NULL'

@app.route('/', methods = ['GET'])
def verify():
	# Webhook verification
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == ACCESS_TOKEN:
			return "Failed validation. Make sure the validation tokens match.", 403
		return request.args["hub.challenge"], 200
	return "Hello", 200

@app.route('/', methods=['POST'])
def listen():
	message = request.get_json()
	message = MsgParser(message)
	recipient_id = message.get_sender()
	message_text = message.get_text()
	
	# Bot receives message from facebook page.
	if message.get_msg_type() == 'page' and recipient_id:
		global USER_STATE
		
		## Basic Game Operation
		# Check record to start a new game or continue an old one.
		if USER_STATE == 'NULL':
			USER_STATE = 'READY'
			respond = Action.check_saved_game(recipient_id)
			dndbot.send_text_message(recipient_id, respond)

		# Users leave game without playing
		elif (USER_STATE == 'READY' or USER_STATE == 'RUNNING') and message_text == u'不':
			USER_STATE = 'NULL'
			dndbot.send_text_message(recipient_id, '那就再見囉～')

		# Game running
		elif USER_STATE == 'READY' and message_text == u'是':
			USER_STATE = 'RUNNING'
			respond = Action.start_game(recipient_id)
			dndbot.send_text_message(recipient_id, respond)
			
		# Game Ends
		elif USER_STATE == 'RUNNING' and message_text == u'掰':
			USER_STATE = 'NULL'
			dndbot.send_text_message(recipient_id, '遊戲已經儲存，歡迎下次再來！')

		## 	
		

	return 'ok', 200


if __name__ == '__main__':
	
	app.run()



