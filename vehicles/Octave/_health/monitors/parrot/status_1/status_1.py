


''''
Octave_1 parrot check_EQ \
--origin "/Metro/vehicles/Octave/_health/monitors/parrot/status_1/example_equality/directory_1" \
--to "/Metro/vehicles/Octave/_health/monitors/parrot/status_1/example_equality/directory_2"
"'''

''''
Octave_1 parrot check_EQ \
--origin "/Metro/vehicles/Octave/_health/monitors/parrot/status_1/example_inequality/directory_1" \
--to "/Metro/vehicles/Octave/_health/monitors/parrot/status_1/example_inequality/directory_2"
"'''

''''
Octave_1 parrot equalize \
--origin "/Metro/vehicles/Octave/_health/monitors/parrot/status_1/example_equality" \
--to "/Metro/vehicles/Octave/_health/monitors/parrot/status_1/example_equality_2"

Octave_1 parrot check_EQ \
--origin "/Metro/vehicles/Octave/_health/monitors/parrot/status_1/example_equality" \
--to "/Metro/vehicles/Octave/_health/monitors/parrot/status_1/example_equality_2"
"'''

''''
	TODO:
		Octave parrot equalize
		Octave parrot check_EQ
		
		__glossary/Octave_1
"'''
def check_1 ():
	return;



checks = {
	'check 1': check_1
}