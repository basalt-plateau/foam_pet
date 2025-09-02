


#\
#
import Emergency
#
#
import rich
import click
#
#
import json
import pathlib
import pprint
from os.path import dirname, join, normpath
import os
import sys
import subprocess
import time
#
#/

this_directory = pathlib.Path (__file__).parent.resolve ()
monitors_path = str (normpath (join (this_directory, f"__monitors")))
rooms_path = str (normpath (join (this_directory, f"rooms")))

mottos_path = "/Metro/Mottos"


def clique ():
	@click.group ()
	def group ():
		pass
	
	
	
	#
	#	prompt='path', 
	#
	#
	@click.command ("run-mottos")
	@click.option ('--path', help='', default = '')
	@click.option ('--pattern', help = '', default = '.Se.py')
	def command_run_mottos (path, pattern):	
		if (len (path) >= 1):
			glob_string = mottos_path + '/' + path
			db_directory = False
		else:
			#glob_string = monitors_path + '/**/*.Se.py'
			glob_string = mottos_path + '/**/*' + pattern;
			db_directory = normpath (join (this_directory, "DB"))
	
		print ("glob string:", glob_string);
	
		relative_path = "/Metro/Mottos"
		rooms_paths = [
			"/Metro/Mottos/_health/rooms"
		]

	
		promote = Emergency.on ({
			
			"intro_port": 52123,
			
			#	
			#	[necessary] 
			#	
			#	This is the file paths of the checks.
			#	
			"glob_string": glob_string,
			
			#
			#	[voluntary] 
			#		original = False
			#
			#	If False, the checks are run 
			#	one at a time.
			#
			"simultaneous": True,
			
			#
			#	[voluntary]
			#		original = 10
			#
			#	This is the limit on the amount
			#	of checks that can be run at the 
			#	same time.
			#
			"simultaneous_capacity": 1,

			#
			#	[voluntary]
			#		original = "99999999999999999999999"
			#
			#	After this time limit, lingering checks are stopped
			#	and reported as 
			#
			"time_limit": 120,
			
			#
			#	[voluntary]
			#		original = []
			#
			#	These are added to the sys.path of the process of
			#	each quest in the glob_string.
			#
			"module_paths": rooms_paths,

			#
			#	[voluntary]
			#		original = False
			#			False returns the absolute path.
			#
			#	This is the path that is subtracted from the absolute path
			#	in the health report.
			#
			#	For example:
			#		absolute path: /habitats/venue.1/health/monitors/health_1.py
			#		relative path: /habitats/venue.1/health/monitors
			#		reported path: health_1.py
			#
			"relative_path": relative_path,
			
			#
			#	[voluntary]
			#		original = False
			#			With False, a DB is not created 
			#			and reports aren't saved.
			#	
			#	This is where the results are kept.
			#	TinyDB is utilized.
			#
			"db_directory": db_directory,
			
			#
			#	[voluntary]
			#		original = 1
			#
			#	This is how the "proceeds" (report) is presented.
			#	1 might not be as good as 2.
			#
			"aggregation_format": 2
		})

		promote ["off"] ()

		#
		#	This is a detailed report
		#	of the technique.
		#
		rich.print_json (data = {
			"paths": promote ["proceeds"] ["paths"]
		})

		#
		#	This is the checks that did 
		#	not finish successfully.
		#
		rich.print_json (data = {
			"alarms": promote ["proceeds"] ["alarms"]
		})

		#
		#	This is concise stats about
		#	the  technique.
		#
		rich.print_json (data = {
			"stats": promote ["proceeds"] ["stats"]
		})
	
	
	#
	#	prompt='path', 
	#
	#
	@click.command ("run")
	@click.option ('--path', help='', default = '')
	@click.option ('--pattern', help = '', default = '.Se.py')
	def command_run (path, pattern):	
		if (len (path) >= 1):
			glob_string = monitors_path + '/' + path
			db_directory = False
		else:
			#glob_string = monitors_path + '/**/*.Se.py'
			glob_string = monitors_path + '/**/*' + pattern;
			db_directory = normpath (join (this_directory, "DB"))
	
		print ("glob string:", glob_string);
	
		promote = Emergency.on ({
			
			"intro_port": 52123,
			
			#	
			#	[necessary] 
			#	
			#	This is the file paths of the checks.
			#	
			"glob_string": glob_string,
			
			#
			#	[voluntary] 
			#		original = False
			#
			#	If False, the checks are run 
			#	one at a time.
			#
			"simultaneous": False,
			
			#
			#	[voluntary]
			#		original = 10
			#
			#	This is the limit on the amount
			#	of checks that can be run at the 
			#	same time.
			#
			"simultaneous_capacity": 1,

			#
			#	[voluntary]
			#		original = "99999999999999999999999"
			#
			#	After this time limit, lingering checks are stopped
			#	and reported as 
			#
			"time_limit": 120,
			
			#
			#	[voluntary]
			#		original = []
			#
			#	These are added to the sys.path of the process of
			#	each quest in the glob_string.
			#
			"module_paths": [
				rooms_path
			],

			#
			#	[voluntary]
			#		original = False
			#			False returns the absolute path.
			#
			#	This is the path that is subtracted from the absolute path
			#	in the health report.
			#
			#	For example:
			#		absolute path: /habitats/venue.1/health/monitors/health_1.py
			#		relative path: /habitats/venue.1/health/monitors
			#		reported path: health_1.py
			#
			"relative_path": monitors_path,
			
			#
			#	[voluntary]
			#		original = False
			#			With False, a DB is not created 
			#			and reports aren't saved.
			#	
			#	This is where the results are kept.
			#	TinyDB is utilized.
			#
			"db_directory": db_directory,
			
			#
			#	[voluntary]
			#		original = 1
			#
			#	This is how the "proceeds" (report) is presented.
			#	1 might not be as good as 2.
			#
			"aggregation_format": 2
		})

		promote ["off"] ()

		#
		#	This is a detailed report
		#	of the technique.
		#
		rich.print_json (data = {
			"paths": promote ["proceeds"] ["paths"]
		})

		#
		#	This is the checks that did 
		#	not finish successfully.
		#
		rich.print_json (data = {
			"alarms": promote ["proceeds"] ["alarms"]
		})

		#
		#	This is concise stats about
		#	the  technique.
		#
		rich.print_json (data = {
			"stats": promote ["proceeds"] ["stats"]
		})
		
	group.add_command (command_run)
	group.add_command (command_run_mottos)
	
	group ()


clique ()