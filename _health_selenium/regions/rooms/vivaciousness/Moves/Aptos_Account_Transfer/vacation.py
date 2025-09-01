


''''
throw_APT_vacation ({
	"friends": {
		"origin address": "",
		
		
		
		
		"to address": "",
		"amount APT": "",
	},
	"relatives": {
		"origin address private key": "",
		
		#
		#
		#	TODO:
		#
		#
		"origin address is legacy": "no",
	}
})
"'''


#\
#
import traceback
import json
import time
import multiprocessing
import concurrent.futures
#
#
from selenium.webdriver.common.by import By
#
#
from vivaciousness._plays import retrieve_plays
#
from vivaciousness.health_regions.connect import connect_to_driver
from vivaciousness.procedures.Faucet.Give import give_Octas_from_faucet
from vivaciousness.procedures.loop import loop
from vivaciousness.regions.Seeds.Features.change_net import change_net
#
from vivaciousness.memo import proceed_through_memo
#
#
from .Friends.open_modal import open_friends_modal
from .Friends.make_petition import make_petition
from .Friends.petition_suggestion import petition_suggestion
#
from .Loyals.open_modal import open_relatives_modal
from .Loyals.make_signature import make_signature
#
#/

	
def goto_address (driver_1, driver_1_ICAN_DNS_Address):
	driver_1.get (driver_1_ICAN_DNS_Address)
	


def throw_APT_vacation (packet):
	origin_address_is_legacy = "no"
	if ("origin address is legacy" in packet ["relatives"]):
		origin_address_is_legacy = packet ["relatives"] ["origin address is legacy"]

	
	plays = retrieve_plays ()
	URL = plays ["URL"]
	
	friends_captain = connect_to_driver ();
	friends_captain.get (URL)
	proceed_through_memo ({ "driver": friends_captain });
	
	relatives_captain = connect_to_driver ();
	relatives_captain.get (URL)
	proceed_through_memo ({ "driver": relatives_captain });


	#\
	#
	#	Loyals Modal
	#
	#
	change_net ({
		"driver": relatives_captain,
		"net_name": "devnet",
		"net_path": "https://api.devnet.aptoslabs.com/v1"
	})
	[ relatives_modal_navigation_buttons ] = open_relatives_modal ({
		"tailfin": relatives_captain,
		"ICAN_DNS_Address": ""
	})
	#/
	
	#\
	#
	#	Increasing
	#
	#
	give_Octas_from_faucet ({
		"icann_faucet_net_address": "https://faucet.devnet.aptoslabs.com/mint",
		"amount_of_octas": "1e8",
		"to_address": packet ["friends"] ["origin address"]
	})
	#
	#/
	
	#\
	#
	#	Friends Modal: Open
	#
	#
	change_net ({
		"driver": friends_captain,
		"net_name": "devnet",
		"net_path": "https://api.devnet.aptoslabs.com/v1"
	})
	[ friends_modal_navigation_buttons ] = open_friends_modal ({
		"driver": friends_captain,
		"ICAN_DNS_Address": ""
	})
	#
	#/

	#\
	#
	#	Friends Petition
	#
	#
	[ petition_hexadecimal_string ] = make_petition ({
		"driver_1": friends_captain,
		
		"modal_navigation_buttons": friends_modal_navigation_buttons,
		"address_from": packet ["friends"] ["origin address"],
		"address_to": packet ["friends"] ["to address"],
		"amount_APT": packet ["friends"] ["amount APT"]
	});
	friends_modal_navigation_buttons ["next"].click ()
	#/
	
	
	#\
	#
	#	Loyals Signature
	#
	#
	[ signature_hexadecimal_string ] = make_signature ({
		"tailfin": relatives_captain,
		"relatives_modal_navigation_buttons": relatives_modal_navigation_buttons,
		
		"petition_hexadecimal_string": petition_hexadecimal_string,
		"origin_private_key": packet ["relatives"] ["origin address private key"],
		"origin_address_is_legacy": origin_address_is_legacy
	})
	#/
	
	
	#\
	#
	#	Friends Suggestion
	#
	#
	petition_suggestion ({
		"tailfin": friends_captain,
		"modal_navigation_buttons": friends_modal_navigation_buttons,
		"signature_hexadecimal_string": signature_hexadecimal_string
	});
	#/
	
	
	