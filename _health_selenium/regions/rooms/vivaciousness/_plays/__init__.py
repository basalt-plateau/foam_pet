
'''
from vivaciousness._plays import retrieve_plays
plays = retrieve_plays ();
'''

''''
"1": {
	"private key": "89ABC8DE9FABDE0716253407612534071562348F9AEDBC8F9EADBC0127653425",
	"address": "522D906C609A3D23B90F072AD0DC74BF857FB002E211B852CE38AD6761D4C8FD"
},
"'''


#
#
#	Development
#
#
def flask_build ():
	open_browser = "yes"
	URL = "http://172.17.0.2:2300"
	has_memo = "yes"
	
	return [ open_browser, URL, has_memo ]

def dev_build ():
	open_browser = "yes"
	URL = "http://172.17.0.2:21000"
	has_memo = "no"
	
	return [ open_browser, URL, has_memo ]


def sanic_build ():
	open_browser = "yes"
	URL = "http://localhost:22000"
	has_memo = "yes"
	
	return [ open_browser, URL, has_memo ]
	

#
#
#	Public
#
#
def VM_build ():
	open_browser = "yes"
	URL = "https://45.63.57.134"
	has_memo = "yes"
	
	return [ open_browser, URL, has_memo ]

def online_build ():
	open_browser = "yes"
	URL = "https://foam.pet"
	has_memo = "yes"
	
	return [ open_browser, URL, has_memo ]



def retrieve_plays ():
	[ open_browser, URL, has_memo ] = flask_build ();
	
	return {
		#
		#	whether to show the browser, "yes"
		#	or not show the browser, "no"
		#
		"open browser": open_browser,
		
		"URL": URL,
		
		"has_memo": has_memo,
		
		"accounts": {
			"1": {
				"private key": "8EB524379EADB4071EADBC9EDAC8FE9DA63426178F9ECBDAE234163F0E9CBE8D",
				"public key": "D18B0A6CBC824212100520ABBC6395D9B11272424284809F33C7CC42DB4F65C5",
				"address": "0EF6BB4B010B888C3740DB64A8C4885BE8D749F78DDDE826BCEDB34DAFB1702C",
				"address, legacy": "B2BD2A4163F4BDECF8481DDC348755FB671D589C7EE5C5F1E2AFAB3DFC7A98EE",			
			},
			"2": {
				"private key": "BF84073526170CB5AE94370DAE9F8437052E1CBF8E9CA52F0486B7052E9CB705",
				"address": "26F4F8D7C5526BA7DA453041D3A858CFEA06D911C90C2E40EDA2A7261826858C"
			}
		}
	}