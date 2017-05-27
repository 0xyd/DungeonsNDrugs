# -*- coding: UTF-8 -*-
import sqlite3
from random import randint
from Events import GodDecides, JudgeEvent, PoliceEvent, GangsterEvent, DiseaseStrokeEvent

def standarlise_output(clsmeth):
	# Return Value Format:
	# (char_state <dict>, story_message <str>)
	def _wrap(cls, user_id):
		rtn = clsmeth(cls, user_id)
		return {
			'character': rtn[0], 
			'message'  : rtn[1]
		}
	return _wrap

class Action():

	conn = sqlite3.connect('./dnd.db')
	cursor = conn.cursor()
	record = None

	@classmethod
	@standarlise_output
	def check_saved_game(cls, user_id):
		
		result = cls.cursor.execute(
			'''SELECT * FROM user WHERE user_id == %s''' % user_id)

		cls.record = result.fetchone()
		if cls.record:
			cls.record = {
				'user_id': cls.record[0],
				'age'    : cls.record[1],
				'health': cls.record[2],
				'money' : cls.record[3],
				'evil'  : cls.record[4],
				'identity': cls.record[5]
			}

			return (cls.record, '歡迎你回到這個遊戲，想要繼續嗎？')
		else:
			return ({}, '你第一次參與這項遊戲，想要開始毒與地下城嗎？')

	@classmethod
	@standarlise_output
	def start_game(cls, user_id):

		if cls.record:
			
			return (cls.record,
				'玩家%s現年%s歲，健康為%s，目前擁有%s元，惡名為%s，身份是名%s' % (
				str(cls.record['user_id']), str(cls.record['age']), str(cls.record['health']),
				str(cls.record['money']), str(cls.record['evil']), cls.record['identity'].encode('utf8')))
		
		# Create a new identity for the new user.	
		else:
			cls.record = {
				'user_id': str(user_id),
				'age':  16,
				'health': 100,
				'money' : 10000,
				'evil'  : 0,
				'identity': '少年'
			}

			result = cls.cursor.execute(
				'''INSERT INTO user VALUES (%s, 16, 100, 10000, 0, '少年')'''
				% str(user_id))

			cls.conn.commit()

			return (cls.record, '你是一個十六歲少年，.... 你目前有10000元，健康值為100，身世清白')

	@classmethod
	def save_game(cls, user_status):

		cls.cursor.execute(
			'''UPDATE user SET age = %s, health = %s, money = %s, evil = %s WHERE user_id=''' 
			% (str(user_status['age']), str(user_status['health']), str(user_status['money']), 
				str(user_status['evil']), user_status['user_id']))

		cls.conn.commit()

		pass

	@classmethod
	def check_status(cls, user_status):
		pass

	@classmethod
	def throw_dice(cls, user_status):
		return randint(1, 12)

	@classmethod
	def travel(cls, user_status):
		pass

	@classmethod
	def buy_drugs(cls, user_status):
		pass

	@classmethod
	def sell_drugs(cls, user_status, transaction):
		god_decision = GodDecides(user_status)
		if god_decision[0]:
			return cls.gain_money(user_status, transaction)
		else:
			return god_decision

	@classmethod
	def gain_money(cls, user_status, transaction):
		income = 0
		for drug, item, price in transaction:
			income = item * price
		user_status['money'] += income
		return (user_status, '共獲得%s元' % str(user_status['money']))

	@classmethod
	def get_rand_evt(cls, user_status):
		pass

	@classmethod
	def conduct_darksocial(cls, user_status):
		pass




