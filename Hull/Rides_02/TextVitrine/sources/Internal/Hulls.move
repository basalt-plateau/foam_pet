


module Builder_01::Module_Hulls {
	friend Builder_01::Module_Ruler_Hulls;	
	friend Builder_01::Module_Ruler_Hull;
	friend Builder_01::Module_Ruler_Texts;

	friend Builder_01::Module_Denizen_Texts;

	friend Builder_01::Module_Guest_Hulls;
	friend Builder_01::Module_Guest_Hull;
	friend Builder_01::Module_Guest_Texts;
	friend Builder_01::Module_Guest_Logs;
	
	use std::vector;
	use std::string::{ Self, String, utf8 };
	use std::signer;
	
	#[view] public fun Volitions () : String { 
		use Builder_01::Rules_Module::{ Volitions_01 }; Volitions_01 ()
	}	

	// use Builder_01::Endings_Module;
	use Builder_01::Module_Ruler::{ Self, ensure_acceptor_is_ruler };
	use Builder_01::Text_Module::{
		Text,
		Text__create,
		
		Text__change_text,
		Text__change_seconds_IX_planet_3_roughly,
		Text__change_sent_at_index,
		
		Text__retrieve_writer_address,
		Text__retrieve_text,
		Text__retrieve_seconds_IX_planet_3_roughly,
		Text__retrieve_sent_at_index
	};
	use Builder_01::Module_Hull::{
		Hull,
		Hull__create,
		Hull__change_status,
		Hull__delete_texts,
		Hull__mut_retrieve_texts,
		Hull__retrieve_status,
		Hull__retrieve_platform,
		Hull__retrieve_texts,
		Hull__retrieve_count_of_texts,
		Hull__retrieve_index_of_next_text,
		Hull__increase_index_of_next_text
	};
	use Builder_01::Module_Hull_Info_Envelope::{
		Hull_Info_Envelope,
		Hull_Info_Envelope__create
		
	};
	use Builder_01::Module_String;
	use Builder_01::Module_Logs::{
		Log,
		Log__create,
		Log__name,
		Log__seconds_IX_planet_3_roughly
	};
	use Builder_01::Module_Guest_Show::{
		Guest_Shows,
		create_guest_shows
	};
	use Builder_01::Module_Text_Envelope::{
		Text_Envelope,
		Text_Envelope__create
	};
	
	const Limiter_Ruler_the_platform_with_writer_address_is_empty : u64 = 0xF000001;	
	const Limiter_writer_has_less_than_the_amount_of_Octas_necessary_to_send : u64 = 0xF000002;
	const Limiter_the_hull_is_not_going : u64 = 0xF000003;
	const Limiter_Text_String_needs_to_be_less_than_one_hundred_characters : u64 = 0xF000004;	
	const Limiter_Refund_must_be_1_apt_or_fewer : u64 = 0xF000005;	
	const Limiter_Hull_String_needs_to_be_less_than_characters_limit : u64 = 0xF000006;
	
	const One_APT : u64 = 100000000;
	
	const Text_length_limit : u64 = 125;
	const Platform_name_length_limit : u64 = 40;

	
	
	/*
		MVP2:
			struct TextVitrine has key, drop {
				hulls : Hulls
			}
		
			struct Hulls has store, drop {
				hulls_vector : vector<Hull>
			}
	*/
	/*
		status:
			playing
			paused
			
		text length limit is 125
	*/
	struct Hulls has key, drop {
		status : String,
		price_of_text_in_octas : u64,
		hulls : vector<Hull>,
		
		logs : vector<Log>,
		
		hull_next_index: u64,
		
		guest_shows : Guest_Shows
	}
	friend fun Hulls_Count () : u64 acquires Hulls {
		let hulls_borrowed = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		vector::length (& hulls_borrowed.hulls)
	}
	
	
	////////
	//
	//	Hulls: Retrieve Mut
	//
	//
	friend fun Hulls__mut_retrieve_hulls (hulls : &mut Hulls) : &mut vector<Hull> {
		&mut hulls.hulls
	}
	friend fun Hulls__mut_retrieve_hull (
		platform_name : String,
		hulls_mline: &mut vector<Hull>
	) : &mut Hull acquires Hulls {
		/*
			let hulls_mline = Hulls__mut_retrieve_hull (
				"Hull 1", 
				borrow_global_mut<Hulls>(Module_Ruler::obtain_address ())
			);
		*/
		let index_of_hull = search_for_index_of_hull (platform_name);
		let hull_mline : &mut Hull = vector::borrow_mut (hulls_mline, index_of_hull);
		hull_mline
	}
	//		
	//	ensure:
	//		Hulls__ensure_is_playing ();
	//		
	public fun Hulls__ensure_is_playing () acquires Hulls {
		let hulls_borrowed = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		if (hulls_borrowed.status != utf8 (b"playing")) {
			abort 0x706175736564
		}
	}
	//
	//
	//
	//	Hulls: Fluctuate
	//
	friend fun Begin_Hulls (ruler : & signer) {
		ensure_acceptor_is_ruler (ruler);
		
		let price_of_text_in_octas : u64 = 100000000;
		
		let hull_verse = 0;
		let front = Hull__create (
			utf8 (b"playing"),
			utf8 (b""),
			vector::empty<Text>(),
			hull_verse
		);
		
		let hulls_vector = vector::empty<Hull>();
		vector::push_back (&mut hulls_vector, front);
		
		let verse = 1;
		let hulls = Hulls {
			status: utf8 (b"playing"),
			price_of_text_in_octas : price_of_text_in_octas,
			hulls : hulls_vector,
			
			logs : vector::empty<Log>(),
			hull_next_index : verse,
			
			guest_shows : create_guest_shows ()
		};
		
		move_to<Hulls>(ruler, hulls)
	}
	friend fun Hulls_Delete () acquires Hulls {
		let ruler = Module_Ruler::obtain_address ();
		move_from<Hulls>(ruler);
	}
	friend fun Hulls_Change_Status (
		ruler : & signer,
		status : String
	) acquires Hulls {
		ensure_acceptor_is_ruler (ruler);
		let ruler_address = Module_Ruler::obtain_address ();
		
		let hulls = borrow_global_mut<Hulls>(ruler_address);
		hulls.status = status;
	}
	//	
	//	
	//	Constants:
	//	
	friend fun are_Hulls_built () : String {
		if (exists<Hulls>(Module_Ruler::obtain_address ())) {
			return utf8 (b"yup")
		};
		
		utf8 (b"no")
	}
	friend fun Hulls_Status () : String acquires Hulls {
		borrow_global<Hulls>(Module_Ruler::obtain_address ()).status
	}
	friend fun retrieve_vector_of_hull_names () : vector<String> acquires Hulls {
		let envelope = vector::empty<String>();
		
		let hulls_ref = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		let hulls_length = vector::length (& hulls_ref.hulls);
		for (index in 0..hulls_length) {
			let hull_ref = vector::borrow (& hulls_ref.hulls, index);
			vector::push_back (&mut envelope, Hull__retrieve_platform (hull_ref));
		};
		
		envelope
	}
	friend fun retrieve_vector_of_hulls_info () : vector<Hull_Info_Envelope> acquires Hulls {
		let envelope = vector::empty<Hull_Info_Envelope>();
		
		let hulls_ref = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		let hulls_length = vector::length (& hulls_ref.hulls);
		for (index in 0..hulls_length) {
			let hull_ref = vector::borrow (& hulls_ref.hulls, index);
			
			let hull_info_envelope = Hull_Info_Envelope__create (
				Hull__retrieve_status (hull_ref),
				Hull__retrieve_platform (hull_ref),
				Hull__retrieve_count_of_texts (hull_ref)
			);
			
			vector::push_back (&mut envelope, hull_info_envelope);
		};
		
		envelope
	}
	
	/*
		let hulls_info = retrieve_screened_vector_of_hulls_info (utf8 (b"platform"));
	*/
	friend fun retrieve_screened_vector_of_hulls_info (platform_name_partial : String) : vector<Hull_Info_Envelope> acquires Hulls {
		let envelope = vector::empty<Hull_Info_Envelope>();
		
		let hulls_ref = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		let hulls_length = vector::length (& hulls_ref.hulls);
		for (index in 0..hulls_length) {
			let hull_ref = vector::borrow (& hulls_ref.hulls, index);
			let platform_name : String = Hull__retrieve_platform (hull_ref);
			
			// screen by name
			if (Module_String::does_string_have_partial (
				& platform_name, 
				& platform_name_partial
			) == utf8 (b"yep")) {
				let hull_info_envelope = Hull_Info_Envelope__create (
					Hull__retrieve_status (hull_ref),
					Hull__retrieve_platform (hull_ref),
					Hull__retrieve_count_of_texts (hull_ref)
				);
				
				vector::push_back (&mut envelope, hull_info_envelope);
			}
		};
		
		envelope
	}
	//
	//
	fun Ensure_Hulls_is_Playing () acquires Hulls {
		if (Hulls_Status () != utf8 (b"playing")) {
			abort Limiter_the_hull_is_not_going
		}
	}
	//
	////////
	
	
	////////
	//
	//	Logs
	//
	//
	friend fun retrieve__text_sent_logs (
		name : String,
		from_ms : u64,
		to_ms : u64
	) : vector<Log> acquires Hulls {
		let envelope = vector::empty<Log>();
		
		let hulls_ref = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		let logs_length = vector::length (& hulls_ref.logs);
		for (index in 0..logs_length) {
			let log = * vector::borrow (& hulls_ref.logs, index);

			if (Log__name (log) != name) {
				continue;
			};
			
			let now_second = Log__seconds_IX_planet_3_roughly (log);
			if (now_second < from_ms) {
				continue;
			};
			if (now_second > to_ms) {
				continue;
			};
			
			vector::push_back (&mut envelope, log);
		};
		
		envelope
	}
	//
	////////
	
	
	////////
	//
	//	Hull Fluctuations:
	//
	//
	friend fun Hulls__Hull__change_status (
		_consenter : & signer,
		platform_name : String,
		status : String
	) acquires Hulls {
		let index_of_hull = search_for_index_of_hull (platform_name);
		
		let hulls_key_mref = borrow_global_mut<Hulls>(Module_Ruler::obtain_address ());
		let hulls_mref = &mut hulls_key_mref.hulls;
		let hull_mref : &mut Hull = vector::borrow_mut (hulls_mref, index_of_hull);
		
		Hull__change_status (hull_mref, status);
	}
	friend fun Hulls__Hull__delete_every_text (
		_consenter : & signer, 
		platform_name : String
	) acquires Hulls {		
		let index_of_hull = search_for_index_of_hull (platform_name);
		
		let hulls_key_mref = borrow_global_mut<Hulls>(Module_Ruler::obtain_address ());
		let hulls_mref = &mut hulls_key_mref.hulls;
		let hull_mref : &mut Hull = vector::borrow_mut (hulls_mref, index_of_hull);
		
		Hull__delete_texts (hull_mref);
	}
	friend fun Hulls__Hull__delete_platform (
		_consenter : & signer, 
		platform_name : String
	) acquires Hulls {
		let index_of_hull = search_for_index_of_hull (platform_name);
		
		let hulls_key_mref = borrow_global_mut<Hulls>(Module_Ruler::obtain_address ());
		let hulls_mref = &mut hulls_key_mref.hulls;
		
		vector::remove (hulls_mref, index_of_hull);
	}
	//
	//	Hull Fluctuations Internal
	//
	//
	fun search_or_begin_hull (platform_name : String) : u64 acquires Hulls {
		/*
			Search for the index of the hull.
			If the hull does not exist, then start it.
		*/
		let hulls = borrow_global_mut<Hulls>(Module_Ruler::obtain_address ());
		let hull_next_index = hulls.hull_next_index;
		hulls.hull_next_index = hulls.hull_next_index + 1;
		
		let hulls_length = vector::length (& hulls.hulls);
		for (index in 0..hulls_length) {
			let hull_ref = vector::borrow (& hulls.hulls, index);
			if (Hull__retrieve_platform (hull_ref) == platform_name) {
				return index
			}
		};
		
		if (string::length (& platform_name) > Platform_name_length_limit) {
			abort Limiter_Hull_String_needs_to_be_less_than_characters_limit
		};
		
		let hull = Hull__create (
			utf8 (b"playing"),
			platform_name,
			vector::empty<Text>(),
			hull_next_index
		);
		
		vector::push_back (&mut hulls.hulls, hull);
		
		let index = vector::length (& hulls.hulls) - 1;
		index
	}
	//
	//	[Constant]
	//
	/*
		let status = Hulls__Hull__retrieve_status (utf8 (b""));
	*/
	friend fun Hulls__Hull__retrieve_status (platform : String) : String acquires Hulls {
		let index_of_hull = search_for_index_of_hull (platform);
		
		let hulls_key_mref = borrow_global_mut<Hulls>(Module_Ruler::obtain_address ());
		let hulls_mref = &mut hulls_key_mref.hulls;
		let hull_mref : &mut Hull = vector::borrow_mut (hulls_mref, index_of_hull);
		
		Hull__retrieve_status (hull_mref)
	}
	friend fun search_for_index_of_hull (platform : String) : u64 acquires Hulls {
		let hulls = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		
		let hulls_length = vector::length (& hulls.hulls);
		for (index in 0..hulls_length) {
			let hull_ref = vector::borrow (& hulls.hulls, index);
			if (Hull__retrieve_platform (hull_ref) == platform) {
				return index
			}
		};
		
		abort 1
	}
	friend fun search_for_index_of_hull_v2 (platform : String) : (bool, u64) acquires Hulls {
		/*
			let (exists, index_of_hull) = search_for_index_of_hull_v2 (platform);
			if (exists != true) {
				return hull_texts_envelope
			};
		*/
		let hulls = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		
		let hulls_length = vector::length (& hulls.hulls);
		for (index in 0..hulls_length) {
			let hull_ref = vector::borrow (& hulls.hulls, index);
			if (Hull__retrieve_platform (hull_ref) == platform) {
				return (true, index)
			}
		};
		
		(false, 0)
	}
	friend fun Retrieve_Texts_with_Thresholds (
		platform : String,
		seconds_begin : u64,
		seconds_end : u64
	) : vector<Text_Envelope> acquires Hulls {
		use aptos_framework::coin;
		use aptos_framework::aptos_coin;
		
		let hull_texts_envelope = vector::empty<Text_Envelope>();
		
		//
		//	if hull not found, 
		//	return an empty vector.
		//
		let (exists, index_of_hull) = search_for_index_of_hull_v2 (platform);
		if (exists != true) {
			return hull_texts_envelope
		};
		
		let hulls = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		let hull_ref : & Hull = vector::borrow (& hulls.hulls, index_of_hull);
		let hull_texts = & Hull__retrieve_texts (hull_ref);
		let count_of_hull_texts = vector::length (hull_texts);
		for (index in 0..count_of_hull_texts) {
			let text_amp = vector::borrow (hull_texts, index);
			let text_ref_writer_address = Text__retrieve_writer_address (text_amp);
			let text_ref_seconds_IX_planet_3_roughly = Text__retrieve_seconds_IX_planet_3_roughly (text_amp);
			
			let writer_balance = coin::balance<aptos_coin::AptosCoin>(
				text_ref_writer_address
			);
			
			if (text_ref_seconds_IX_planet_3_roughly >= seconds_begin && text_ref_seconds_IX_planet_3_roughly <= seconds_end) {
				let this_text_envelope = Text_Envelope__create (
					text_ref_writer_address,
					writer_balance,
					Text__retrieve_text (text_amp),
					Text__retrieve_sent_at_index (text_amp),
					Text__retrieve_seconds_IX_planet_3_roughly (text_amp)				
				);

				vector::push_back (&mut hull_texts_envelope, this_text_envelope);
			}
		};
		
		hull_texts_envelope
	}
	
	//
	////////
	
	
	////////
	//
	//	Texts: 
	//		[Constants]
	//
	friend fun Retrieve_Count_of_Texts (platform : String) : u64 acquires Hulls {
		//
		//	if hull not found, 
		//
		let (exists, index_of_hull) = search_for_index_of_hull_v2 (platform);
		if (exists != true) {
			return 0
		};
		
		let hulls = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		let hull_ref : & Hull = vector::borrow (& hulls.hulls, index_of_hull);
		let hull_texts = & Hull__retrieve_texts (hull_ref);
		
		vector::length (hull_texts)
	}
	friend fun Retrieve_Texts (platform : String) : vector<Text_Envelope> acquires Hulls {
		use aptos_framework::coin;
		use aptos_framework::aptos_coin;
		
		let hull_texts_envelope = vector::empty<Text_Envelope>();
		
		//
		//	if hull not found, 
		//	return an empty vector.
		//
		let (exists, index_of_hull) = search_for_index_of_hull_v2 (platform);
		if (exists != true) {
			return hull_texts_envelope
		};
		
		let hulls = borrow_global<Hulls>(Module_Ruler::obtain_address ());
		let hull_ref : & Hull = vector::borrow (& hulls.hulls, index_of_hull);
		let hull_texts = & Hull__retrieve_texts (hull_ref);
		let count_of_hull_texts = vector::length (hull_texts);
		for (index in 0..count_of_hull_texts) {
			let text_ref = vector::borrow (hull_texts, index);
			let text_ref_writer_address = Text__retrieve_writer_address (text_ref);
			
			let writer_balance = coin::balance<aptos_coin::AptosCoin>(text_ref_writer_address);

			let this_text_envelope = Text_Envelope__create (
				text_ref_writer_address,
				writer_balance,
				Text__retrieve_text (text_ref),
				Text__retrieve_sent_at_index (text_ref),
				Text__retrieve_seconds_IX_planet_3_roughly (text_ref)				
			);
			
			vector::push_back (&mut hull_texts_envelope, this_text_envelope);
		};
		
		hull_texts_envelope
	}
	
	//
	//
	//	[Flux]
	//
	/*
		This returns the send_index (sent_at_index)
	*/
	friend fun Send_Text (
		writer : & signer,
		text : String,
		platform : String
	) : u64 acquires Hulls {
		use aptos_framework::coin;
		use aptos_framework::aptos_coin::{ AptosCoin };
		
		////
		//
		//	Rules
		//
		//
		if (string::length (& text) > Text_length_limit) {
			abort Limiter_Text_String_needs_to_be_less_than_one_hundred_characters
		};
		//
		////
		
		let writer_address = signer::address_of (writer);
		let ruler_address = Module_Ruler::obtain_address ();
		
		////
		//
		//	
		//
		//
		let index_of_hull = search_or_begin_hull (platform);
		let hulls_mref = borrow_global_mut<Hulls>(ruler_address);
		let hull_mref : &mut Hull = vector::borrow_mut (&mut hulls_mref.hulls, index_of_hull);
		let price_of_text_in_octas = hulls_mref.price_of_text_in_octas;
		//
		////
		
		////
		//
		//	Deduct 1 APT
		//		* Ensure Consenter has >= 1 * "amount_of_plays_to_buy" APT.
		//		* Deduct the APT
		//
		if (coin::balance<AptosCoin>(writer_address) < price_of_text_in_octas) { 
			abort Limiter_writer_has_less_than_the_amount_of_Octas_necessary_to_send
		};
		coin::transfer<AptosCoin>(writer, ruler_address, price_of_text_in_octas);
		//
		////
		
		////
		//
		//	Add to Log
		//
		//
		vector::push_back (
			&mut hulls_mref.logs, 
			Log__create (utf8 (b"send_text"), writer_address, 1)
		);
		//
		////
		
		let send_index = Hull__retrieve_index_of_next_text (hull_mref);
		Hull__increase_index_of_next_text (hull_mref);
		
		let hull_texts = Hull__mut_retrieve_texts (hull_mref);
		for (index in 0..vector::length (hull_texts)) {
			let text_mref = vector::borrow_mut (hull_texts, index);
			if (Text__retrieve_writer_address (text_mref) == writer_address) {
				//
				//	The texter already has a text on this platform,
				//	therefore a text modification occurs.
				//
				Text__change_text (text_mref, text);
				Text__change_seconds_IX_planet_3_roughly (text_mref);
				Text__change_sent_at_index (text_mref, send_index);
								
				return send_index
			}
		};
		
		
		//
		//	The texter does not have a text on this platform,
		//	therefore a text is written.
		//
		let this_text = Text__create (writer_address, text, send_index);
		vector::push_back (hull_texts, this_text);
		
		send_index
	}
	friend fun Delete_Text (texter : & signer, platform : String) acquires Hulls {
		let texter_address = signer::address_of (texter);		
		
		let index_of_hull = search_for_index_of_hull (platform);
		let hulls = borrow_global_mut<Hulls>(Module_Ruler::obtain_address ());
		let hull_ref : &mut Hull = vector::borrow_mut (&mut hulls.hulls, index_of_hull);

		let hull_texts = Hull__mut_retrieve_texts (hull_ref);
		for (index in 0..vector::length (hull_texts)) {
			let text_ref = vector::borrow_mut (hull_texts, index);
			if (Text__retrieve_writer_address (text_ref) == texter_address) {
				vector::remove (hull_texts, index);
				return;
			}
		};
		
		abort 260141
	}
	
	/*
		Denizen_Text_Delete_at_Send_Index (texter_acceptance
	*/
	friend fun Denizen_Text_Delete_at_Send_Index (
		deleter_acceptance : & signer,
		platform_name : String,
		sent_index : u64
	) : String acquires Hulls {
		let ride_address = Module_Ruler::obtain_address ();
		let deleter_address = signer::address_of (deleter_acceptance);	
		
		let index_of_hull = search_for_index_of_hull (platform_name);
		let hulls = borrow_global_mut<Hulls>(ride_address);
		let hull_mref : &mut Hull = vector::borrow_mut (&mut hulls.hulls, index_of_hull);
		
		let hull_texts = Hull__mut_retrieve_texts (hull_mref);
		for (index_of_text in 0..vector::length (hull_texts)) {
			let text_ref = vector::borrow_mut (hull_texts, index_of_text);
			
			if (Text__retrieve_sent_at_index (text_ref) == sent_index) {
				let texter_address = Text__retrieve_writer_address (text_ref);
				
				if (deleter_address == texter_address) {
					vector::remove (hull_texts, index_of_text);
					return utf8 (b"deleted")
				}
				else {
					abort 0x04938;
				}
			}
		};
		
		abort Limiter_Ruler_the_platform_with_writer_address_is_empty
	}
	
	friend fun Text_Delete_at_Send_Index (
		platform_name : String,
		sent_index : u64
	) : String acquires Hulls {
		let ride_address = Module_Ruler::obtain_address ();
		
		let index_of_hull = search_for_index_of_hull (platform_name);
		let hulls = borrow_global_mut<Hulls>(ride_address);
		let hull_mref : &mut Hull = vector::borrow_mut (&mut hulls.hulls, index_of_hull);
		
		let hull_texts = Hull__mut_retrieve_texts (hull_mref);
		for (index_of_text in 0..vector::length (hull_texts)) {
			let text_ref = vector::borrow_mut (hull_texts, index_of_text);
			
			if (Text__retrieve_sent_at_index (text_ref) == sent_index) {
				vector::remove (hull_texts, index_of_text);
				return utf8 (b"deleted")
			}
		};
		
		abort Limiter_Ruler_the_platform_with_writer_address_is_empty
	}
	
	
	friend fun Ruler_Text_Delete_with_Refund_at_Index (
		deleter_acceptance : & signer,
		platform_name : String,
		send_index : u64, 
		octas_refund : u64
	) acquires Hulls {
		use aptos_framework::coin;
		use aptos_framework::aptos_coin::{ AptosCoin };
		
		let deleter_address = signer::address_of (deleter_acceptance);
		
		assert! (
			Text_Delete_at_Send_Index (platform_name, send_index) == utf8 (b"deleted"),
			0xEF00000
		);
		
		
		////
		//
		//	Deduct Refund Octas
		//		* Ensure octas_refund is less than 1 apt.
		//		* Deduct the APT
		//
		if (octas_refund > 100000000) { 
			abort Limiter_Refund_must_be_1_apt_or_fewer
		};
		coin::transfer<AptosCoin>(deleter_acceptance, deleter_address, octas_refund);
		//
		////
		
		
		////
		//
		//	Add to Log
		//
		//
		let hulls_mref = borrow_global_mut<Hulls>(Module_Ruler::obtain_address ());
		vector::push_back (
			&mut hulls_mref.logs, 
			Log__create (utf8 (b"refund"), deleter_address, 1)
		);
		//
		////
	}
	
	/*
		Delete a platform text by it's envelope index.
	*/
	friend fun Ruler_Text_Delete_at_Index (
		consenter : & signer,
		platform_name : String,
		sent_at_index : u64
	) : address acquires Hulls {
		ensure_acceptor_is_ruler (consenter);
		
		let ruler_address = Module_Ruler::obtain_address ();
		
		let index_of_hull = search_for_index_of_hull (platform_name);
		let hulls = borrow_global_mut<Hulls>(ruler_address);
		let hull_mref : &mut Hull = vector::borrow_mut (&mut hulls.hulls, index_of_hull);
		
		let hull_texts = Hull__mut_retrieve_texts (hull_mref);
		for (index_of_text in 0..vector::length (hull_texts)) {
			let text_ref = vector::borrow_mut (hull_texts, index_of_text);
			if (Text__retrieve_sent_at_index (text_ref) == sent_at_index) {
				let texter_address = Text__retrieve_writer_address (text_ref);
				vector::remove (hull_texts, index_of_text);
				return texter_address
			}
		};
		
		abort Limiter_Ruler_the_platform_with_writer_address_is_empty
	}
	friend fun Ruler_Text_Delete_with_Refund (
		consenter : & signer,
		writer_address : address,
		platform : String,
		octas_refund : u64
	) acquires Hulls {
		use aptos_framework::coin;
		use aptos_framework::aptos_coin::{ AptosCoin };
		
		Ruler_Delete_Text (consenter, writer_address, platform);
		
		if (octas_refund > 100000000) { 
			abort Limiter_Refund_must_be_1_apt_or_fewer
		};
		
		////
		//
		//	Deduct Refund Octas
		//		* Ensure Consenter has >= 1 * "amount_of_plays_to_buy" APT.
		//		* Deduct the APT
		//
		if (coin::balance<AptosCoin>(writer_address) < octas_refund) { 
			abort Limiter_writer_has_less_than_the_amount_of_Octas_necessary_to_send
		};
		coin::transfer<AptosCoin>(consenter, writer_address, octas_refund);
		//
		////
		
		
		////
		//
		//	Add to Log
		//
		//
		let hulls_mref = borrow_global_mut<Hulls>(Module_Ruler::obtain_address ());
		vector::push_back (
			&mut hulls_mref.logs, 
			Log__create (utf8 (b"refund"), writer_address, 1)
		);
		//
		////
	}
	friend fun Ruler_Delete_Text (
		consenter : & signer,
		writer_address : address,
		platform : String 
	) acquires Hulls {
		ensure_acceptor_is_ruler (consenter);
		
		let ruler_address = Module_Ruler::obtain_address ();
		
		let index_of_hull = search_for_index_of_hull (platform);
		let hulls = borrow_global_mut<Hulls>(ruler_address);
		let hull_mref : &mut Hull = vector::borrow_mut (&mut hulls.hulls, index_of_hull);
		
		let hull_texts = Hull__mut_retrieve_texts (hull_mref);
		for (index_of_text in 0..vector::length (hull_texts)) {
			let text_ref = vector::borrow_mut (hull_texts, index_of_text);
			if (Text__retrieve_writer_address (text_ref) == writer_address) {
				vector::remove (hull_texts, index_of_text);
				return;
			}
		};
		
		abort Limiter_Ruler_the_platform_with_writer_address_is_empty
	}
	//
	////////
	

	
	


}