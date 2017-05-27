# -*- coding: UTF-8 -*-
import json
import requests

from pymessenger import Bot
from pymessenger.graph_api import FacebookGraphApi
import pymessenger.utils as utils


class View():
	
	def __init__(self, bot):
		self.bot = bot

	def gen_text_template(self, recipient_id, message):

		return self.bot.send_text_message(recipient_id, message)

	def gen_list_template(self, recipient_id, elements):

		payload = {
			'recipient': {
				'id': recipient_id
			},
			'message': {
				"attachment": {
					"type": "template",
					"payload": {
						"template_type": "list",
						"top_element_style": "compact",
						"elements": elements
					}
				}
			}
		}
		return self.bot.send_raw(payload)

	def gen_carousel_sqr_template(self, recipient_id, elements):

		payload = {
            'recipient': {
                'id': recipient_id
            },
            'message': {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "image_aspect_ratio": "square",
                        "elements": elements
                    }
                }
            }
        }

		return self.bot.send_raw(payload)

	def gen_generic_template(self, recipient_id, title, image_url, subtitle, button_title):

		elements = [{
			"title" : title,
			"image_url": image_url,
			"subtitle": subtitle,
			"buttons":[{
				"type":"postback",
				"title":button_title,
				"payload":"{'event': '@'}"
				}]
			}]
		
		return self.bot.send_generic_message(recipient_id, elements)

	def gen_generic_nobutton_template(self, recipient_id, title, image_url, subtitle):

		elements = [{
			"title" : title,
			"image_url": image_url,
			"subtitle": subtitle
			}]
		
		return self.bot.send_generic_message(recipient_id, elements)

	def gen_button_template(self, recipient_id, text, button_title, value):

		buttons = [{
			"type" : "postback",
			"title": button_title,
			"payload":str(value)
			}]
		
		return self.bot.send_button_message(recipient_id, text, buttons)

	def gen_quickreplies_template(self, recipient_id, text, quick_replies):

		
		payload = {
			'recipient': {
				'id': recipient_id
			},
			'message': {
				"text": text,
				"quick_replies": quick_replies
			}
		}
		return self.bot.send_raw(payload)

	def gen_googlemap_template(self):
		pass

