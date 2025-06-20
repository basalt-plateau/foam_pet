

/*
	import { loop } from '$lib/taverns/loop/index.js'
	 
	const loop_1 = loop ({
		wait: 2000,
		action: () => {
		 
		}
	})
	
	loop_1.play ()
		//
		//	This is like a planet spinning,
		//	Action happens, then like clock
		//	starts another action.
		//
		//	Example:
		// 		Action
		// 		await 2000 -> Action
		// 		await 2000 -> Action
		//
	
	loop_1.stop ()
	loop_1.play ()
*/

/*
	import { loop } from '$lib/taverns/loop'
	
	const loop_1 = loop ({
		wait: 2000,
		wait_for_response: "yes",
		action: async () => {
		 
		}
	})
	
	loop_1.play ()
		//
		//	This waits for action to complete,
		//	before starting wait period.
		//
		// await Action
		// await 2000
		// await Action
		// await 2000
		//
	
	loop_1.stop ()
	loop_1.play ()
*/

/*
	Action
	wait 2000
	Action
	wait 2000
*/

/*
	wait_for_response = "yes"
	
		This waits for the action to complete
		before starting the next cycle.
		
		
	wait_for_response = "no"
	
		This is like a planet orbiting a star.
		
		The next cycle starts without waiting
		for the action to complete.
*/


export const loop = ({
	wait,
	action,
	wait_for_response = "no"
}) => {
	let playing = "no"
	
	let timeout = ""
	const the_loop = async () => {
		if (playing === "yes") {
			if (wait_for_response === "yes") {
				try {
					await action ();
				}
				catch (exception) {
					console.error (exception)
				}
			}
			else {
				setTimeout (() => {
					action ();
				})
			}
		}
		
		await new Promise (resolve => {
			timeout = setTimeout (() => {
				resolve ()
			}, wait)
		})
		
		if (playing === "yes") {
			clearTimeout (timeout)
			the_loop ();
		}
	}
	
	return {
		play: () => {
			if (playing === "no") {
				playing = "yes"
				the_loop ()
			}
		},
		stop: () => {
			clearTimeout (timeout)
			playing = "no"
		}
	}
}