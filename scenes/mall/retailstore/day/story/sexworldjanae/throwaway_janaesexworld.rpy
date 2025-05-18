## Janae Sexworld ##
label lbl_mall_daysexworld_janae:
    if sexaroundtownretailstore == 0:
        jump lbl_mall_daysexworld_janae_0
    else:
        jump lbl_mall_daysexworld_janae_1

label lbl_mall_daysexworld_janae_0:
    show pov embarrassed_talk at left
    with dissolve
    show jan neutral at right
    if store_counter == 1:
        show counter retailstore at right
    with dissolve


    pov "Hey."
    show pov embarrassed at left
    show jan neutral_talk at right
    jan "Hi, how can I help you today?"
    show pov embarrassed_talk at left
    show jan neutral at right
    pov "W-what's going on here?"
    show pov sad at left
    show jan neutral_talk at right
    jan "Oh, we're having a clearance sale, which would probably explain why today's so busy."
    show pov embarrassed_talk at left
    show jan confused at right
    pov "T-that isn't what I mean..."
    show pov embarrassed at left
    show jan confused_talk at right
    jan "What do you mean?"
    show pov embarrassed_talk at left
    show jan confused at right
    pov "The uh... why's everyone just... having sex out in the open?"
    show pov sad at left
    show jan confused_talk at right
    jan "Is... there a problem with other customers?"
    show pov sad_talk at left
    show jan confused at right
    pov "It's really freaking me out. Are you sure this place is for real?"
    show pov embarrassed at left
    show jan confused_talk at right
    jan "As long as you don't make a mess on the items; food, drinks, and cum are allowed in the store."
    show pov embarrassed_talk at left
    show jan neutral at right
    pov "Cum... right."
    show pov embarrassed at left
    show jan neutral_talk at right
    jan "Yeah, there aren't really bins around to dump your rubbish as we opt for a smell-free area."
    show pov shocked at left
    show jan neutral_talk at right
    jan "But you're free to dump your cum inside someone if you please."
    show pov shocked_talk at left
    show jan neutral at right
    pov "Uh.. huh..."
    show pov embarrassed at left
    show jan neutral_talk at right
    jan "Is there anything else that I can help you with? Are you looking for something?"
    show pov embarrassed_talk at left
    show jan confused at right
    pov "...Nope... Just answers."
    show pov embarrassed at left
    show jan smirk_talk at right
    jan "Alright then? Have a good day."
    $ sexaroundtownretailstore = 1

    jump lbl_retailstore_day_setup

label lbl_mall_daysexworld_janae_1:
    show pov embarrassed_talk at left
    with dissolve
    show jan neutral at right
    if store_counter == 1:
        show counter retailstore at right
    with dissolve

    pov "Hey."
    show pov embarrassed at left
    show jan neutral_talk at right
    jan "Hey, again. Are you looking for something?"
    show pov embarrassed_talk at left
    show jan embarrassed at right
    pov "Yeah... my sanity."
    show pov embarrassed at left
    show jan embarrassed_talk at right
    jan "Well... I don't think we have any of those but we have a special on bathroom odor sprays."
    show jan embarrassed at right
    pov "..."
    show pov embarrassed_talk at left
    show jan neutral at right
    pov "No, thanks."

    jump lbl_retailstore_day_setup
