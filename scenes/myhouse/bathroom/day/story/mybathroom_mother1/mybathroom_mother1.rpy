## My Bathroom Mother 1 ##
label lbl_mybathroom_day_mother1:
    if winc == 0:
        pov "{i}Oh my God.. it's [missus].{/i}"
    else:
        pov "{i}Oh my God.. it's Mom.{/i}"
    pov "{i}What is she doing..?{/i}"
    call screen scr_mybathroom_day_mother1

screen scr_mybathroom_day_mother1():
    add "bg mybathroom_day_mother1_1"
    imagebutton auto "btn mybathroom_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mybathroom_day_mother1_2")
    imagebutton auto "btn mybathroom_day_wall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_myhallway_day_setup")

label lbl_mybathroom_day_mother1_2:

    scene bg mybathroom_day_mother1_2
    $ renpy.pause (0.3,hard=True)

    scene bg mybathroom_day_mother1_3
    mum "[povname]?! Is that you? I'm in here!"
    mum "Close the door, I'm almost done."
    if mum_path >= 23:
        menu:
            "Sorry":
                pass
            "Mind if I join you?":
                pov "Mind if I join you? I could use a shower."
                mum "Oh- alright-"
                if winc == 0:
                    pass
                else:
                    mum "My baby."
                mum "Let's be quick, okay?"
                mum "I don't want a huge water bill this month."

                jump lbl_mom_shower_standing_legup
    else:
        pass
    if winc == 0:
        pov "Sorry, [missus]. Take your time."
    else:
        pov "Sorry, Mom. Take your time."

    jump lbl_myhallway_day_setup
