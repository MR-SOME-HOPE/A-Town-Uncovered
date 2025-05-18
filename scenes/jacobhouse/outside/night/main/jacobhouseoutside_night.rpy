###############
## Setup
## Story Path
label lbl_jacobhouseoutside_night_setup:

    ## Getting Back Home First Night
    if main_story == 1:
        pov "{i}That is indeed a house, but not mine. From what I remember, my house has a red roof.{/i}"

        jump lbl_townmap_setup

    ## Pre Effie Reveal Who's House
    elif main_story <= 11:
        scene bg jacobhouseoutside_night
        pov "I don't know who lives here, I should go."

        jump lbl_townmap_setup

    ## No Event
    else:
        jump lbl_jacobhouseoutside_night

###############
## Room Navigation
## This is the map for jacob house outside during the night
label lbl_jacobhouseoutside_night:

    scene bg jacobhouseoutside_night
    call screen scr_jacobhouseoutside_night

screen scr_jacobhouseoutside_night():
    imagebutton auto "btn jacobhouseoutside_night_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_jacobhouseoutside_night_door")
    use hud_overlay

###############
## Labels
## Locations
label lbl_jacobhouseoutside_night_door:

## Lailah is available Mon, Tue, Wed, Thur Night and Afternoon, and Sun Night

    ## Lailah
    if gtime == 2:
        pov "{i}I shouldn't knock on his door at this hour.{/i}"
        "Knock anyway?"

        menu:
            "Yes":
                if day <= 4 or day == 6:
                    jump lbl_throwaway_lailah_jacobhouseoutside_night
                else:
                    "{i}*Knock knock*{/i}"
                    "..."
                    pov "{i}No one's home.{/i}"
            "No":
                pass

        jump lbl_jacobhouseoutside_night
    else:
        pov "{i}I really seriously should not knock on their door at this late-late hour.{/i}"

        jump lbl_jacobhouseoutside_night
