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
GAME_STATE = 'NULL' # Player's Game State
CHAR_STATE = {}     # Player's Character State
RAND_EVENT = None

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

		global GAME_STATE
		global CHAR_STATE
		global RAND_EVENT
		
		## Basic Game Operation
		# Check record to start a new game or continue an old one.
		if GAME_STATE == 'NULL':
			
			act_result = Action.check_saved_game(recipient_id)
			respond    = act_result['message']
			CHAR_STATE = act_result['character']
			GAME_STATE = 'READY'

			dndbot.send_text_message(recipient_id, respond)

		# Users leave game without playing
		elif (GAME_STATE == 'READY' or GAME_STATE == 'RUNNING') and message_text == u'不':
			GAME_STATE = 'NULL'
			dndbot.send_text_message(recipient_id, '那就再見囉～')

		# Game running
		elif GAME_STATE == 'READY' and message_text == u'是':
			GAME_STATE = 'RUNNING'
			act_result = Action.start_game(recipient_id)
			respond    = act_result['message']
			CHAR_STATE = act_result['character']
			dndbot.send_text_message(recipient_id, respond)
			
		# Game Ends
		elif (GAME_STATE == 'RUNNING' or GAME_STATE == 'DECIDING') and message_text == u'掰':
			GAME_STATE = 'NULL'
			Action.save_game(CHAR_STATE)
			dndbot.send_text_message(recipient_id, '遊戲已經儲存，歡迎下次再來！')

		## MUST GO THROUGH PROCESS

		## Working
		# Use the dice to determine ur fate!
		elif GAME_STATE == 'DICING' and message_text == u'我擲':
			dice_value = Action.throw_dice()
			act_result = Action.get_event_result(CHAR_STATE, RAND_EVENT, dice_value)
			dndbot.send_text_message(recipient_id, act_result)
			GAME_STATE = 'RUNNING'
			report_status = Action.check_status(CHAR_STATE)
			dndbot.send_text_message(recipient_id, report_status)

		## The Processes while gaming 
		else:
			make_decision(recipient_id, message_text)
			

	return 'ok', 200


def make_decision(recipient_id, message_text):

	global GAME_STATE
	global CHAR_STATE
	global RAND_EVENT
	global dndbot

	# Add 0.5 age for each decision
	CHAR_STATE['age'] += 0.5
	
	if GAME_STATE == 'DECIDING':

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
			is_random, respond = Action.sell_drugs(CHAR_STATE)

			# If god let random event happens, let it be~~
			if is_random:

				RAND_EVENT = respond
				# come_across_randevt(recipient_id, message_text, respond)
				dndbot.send_text_message(recipient_id, respond.show_event())
				#### Have to display view for users to play dice
				dndbot.send_text_message(recipient_id, '請擲骰子')
				GAME_STATE = 'DICING'
				return None
			else:
				action_result = Action.gain_money(CHAR_STATE, transaction)
				dndbot.send_text_message(recipient_id, action_result[1])
			### TODO: Disease Random Strike

		elif message_text == '3':
			dndbot.send_text_message(recipient_id, '開始行動3')
		elif message_text == '4':
			dndbot.send_text_message(recipient_id, '開始行動4')
		
		GAME_STATE = 'RUNNING'
		
		dndbot.send_text_message(recipient_id, CHAR_STATE)

	elif GAME_STATE == 'RUNNING':
		dndbot.send_text_message(
			recipient_id, '選擇行動:\n 1) 闖蕩江湖\n 2) 販賣毒品\n 3) 購買毒品\n 4) 移動')

		GAME_STATE = 'DECIDING'




## WARNING: message_text might be replaced by other parameters 
# def come_across_randevt(recipient_id, message_text, event):

# 	global dndbo
# 	global GAME_STATE
	
# 	dndbot.send_text_message(recipient_id, event.get())
# 	#### Have to display view for users to play dice
# 	dndbot.send_text_message(recipient_id, '請擲骰子')
# 	GAME_STATE = 'DICING'



if __name__ == '__main__':
	
	app.run()



