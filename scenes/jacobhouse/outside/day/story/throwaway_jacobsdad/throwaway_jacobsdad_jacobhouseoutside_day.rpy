## Throwaway Jacob's Dad Jacob's House Outside Day Conversation ##
label lbl_throwaway_jacobsdad_jacobhouseoutside_day:

## Main Story Conversation
## Side Story Conversation
    if jacobsdad_path == 0:
        jump lbl_jacobhouseoutside_day_jacobsdad_convo
        #jump lbl_meet_jacobs_dad  ## Activate in 0.24
    #elif jacdad_path == 0.5: ## Activate in 0.24
        #jump lbl_meet_jacobs_dad_2 ## Activate in 0.24

## No Event
    else:
        jump lbl_jacobhouseoutside_day_jacobsdad_convo

label lbl_jacobhouseoutside_day_jacobsdad_convo:

## 1 - 10 is interchangable
    if date == 9 or date == 11 or date == 28 or date == 31:
        jump lbl_jacobhouseoutside_day_jacobsdad_1
    elif date == 1 or date == 12 or date == 30:
        jump lbl_jacobhouseoutside_day_jacobsdad_2
    elif date == 2 or date == 14 or date == 29:
        jump lbl_jacobhouseoutside_day_jacobsdad_3
    elif date == 3 or date == 13 or date == 23:
        jump lbl_jacobhouseoutside_day_jacobsdad_4
    elif date == 4 or date == 16 or date == 22:
        jump lbl_jacobhouseoutside_day_jacobsdad_5
    elif date == 6 or date == 15 or date == 21:
        jump lbl_jacobhouseoutside_day_jacobsdad_6
    elif date == 5 or date == 17 or date == 26:
        jump lbl_jacobhouseoutside_day_jacobsdad_7
    elif date == 7 or date == 18 or date == 25:
        jump lbl_jacobhouseoutside_day_jacobsdad_8
    elif date == 8 or date == 20 or date == 24:
        jump lbl_jacobhouseoutside_day_jacobsdad_9
    elif date == 10 or date == 19 or date == 27:
        jump lbl_jacobhouseoutside_day_jacobsdad_10

## Interchangable
label lbl_jacobhouseoutside_day_jacobsdad_1: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_jacobsdad_2: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_jacobsdad_3: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_jacobsdad_4: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_jacobsdad_5: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_jacobsdad_6: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_jacobsdad_7: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_jacobsdad_8: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_jacobsdad_9: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_jacobsdad_10: ##
    show pov smirk_talk at left
    pov "Hello, sir."
    show jacdad bored at right
    jacdad "Hello, what can I do you for."
    show pov smirk_talk at left
    pov "I'm looking for Jacob?"
    show jacdad neutral_talk at right
    jacdad "Oh! Jacob? He's not here at the moment."
    show pov smirk_talk at left
    pov "That's alright. I'll go look for him."
    show jacdad neutral_talk at right
    jacdad "You have a good day now."

    jump lbl_jacobhouseoutside_day