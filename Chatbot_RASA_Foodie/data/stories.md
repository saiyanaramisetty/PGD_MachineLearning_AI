## happy scenario
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "Hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "bangalore"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "bangalore"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* telling_email{"email": "indlasunil.ai@gmail.com"}
    - slot{"email": "indlasunil.ai@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* telling_location_cuisine{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
* telling_location{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "Prayagraj"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "amaravati"}
    - slot{"location": "amaravati"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
* telling_location{"location": "Tirupati"}
    - slot{"location": "Tirupati"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
* telling_location{"location": "Visakhapatnam"}
    - slot{"location": "Visakhapatnam"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "Visakhapatnam"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_anythingelse
* telling_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* telling_location_cuisine{"cuisine": "chinese", "location": "agra"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "agra"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "agra"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* telling_budget{"budget": "pocket friendly budget"}
    - slot{"budget": "pocket friendly budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* telling_location_cuisine{"cuisine": "north indian", "location": "Patna"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Patna"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "Patna"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* deny
    - utter_ask_location
* telling_location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "mumbai"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm{"affirm": "Yop"}
    - utter_ask_emailtosend
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* telling_location_cuisine{"cuisine": "mexican", "location": "hyderabad"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* telling_location_cuisine{"cuisine": "chinese", "budget": "high budget"}
    - slot{"budget": "high budget"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* telling_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "bangalore"}
    - slot{"location_match": "one"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* deny
    - utter_ask_howcanhelp
* telling_budget{"location": "hyderabad", "budget": "pocket friendly budget"}
    - slot{"budget": "pocket friendly budget"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_affirm_cuisine
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
* goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "pune"}
    - slot{"location": "pune"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "pune"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_cuisine{"budget": "low budget", "cuisine": "chinese"}
    - slot{"budget": "low budget"}
    - slot{"cuisine": "chinese"}
    - utter_slot_values
* deny
    - utter_ask_howcanhelp
* restaurant_search
    - utter_ask_location
* telling_location_cuisine{"cuisine": "south indian", "location": "delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "delhi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "delhi"}
    - slot{"location_match": "one"}
    - utter_slot_values
* deny
    - utter_ask_location
* telling_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "delhi"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_location{"location": "south indian"}
    - slot{"location": "south indian"}
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* telling_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "delhi"}
    - slot{"location_match": "one"}
    - utter_slot_values
* deny
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_anythingelse
* affirm
    - utter_ask_emailaddress
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* telling_location_cuisine{"budget": "pocket friendly budget", "cuisine": "italian", "location": "hyderabad"}
    - slot{"budget": "pocket friendly budget"}
    - slot{"cuisine": "italian"}
    - slot{"location": "hyderabad"}
    - utter_slot_values
* deny
* deny
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm{"affirm": "Yop"}
    - utter_ask_emailtosend
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_restart

## interactive_story_3
* telling_cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_location
* telling_location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_anythingelse
* deny
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_4
* restaurant_search
    - utter_ask_location
* telling_location{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "kanpur"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_budget{"budget": "pocket friendly budget", "cuisine": "italian"}
    - slot{"budget": "pocket friendly budget"}
    - slot{"cuisine": "italian"}
    - utter_slot_values
* deny
    - utter_ask_location
* telling_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "delhi"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_budget{"budget": "moderate budget", "cuisine": "italian"}
    - slot{"budget": "moderate budget"}
    - slot{"cuisine": "italian"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_restart

## happy scenario
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "more than 700"}
    - slot{"budget": "more than 700"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "Hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "bangalore"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "bangalore"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* telling_email{"email": "indlasunil.ai@gmail.com"}
    - slot{"email": "indlasunil.ai@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* telling_location_cuisine{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
* telling_location{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "Prayagraj"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
* goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "amaravati"}
    - slot{"location": "amaravati"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
* telling_location{"location": "Tirupati"}
    - slot{"location": "Tirupati"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
* telling_location{"location": "Visakhapatnam"}
    - slot{"location": "Visakhapatnam"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "Visakhapatnam"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_anythingelse
* telling_location
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* telling_location_cuisine{"cuisine": "chinese", "location": "agra"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "agra"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "agra"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine

## interactive_story_2
* greet
    - utter_greet
* telling_location_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_location
    - action_affirm_location

## interactive_story_3
* greet
    - utter_greet
* telling_location_cuisine{"cuisine": "chinese", "location": "agra"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "agra"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "agra"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* telling_budget{"budget": "pocket friendly budget"}
    - slot{"budget": "pocket friendly budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* telling_cuisine{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_ask_location
* telling_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "delhi"}
    - slot{"location_match": "one"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "indlasunil.ai@gmail.com"}
    - slot{"email": "indlasunil.ai@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* telling_location{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "delhi"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "indlasuni.ai@gmail.com"}
    - slot{"email": "indlasuni.ai@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart

## interactive_story_User greeted and then only denying
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_both cuisine and location
* greet
    - utter_greet
* telling_location_cuisine{"cuisine": "italian", "location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"location": "hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "indlasunil.ai@gmail.com"}
    - slot{"email": "indlasunil.ai@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "kochi"}
    - slot{"location": "kochi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "kochi"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget", "location": "cost"}
    - slot{"budget": "moderate budget"}
    - slot{"location": "cost"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "zero"}
* telling_cuisine{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_slot_values
* deny
* telling_cuisine{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* telling_location{"location": "kochi"}
    - slot{"location": "kochi"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "kochi"}
    - slot{"location_match": "one"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_restart

## interactive_story_2
* telling_location_cuisine{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "south indian", "budget": "high budget"}
    - slot{"budget": "high budget"}
    - slot{"cuisine": "south indian"}
    - utter_slot_values
* deny
    - utter_ask_location
* telling_location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* affirm
    - utter_ask_emailaddress
* affirm
    - utter_ask_emailaddress
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* telling_location{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "jaipur"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_budget{"budget": "pocket friendly budget", "cuisine": "south indian"}
    - slot{"budget": "pocket friendly budget"}
    - slot{"cuisine": "south indian"}
    - utter_slot_values
* deny
    - utter_ask_location
* telling_location{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "jaipur"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "zero"}
    - utter_anythingelse
* deny
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_restart

## interactive_story_4
* telling_location_cuisine{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "kolkata"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "pocket friendly budget"}
    - slot{"budget": "pocket friendly budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "zero"}
    - utter_anythingelse
* telling_location_cuisine{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "kolkata"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "pocket friendly budget"}
    - slot{"budget": "pocket friendly budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm{"affirm": "yop"}
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "saiyana763@gmail.com"}
    - slot{"email": "saiyana763@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_restart

## interactive_story_5
* telling_location_cuisine{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "chandigarh"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* telling_budget{"budget": "pocket friendly budget"}
    - slot{"budget": "pocket friendly budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_restart

## interactive_story_6
* restaurant_search
    - utter_ask_location
* telling_location{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
* telling_location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "mumbai"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "pocket friendly budget"}
    - slot{"budget": "pocket friendly budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "zero"}
    - utter_anythingelse
* deny
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_affirm_cuisine
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_did_that_help
* affirm
    - utter_ask_emailtosend
* deny
    - utter_email_nosent
    - utter_goodbye
    - action_restart

## interactive_story_user want to change the details entered details
* greet
    - utter_greet
* telling_location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* deny
    - utter_ask_location
* telling_location{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "high budget"}
    - slot{"budget": "high budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "indlasunil1994@gmail.com"}
    - slot{"email": "indlasunil1994@gmail.com"}
    - action_send_email
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots


## interactive_story_both telling_location_cuisine without greet
* telling_location_cuisine{"cuisine": "italian", "location": "hyderabad"}
    - slot{"cuisine": "italian"}
    - slot{"location": "hyderabad"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "hyderabad"}
    - slot{"location_match": "one"}
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "indlasunil.ai@gmail.com"}
    - slot{"email": "indlasunil.ai@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart

## interactive_story_loaction does not present
* greet
    - utter_greet
* telling_location{"location": "kadapa"}
    - slot{"location": "kadapa"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": null}
    - slot{"location_match": "zero"}
* telling_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_affirm_location
    - action_affirm_location
    - slot{"location": "bangalore"}
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* telling_cuisine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_affirm_cuisine
    - utter_ask_budget
* telling_budget{"budget": "moderate budget"}
    - slot{"budget": "moderate budget"}
    - utter_slot_values
* affirm
    - utter_searching
    - action_get_restaurants
    - slot{"results_found": "one"}
    - utter_ask_emailtosend
* affirm
    - utter_ask_emailaddress
* telling_email{"email": "indlasuni.ai@gmail.com"}
    - slot{"email": "indlasuni.ai@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_email_sent
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - action_restart

