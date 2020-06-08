# ## Start conversation
# * greet
#   - utter_greet_name
# * my_name
#   - utter_greet_country_name
# * my_country
#   - utter_greet_name_help
  
## Thank you
* Thank_you
  - utter_thank_you

## back to previous intent
* back_me
  - utter_howto_help

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
  
# ## more information
# * search_hospital
#   - action_hospital_search
# * more_information
#   - action_more_info

## More Information
* more_information
  - action_more_info




  
# ## corona state
# * greet
#   - utter_greet_name
# * my_name
#   - action_name_title_slot
#   - utter_greet_country_name
# * my_country
#   - action_name_slot
#   - utter_greet_name_help
# * corona_status
#   - utter_enter_state
# * corona_state
#   - action_corona_state
# * Thank_you
#   - utter_thank_you
  
 
## corona state
* greet
  - utter_howto_help
* corona_live
  - utter_greet_name
* my_name
  - action_name_title_slot
  - utter_greet_country_name
* my_country
  - action_name_slot
  - utter_greet_name_help
* corona_live
  - utter_enter_state
* corona_state
  - action_corona_state
* Thank_you
  - utter_thank_you


## HOSPITAL CHECK WITH DISEASE
* greet
  - utter_howto_help
* check_symptons
  - utter_check_sympton
  
  
## DOCTOR AVAILABILITY
* greet
  - utter_howto_help
* check_symptons
  - utter_check_sympton
* doctor_available
  - utter_doctor_consult
  - utter_feedback
*mood_great
  - utter_thank_feedback
  
## INSTANCE FINACE BENIFITS
* greet
  - utter_howto_help
* finance_benifits
  - utter_finance_benifit
* registration
  - registration_form
  - form{"name":"registration_form"}
  - form{"name": null}
  - utter_slots_value
  - utter_finalsubmit
* submit
  - utter_submit
## MEDICINE
* greet
  - utter_howto_help
* medicine
  - utter_medicine
## EMERGENCY CARE
* greet
  - utter_howto_help
* emergency_care
  - utter_emergency

## feed back
* feed_back
  - utter_feedback
*mood_great
  - utter_thank_feedback


## Registrations_back path

* registration
  - registration_form
  - form{"name":"registration_form"}
  - form{"name": null}
  - utter_slots_value
  - utter_finalsubmit
* back_me
  - utter_howto_help
* finance_benifits
  - utter_finance_benifit
* registration
  - registration_form
  - form{"name":"registration_form"}
  - form{"name": null}
  - utter_slots_value
  - utter_finalsubmit
# ## test_pm
# * greet
#   - utter_greet_name
# * my_name
#   - action_name_title_slot
#   - utter_greet_country_name
# * my_country
#   - action_name_slot
#   - utter_show_country_pm
#   - utter_greet_name_help
# * corona_status
#   - utter_enter_state
# * corona_state
#   - action_corona_state
# * Thank_you
#   - utter_thank_you