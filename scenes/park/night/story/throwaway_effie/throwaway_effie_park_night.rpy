## Throwaway Effie Park Night Conversation ##
label lbl_park_night_effie:
    show btn_park_night_effie_idle2
## Main Story Conversation
## Side Story Conversation
## No Event
    jump lbl_park_night_effie_convo

label lbl_park_night_effie_convo:
## 1 - 4 is classroom exclusive
## 5 - 8 is cafe exclusive
## 9 - 12 is park exclusive
## 13 - 15 is interchangable
    if date == 7 or date == 11 or date == 26:
        jump lbl_park_night_effie_9
    elif date == 17 or date == 30:
        jump lbl_park_night_effie_10
    elif date == 9 or date == 12 or date == 21:
        jump lbl_park_night_effie_11
    elif date == 1 or date == 18 or date == 22:
        jump lbl_park_night_effie_12
    elif date == 2 or date == 13 or date == 24:
        jump lbl_park_night_effie_9
    elif date == 3 or date == 19 or date == 23:
        jump lbl_park_night_effie_10
    elif date == 6 or date == 14 or date == 25:
        jump lbl_park_night_effie_11
    elif date == 5 or date == 15 or date == 29:
        jump lbl_park_night_effie_12
    elif date == 4 or date == 16 or date == 28:
        jump lbl_town_day_effie_13
    elif date == 10 or date == 27:
        jump lbl_town_day_effie_14
    elif date == 8 or date == 20 or date == 31:
        jump lbl_town_day_effie_15

## Park Exclusive
label lbl_park_night_effie_9:
    show pov neutral_talk at left
    with dissolve
    hide btn_park_night_effie_idle2
    show eff neutral at right
    with dissolve
    pov "Hey, Effie. Nice night."
    show pov neutral at left
    show eff neutral_talk at right
    eff "As it always is in this town."
    show pov smirk_talk at left
    show eff neutral at right
    pov "Whatcha' thinking about?"
    show pov neutral at left
    show eff embarrassed_talk at right
    eff "This and that."
    eff "More thoughts, less talks."
    show pov neutral_talk at left
    show eff embarrassed at right
    pov "I feel you. As you were."

    jump lbl_park_night

label lbl_park_night_effie_10:
    show pov neutral_talk at left
    with dissolve
    hide btn_park_night_effie_idle2
    show eff neutral at right
    with dissolve
    pov "Evening, Effie."
    show pov neutral at left
    show eff neutral_talk at right
    eff "Good ol' evening, [povname]."
    show pov confused_talk at left
    show eff neutral at right
    pov "Aren't you cold? It's a little chilly out here."
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "I like it, I find it calming."
    show pov confused at left
    show eff smirk_talk at right
    eff "Was that a little subtle invitation to cuddle up with me?"
    show pov smirk_talk at left
    show eff smirk at right
    pov "I'm not that much of a flirt, am I?"

    jump lbl_park_night

label lbl_park_night_effie_11:
    show pov neutral at left
    with dissolve
    hide btn_park_night_effie_idle2
    show eff smirk_talk at right
    with dissolve
    eff "Goodnight, [povname]."
    show pov embarrassed_talk at left
    show eff smirk at right
    pov "Good- night... Effie?"
    show pov confused_talk at left
    show eff neutral at right
    pov "... Why is it that 'good-night' acts more like a 'good-bye' than a 'good-day'?"
    show pov confused at left
    show eff smirk_talk at right
    eff "It's because 'good-evening' is the greeting and 'good-night' is the farewell."
    show eff confused_talk at right
    eff "I feel like I've told you this one already..."
    show pov confused_talk at left
    show eff embarrassed at right
    pov "Yeah- honestly, I feel like you have..."

    jump lbl_park_night

label lbl_park_night_effie_12:
    show pov confused at left
    with dissolve
    hide btn_park_night_effie_idle2
    show eff embarrassed_talk at right
    with dissolve
    eff "Hey, [povname]. Rough night?"
    show pov confused_talk at left
    show eff confused at right
    pov "What made you think that?"
    show pov embarrassed at left
    show eff smirk_talk at right
    eff "You're out here at the park- in the middle of the night, alone."
    show pov embarrassed_talk at left
    show eff smirk at right
    pov "I'm with you, aren't I?"
    show pov smirk at left
    show eff smirk_talk at right
    eff "Technically. I guess now we can be alone together."
    show pov neutral_talk at left
    show eff confused at right
    pov "It's a bitter-sweet symphony, that's li-ife."

    jump lbl_park_night
