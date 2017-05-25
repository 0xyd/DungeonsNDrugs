# -*- coding: UTF-8 -*-
import sqlite3

class Action():

	conn = sqlite3.connect('./dnd.db')
	cursor = conn.cursor()
	record = None

	@classmethod
	def check_saved_game(cls, user_id):
		
		result = cls.cursor.execute(
			'''SELECT * FROM user WHERE user_id == %s''' % user_id)

		cls.record = result.fetchone()
		if cls.record:

			return '歡迎你回到這個遊戲，想要繼續嗎？'
		else:
			return '你第一次參與這項遊戲，想要開始毒與地下城嗎？'

	@classmethod
	def start_game(cls, user_id):

		if cls.record:
			
			return '玩家%s現年%s歲，健康為%s，目前擁有%s元，惡名為%s，身份是名%s' % (
				str(cls.record[0]), str(cls.record[1]), str(cls.record[2]),
				str(cls.record[3]), str(cls.record[4]), cls.record[5].encode('utf8'))
				
		else:
			result = cls.cursor.execute(
				'''INSERT INTO user VALUES (%s, 16, 100, 10000, 0, '少年')'''
				% str(user_id))
			cls.conn.commit()

			return '你是一個十六歲少年，.... 你目前有10000元，健康值為100，身世清白'

	@classmethod
	def read_save_game(cls, user_id):
		pass

	@classmethod
	def check_status(cls, user_id):
		pass

	@classmethod
	def throw_dice(cls, user_id):
		pass

	@classmethod
	def choose_city():
		pass

	def get_event():
		pass

	def buy_drugs():
		pass

	def sell_drugs():
		pass



