from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from typing import Any, Dict, List, Text
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from location_check import validate_city
from send_email import send_email
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted
import zomatopy
import json
import pandas as pd

# Zomato user access key
zomato_config={ "user_key":"807668cd0184f776a18b69c9ca12bd71"}

# To store email body
top10_result = ""
top5_result = ""

class ActionAffirmLocation(Action):

    def name(self) -> Text:
        return "action_affirm_location"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        loc = tracker.get_slot('location')
        location_check = validate_city(loc, dispatcher)
        return [SlotSet('location', location_check['location']), SlotSet('location_match', location_check['location_match'])]

class ActionGetRestaurants(Action):

    def name(self) -> Text:
        return "action_get_restaurants"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        global top10_result
        top10_result = ""
        top5_result = ""

        # Getting slot values
        loc = tracker.get_slot('location').lower()
        cuisine = tracker.get_slot('cuisine').lower()
        budget = tracker.get_slot('budget')

        zomato = zomatopy.initialize_app(zomato_config)
        loc_details = zomato.get_location(loc, 1)
        loc_json = json.loads(loc_details)
        lat = loc_json["location_suggestions"][0]["latitude"]
        lon = loc_json["location_suggestions"][0]["longitude"]
        cuisines_dict = {'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85}

        # Fetching restaurants
        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50000)
        d = json.loads(results)
        # Sorting restaurants based on user aggregate rating
        restaurants_data = sorted(d['restaurants'], key = lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse = True)

        # budget classes
        budget_range = {'pocket friendly budget': 1, 'moderate budget': 2, 'high budget': 3}
        budget_display = {1: 'Pocket-Friendly (< Rs.300)', 2: 'Moderate (Rs.300 - 700)', 3: 'Costliest (> Rs.700)'}
        count = 0

        if len(restaurants_data) == 0:
            # Zomato API has returned no restaurants
            dispatcher.utter_message("Sorry, No results found for your criteria. Would you like to search for some other restaurants?")
        else:
            for restaurant in restaurants_data:
                # Fetching details to display to the user
                cost_for_two = restaurant['restaurant']['average_cost_for_two']
                name = restaurant['restaurant']['name']
                address = restaurant['restaurant']['location']['address']
                rating = restaurant['restaurant']['user_rating']['aggregate_rating']

                if count < 10:
                    if budget_range.get(budget) == 1:
                        # Pocket friendly budget range
                        if cost_for_two < 300:
                            # Storing restaurant details
                            top10_result = top10_result + str(count + 1) + ". " + name + " in " + address + " has been rated " + str(rating) + " with an average budget for two people as Rs." + str(cost_for_two) + "/-\n\n"
                            if count < 5:
                                top5_result = top5_result + str(count + 1) + ". " + name + " in " + address + " has been rated " + str(rating) + " with an average budget for two people as Rs." + str(cost_for_two) + "/-\n\n"
                            count = count + 1
                    elif budget_range.get(budget) == 2:
                        # Moderate budget range
                        if (cost_for_two >= 300 and cost_for_two <=700):
                            # Storing restaurant details
                            top10_result = top10_result + str(count + 1) + ". " + name + " in " + address + " has been rated " + str(rating) + " with an average budget for two people as Rs." + str(cost_for_two) + "/-\n\n"
                            if count < 5:
                                top5_result = top5_result + str(count + 1) + ". " + name + " in " + address + " has been rated " + str(rating) + " with an average budget for two people as Rs." + str(cost_for_two) + "/-\n\n"
                            count = count + 1
                    elif budget_range.get(budget) == 3:
                        # High budget range
                        if cost_for_two > 700:
                            # Storing restaurant details
                            top10_result = top10_result + str(count + 1) + ". " + name + " in " + address + " has been rated " + str(rating) + " with an average budget for two people as Rs." + str(cost_for_two) + "/-\n\n"
                            if count < 5:
                                top5_result = top5_result + str(count + 1) + ". " + name + " in " + address + " has been rated " + str(rating) + " with an average budget for two people as Rs." + str(cost_for_two) + "/-\n\n"
                            count = count + 1
                    else:
                        # Budget range doesnt match
                        dispatcher.utter_message("Sorry, No results found for your criteria. Would you like to search for some other restaurants?")
                else:
                    # Break when we got 10 restaurants at max
                    break

        # Displaying results
        if len(top5_result) > 0:
            if count < 5:
                top5_result = "These are the top " + str(count) + " restaurants based on your preferences: \n\n" + top5_result
            else:
                top5_result = "These are the top 5 restaurants based on your preferences: \n\n" + top5_result
            dispatcher.utter_message(top5_result)
        else:
            top5_result = "Sorry, No results found for your criteria. Would you like to search for some other restaurants?"
            dispatcher.utter_message(top5_result)

        # Storing data for email body
        if len(top10_result) > 0:
            if count < 10:
                top10_result = "These are the top " + str(count) + " restaurants based on your preferences: \n\n - Location: " + loc + "\n - Cuisine: " + cuisine + "\n - Average Budget for Two people: " + str(budget_display.get(budget_range.get(budget))) + "\n\n" + top10_result
            else:
                top10_result = "These are the top 10 restaurants based on your preferences: \n\n - Location: " + loc + "\n - Cuisine: " + cuisine + "\n - Average Budget for Two people: " + str(budget_display.get(budget_range.get(budget))) + "\n\n" + top10_result
            return [SlotSet('results_found', "one")]
        else:
            return [SlotSet('results_found', "zero")]

# Sending Email
class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        send_email(top10_result, tracker, dispatcher)
        return [AllSlotsReset()]

# Restart after end
class ActionRestart(Action):

    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        return[Restarted()]

# Clear slot values if needed
class ActionSlotReset(Action):

    def name(self) -> Text:
        return "action_slot_reset"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        return[AllSlotsReset()]