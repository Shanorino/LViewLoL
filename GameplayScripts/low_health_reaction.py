from lview import *
from commons.targeting import TargetingConfig
from commons.skills import *
import json, time
from pprint import pprint

lview_script_info = {
	"script": "Low Health Reaction",
	"author": "laiwuzi",
	"description": "React when HP is low",
}

cast_keys = {
	'R': 19
}

item_keys = {
	'item 1': 2,
	'item 2': 3,
	'item 3': 4,
	'item 4': 5,
	'item 5': 6,
	'item 6': 7
}

low_health_limit = 0
low_health_limit_percentage = 10
cast_frequency = 1
auto_health = True
reacted = False

def lview_load_cfg(cfg):
	global cast_keys, low_health_limit, cast_frequency, auto_health, low_health_limit_percentage
	cast_keys = json.loads(cfg.get_str('cast_keys', json.dumps(cast_keys)))
	low_health_limit = cfg.get_float("low_health_limit", 100)
	cast_frequency = cfg.get_int("cast_frequency", 1)
	low_health_limit_percentage = cfg.get_int("low_health_limit_percentage", 10)
	
def lview_save_cfg(cfg):
	global cast_keys, low_health_limit, cast_frequency, auto_health, low_health_limit_percentage
	cfg.set_str('cast_keys', json.dumps(cast_keys))
	cfg.set_float("low_health_limit", low_health_limit)
	cfg.set_int("cast_frequency", cast_frequency)
	cfg.set_bool("auto_health", auto_health)
	cfg.set_int("low_health_limit_percentage", low_health_limit_percentage)

def lview_draw_settings(game, ui):
	global cast_keys, low_health_limit, cast_frequency, auto_health, low_health_limit_percentage
	low_health_limit = ui.dragfloat("HP to activate skill", low_health_limit, 50, 50, 1000)
	cast_frequency = ui.dragint("Times to cast skill", cast_frequency, 1, 0, 10)
	auto_health = ui.checkbox("Auto HP Limit Adjustment", auto_health)
	low_health_limit_percentage = ui.dragint("HP Limit %", low_health_limit_percentage, 1, 0, 100)
	
	for slot, key in cast_keys.items():
		cast_keys[slot] = ui.keyselect(f'Key to cast {slot}', key)
	draw_prediction_info(game, ui)
	
def lview_update(game, ui):
	global cast_keys, reacted, low_health_limit, cast_frequency, low_health_limit_percentage
	current_time = game.time
	player = game.player

	# automatically adjust low_health_limit
	if (auto_health):
		low_health_limit = game.player.max_health * low_health_limit_percentage / 100
		#low_health_limit = 300 if low_health_limit > 300 else 100 + (current_time / 60) * 8

	if (player.health > low_health_limit and reacted):
		reacted = False

	for slot, key in cast_keys.items():
		skill = getattr(game.player, slot)
		if (player.health < low_health_limit and player.health > 0 and not reacted):
			for i in range(0, cast_frequency):
				skill.trigger()
			reacted = True