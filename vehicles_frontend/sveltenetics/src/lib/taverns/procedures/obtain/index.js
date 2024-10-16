

/*
	// this always returns a string

	import { obtain } from '$lib/taverns/procedures/obtain'
	
	//
	//	obtain 'number' returns 0 if cannot determine....
	//
	obtain ('number') ({ 's': '1' }, [ 's' ], '')
*/


import _get from 'lodash/get'


export function obtain (to_obtain) {
	return function () {
		try {
			
			let candidate = undefined;
			if (arguments.length === 3) {
				candidate = _get (
					arguments [0], 
					arguments [1], 
					arguments [2]
				)
			}
			else if (arguments.length === 2) {
				candidate = _get (
					arguments [0], 
					arguments [1], 
					''
				)
			}
			else if (arguments.length === 1) {
				candidate = arguments [0]
			}
			
			if (typeof candidate === to_obtain) {
				return candidate;
			}
			
			console.log (arguments);
			throw new Error (`A ${ to_obtain } could not be obtained from the preceeding arguments.`)		
		}
		catch (exception) {
			console.warn (exception)
		}
		
		if (to_obtain === 'number') {
			return 0
		}
		
		return ''
	}
}