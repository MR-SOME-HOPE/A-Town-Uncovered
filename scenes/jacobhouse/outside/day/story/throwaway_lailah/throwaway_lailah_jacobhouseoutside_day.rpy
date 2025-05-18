## Throwaway Lailah Jacob's House Outside Day Conversation ##
default lailah_lydingdoggy = 0

## Main Story Conversation
label lbl_throwaway_lailah_jacobhouseoutside_day:
    ## Side Story Conversation
    if lailah_path == 0:
       jump lbl_jacobhouseoutside_day_lailah_convo

    ## No Event
    else:
        $ lailah_lyingdoggy = renpy.random.randint(1,5)

        if lailah_lyingdoggy == 1:
            jump lbl_lailah_lying_doggy_pre

        else:
            show pov neutral at left
            with dissolve
            show lai smirk_talk at right
            with dissolve

        jump lbl_jacobhouseoutside_day_lailah_convo

label lbl_jacobhouseoutside_day_lailah_convo:
## 1 - 5 is day exclusive
## 6 - 10 is night exclusive
## 11 - 15 is interchangeable
    if date == 10 or date == 18 or date == 21 or date == 31:
        jump lbl_jacobhouseoutside_day_lailah_1
    elif date == 5 or date == 19 or date == 28:
        jump lbl_jacobhouseoutside_day_lailah_2
    elif date == 4 or date == 11 or date == 22:
        jump lbl_jacobhouseoutside_day_lailah_3
    elif date == 3 or date == 12 or date == 29:
        jump lbl_jacobhouseoutside_day_lailah_4
    elif date == 2 or date == 15 or date == 23:
        jump lbl_jacobhouseoutside_day_lailah_5
    elif date == 1 or date == 13 or date == 30:
        jump lbl_jacobhouseoutside_day_lailah_11
    elif date == 8 or date == 14 or date == 24:
        jump lbl_jacobhouseoutside_day_lailah_12
    elif date == 9 or date == 16 or date == 26:
        jump lbl_jacobhouseoutside_day_lailah_13
    elif date == 7 or date == 17 or date == 25:
        jump lbl_jacobhouseoutside_day_lailah_14
    elif date == 6 or date == 20 or date == 27:
        jump lbl_jacobhouseoutside_day_lailah_15

## Day Exclusive
label lbl_jacobhouseoutside_day_lailah_1: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_lailah_2: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_lailah_3: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_lailah_4: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day

label lbl_jacobhouseoutside_day_lailah_5: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day

## Interchangable
label lbl_jacobhouseoutside_day_lailah_11: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day_lailah_end

label lbl_jacobhouseoutside_day_lailah_12: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day_lailah_end

label lbl_jacobhouseoutside_day_lailah_13: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day_lailah_end

label lbl_jacobhouseoutside_day_lailah_14: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day_lailah_end

label lbl_jacobhouseoutside_day_lailah_15: ##
    show pov neutral_talk at left
    show lai neutral at right
    pov "Hello, Lailah."
    show pov neutral at left
    show lai neutral_talk at right
    lai "Hi, [povname]. How are you?"
    show pov neutral_talk at left
    show lai neutral at right
    pov "I'm doing good, thanks."
    show pov smirk_talk at left
    show lai neutral at right
    pov "Is Jacob around?"
    show pov embarrassed at left
    show lai embarrassed_talk at right
    lai "Oh, I'm so sorry, you {i}just{/i} missed him!"
    show pov neutral_talk at left
    show lai neutral at right
    pov "Drats, oh well. Thanks anyways."

    jump lbl_jacobhouseoutside_day_lailah_end

## Redirect End
label lbl_jacobhouseoutside_day_lailah_end:
    if gtime <= 1:
        jump lbl_jacobhouseoutside_day
    else:
        jump lbl_jacobhouseoutside_night
