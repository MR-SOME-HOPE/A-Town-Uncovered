## My Bathroom Sister 1 ##
label lbl_mybathroom_day_sister1:
    pov "{i}Oh my God.. it's [sister].{/i}"
    pov "{i}Her body looks so sexy when wet..{/i}"
    call screen scr_mybathroom_day_sister1

screen scr_mybathroom_day_sister1():
    add "bg mybathroom_day_sister1_1"
    imagebutton auto "btn mybathroom_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybathroom_day_sister1_2")
    imagebutton auto "btn mybathroom_day_wall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_day_setup")

label lbl_mybathroom_day_sister1_2:

    scene bg mybathroom_day_sister1_2
    $ renpy.pause (0.3,hard=True)

    scene bg mybathroom_day_sister1_3
    sis "Hey! Someone's in here!"

    if sister_path >= 36 and sister_points >= 7:
        scene bg mybathroom_day_sister1_6
        sis "Oh- [povname]. What's up?"
        scene bg mybathroom_day_sister1_4
        sis "Wanna join me?"
        sis "Get in here, it'll be an easy clean up."
        menu:
            "Join her":
                jump lbl_sister_shower_standing_doggy
            "Not right now.":
                scene bg mybathroom_day_sister1_5
                pov "Sorry, I'm actually in the middle of something."
                pov "Raincheck?"
                scene bg mybathroom_day_sister1_4
                sis "Rain-? Don't be silly, it's called a shower. Rain is outside."
                scene bg mybathroom_day_sister1_5
                pov "..."
                jump lbl_myhallway_day_setup
    else:
        sis "[povname]! What the fuck, get out of here, I'm showering."
        pov "Sorry, I didn't think anyone was using the bathroom."
        sis "Why are you such a pervert!"

    jump lbl_myhallway_day_setup
