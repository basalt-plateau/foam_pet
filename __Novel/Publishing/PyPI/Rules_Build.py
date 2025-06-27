

''''
	python3 /Metro/__Novel/Publishing/PyPI/Rules_Build.py
"'''


''''
	Description:
		Frontend:
			* delete /Metro/.pnpm-store
			
			* Builds the rules inside the Python3 module:
				* full licenses to:
					$Rules_Path/Laboratory/frontend_rules_entire.txt
					
				* license legend to:
					$Rules_Path/Laboratory/frontend_rules_legend.txt
				
		Python3:
			* Builds these inside the Python3 modules
			
		* clone rules into Sveltenetics
		
		* Build sveltnetics into Python3
"'''

''''
	Asks:
		Frontend: $Rules_Path/Frontend/
		Backend:  $Rules_Path/Python3/
"'''

import os
import subprocess


#--
#
FE_Path = "/Metro/Frontend_Vercel"
Python_Module_Path = "/Metro/vehicles/Mech_Pet"
#
#
Rules_Path = Python_Module_Path + "/Rules/Modules"
#
#
Rules_Path_FE = Rules_Path + "/Frontend"
Rules_Path_BE = Rules_Path + "/Python3"
#
#
Original_Rules_Path_PyPI = Python_Module_Path + "/Rules/Originals"
Original_Rules_Path_Svelte = FE_Path + "/static/Rules/Originals"
#
Sveltenetics_Static_Path = FE_Path + "/static/Rules/Modules"
#
#
Le_env = os.environ.copy ()
Le_env ["Rules_Path_FE"] = Rules_Path_FE;
#
#--

def system_proc (screenplay):
	print ("screenplay:", screenplay);
	os.system (screenplay);

def proc (screenplay):
	result = subprocess.run(
		screenplay, 
		cwd = FE_Path,
		env = Le_env
	)
	assert (result.returncode == 0);
	print ("played:", screenplay);

def build_rules ():
	os.system ("rm -rf /Metro/.pnpm-store");
	system_proc (f"rm -rf '{ Rules_Path }'");
	
	#
	#
	#	FE Modules Rules
	#
	#
	proc (["pnpm", "run", "build_frontend"])
	proc (["pnpm", "run", "rules_build"])

	
	#
	#
	#	PyPI Modules Rules
	#
	#
	system_proc (f"mkdir -p '{ Rules_Path_BE }'")
	system_proc (f"pip-licenses --with-license-file --format=json > '{ Rules_Path_BE }/PyPI_rules_entire.json'")
	system_proc (f"pip-licenses > '{ Rules_Path_BE }/PyPI_rules_legend.txt'")


	#
	#	Clone the module rules: PyPI to Sveltenetics
	#
	#
	system_proc (f"rm -rf '{ Sveltenetics_Static_Path }'");
	system_proc (f"mkdir -p '{ Sveltenetics_Static_Path }'");
	system_proc (f"cp -Rv '{ Rules_Path }/'* '{ Sveltenetics_Static_Path }/'");
	
	
	#
	#	Clone the original rules: PyPI to Sveltenetics
	#
	#
	#
	system_proc (f"rm -rf '{ Original_Rules_Path_Svelte }'");
	system_proc (f"mkdir -p '{ Original_Rules_Path_Svelte }'");
	system_proc (f"cp -Rv '{ Original_Rules_Path_PyPI }/'* '{ Original_Rules_Path_Svelte }/'");

	#
	#
	#	Need to build the frontend again for the PyPI module.
	#		Svelnetics -> PyPI
	#
	proc (["pnpm", "run", "build_frontend"])
	
	

build_rules ();