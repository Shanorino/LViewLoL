from lview import *
from commons.skills import *

enable_smite_key = 0
enable_ignite_key = 0

show_smitable = False

enabled_autosmite = False
enabled_autoignite = False

lview_script_info = {
	"script": "Auto Summoner Spell",
	"author": "laiwuzi",
	"description": "Auto summoner spell"
}

def lview_load_cfg(cfg):
	global enable_smite_key, show_smitable, enable_ignite_key
	enable_ignite_key = cfg.get_int("enable_ignite_key", 0)
	enable_smite_key = cfg.get_int("enable_smite_key", 0)
	show_smitable = cfg.get_bool("show_smitable", True)
	
def lview_save_cfg(cfg):
	global enable_smite_key, show_smitable, enable_ignite_key
	cfg.set_int("enable_ignite_key", enable_ignite_key)
	cfg.set_int("enable_smite_key", enable_smite_key)
	cfg.set_bool("show_smitable", show_smitable)
	
def lview_draw_settings(game, ui):
	global enable_smite_key, show_smitable, enable_ignite_key
	show_smitable = ui.checkbox("Show when to smite", show_smitable)
	enable_ignite_key = ui.keyselect("(dian ran) Enable auto ignite key", enable_ignite_key)
	enable_smite_key = ui.keyselect("(cheng jie) Enable auto smite key", enable_smite_key)
	
def lview_update(game, ui):
	global enable_smite_key, enabled_autosmite, enabled_autoignite, show_smitable
	
	smite = game.player.get_summoner_spell(SummonerSpellType.Smite)
	ignite = game.player.get_summoner_spell(SummonerSpellType.Ignite)

	if game.was_key_pressed(enable_smite_key):
		enabled_autosmite = ~enabled_autosmite
	if game.was_key_pressed(enable_ignite_key):
		enabled_autoignite = ~enabled_autoignite

	if smite == None: 
		pass
	else:
		smite_ready_at = smite.ready_at
		
		hovered = game.hovered_obj
		is_smitable = (hovered and hovered.has_tags(UnitTag.Unit_Monster_Epic) and hovered.health - smite.value <= 0 and smite_ready_at < game.time)
		if enabled_autosmite:
			p = game.world_to_screen(game.player.pos)
			p.y -= 50
			game.draw_button(p, "AutoSmite-Ready", Color.BLACK, Color.YELLOW, 10)
		
			if is_smitable:
				smite.trigger()
				#enabled_autosmite = False
		
		if show_smitable and is_smitable:
			game.draw_circle_world(hovered.pos, hovered.gameplay_radius, 30, 3, Color.YELLOW)

	if ignite == None: 
		pass
	else:
		ignite_ready_at = ignite.ready_at
		if enabled_autoignite and ignite_ready_at <= game.time:
			# first draw "ready"
			p = game.world_to_screen(game.player.pos)
			p.y -= 30
			game.draw_button(p, "AutoIgnite-Ready", Color.BLACK, Color.RED, 10)
			# then check and cast
			nearest_champion = find_nearest_champion_with_lowest_hp(game)
			if nearest_champion:
				is_ignitable = (nearest_champion.health - ignite.value <= 0)
				if enabled_autoignite and is_ignitable:
					cast_point = game.world_to_screen(nearest_champion.pos)
					old_cpos = game.get_cursor()
					game.move_cursor(cast_point)
					ignite.trigger()
					time.sleep(0.01)
					game.move_cursor(old_cpos)

def find_nearest_champion_with_lowest_hp(game):
	ignite_range = 600
	min_health = 9999999999
	target = None
	for champion in game.champs:
		if champion.is_enemy_to(game.player) and champion.is_alive and champion.health < min_health and game.distance(game.player, champion) < ignite_range:
			target = champion
			min_health = champion.health
		
	return target