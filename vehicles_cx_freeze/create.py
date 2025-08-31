

''''
	This doesn't work yet.
"'''

import os
import time
import shutil

#version = "v2_1_0_0"

version = "v3_0_0_0"
Le_OS = "linux-x86_64"

name_softwhere = f"Mech_Pet.{ Le_OS }.{ version }"
name_rules = f"Mech_Pet.{ Le_OS }.{ version }.Rules"


assets_path = "/Metro/vehicles_cx_freeze/assets"
build_path = "/Metro/vehicles_cx_freeze/build"
distributions_path = f"/Metro/vehicles_cx_freeze/_distributions"

#
#	Build: Softwhere
#
#
module_build_path = f"{ build_path }/{ name_softwhere }"
module_rules_path = f"{ build_path }/{ name_softwhere }/lib/Mech_Pet/Rules"
module_build_path_zip = f"{ build_path }/{ name_softwhere }.zip"

#
#	Build: The outer rules
#
#
module_outer_rules_path = f"{ build_path }/{ name_rules }"
module_outer_rules_path_zip = f"{ build_path }/{ name_rules }.zip"


#
#	The distribution
#
#
distribution_path_softwhere =		f"{ distributions_path }/{ version }/{ name_softwhere }"
distribution_path_softwhere_zip = 	f"{ distributions_path }/{ version }/{ name_softwhere }.zip"

distribution_path_rules = 			f"{ distributions_path }/{ version }/{ name_rules }"
distribution_path_rules_zip =		f"{ distributions_path }/{ version }/{ name_rules }.zip"



#
#
#	GH
#
#
GH_Repo = "https://github.com/Planet-IV/Mech_Pet"


def mimic (packet):
	origin = packet ["origin"]
	to = packet ["to"]
	print ("mimic:", origin, to);
	
	shutil.copy (origin, to)
	
	#os.system (f"cp '{ origin }' '{ to }'")

def mimic_recursively (packet):
	origin = packet ["origin"]
	to = packet ["to"]
	
	print ("mimic_recursively:", origin, to);
	
	shutil.copytree (origin, to, dirs_exist_ok = True)
	
	#os.system (f"cp -R '{ origin }' '{ to }'")



os.system ('apt install zip -y')



#--
#
#	This adds to the "build"
#
#		* Scroll (Brochure)
#		* Rules
#
mimic ({
	"origin": f"{ assets_path }/Rules.E.HTML",
	"to": f"{ module_build_path }/Rules.HTML"
})
mimic ({
	"origin": f"{ assets_path }/Scroll.E.HTML",
	"to": f"{ module_build_path }/Scroll.HTML"
})
#
#--



#--
#
#	Outer Rules:
#
#
#
os.system (f"rm -rf '{ module_outer_rules_path }'")
os.system (f"mkdir -p { module_outer_rules_path }")
#os.system (f"mkdir -p '{ module_outer_rules_path }/lib/Mech_Pet/Rules'")
mimic ({
	"origin": 	f"{ assets_path }/Rules.E.HTML",
	"to": 		f"{ module_outer_rules_path }/Rules.E.HTML"
})
mimic_recursively ({
	"origin": 	f"{ module_build_path }/lib/Mech_Pet/Rules",
	"to": 		f"{ module_outer_rules_path }/lib/Mech_Pet/Rules"
})
mimic ({
	"origin": 	f"{ module_build_path }/frozen_application_license.txt",
	"to":		f"{ module_outer_rules_path }/frozen_application_license.txt"
})
#
#--



#
#
#	zip
#
#
print ("zipping");
os.system (f"chmod -R 777 /Metro")
os.system (f'(cd { build_path } && zip -r "Mech_Pet.linux-x86_64.{ version }.zip" "Mech_Pet.linux-x86_64.{ version }")');
os.system (f'(cd { build_path } && zip -r "Mech_Pet.linux-x86_64.{ version }.Rules.zip" "Mech_Pet.linux-x86_64.{ version }.Rules")');
os.system (f"chmod -R 777 /Metro")
print ("done zipping");


#
#
#	create distribtuion
#
#
mimic_recursively ({
	"origin": 	module_build_path,
	"to": 		distribution_path_softwhere
})
mimic_recursively ({
	"origin": 	module_rules_path,
	"to": 		distribution_path_rules
})

mimic ({
	"origin": 	module_build_path_zip,
	"to":		distribution_path_softwhere_zip
})
mimic ({
	"origin": 	module_outer_rules_path_zip,
	"to":		distribution_path_rules_zip
})

#
#	
#	This is the Github message.
#
#
print (f"""

This is a Mech Pet that can live in a Linux OS that use a x86-64 Processor.

[Store Rules on OS]({ GH_Repo }/releases/download/publication_{ version }/Mech_Pet.{ Le_OS }.{ version }.Rules.zip)
[Adopt (Store to OS)]({ GH_Repo }/releases/download/publication_{ version }/Mech_Pet.{ Le_OS }.{ version }.zip)

Opening:
Open a terminal and run:

./Mech_Pet_{ version }.linux-x86_64/clap

After that, the Mech Pet should be here:
http://localhost:2300/

""")