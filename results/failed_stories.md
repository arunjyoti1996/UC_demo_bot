## happy path 1 (C:\Users\ARUNAJ~1\AppData\Local\Temp\tmp5kljg83r\dfe5414f0e0741adbe99282b27ccf4cf_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: utter_howto_help -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_check_sympton -->


## happy path 2 (C:\Users\ARUNAJ~1\AppData\Local\Temp\tmp5kljg83r\dfe5414f0e0741adbe99282b27ccf4cf_conversation_tests.md)
* greet: hello there!
    - utter_greet   <!-- predicted: utter_howto_help -->
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_check_sympton -->
* goodbye: bye-bye!
    - utter_goodbye


## sad path 1 (C:\Users\ARUNAJ~1\AppData\Local\Temp\tmp5kljg83r\dfe5414f0e0741adbe99282b27ccf4cf_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: utter_howto_help -->
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_finance_benifit -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy   <!-- predicted: utter_check_sympton -->


## sad path 2 (C:\Users\ARUNAJ~1\AppData\Local\Temp\tmp5kljg83r\dfe5414f0e0741adbe99282b27ccf4cf_conversation_tests.md)
* greet: hello
    - utter_greet   <!-- predicted: utter_howto_help -->
* mood_unhappy: not good   <!-- predicted: deny: not good -->
    - utter_cheer_up   <!-- predicted: utter_finance_benifit -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye   <!-- predicted: utter_finance_benifit -->


## sad path 3 (C:\Users\ARUNAJ~1\AppData\Local\Temp\tmp5kljg83r\dfe5414f0e0741adbe99282b27ccf4cf_conversation_tests.md)
* greet: hi
    - utter_greet   <!-- predicted: utter_howto_help -->
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: action_name_slot -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye   <!-- predicted: utter_finance_benifit -->


