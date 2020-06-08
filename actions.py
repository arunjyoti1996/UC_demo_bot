# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import re
# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#      def name(self) -> Text:
#          return "action_hello_world"

#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#          dispatcher.utter_message(text="Hello World!")

#          return []



class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_more_info"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         Link="http://ultracures.herokuapp.com/"
         #dispatcher.utter_message(text="You can searh in google or internet")
         dispatcher.utter_template("utter_moreinformation",tracker,link=Link)

         return []


class ActionHospital(Action):

     def name(self) -> Text:
         return "action_hospital_search"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hello wecome to hospital search")

         return []
##THIS IS FOR CORONA STATUS OF INDIA WITH STATE_WISE

class Actioncoronastate(Action):

      def name(self) -> Text:
          return "action_corona_state"

      def run(self, dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          responce=requests.get("https://api.covid19india.org/data.json").json()
          entities=tracker.latest_message["entities"]
          print("Last message Now",entities)
          state=None
          for e in entities:
              if e["entity"] == "state":
                  state =e['value']
          message="please enter Correct state name \nFor Jammu and Kashmir:Jammu kashmir\nFor Dadra and Nagar Haveli and Daman and Diu :Dadra nagar haveli \nFor Andaman and Nicobar Islands : Andaman nicobar"
          
          if state == "india":
              state = "Total"
          elif state == 'jammu kashmir':
              state = "Jammu and Kashmir"
          elif state == 'andaman nicobar':
              state = "Andaman and Nicobar Islands"
          elif state == "dadra nagar haveli":
              state = "Dadra and Nagar Haveli and Daman and Diu"
          else:
              state = state
        
          for data in responce["statewise"]:  
              if data["state"] == state.title():
                  print(data)
                  message = state + " Corona Status Is :" +" Active : " + data["active"] + " Confirmed : " + data["confirmed"] + " Total Death case :" + data["deaths"] + " Total recovered case :" + data["recovered"]
              elif data["state"] == state:
                  print(data)
                  message = state + " Corona Status Is :" + " Active : " + data["active"] + " Confirmed : " + data["confirmed"]  + " Total Death case :" + data["deaths"] + " Total recovered case :" + data["recovered"]
              elif data["state"] == state:
                  print(data)
                  message = state + " Corona Status Is :" + " Active : " + data["active"] + " Confirmed : " + data["confirmed"]  + " Total Death case :" + data["deaths"] + " Total recovered case :" + data["recovered"]
              elif data["state"] == state:
                  print(data)
                  message = state + " Corona Status Is :" + " Active : " + data["active"] + " Confirmed : " + data["confirmed"]  + " Total Death case :" + data["deaths"] + " Total recovered case :" + data["recovered"]
          print(message)
          dispatcher.utter_message(message)
          return []

## Slots set by Actions



class Actionnameslots(Action):

      def name(self) -> Text:
          return "action_name_slot"

      def run(self, dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          name = tracker.get_slot("name")
          name= name.title()
          country = tracker.get_slot("country")
          leader_name=""
          if country.lower()=="us":
              leader_name="Donald Trump"
          elif country.lower()=="india":
              leader_name="Mr Modi"
          else:
              leader_name="Data base is not found"
          message="{} belongs to {} country and leader name is {}".format(name,country,leader_name)
          
          print(message)
             
          

          dispatcher.utter_message(Text= message)

          return [SlotSet("leader",leader_name)]
      
        
## Slots for  name

class Actionname_slots(Action):

      def name(self) -> Text:
          return "action_name_title_slot"

      def run(self, dispatcher: CollectingDispatcher,
              tracker: Tracker,
              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
          name = tracker.get_slot("name")
          name= name.title()
          
          message="my name is {}".format(name)
          
          print(message)
             
          

          dispatcher.utter_message()

          return [SlotSet("name_title",name)]      

# This Action File is for regestration Form
#Here we are taking name,number,email id for Complete Registration

class ActionForForm(FormAction):

    def name(self) -> Text:
        return "registration_form"
    
    @staticmethod
    def required_slots(tracker:Tracker)-> List[Text]:
        print("required_slots(tracker:Tracker)")
        return ["name","number","email"]
    def validate_number(self, value: Text, dispatcher : CollectingDispatcher,
            tracker:Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        if len(value) == 10:
            return{"number":value}
        else:
            
            dispatcher.utter_message(template="utter_wrong_number")
            
            return{"number":None}


    def validate_email(self, value: Text, dispatcher : CollectingDispatcher,
            tracker:Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        
        match = re.search(r'[\w.-]+@[\w.-]+.\w+',value)

        if match: 
            return{"email":value}
        else: 
            dispatcher.utter_message(template="utter_wrong_email")
            
            return{"email":None}
       

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message(template="utter_recheck")

        return []
