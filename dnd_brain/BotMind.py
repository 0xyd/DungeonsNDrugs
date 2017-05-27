# -*- coding: UTF-8 -*-
import re
import json
from flask import Flask, request
from pymessenger.bot import Bot

from Action import Action
from setting import ACCESS_TOKEN, VERIFIED_TOKEN
from MsgParser import MsgParser

app = Flask(__name__)
dndbot = Bot(ACCESS_TOKEN)

# 20170525 Y.D.: User's game state.
USER_STATE = 'NULL' # Player's Game State
CHAR_STATE = {}     # Player's Character State

@app.route('/', methods = ['GET'])
def verify():
	# Webhook verification
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFIED_TOKEN:
			return "Failed validation. Make sure the validation tokens match.", 403
		return request.args["hub.challenge"], 200
	return "Hello", 200

@app.route('/', methods=['POST'])
def listen():
	message = request.get_json()
	message = MsgParser(message)
	recipient_id = message.get_sender()
	message_text = message.get_text()
	
	# Bot receives message from facebook page and only respond to human message.
	if message.get_msg_type() == 'page' and message.is_echo() == False:

		global USER_STATE
		global CHAR_STATE
		
		## Basic Game Operation
		# Check record to start a new game or continue an old one.
		if USER_STATE == 'NULL':
			
			act_result = Action.check_saved_game(recipient_id)
			respond    = act_result['message']
			CHAR_STATE = act_result['character']
			USER_STATE = 'READY'

			dndbot.send_text_message(recipient_id, respond)

		# Users leave game without playing
		elif (USER_STATE == 'READY' or USER_STATE == 'RUNNING') and message_text == u'不':
			USER_STATE = 'NULL'
			dndbot.send_text_message(recipient_id, '那就再見囉～')

		# Game running
		elif USER_STATE == 'READY' and message_text == u'是':
			USER_STATE = 'RUNNING'
			act_result = Action.start_game(recipient_id)
			respond    = act_result['message']
			CHAR_STATE = act_result['character']
			dndbot.send_text_message(recipient_id, respond)
			
		# Game Ends
		elif (USER_STATE == 'RUNNING' or USER_STATE == 'DECIDING') and message_text == u'掰':
			USER_STATE = 'NULL'
			Action.save_game(CHAR_STATE)
			dndbot.send_text_message(recipient_id, '遊戲已經儲存，歡迎下次再來！')

		## MUST GO THROUGH PROCESS

		## The Processes while gaming 
		else:
			make_decision(recipient_id, message_text)
			

	return 'ok', 200


def make_decision(recipient_id, message_text):

	global USER_STATE
	global CHAR_STATE
	global dndbot
	
	if USER_STATE == 'DECIDING':

		# 1: 闖蕩江湖
		# 2: 販賣毒品
		# 3: 購買毒品
		# 4: 移動
		if message_text == '1':
			dndbot.send_text_message(recipient_id, '開始行動1')

		elif message_text == '2':
			dndbot.send_text_message(recipient_id, '開始行動2')
			### For testing purpose
			### TODO: Select Drugs to sell
			transaction = [('安非他命', 4000, 2)]
			###
			action_result = Action.sell_drugs(CHAR_STATE, transaction)

			if action_result[0]:
				come_across_randevt(recipient_id, action_result[1])
				# dndbot.send_text_message(recipient_id, action_result[1])

		elif message_text == '3':
			dndbot.send_text_message(recipient_id, '開始行動3')
		elif message_text == '4':
			dndbot.send_text_message(recipient_id, '開始行動4')
		
		USER_STATE = 'RUNNING'	

	elif USER_STATE == 'RUNNING':
		dndbot.send_text_message(
			recipient_id, '選擇行動:\n 1) 闖蕩江湖\n 2) 販賣毒品\n 3) 購買毒品\n 4) 移動')

		USER_STATE = 'DECIDING'


def come_across_randevt(recipient_id, event):

	global dndbot

	dndbot.send_text_message(recipient_id, event)
	#### Have to display view for users to play dice
	dndbot.send_text_message(recipient_id, '請躑骰子')



if __name__ == '__main__':
	
	app.run()



