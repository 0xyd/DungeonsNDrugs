from random import randrange

# Throw dice to make decision
class DiceDecides():


# Events that you can not avoid.
class GodDecides():



class RandomEvent():

	def __init__(self, user_state):

		self.state = {
			'evil' : '',
			'money': '',
			'health': '',
			'items' : ''
		}

class JudgeEvent(RandomEvent):
	def __init__(self):
		pass

class PoliceEvent(RandomEvent):
	def __init__(self, evil_value):

		if evil_value < 100:
			print('臨檢事件')
		elif evil_value >= 100 and evil < 500:
			print('臨檢事件, 刑警攻堅')


class GangsterEvent(RandomEvent):
	def __init__(self, money_value):
		pass

class DiseaseStrokeEvent(RandomEvent):
	def __init__(self,):
		pass

class SellDrugEvent(RandomEvent):
	def __init__(self, evil_value, money_value):
		pass

class DarkSocialEvent(RandomEvent):
	def __init__(self, evil_value, money_value):
		pass

class TravelEvent(RandomEvent):
	def __init__(self, evil_value, money_value):
		pass



