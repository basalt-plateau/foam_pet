
''''
	python setup.py build
"'''

''''
	??
		This perhaps run after pypi publication is published?

"'''

from cx_Freeze import setup, Executable

'''
# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": ["tkinter", "unittest"],
    "zip_include_packages": ["encodings", "PySide6", "shiboken6"],
}
'''

# .py_3_11

version = "v1_1_0_0"


#
#
#	OS: Linux
#
#
name = f"octave_nexus.linux-x86_64.{ version }"

#base = "Win32GUI"
base = "gui"

#
#
#--
#
#

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