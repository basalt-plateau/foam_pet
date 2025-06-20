



import os
import pathlib
from os.path import dirname, join, normpath
import sys
	
this_directory = pathlib.Path (__file__).parent.resolve ()	


Accounts = {
	"1": {
		"Private Key": "9687BC1623C8796BC2D1F8E9CBA97043717A69CB7869CADBF8E9DABCBF8E9446",
		"Legacy Address": "8E0F71D98112EA5DCDAF6BBAB057BBBB9D7132D1AC2F13215D95ED1D15ECAF13"
	},
	"2": {
		"Private Key": "CB7869CADBC8F9E9ABC012365C89ABFED89CAB760152CF8E9DABC4152C38E94A",
		"Legacy Address": "BBEADEC4B68BB5C13E18EAB956358FB4A8CDAA4F8CD9AF266E9B6F0BDCFE3940"
	}
};
Account = Accounts ["2"]
Ruler_Address = Account ["Legacy Address"]
Ruler_Private_Key = Account ["Private Key"]

Build_Site_Address = Account ["Legacy Address"]

def retrieve_named_addresses ():
	'''
		Petra 		= "F5565CC1D71781D6EF766A2A50ED459B9D3B430CEB6F7BBF79393C3626A979CD"
		Pannier_03 	= "8E0F71D98112EA5DCDAF6BBAB057BBBB9D7132D1AC2F13215D95ED1D15ECAF13"
	'''
	named_addresses = ", ".join ([
		f"""Ruler_01={ Ruler_Address }""",
		f"""Builder_01={ Build_Site_Address }"""
	]);
	
	return "--named-addresses '" + named_addresses + "'";




def steady ():
	named_addresses = retrieve_named_addresses ();
	
	filter = ""
	filter = "--filter Texts_Preferential"
	
	screenplay = " ".join ([
		f"cd { this_directory }",
		"&&",
		"aptos move test",
		"--ignore-compile-warnings",
		filter,
		named_addresses
	]);
	
	print ("screenplay:", screenplay);
	
	os.system (screenplay);
	os.system (f"cd '{ this_directory }' && chmod -R 777 .")
	
'''
	This means you're not logged in as the publisher account at .config:
		{
			"Error": "Simulation failed with status: CONSTRAINT_NOT_SATISFIED\nExecution failed with message: metadata and code bundle mismatch: unregistered dependency: 'd1790823b031ab184af37b141567394dfa759d6a92c2a030c0c5f0a36a1f6212::Rules_Module'"
		}
		
		(cd /Metro/Hull && aptos init --network devnet --assume-yes --private-key CB7869CADBC8F9E9ABC012365C89ABFED89CAB760152CF8E9DABC4152C38E94A)
'''
def publish ():
	named_addresses = retrieve_named_addresses ();

	screenplay = " ".join ([
		f"cd { this_directory }",
		"&&",
		"aptos move publish",
		named_addresses,
		"--assume-yes"
	]);
	
	print ("screenplay:", screenplay);

	os.system (screenplay);
	



'''

def movie (plays):
	import asyncio
	import os

	async def run_this (_plays):
		async def run_play (play):
			print (f"play: '{play}'")
			await asyncio.sleep (1)
			await asyncio.to_thread (os.system, play)

		tasks = [run_play(play) for play in _plays]
		await asyncio.gather (* tasks)
		
	asyncio.run (run_this (plays))
'''

    
	
def movie (plays):
	for play in plays:
		print (f"play: '{ play }'")
		os.system (play)	

'''
	aptos move view --function-id 8E0F71D98112EA5DCDAF6BBAB057BBBB9D7132D1AC2F13215D95ED1D15ECAF13::Module_Guest_Hulls::Status
'''
def begin (Build_Address):
	movie ([
		f"aptos move run --function-id { Build_Address }::Module_Ruler_Hulls::Begin --assume-yes",
		f"aptos move view --function-id { Build_Address }::Module_Guest_Hulls::Status"
	]);

'''
aptos move run --assume-yes --function-id 8E0F71D98112EA5DCDAF6BBAB057BBBB9D7132D1AC2F13215D95ED1D15ECAF13::Module_Denizen_Texts::Send_Text --args String:Veganism String:Vegans String:'I accept.'
'''
def send_texts (Build_Address):
	movie ([
		f"aptos move run --assume-yes --function-id { Build_Address }::Module_Denizen_Texts::Send_Text --args String:Veganism String:Vegans String:'I accept.'",
		f"aptos move run --assume-yes --function-id { Build_Address }::Module_Denizen_Texts::Send_Text --args String:Text_1 String:Silicon String:'I accept.'",
		f"aptos move run --assume-yes --function-id { Build_Address }::Module_Denizen_Texts::Send_Text --args String:Text_1 String:Plants String:'I accept.'",
		f"aptos move run --assume-yes --function-id { Build_Address }::Module_Denizen_Texts::Send_Text --args String:Text_1 String:Mercyism String:'I accept.'",
		f"aptos move run --assume-yes --function-id { Build_Address }::Module_Denizen_Texts::Send_Text --args String:Text_1 String:Nutrition String:'I accept.'",
		f"aptos move run --assume-yes --function-id { Build_Address }::Module_Denizen_Texts::Send_Text --args String:Text_1 String:Diet String:'I accept.'",
		f"aptos move run --assume-yes --function-id { Build_Address }::Module_Denizen_Texts::Send_Text --args String:Text_1 String:Similarities String:'I accept.'",
	]);


def open_account (private_key):
	movie ([
		f"(cd /Metro/Hull && aptos init --assume-yes --network devnet --private-key { private_key })",
		"aptos account fund-with-faucet --amount 200000000"
	]);
	
	
# steady ();

open_account (Ruler_Private_Key);
# publish ()


# begin (Ruler_Address);
send_texts (Ruler_Address);










#