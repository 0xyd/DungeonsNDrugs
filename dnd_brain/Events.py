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
	evil_prob  = 0.4 * (evil_val  / (money_val + evil_val))
	money_prob = 0.4 * (money_val / (money_val + evil_val))
	gods_decision = uniform(0, total_val)
	
	if gods_decision < 0.6:
		return (is_rand, '交易成功')
	elif gods_decision < 0.6 + evil_prob and evil_val > 0:
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
## (evil_var <int>, money_var <int>, health_var <int>, age_var <int>, message <str>, judge_flag <bool>)
class JudgeEvent():

	def __init__(self, char_status):
		self.event = char_status['crime_state']
		self.sell_crimes = set(['販賣第一級毒品', '販賣第二級毒品', '販賣第三級毒品', '販賣第四級毒品'])

	def judge_ask(self):
		if self.event in self.sell_crimes:
			return ('法官審理', '本件準備程序開始，法官除詢問犯罪事實相關疑問外，尚會斟酌被告於庭上之表現，是請注意你於法庭上的陳述內容及態度，此些皆會影響法官心證乃至本件宣判刑度。法官問：「對檢察官起訴之犯罪事實有何意見？」')
		else:
			return ('Other', 'Other Info')

	def show_dice(self):

		if self.event in self.sell_crimes:
			return ('擲骰子', 
				'1~3點：自白承認，且深感悔悟，表達不會再犯之意。\n'
				'4~6點：全部否認\n'
				'7~9點：本空口胡言，堅決否認有為本件犯行，嗣遭庭上嚇斥後，便改口承認確有為本件犯行，請求鈞院減輕刑罰。\n'
				'10~12點：狡辯、臨訟杜撰，經檢察官提示相關事證後，仍不知悔悟，持續詭辯，庭上態度惡劣\n')

	def verdict(self, dice_value):

		if self.event == '販賣第一級毒品':
			return self._verdict_sell_1_behav
		elif self.event == '販賣第二級毒品':
			return self._verdict_sell_2_behav
		elif self.event == '販賣第三級毒品':
			return self._verdict_sell_3_behav
		elif self.event == '販賣第四級毒品':
			return self._verdict_sell_4_behav

	def _verdict_sell_1_behav(self, dice_value):

		sentence = 0

		if dice_value <= 3:
			sentence = randint(10, 1.3*10)
			return (0, 0, 0, sentence, '', False)
		elif dice_value <= 6:
			sentence = randint(1.3*10, 1.6*10)
			return (0, 0, 0, sentence, '', False)
		elif dice_value <= 9:
			sentence = randint(1.6*10, 1.9*10)
			return (0, 0, 0, sentence, '', False)
		elif dice_value <= 11:
			sentence = randint(1.9*10, 2.2*10)
			return (0, 0, 0, sentence, '', False)
		else:
			return (0, 0, 0, 100, '從此與世隔絕，囹圄之中便是你的世界', False)

	def _verdict_sell_2_behav(self, dice_value):

		sentence = 0

		if dice_value <= 3:
			sentence = randint(7, int(1.3*7))
			return (0, 0, 0, sentence, '%s年有期徒刑，請好好反省前非' % str(sentence), False)
		elif dice_value <= 6:
			sentence = randint(int(1.3*7), int(1.6*7))
			return (0, 0, 0, sentence, '%s年有期徒刑，請好好反省前非' % str(sentence), False)
		elif dice_value <= 9:
			sentence = randint(int(1.6*7), int(1.9*7))
			return (0, 0, 0, sentence, '%s年有期徒刑，請好好反省前非' % str(sentence), False)
		elif dice_value <= 11:
			sentence = randint(int(1.9*7), int(2.2*7))
			return (0, 0, 0, sentence, '%s年有期徒刑，請好好反省前非' % str(sentence), False)
		else:
			return (0, 0, 0, 100, '', False)

	def _verdict_sell_3_behav(self, dice_value):

		sentence = 0

		if dice_value <= 3:
			sentence = randint(5, int(1.3*5))
			return (0, 0, 0, sentence, '%s年有期徒刑，請好好反省前非' % str(sentence), False)
		elif dice_value <= 6:
			sentence = randint(int(1.3*5), int(1.6*5))
			return (0, 0, 0, sentence, '%s年有期徒刑，請好好反省前非' % str(sentence), False)
		elif dice_value <= 9:
			sentence = randint(int(1.6*5), int(1.9*5))
			return (0, 0, 0, sentence, '%s年有期徒刑，請好好反省前非' % str(sentence), False)
		else:
			sentence = randint(int(1.9*5), int(2.2*5))
			return (0, 0, 0, sentence, '%s年有期徒刑，請好好反省前非' % str(sentence), False)

	def _verdict_sell_4_behav(self, dice_value):

		sentence = 0

		if dice_value <= 3:
			sentence = randint(3, int(1.3*3))
			return (0, 0, 0, sentence, '', False)
		elif dice_value <= 6:
			sentence = randint(int(1.3*3), int(1.6*3))
			return (0, 0, 0, sentence, '', False)
		elif dice_value <= 9:
			sentence = randint(int(1.6*3), int(1.9*3))
			return (0, 0, 0, sentence, '', False)
		else:
			sentence = randint(int(1.9*3), 10)
			return (0, 0, 0, sentence, '', False)


## Police Event Class
class PoliceEvent():

	def __init__(self, evil_value):

		self.event = None
		events = []

		if evil_value < 200:
			events = ['臨檢事件']
		elif evil_value < 300:
			events = ['臨檢事件', '檢調搜索']
		elif evil_value < 500:
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
			return ('開車遭臨檢', '開車行經中山路，遇到前方有警員設路障盤查，前方排隊車龍還長，心中盤算究竟該如何是好...》', 'https://raw.githubusercontent.com/yudazilian/DungeonsNDrugs/master/dnd_brain/public/news3.png')
		elif self.event == '檢調搜索':
			return ("檢調搜索", "你因為事業越做越大，開始受到警方關注，警方除佈下人力跟監，亦順利聲請通訊監察，而你卻毫無察覺...某日，尖銳的電鈴聲劃破早晨的寧靜，警察：「我們是偵查隊刑警，依檢字106年0000689號搜索票執行搜索，請開門配合搜索，謝謝。」驚惶失措的你，只有幾秒反應時間...", "https://raw.githubusercontent.com/yudazilian/DungeonsNDrugs/master/dnd_brain/public/news1.png")
		elif self.event == '刑警攻堅':
			return ("刑警攻堅", "", "https://raw.githubusercontent.com/yudazilian/DungeonsNDrugs/master/dnd_brain/public/news2.png")


	def show_dice(self):

		if self.event == '臨檢事件':
			return "擲骰子:\n1~4  無處可逃，馬上被員警發現，並當場查獲毒品，立刻沒收並上銬帶回警局\n5~8  於前方路口迴轉加速逃逸，但立刻遭警網包圍，當場查獲毒品並帶回警局偵詢\n9~12  僅是酒測臨檢，故作鎮定順利通過"
		elif self.event == '檢調搜索':
			return "擲骰子:\n1~5  突如其來的狀況，驚嚇的雙腿一軟，只能痴呆的任由警方搜索出藏匿的毒品及現金，但這就是違法的必然下場。\n6~11   你不願乖乖就範，立刻將門關上上鎖，迅速逃跑，自以為能從防火巷逃跑，惟警方早就設下天羅地網，你就如同甕中之鱉，縱奮力掙扎，上銬帶回是你唯一宿命\n12  你剛好在外過夜，僥倖地逃過被逮捕的命運，但屋內的毒品及現金盡遭扣押  "
		elif self.event == '刑警攻堅':
			return " "

	def make_result(self, dice_value):

		if self.event == '臨檢事件':
			return self._meet_police(dice_value)
		elif self.event == '檢調搜索':
			return self._raid(dice_value)
		elif self.event == '刑警攻堅':
			pass

	def _meet_police(self, dice_value):

		if dice_value <= 4:
			return (50, -30000, -2, 0,
				'你無處可逃，馬上被員警發現，並當場查獲毒品，立刻沒收並上銬帶回警局', True)	
		elif dice_value <= 8:
			return (80, -17500, -5, 0,
				'你於前方路口迴轉加速逃逸，但立刻遭警網包圍，當場查獲毒品並帶回警局偵詢', True)	
		else:
			return (0, 0, -1, 0, '僅是酒測臨檢，故作鎮定順利通過', False)

	def _raid(self, dice_value):

		if dice_value <= 5:
			return (150, -50000, -2, 0,'突如其來的狀況，驚嚇的雙腿一軟，只能痴呆的任由警方搜索出藏匿的毒品及現金，但這就是違法的必然下場。', True)
		elif dice_value <= 11:
			return (150, -50000, -7, 0,'你不願乖乖就範，立刻將門關上上鎖，迅速逃跑，自以為能從防火巷逃跑，惟警方早就設下天羅地網，你就如同甕中之鱉，縱奮力掙扎，上銬帶回是你唯一宿命', True)
		else:
			return (175, -50000,  0, 0,'你剛好在外過夜，僥倖地逃過被逮捕的命運，但屋內的毒品及現金盡遭扣押', False) 

	def _police_attack(self, dice_value):
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
			events = ['搶奪地盤', '黑幫霸凌']
		# elif self.money > 1e4:
		else:
			events = ['黑幫霸凌']

		# Use random to decide event
		if len(events) == 1:
			self.event = events[0]
		else:
			pick = randint(1, len(events))
			self.event = events[pick]
	
	def show_event(self):

		if self.event == '黑幫霸凌':
			return ('黑幫霸凌', "身為校園邊緣人的你，加入幫派後依然沒有例外，22k幫向以財力作為地位高低衡量，窮困潦倒的你，連菜鳥都把你當小弟使喚，面對如此困境，你決定...", "https://raw.githubusercontent.com/yudazilian/DungeonsNDrugs/master/dnd_brain/public/news8.png")
		elif self.event == '搶奪地盤':
			return ('搶奪地盤', '販賣毒品之利益驚人，終引起幫派間之械鬥，互爭地盤，你在這場爭奪戰中，不幸遭對方幫派擄走以作為交涉籌碼，遭綁架斷水斷食的你該…', 'https://raw.githubusercontent.com/yudazilian/DungeonsNDrugs/master/dnd_brain/public/news6.png')
		elif self.event == '仇家尋仇':
			return ('仇家尋仇', '你初出江湖，對於道上規矩多有不知，於販賣毒品時，偶有不慎侵擾他人生意地盤。仇家們無不虎視眈眈，等待機會將所受損害加倍奉還...', 'https://raw.githubusercontent.com/yudazilian/DungeonsNDrugs/master/dnd_brain/public/news4.png')
		elif self.event == '遭到背叛':
			return ('遭到背叛', '', 'https://raw.githubusercontent.com/yudazilian/DungeonsNDrugs/master/dnd_brain/public/news5.png')	

	def show_dice(self):

		if self.event == '黑幫霸凌':
			return "擲骰子:\n 1 怨嘆不是含著金湯匙出身的富二代，決定砍掉重練\n 2~8   任命不願抵抗，生無大志只求小確幸，過一日算一日，\n9~10  忍辱負重，持續耕耘，等待翻身的一天\n11~12  奮力抵抗體制，雖歷經一番掙扎、多了幾道傷疤，但終獲尊重 "
		elif self.event == '搶奪地盤':
			return "擲骰子:\n 1  慘遭撕票，淪為幫派間利益爭奪的犧牲品。\n2~7  以讓出地盤作為代價而獲得釋放，重獲自由很棒，但卻也損失了獲益最豐的地段。\n8~11    幫派小弟以武力強行將你救出，惟你早以飽受折磨，元氣大傷。\n12     你順利趁綁匪熟睡之際偷溜，並成功發起反擊，振興幫派版圖。"
		elif self.event == '仇家尋仇':
			return "擲骰子:\n 1~4  深夜外出購買鹹酥雞時，遭仇家圍堵，以箱型車強行帶至深山毆打，並帶走全身衣物及現金，身心飽受巨大傷害。 \n 5~7   仇家在外四處張揚你賣的是假貨等不實訊息，造成你連續幾個月的慘澹生意。 \n 8~10  你的轎車車輪被戳洞、車身被刮花，半夜時窗戶亦遭不明人士丟擲石塊砸破，夜不安眠，精神緊繃。\n11~12    對於會遭報復之事，你早已有所防範，是除住處被噴漆及灑冥紙外，並無其他損害。"
		elif self.event == '遭到背叛':
			return ""

	def make_result(self, dice_value):

		if self.event == '黑幫霸凌':
			return self._be_bully(dice_value)
		elif self.event == '搶奪地盤':
			return self._fight_spots(dice_value)
		elif self.event == '被綁架':
			return self._be_kinapped(dice_value)
		elif self.event == '仇家尋仇':
			return self._be_revenged(dice_value)
		elif self.event == '遭到背叛':
			return self._be_betrayed(dice_value)

	def _be_bully(self, dice_value):

		if dice_value == 1:
			return (-500, 0, -100, 0, '怨嘆不是含著金湯匙出身的富二代，決定砍掉重練', False)
		elif dice_value < 9:
			return (-200, 0, -15, 0, '任命不願抵抗，生無大志只求小確幸，過一日算一日', False)
		elif dice_value < 11:
			return (0, 0, 0, 0, '忍辱負重，持續耕耘，等待翻身的一天', False)
		else:
			return (10, 20000, 0, 0, '奮力抵抗體制，雖歷經一番掙扎、多了幾道傷疤，但終獲尊重', False)

	def _be_betrayed(self):

		return (0,0,0, '遭到背叛', False)

	def _be_kinapped(self, dice_value):
		
		if dice_value == 1:
			return (0, 0, -100, 0,'慘遭撕票，淪為幫派間利益爭奪的犧牲品。', False)
		elif dice_value < 8:
			return (0, -40000, -10, 0, '以讓出地盤作為代價而獲得釋放，重獲自由很棒，但卻也損失了獲益最豐的地段。', False)
		elif dice_value < 12:
			return (5, -10000, -15, 0, '幫派小弟以武力強行將你救出，惟你早以飽受折磨，元氣大傷。', False)
		else:
			return (20, 25000, -3, 0,'你順利趁綁匪熟睡之際偷溜，並成功發起反擊，振興幫派版圖。。', False)

	def _fight_spots(self, dice_value):

		if dice_value > 3:
			return (0, 0, 0, 0,'搶到地盤', False)
		else:
			return (0, 0, 0, 0,'搶奪地盤失敗，負傷。', False)

	def _be_revenged(self, dice_value):

		if dice_value < 5:
			return (-10, -5000, -10, 0, '深夜外出購買鹹酥雞時，遭仇家圍堵，以箱型車強行帶至深山毆打，並帶走全身衣物及現金，身心飽受巨大傷害。', False)
		elif dice_value < 8:
			return (-20, -40000, 0, 0, "仇家在外四處張揚你賣的是假貨等不實訊息，造成你連續幾個月的慘澹生意。", False)
		elif dice_value < 11:
			return (0, -20000, -3, 0, "你的轎車車輪被戳洞、車身被刮花，半夜時窗戶亦遭不明人士丟擲石塊砸破，夜不安眠，精神緊繃。", False)
		else:
			return (0, -5000, -1, 0, "對於會遭報復之事，你早已有所防範，是除住處被噴漆及灑冥紙外，並無其他損害。", False)
		

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



