label lbl_beachbehindrocks_day_principallashleysunscreen:

    scene bg beachbehindrocks_day
    show changeroom principallashleysunscreen_1
    $ renpy.pause()
    pov "Miss... Lashley?"
    show changeroom principallashleysunscreen_2
    pri "Hi..."
    show changeroom principallashleysunscreen_3
    pov "What are you doing at a nudist beach? I never would have imagined that you were okay with this..."
    show changeroom principallashleysunscreen_2
    pri "To an extent; That's why I'm hiding behind here away from everyone else."
    show changeroom principallashleysunscreen_4
    pri "Remember, before Eve ate from the Tree of Knowledge, God made man shameless and free."
    show changeroom principallashleysunscreen_5
    pov "I guess if you put it that way..."
    show changeroom principallashleysunscreen_2
    pri "Hey, um... this is out of the blue but..."
    show changeroom principallashleysunscreen_2
    pri "Can you help me apply some sunscreen?"

    menu:
        "Sure.":
            show changeroom principallashleysunscreen_5
            pov "Sure. I'm assuming on your back, right?"
            show changeroom principallashleysunscreen_4
            pri "Somewhere with a little more surface area..."

            jump lbl_beachbehindrocks_day_principallashleysunscreen_2
        "Maybe next time?":
            show changeroom principallashleysunscreen_3
            pov "Actually, I'm a little pre-occupied at the moment. Maybe next time?"
            show changeroom principallashleysunscreen_2
            pri "Oh, sorry to bother you. I'm sure I can manage myself."

            jump lbl_beachmain_day_setup

label lbl_beachbehindrocks_day_principallashleysunscreen_2:

    scene bg beachbehindrocks_principallashleysunscreen_1
    $ count = 0
    $ num = math.ceil(max(skill_sta, 1) * .2) * 2
    while count < num:
        $ count += 1
        show bg beachbehindrocks_principallashleysunscreen_1
        $ renpy.pause(0.4,hard=True)
        show bg beachbehindrocks_principallashleysunscreen_2
        $ renpy.pause(0.4,hard=True)
        show bg beachbehindrocks_principallashleysunscreen_3
        $ renpy.pause(0.4,hard=True)

    jump lbl_beachbehindrocks_day_principallashleysunscreen_3

label lbl_beachbehindrocks_day_principallashleysunscreen_3:
    pri "Thanks. There's just so much... 'chest'... that I tend to miss spots when I do it myself."
    pov "It's no problem at all, Ms. Lashley."
    pri "You're a very mature, well-behaved boy. Thanks for not doing anything sinful."
    pri "People these days are just so blinded by lust. Absolutely disgraceful."

    jump lbl_beachmain_day_setup
