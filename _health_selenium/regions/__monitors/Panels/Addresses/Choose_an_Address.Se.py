

#
#	python3 health.proc.py run --path="Regions/Loyals/Addresses/Choose_an_Address.Se.py"
#
#

#
#
#	Pannier?
#
#

''''
	TODO:
		Can download?
"'''

#/
#
#
import time
#
#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
#
#
from vivaciousness.procedures.loop import loop
from vivaciousness.health_regions.connect import connect_to_driver
from vivaciousness._plays import retrieve_plays
from vivaciousness.memo import proceed_through_memo
from vivaciousness.Milieus.navigate import Milieus_Navigate
from vivaciousness.Milieus.navigate import Milieus_Navigate_to_Greetings
#
#\


def check_1 ():
	driver = connect_to_driver ();
	plays = retrieve_plays ();
	URL = plays ["URL"]
	
	driver.get (URL)
	proceed_through_memo ({ "driver": driver });
	Milieus_Navigate_to_Greetings ({ "driver": driver });
	
	
	def open_accounts_panel ():
		button = loop (lambda : driver.find_element (
			By.CSS_SELECTOR, 
			f'[monitor="accounts opener"]'
		))
		driver.execute_script("arguments[0].scrollIntoView(true);", button)
		button.click ();
	
	open_accounts_panel ();
	
	def open_panels__single_key_account_from_keyboard_glyph_modifier ():
		def account_type__EEC_25519_single_key_account ():
			account_type_select = driver.find_element (
				By.CSS_SELECTOR, 
				'[monitor="accounts leaf"] [monitor="Account Type"]'
			)
			
			Select (account_type_select).select_by_value ("EEC_25519_single_key_account")
			
			
		def form_type__from_private_key_glyphs ():
			form_type_select = driver.find_element (
				By.CSS_SELECTOR, 
				'[monitor="accounts leaf"] [monitor="Form Type"]'
			)
			Select (form_type_select).select_by_value ("from_private_key_glyphs")

	
		#
		# 	loop find:
		#		monitor="EEC 25519 Single Key"
		#
		loop (lambda : account_type__EEC_25519_single_key_account ())
		loop (lambda : form_type__from_private_key_glyphs ())
		
	
	
	elements = {}
	def check_has_elements ():
		elements ["private_key_glyphs_textarea"] = driver.find_element (
			By.CSS_SELECTOR, 
			'[address_from_keyboard_glyphs] textarea[private_key_glyphs]'
		)
		elements ["directory_name"] = driver.find_element (
			By.CSS_SELECTOR, 
			'[address_from_keyboard_glyphs] textarea[directory_name]'
		)
		elements ["address"] = driver.find_element (
			By.CSS_SELECTOR, 
			'[address_from_keyboard_glyphs] [address] [code_wall_text]'
		)
		elements ["legacy_address"] = driver.find_element (
			By.CSS_SELECTOR, 
			'[address_from_keyboard_glyphs] [legacy_address] [code_wall_text]'
		)	
		elements ["private_key"] = driver.find_element (
			By.CSS_SELECTOR, 
			'[address_from_keyboard_glyphs] [private_key] [code_wall_text]'
		)
		elements ["public_key"] = driver.find_element (
			By.CSS_SELECTOR, 
			'[address_from_keyboard_glyphs] [public_key] [code_wall_text]'
		)
		
		
		
	def create ():	
		elements ["private_key_glyphs_textarea"].clear ()
		elements ["private_key_glyphs_textarea"].send_keys ('sdfgksjdfhgkljsdhflgjkwoeirutyowieurtyoisudhfgkljsdhflgkjweority')
		
		
	def check_revenue ():
		assert (
			elements ["address"].text ==
			'188EB5EB600E70F53FE83231668284A7E6F688147E6FD1C0CF2899DD52755C32'
		), elements ["address"].text
		
		assert (
			elements ["legacy_address"].text ==
			'3EC593D2159ACF3921C7A14F9BA7F107A38977CC5B798033D6FECB416F5F946A'
		), elements ["legacy_address"].text
	
		assert (
			elements ["private_key"].text == 
			'89ABE8D9ACBEFD89CAFBDE071625347061523476859CABEFD89CAFBED0172634'
		), elements ["private_key"].text
		assert (
			elements ["public_key"].text ==
			'95CDD7293EB3A65CF2EA7CF91BD899A45A8E55B31513E402EFC15528DA885D4B'
		), elements ["public_key"]
		
	
	open_panels__single_key_account_from_keyboard_glyph_modifier ();
	
	loop (check_has_elements)
	create ()
	loop (check_revenue)
	
	
checks = {
	'can choose an address from a input converter': check_1
}