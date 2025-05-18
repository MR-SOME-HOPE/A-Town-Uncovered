## Throwaway Effie's Dad Effie's House Outside Night Conversation ##
label lbl_throwaway_effiesdad_effiehouseoutside_night:

## Main Story Conversation
    if effiesdad_path == 0:
        jump lbl_meet_effies_dad

## Side Story Conversation
## No Event
    else:
        jump lbl_effiehouseoutside_night_effiesdad_convo

label lbl_effiehouseoutside_night_effiesdad_convo:
## 1 - 3 is day exclusive
## 4 - 6 is night exclusive
## 7 - 10 is interchangeable
    if date == 2 or date == 13 or date == 27 or date == 31 or date == 17:
        jump lbl_effiehouseoutside_night_effiesdad_4
    elif date == 9 or date == 14 or date == 24 or date == 23 or date == 6:
        jump lbl_effiehouseoutside_night_effiesdad_5
    elif date == 1 or date == 12 or date == 28 or date == 16 or date == 21:
        jump lbl_effiehouseoutside_night_effiesdad_6
    elif date == 10 or date == 11 or date == 26 or date == 5:
        jump lbl_effiehouseoutside_day_effiesdad_7
    elif date == 8 or date == 19 or date == 25 or date == 7:
        jump lbl_effiehouseoutside_day_effiesdad_8
    elif date == 3 or date == 18 or date == 29 or date == 22:
        jump lbl_effiehouseoutside_day_effiesdad_9
    elif date == 4 or date == 15 or date == 30 or date == 20:
        jump lbl_effiehouseoutside_day_effiesdad_10

## Night Exclusive
label lbl_effiehouseoutside_night_effiesdad_4: ##
    show pov neutral_talk at left
    with dissolve
    show effdad bored at right
    with dissolve
    pov "Hello, sir. Is Effie in?"
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "{i}*Sigh*{/i} No, she isn't."
    show pov embarrassed_talk at left
    show effdad bored at right
    pov "Do you know where she may be?"
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "No, I do not."
    show pov embarrassed_talk at left
    show effdad confused at right
    pov "Oh, okay. Thanks, anyways."
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "Whatever."

    jump lbl_effiehouseoutside_night

label lbl_effiehouseoutside_night_effiesdad_5: ##
    show pov neutral_talk at left
    with dissolve
    show effdad bored at right
    with dissolve
    pov "Hello, sir. Is Effie in?"
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "{i}*Sigh*{/i} No, she isn't."
    show pov embarrassed_talk at left
    show effdad bored at right
    pov "Do you know where she may be?"
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "No, I do not."
    show pov embarrassed_talk at left
    show effdad confused at right
    pov "Oh, okay. Thanks, anyways."
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "Whatever."

    jump lbl_effiehouseoutside_night

label lbl_effiehouseoutside_night_effiesdad_6: ##
    show pov neutral_talk at left
    with dissolve
    show effdad bored at right
    with dissolve
    pov "Hello, sir. Is Effie in?"
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "{i}*Sigh*{/i} No, she isn't."
    show pov embarrassed_talk at left
    show effdad bored at right
    pov "Do you know where she may be?"
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "No, I do not."
    show pov embarrassed_talk at left
    show effdad confused at right
    pov "Oh, okay. Thanks, anyways."
    show pov embarrassed at left
    show effdad bored_talk at right
    effdad "Whatever."

    jump lbl_effiehouseoutside_night
