###############
## Setup
## Story Path
label lbl_jacobhouseoutside_day_setup:
    ## Pre Effie Reveal Who's House
    if main_story <= 19:
        scene bg jacobhouseoutside_day
        pov "{i}I don't know who lives there yet.{/i}"
        jump lbl_townmap_setup
    ## First Morning in the Sex World
    elif main_story <= 32 and insexworld == 1:
        pov "{i}I should get to university. No fooling around today.{/i}"
        jump lbl_townmap_setup
    ## No Event
    else:
        jump lbl_jacobhouseoutside_day

###############
## Room Navigation
## This is the map for jacob house outside during the day
label lbl_jacobhouseoutside_day:
    scene bg jacobhouseoutside_day
    call screen scr_jacobhouseoutside_day

screen scr_jacobhouseoutside_day():
    imagebutton auto "btn jacobhouseoutside_day_door_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_jacobhouseoutside_day_door")

    use hud_overlay

###############
## Labels
## Locations
label lbl_jacobhouseoutside_day_door:
    ## Jacob's Dad is available every Morning and Weekend Afternoons
    ## Lailah is available Mon, Tue, Wed, Thur Night and Afternoon, and Sun Night

    ## Jacob's Dad
    if gtime == 0 or (day >= 5 and gtime == 1):
        if day <= 4 and gtime == 0:
            pov "{i}Jacob's at uni. I shouldn't knock on his door for no reason.{/i}"
        elif gtime == 1 or (gtime == 0 and day >= 5):
            pov "{i}Jacob's probably hanging out at the comic book store.{/i}"
        "Knock anyway?"
        menu:
            "Yes":
                if jacobsdad_path == 0:
                    jump lbl_meet_jacobs_dad
                else:
                    jump lbl_throwaway_jacobsdad_jacobhouseoutside_day
            "No":
                pass
        jump lbl_jacobhouseoutside_day

    ## Lailah
    elif gtime == 1 and day <= 4:
        if day <= 4 and gtime == 0:
            pov "{i}Jacob's at uni. I shouldn't knock on his door for no reason.{/i}"
        elif gtime == 1 or (gtime == 0 and day >= 5):
            pov "{i}Jacob's probably hanging out at the comic book store.{/i}"
        "Knock anyway?"
        menu:
            "Yes":
                if lailah_path == 0:
                    jump lbl_meet_lailah
                else:
                    jump lbl_throwaway_lailah_jacobhouseoutside_day
            "No":
                pass
        jump lbl_jacobhouseoutside_day

    ## No One's Home
    else:
        if day <= 4 and gtime == 0:
            pov "{i}Jacob's at uni. I shouldn't knock on his door for no reason.{/i}"
        elif gtime == 1 or (gtime == 0 and day >= 5):
            pov "{i}Jacob's probably hanging out at the comic book store.{/i}"
        "Knock anyway?"
        menu:
            "Yes":
                "{i}*Knock knock*{/i}"
                "..."
                pov "{i}No one's home.{/i}"
            "No":
                pass
        jump lbl_jacobhouseoutside_day
