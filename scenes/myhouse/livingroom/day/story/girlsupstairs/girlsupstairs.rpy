## Girls Upstairs
label lbl_girls_upstairs:
    #-You arrive home to meet the living room rather quiet, no sign of anyone around-

    scene bg mylivingroom_day
    with fade
    show pov confused at left
    with dissolve
    pov "{i}That’s weird, usually Mom is our watching her dramas or one of her crime shows at this hour.{/i}"
    show pov confused_talk at left
    pov "Hello?"
    pov "I’m home!"
    pov "Anyone in here?"

    #-You suddenly hear some noise up the stairs and the sound of a door opening in the second floor-

    show pov confused at left
    sis "We’re up here, [povname]!"
    sis "Get over here, we are watching some old movies!"
    mum "Hurry up! You're missing the best part!"

    #-The door closes and you are left back in silence-

    show pov neutral_talk at left
    pov "Well, at least there is something to do in the house."

    $ townmap_enabled = 0

    $ main_story = 78

    jump lbl_mylivingroom_day_setup
