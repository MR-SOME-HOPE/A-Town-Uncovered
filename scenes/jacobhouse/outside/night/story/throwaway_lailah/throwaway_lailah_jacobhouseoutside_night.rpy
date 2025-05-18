## Throwaway Lailah Jacob's House Outside Night Conversation ##
label lbl_throwaway_lailah_jacobhouseoutside_night:

## Main Story Conversation
## Side Story Conversation
    #if lailah_path == 0:

    #    jump lbl_jacobhouseoutside_night_lailah_convo
        #jump lbl_meet_lailah ## Activate in 0.24
    #elif lailah_path == 0.5: ## Activate in 0.24
        #jump lbl_meet_lailah_2 ## Activate in 0.24

## No Event
    #else:
    show pov neutral at left
    with dissolve
    show lai smirk_talk at right
    with dissolve
    jump lbl_jacobhouseoutside_night_lailah_convo

label lbl_jacobhouseoutside_night_lailah_convo:
## 1 - 5 is day exclusive
## 6 - 10 is night exclusive
## 11 - 15 is interchangeable
    if date == 8 or date == 20 or date == 21 or date == 31:
        jump lbl_jacobhouseoutside_night_lailah_6
    elif date == 9 or date == 19 or date == 23:
        jump lbl_jacobhouseoutside_night_lailah_7
    elif date == 7 or date == 18 or date == 25:
        jump lbl_jacobhouseoutside_night_lailah_8
    elif date == 10 or date == 17 or date == 30:
        jump lbl_jacobhouseoutside_night_lailah_9
    elif date == 6 or date == 15 or date == 29:
        jump lbl_jacobhouseoutside_night_lailah_10
    elif date == 5 or date == 14 or date == 28:
        jump lbl_jacobhouseoutside_day_lailah_11
    elif date == 4 or date == 13 or date == 27:
        jump lbl_jacobhouseoutside_day_lailah_12
    elif date == 3 or date == 16 or date == 26:
        jump lbl_jacobhouseoutside_day_lailah_13
    elif date == 2 or date == 12 or date == 24:
        jump lbl_jacobhouseoutside_day_lailah_14
    elif date == 1 or date == 11 or date == 22:
        jump lbl_jacobhouseoutside_day_lailah_15

## Night Exclusive
label lbl_jacobhouseoutside_night_lailah_6: ##
    pov "Hello, miss."
    lai "Hi, [povname]. How are you?"
    pov "I'm doing good, thanks."
    pov "Is Jacob around?"
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_night

label lbl_jacobhouseoutside_night_lailah_7: ##
    pov "Hello, miss."
    lai "Hi, [povname]. How are you?"
    pov "I'm doing good, thanks."
    pov "Is Jacob around?"
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_night

label lbl_jacobhouseoutside_night_lailah_8: ##
    pov "Hello, miss."
    lai "Hi, [povname]. How are you?"
    pov "I'm doing good, thanks."
    pov "Is Jacob around?"
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_night

label lbl_jacobhouseoutside_night_lailah_9: ##
    pov "Hello, miss."
    lai "Hi, [povname]. How are you?"
    pov "I'm doing good, thanks."
    pov "Is Jacob around?"
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_night

label lbl_jacobhouseoutside_night_lailah_10: ##
    pov "Hello, miss."
    lai "Hi, [povname]. How are you?"
    pov "I'm doing good, thanks."
    pov "Is Jacob around?"
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_night
