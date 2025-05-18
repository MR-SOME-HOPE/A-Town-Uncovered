## Throwaway Jacob Comic Book Store Day Conversation ##
label lbl_comicbookstore_day_jacob:
    if not (day == 5 and hitomibeach_day == 0 and insexworld == 0):
        show btn_comicbookstore_day_hitomi_idle2
    show btn_comicbookstore_day_jacob_idle2
    $ renpy.pause(0.001)

    ## MAIN STORY
    # if main_story == 165:
    #     jump lbl_the_sexworld_side_effect_setup

## 1 - 5 is morning exclusive
## 6 - 10 is afternoon exclusive
## 11 - 15 is interchangeable
    if date == 1 or date == 19 or date == 27:
        jump lbl_comicbookstore_day_jacob_6
    elif date == 3 or date == 12 or date == 21:
        jump lbl_comicbookstore_day_jacob_7
    elif date == 5 or date == 14 or date == 25:
        jump lbl_comicbookstore_day_jacob_8
    elif date == 7 or date == 11 or date == 23:
        if abouthitomi_magazine >= 1:
            jump lbl_comicbookstore_day_jacob_9
        else:
            jump lbl_comicbookstore_day_jacob_6
    elif (date == 9 or date == 17 or date == 30):
        if abouthitomi_magazine == 1:
            jump lbl_comicbookstore_day_jacob_10
        else:
            jump lbl_town_day_jacob_11
    elif date == 10 or date == 15 or date == 29:
        jump lbl_town_day_jacob_11
    elif date == 8 or date == 13 or date == 22:
        jump lbl_town_day_jacob_12
    elif date == 6 or date == 18 or date == 26:
        jump lbl_town_day_jacob_13
    elif date == 4 or date == 20 or date == 28:
        jump lbl_town_day_jacob_14
    elif date == 2 or date == 16 or date == 24 or date == 0:
        jump lbl_town_day_jacob_15

## Afternoon and Weekend Exclusive
label lbl_comicbookstore_day_jacob_6:
    show pov neutral_talk at left with dissolve
    hide btn_comicbookstore_day_jacob_idle2
    show jac neutral at right
    with dissolve
    pov "Whatcha' have there?"
    show pov confused at left
    show jac neutral_talk at right
    jac "Newest issue of Big Booted Babes."
    show jac smirk_talk at right
    jac "It's a whole magazine full of farmer chicks wearing nothing but boots."
    show jac neutral at right
    pov "..."
    show pov confused_talk at left
    pov "Hmm.. y'know. I like the jugs on that girl but why do they always have buckteeth?"

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_jacob_7:
    show pov neutral_talk at left with dissolve
    hide btn_comicbookstore_day_jacob_idle2
    show jac neutral at right
    with dissolve
    pov "Yo, Jacob. More pornozines?"
    show pov confused at left
    show jac embarrassed_talk at right
    jac "There aren't any new ones today. Just perusing my old favourites."
    show pov confused_talk at left
    show jac confused at right
    pov "So technically, that's a yes?"
    show pov confused at left
    show jac confused_talk at right
    jac "Technically, yes."
    show pov confused_talk at left
    show jac smirk at right
    pov "I worry you're desensitizing yourself to the real thing."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_jacob_8:
    show pov smirk_talk at left with dissolve
    hide btn_comicbookstore_day_jacob_idle2
    show jac smirk at right
    with dissolve
    pov "Hitomi looks cute today, doesn't she?"
    show pov smirk at left
    show jac smirk_talk at right
    jac "She always looks cute, dude."
    show pov confused at left
    show jac embarrassed_talk at right
    jac "The way she looks at me judgementally while I enjoy my pornozines."
    jac "Makes my spine tingle."
    show pov confused_talk at left
    show jac bored at right
    pov "Does your spine tingle when everyone else looks at you like that?"

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_jacob_9:
    show pov shocked at left with dissolve
    hide btn_comicbookstore_day_jacob_idle2
    show jac smirk_talk at right
    with dissolve
    jac "Aye! [povname]. You here to grab the newest issue of 'Fuck Bitches, Pay Weekly'?"
    show pov embarrassed_talk at left
    show jac smirk at right
    pov "One magazine is enough for me right now. I have this thing called..."
    show pov bored_talk at left
    show jac bored at right
    pov "The internet?"
    show pov smirk_talk at left
    pov "Yeah, it's actually a pretty neat little gizmo. I'll walk you through it sometime."
    show pov smirk at left
    show jac bored_talk at right
    jac "You kids and your cellular devices. You don't know what you're missing."

    jump lbl_comicbookstore_day

label lbl_comicbookstore_day_jacob_10:
    show pov neutral at left with dissolve
    hide btn_comicbookstore_day_jacob_idle2
    show jac neutral_talk at right
    with dissolve
    jac "Yo, you here again? Has this place grown on you?"
    show pov neutral_talk at left
    show jac neutral at right
    pov "It has a place in my heart."
    show pov embarrassed_talk at left
    show jac confused at right
    pov "And I like the uh.. company here."
    show pov bored at left
    show jac confused_talk at right
    jac "Really? ... Didn't think you really like Kevin THAT much."
    show pov bored_talk at left
    show jac confused at right
    pov "Uh.. yeah. Him."

    jump lbl_comicbookstore_day
