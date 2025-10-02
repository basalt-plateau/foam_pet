
''''
	python setup.py build
"'''

''''
	??
		This perhaps run after pypi publication is published?

"'''

'''
# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
}
'''

from cx_Freeze import setup, Executable



#
#
#	OS: Linux
#	
#
'''
	base:
		gui -> linux?
		Win32GUI
'''
version = "v2_0_0_0"
name = f"octave_nexus.linux-x86_64.{ version }"
base = "gui"


setup(
    name = "octave_nexus_cx",
    version = "0.1",
    description = "",
    options = {
		"build_exe": {
			"build_exe": f"vehicles_cx_freeze/build/{ name }",
			"include_path": [
				"vehicles"
			],
			"excludes": [],
			"zip_include_packages": [ ],
		}
	},
    executables = [
		Executable (
			"vehicles/octave_nexus/octave_nexus.py", 
			base = base
		),
		Executable (
			"vehicles/octave_nexus/clap.py", 
			base = base
		)
	],
)