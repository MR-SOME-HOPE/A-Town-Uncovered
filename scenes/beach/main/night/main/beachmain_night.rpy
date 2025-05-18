###############
## Setup
## Story Path
label lbl_beachmain_night_setup:
    if main_story == 1:
        pov "{i}That's the beach, I haven't been there before. I'll visit there sometime. From what I remember, my house has a red roof, that's where I should be heading.{/i}"

        jump lbl_townmap_setup
    elif not insexworld:
        $ randomevent_beachnight = renpy.random.randint(1,100)
        if randomevent_beachnight <= 10:
            scene bg skinnydipping_1
            with fade

            jump lbl_randomevent_beach_skinnydipping_1

    jump lbl_beachmain_night

###############
## Room Navigation
## This is the map for beach main during the night
label lbl_beachmain_night:

    scene bg beachmain_night
    call screen scr_beachmain_night

screen scr_beachmain_night():
    imagebutton auto "btn beachmain_night_rocks_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachbehindrocks_night_setup")
    imagebutton auto "btn beachmain_night_chair_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachmain_night_chair")
    imagebutton auto "btn beachmain_night_blue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachchangeroom_blue_night_setup")
    imagebutton auto "btn beachmain_night_purple_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachchangeroom_purple_night_setup")
    imagebutton auto "btn beachmain_night_green_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachchangeroom_green_night_setup")
    imagebutton auto "btn beachmain_night_red_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_beachchangeroom_red_night_setup")
    use hud_overlay

###############
## Labels
label lbl_beachmain_night_chair:
    pov "{i}Where's the lifeguard?{/i}"
    call screen scr_beachmain_night
