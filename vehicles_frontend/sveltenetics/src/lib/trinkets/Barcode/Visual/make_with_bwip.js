

//	The licensing for this one is kinda tough,
//	so commenting this for now.

/*
	barcode: [ 'azteccode', 'Aztec Code' ],
	barcode_options: [
		[ 'qrcode', 'QR Code' ],
		[ 'azteccode', 'Aztec Code' ]
	]
	
	<canvas 
		id="result" 
		bind:this={ barcode_element }
		
		style=""
	></canvas>
*/

/*
	make_with_bwip ({
		barcode_element, 
		packed_hexadecimal_string,
		size
	})
*/

/*
import bwipjs from 'bwip-js';

export const make_with_bwip = ({
	barcode_element,
	packed_hexadecimal_string,
	size
}) => {
	const canvas = barcode_element;
	
	const palette = '000000'
	
	// [ 'qrcode', 'QR Code' ],
	// [ 'azteccode', 'Aztec Code' ],
	
	const SVG = bwipjs.toSVG ({
		bcid: 'qrcode',
		
		text: packed_hexadecimal_string,
		
		scale: 3,
		height: 29,
		
		includetext: true,
		textxalign: 'center',

		barcolor: palette, 
		bordercolor: palette,
		textcolor: palette 
	});
	
	console.log ({ SVG })
	
	barcode_element.innerHTML = SVG;
}
*/