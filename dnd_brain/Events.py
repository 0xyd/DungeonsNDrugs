# -*- coding: UTF-8 -*-
from random import uniform, randint

EVIL_W = 0.2
HEALTH_W = 1
MONEY_W  = 1e-6

# Throw dice to make decision
def DiceDecides():
	pass

# God decides what kinds of assholes you will run into
# return (is_rand <booloean>, event <object>)
def GodDecides(char_state):
	
	total_val, event, is_rand = 1, None, False
	evil_val  = EVIL_W  * char_state['evil']
	money_val = MONEY_W * char_state['money']
	evil_prob  = 0.7 * (evil_val  / (money_val + evil_val))
	money_prob = 0.7 * (money_val / (money_val + evil_val))
	gods_decision = uniform(0, total_val)
	
	if gods_decision < 0.3:
		return (is_rand, '交易成功')
	elif gods_decision < 0.3 + evil_prob and evil_val > 0:
		is_rand = True
		police_event = PoliceEvent(char_state['evil'])
		event = police_event
	elif money_val > 0:
		is_rand = True
		gang_event = GangsterEvent(char_state['money'])
		event = gang_event
		
	return (is_rand, event)

# TODO: Sudden Damage from disease
def GodeMakesUSick(char_state):

	health = HEALTH_W * (100 - char_state['health'])


	return ()

## All Random Events.
## (evil_var <int>, money_var <int>, health_var <int>, message <str>)
class JudgeEvent():

	def __init__(self):
		pass

## Police Event Class
class PoliceEvent():

	def __init__(self, evil_value):

		self.event = None
		events = []

		if evil_value < 200:
			events = ['臨檢事件']
		elif evil_value >= 200 and evil < 300:
			events = ['臨檢事件', '檢調搜索']
		elif evil_value >= 300 and evil < 500:
			events = ['臨檢事件', '檢調搜索']
		else:
			events = ['刑警攻堅']

		# Use random to decide event
		if len(events) == 1:
			self.event = events[0]
		else:
			pick = randint(1, len(events))
			self.event = events[pick]

	def get(self):
		return self.event

	def show_event(self):

		if self.event == '臨檢事件':
			return "開車遭臨檢:\n開車行經中山路，遇到前方有警員設路障盤查，前方排隊車龍還長，心中盤算究竟該如何是好...》\n擲骰子:\n1~4  無處可逃，馬上被員警發現，並當場查獲毒品，立刻沒收並上銬帶回警局\n5~8  於前方路口迴轉加速逃逸，但立刻遭警網包圍，當場查獲毒品並帶回警局偵詢\n9~12  僅是酒測臨檢，故作鎮定順利通過"
		else:
			return "其他事件"

	def make_result(self, dice_value):

		if self.event == '臨檢事件':
			return self._meet_police(dice_value)
		elif self.event == '檢調搜索':
			pass
		elif self.event == '刑警攻堅':
			pass

	def _meet_police(self, dice_value):

		return (0, 0, 0, '遇到警察臨檢')	


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
	
	def show_event(self):

		if self.event == '遭到霸凌':
			return "開車遭臨檢:\n開車行經中山路，遇到前方有警員設路障盤查，前方排隊車龍還長，心中盤算究竟該如何是好...》\n擲骰子:\n1~4  無處可逃，馬上被員警發現，並當場查獲毒品，立刻沒收並上銬帶回警局\n5~8  於前方路口迴轉加速逃逸，但立刻遭警網包圍，當場查獲毒品並帶回警局偵詢\n9~12  僅是酒測臨檢，故作鎮定順利通過"
		else:
			return "其他事件"

	def make_result(self, dice_value):

		if self.event == '遭到霸凌':
			return self._be_bully(dice_value)
		elif self.event == '搶奪地盤':
			return self._fight_spots(dice_value)
		elif self.event == '被綁架':
			return self._be_kinapped(dice_value)
		elif self.event == '仇家尋仇':
			return self._b
		elif self.event == '遭到背叛':
			return self._be_betrayed(dice_value)

	def _be_bully(self, dice_value):

		if dice_value < 6:
			money_loss = -100 * dice_value
			return (0, money_loss, 0, '你受到霸凌，損失%s元。' % (str(abs(money_loss))))
		else:
			return (0, 0, 0, '惡霸無法得逞。')

	def _be_betrayed(self):

		return (0,0,0, '遭到背叛')

	def _be_kinapped(self, dice_value):
		if dice_value > 4:
			return (0, 0, 0, '成功掙脫且逃逸')
		else:
			return (0, 0, 0, '支付贖金。')

	def _fight_spots(self, dice_value):

		if dice_value > 3:
			return (0, 0, 0,'搶到地盤')
		else:
			return (0, 0, 0, '搶奪地盤失敗，負傷。')

	def _be_revenged(self, dice_value):

		return (0, 0, 0,'仇家尋仇')
		

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



