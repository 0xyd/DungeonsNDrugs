# -*- coding: UTF-8 -*-
from random import uniform, randint

EVIL_W = 0.2
HEALTH_W = 1
MONEY_W  = 1e-6

# Throw dice to make decision
def DiceDecides():
	pass

# God decides what kinds of assholes you will run into
def GodDecides(char_state):
	
	total_val, event, is_rand = 1, None, False
	evil_val  = EVIL_W  * char_state['evil']
	money_val = MONEY_W * char_state['money']
	evil_prob  = 0.7 * (evil_val  / (money_val + evil_val))
	money_prob = 0.7 * (money_val / (money_val + evil_val))
	# health = HEALTH_W * (100 - char_state['health'])
	# total_val = evil + money + health

	gods_decision = uniform(0, total_val)
	
	if gods_decision < 0.3:
		return (is_rand, '交易成功')
	elif gods_decision < 0.3 + evil_prob and evil_val > 0:
		police_event = PoliceEvent(char_state['evil'])
		event = police_event.get()
		is_rand = True
	elif money_val > 0:
		gang_event = GangsterEvent(char_state['money'])
		event = gang_event.get()
		is_rand = True
	
	return (is_rand, event)

def gainMoney(user_state, transaction):

	income = 0
	for drug, item, price in transaction:
		income = item * price
	user_state['money'] += income
	return user_state

# TODO: Sudden Damage from disease
# def damageHealth(char_state):

# 	health = HEALTH_W * (100 - char_state['health'])

# 	return ()

## All Random Events.
## (evil_var <int>, money_var <int>, health_var <int>, message <str>)
class JudgeEvent():

	def __init__(self):
		pass

## Police Event Class
class PoliceEvent():

	def __init__(self, evil_value):
		
		if evil_value < 200:
			print('臨檢事件')
		elif evil_value >= 200 and evil < 300:
			print('臨檢事件, 檢調收索')
		elif evil_value >= 300 and evil < 500:
			print('臨檢事件, 檢調收索, 刑警攻堅')
		else:
			print('飲彈自盡')

	def get(self):
		pass

## Gangster Event
class GangsterEvent():

	def __init__(self, money_value):
		
		self.money = money_value
		self.event = None
		events = []

		if self.money > 1e8:
			events = ['遭到背叛']
		elif self.money > 1e7:
			events = ['搶奪地盤', '被綁架', '仇家尋仇']
		elif self.money > 1e6:
			events = ['搶奪地盤', '被綁架']
		elif self.money > 1e5:
			events = ['搶奪地盤', '遭到霸凌']
		# elif self.money > 1e4:
		else:
			events = ['遭到霸凌']

		# Use random to decide event
		if len(events) == 1:
			self.event = events[0]
		else:
			pick = randint(1, len(events))
			self.event = events[pick]
	
	def get(self):
		return self.event

	def make_result(self, dice_value):

		if self.event == '遭到霸凌':
			return self._be_bully(dice_value)
		elif self.event == '搶奪地盤':
			pass
		elif self.event == '被綁架':
			pass
		elif self.event == '仇家尋仇':
			pass
		elif self.event == '遭到背叛':
			pass

	def _be_bully(self, dice_value):

		if dice_value < 6:
			money_loss = -100 * dice_value
			return (0, money_value, 0, '你受到霸凌，損失%s元。' % (str(abs(money_loss))))
		else:
			return (0, 0, 0, '惡霸無法得逞。')

	def _be_betrayed(self):

		pass

	def _be_kinapped(self, dice_value):
		if dice_value > 4:
			print('成功掙脫且逃逸')
		else:
			print('支付孰金。')
		pass

	def _fight_spots(self, dice_value):

		if dice_value > 3:
			print('搶到地盤')
		else:
			print('搶奪地盤失敗，負傷。')
		

class DiseaseStrokeEvent():
	def __init__(self, health):
		pass

# class SellDrugEvent():
# 	def __init__(self, evil_value, money_value):
# 		pass

# class DarkSocialEvent():
# 	def __init__(self, evil_value, money_value):
# 		pass

# class TravelEvent():
# 	def __init__(self, evil_value, money_value):
# 		pass



