import zomatopy
import json

zomato_config={ "user_key":"807668cd0184f776a18b69c9ca12bd71"}

cities = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune', 'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Dindigul', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 'Hamirpur', 'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Karnal', 'Kochi', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Patna', 'Pondicherry', 'Purulia', 'Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Surat', 'Thanjavur', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']

cities = [x.lower() for x in cities]

# Method to check if the location entered by the user is valid or not 
def validate_city(loc, dispatcher, cities = cities):
    if loc.lower() in cities:
        # dispatcher.utter_message(template="utter_affirm_location")
        return {'location': loc, 'location_match': 'one'}
    else:
        try:
            zomato = zomatopy.initialize_app(zomato_config)
            loc_details = zomato.get_location(loc, 1)
            loc_json = json.loads(loc_details)
            loc_results = len(loc_json['location_suggestions'])

            if loc_results == 0:
                # There are no locations with that name
                dispatcher.utter_message(template="utter_locationnotfound")
                return {'location': None, 'location_match': 'zero'}
            else: 
                # Tier 3 city
                dispatcher.utter_message(template="utter_sorry_dontoperate")
                return {'location': None, 'location_match': 'zero'}
        except:
            dispatcher.utter_message(template="utter_locationnotfound")
            return {'location': None, 'location_match': 'zero'}
         