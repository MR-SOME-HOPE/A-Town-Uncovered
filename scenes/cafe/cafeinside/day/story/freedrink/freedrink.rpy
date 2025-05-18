## Free Drink ##
label lbl_free_drink:
    scene bg cafeinside_day
    with fade
    show pov neutral at left
    with dissolve
    show effw neutral_talk at right
    with dissolve
    if store_counter == 1:
        show counter cafe at right
        with dissolve
    else:
        pass
    eff "Hey, [povname]."
    show pov neutral_talk at left
    show effw neutral at right
    pov "Hey, Effie. How's work so far?"
    show pov neutral at left
    show effw bored_talk at right
    eff "It's so-so. Pretty normal: no strange encounters yet."
    show pov neutral_talk at left
    show effw neutral at right
    pov "That's a shame. An alien invasion or a streaker with a donut around their weiner always makes a day worth living."
    show pov neutral at left
    show effw neutral_talk at right
    eff "Couldn't agree with you more, dude."
    show pov neutral_talk at left
    show effw neutral at right
    pov "Since I'm here, I'll take that free drink if you don't mind."
    if effie_points <= 1:
        show pov embarrassed at left
        show effw angry_talk at right
        eff "I offer a free drink and that's all you're here for? You don't even want to chat?"
        show pov embarrassed_talk at left
        show effw bored at right
        pov "No, no. I didn't mean to-"
        show pov embarrassed at left
        show effw neutral_talk at right
        eff "Hey, [povname], I'm just messing with you. One chocolate milkshake with extra whip cream and chocolate drizzle coming up. Meet me outside."
        show pov neutral_talk at left
        show effw neutral at right
        pov "You're already making my mouth water."
    else:
        show pov neutral at left
        show effw neutral_talk at right
        eff "Sure thing! Wait for me outside while I fix it up for you. How does a chocolate milkshake with extra whip cream and chocolate drizzle sound?"
        show pov neutral_talk at left
        show effw neutral at right
        pov "That sounds so good. I can't wait to try it."

    $ main_story = 10
    $ townmap_enabled = 0
    $ renpy.notify("New Objective: Meet Effie Outside the Cafe")

    jump lbl_cafeinside_day_setup
