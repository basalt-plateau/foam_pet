





#
#	python3 health.proc.py run --path="Moves/Aptos_Account_Transfer/Verification_2.Se.py"
#


''''
	* open the ICAN Domain Address
	
	* change the inputs:
		* devnet
"'''



from vivaciousness.Moves.Aptos_Account_Transfer.vacation import throw_APT_vacation
from vivaciousness._plays import retrieve_plays

def check_1 ():
	plays = retrieve_plays ();
	
	##
	#
	accounts = plays ["accounts"]
	#
	origin_address = accounts ["1"] ["address, legacy"]
	origin_private_key = accounts ["1"] ["private key"]
	#
	address_to = accounts ["2"] ["address"]
	#
	##
	
	throw_APT_vacation ({
		"friends": {
			"origin address": origin_address,
			"to address": address_to,
			"amount APT": "0.01",
		},
		"relatives": {
			"origin address private key": origin_private_key,
			"origin address is legacy": "yes"
		}
	})

	
checks = {
	'check 1': check_1
}