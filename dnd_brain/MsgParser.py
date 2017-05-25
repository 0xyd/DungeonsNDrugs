class MsgParser():

	def __init__(self, msg):
		
		# Flatten the message's json format
		page = msg['object']
		msg  = msg['entry'][0]['messaging'][0]

		self.msg = {
			'is_echo'  : False,
			'sender_id': '',
			'text'     : '',
			'object'   : ''
		}

		try:
			self.msg['sender_id'] = msg['sender']['id']
			self.msg['text']      = msg['message']['text']
			self.msg['object']    = page

			if 'is_echo' in msg['message']:
				self.msg['is_echo'] = True

		except KeyError as e:
			pass

	def get_msg_type(self):
		return self.msg['object']

	def get_sender(self):
		return self.msg['sender_id']

	def get_text(self):
		return self.msg['text']

	def is_echo(self):
		return self.msg['is_echo']


		

