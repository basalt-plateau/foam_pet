
/*
	import { parse_styles } from '$lib/trinkets/styles/parse'
	let styles = parse_styles ({})

*/

export function parse_styles (styles) {
	let parsed = ""
	for (let key in styles) {
		parsed += key + ": " + styles [key] + "; "
	}
	
	return parsed;
}