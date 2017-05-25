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
# USER_ENTER = False
# START_GAME = False
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

	# Bot receives message from facebook page.
	if message.get_msg_type() == 'page' and recipient_id:

		global USER_STATE

		# Check record to start a new game or continue an old one.
		if USER_STATE == 'NULL':
			respond = Action.check_record(recipient_id)
			dndbot.send_text_message(recipient_id, respond)
			USER_STATE = 'READY'
			
			return 'ok', 200

		# Game Start
		if USER_STATE == 'READY' and message.get_text() == '是' or '好':
			USER_STATE == 'START'
			dndbot.send_text_message(recipient_id, '遊戲開始')
			return 'ok', 200
		

		# else:
	else:
		return 'No respond', 404
	return 'ok', 200


if __name__ == '__main__':
	
	app.run()



