## The Virus ##
label lbl_the_virus:

    scene bg thevirus_0
    with fade
    pov "{i}Alright, let's see what damage you've done this time.{/i}"
    show bg thevirus_1
    with dissolve
    show bg thevirus_2_1
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_2
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_3
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_4
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_5
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_6
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_7
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_8
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_9
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_10
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_11
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_12
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_13
    $ renpy.pause(0.5,hard=True)
    pov "{i}Jesus, that's a lot of shit on the screen.{/i}"
    pov "{i}What the hell did you download? I told you not to download anything without asking me about it.{/i}"

    jump lbl_the_virus_0

label lbl_the_virus_0:

    scene bg thevirus_2_13
    call screen scr_the_virus_0

screen scr_the_virus_0():
    add "bg thevirus_2_13"
    imagebutton auto "btn thevirus_cross1_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_the_virus_1")
    imagebutton auto "btn thevirus_links1_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_the_virus_links_0")

label lbl_the_virus_links_0:
    pov "{i}I don't think clicking on that is the best way to get rid of them.{/i}"

    jump lbl_the_virus_0

label lbl_the_virus_links_1:
    pov "{i}I REALLY don't think clicking on that is the best way to get rid of them. No matter how tempting.{/i}"

    jump lbl_the_virus_1

label lbl_the_virus_1:

    scene bg thevirus_2_14
    call screen scr_the_virus_1

screen scr_the_virus_1():
    add "bg thevirus_2_14"
    imagebutton auto "btn thevirus_cross2_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_the_virus_2")
    imagebutton auto "btn thevirus_links2_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_the_virus_links_1")

label lbl_the_virus_2:

    scene bg thevirus_2_15
    $ renpy.pause()
    pov "{i}Alright... that is doing the total opposite of what it was supposed to happen.{/i}"
    pov "{i}Let me see if I can download an antivirus scanner.{/i}"
    show bg thevirus_3_1
    $ renpy.pause(1,hard=True)
    show bg thevirus_3_2
    $ renpy.pause(1,hard=True)
    show bg thevirus_3_3
    $ renpy.pause(1,hard=True)
    pov "{i}The hell? The wifi is down?{/i}"
    pov "{i}It's connected on my phone though. This virus must be fucking up with the network connection on here.{/i}"
    if winc == 0:
        pov "{i}Jesus, [missus], you just got this laptop...{/i}"
    else:
        pov "{i}Jesus, Mom, you just got this laptop...{/i}"
    if skill_int >= 4:
        pov "{i}I guess I'll have to do it old-school and buy an antivirus CD from the mall.{/i}"
        $ renpy.notify("New Objective: Buy an Antivirus CD from the mall")
    elif skill_int <= 1:
        pov "{i}Well... if I can't download an antivirus, then I don't know what to do.{/i}"
    $ mum_path = 3

    jump lbl_parentsbedroom_day_setup
