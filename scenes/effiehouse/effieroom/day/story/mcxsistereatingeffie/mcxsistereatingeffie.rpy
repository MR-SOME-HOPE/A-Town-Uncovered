## MC x Sister Eating Effie
label lbl_mcxsister_eating_effie:
    scene bg mcxsistereatingeffie_1
    with fade

    jump lbl_mcxsister_eating_effie_0

####################
## Eating Effie Reset
label lbl_mcxsister_eating_effie_0:
    scene bg mcxsistereatingeffie_1

    jump lbl_mcxsister_eating_effie_1

####################
## Stage 1
label lbl_mcxsister_eating_effie_1:
    scene img_allawayxeffiexmc_effiebed_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_mcxsister_eating_effie_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mcxsister_eating_effie_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mcxsister_eating_effie_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mcxsister_eating_effie_1

image img_allawayxeffiexmc_effiebed_stage_1:
    "bg mcxsistereatingeffie_1"
    pause 0.2
    "bg mcxsistereatingeffie_2"
    pause 0.2
    "bg mcxsistereatingeffie_3"
    pause 0.2
    "bg mcxsistereatingeffie_4"
    pause 0.2
    "bg mcxsistereatingeffie_2"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_mcxsister_eating_effie_2:
    scene img_allawayxeffiexmc_effiebed_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_mcxsister_eating_effie_menu
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mcxsister_eating_effie_3
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mcxsister_eating_effie_2

image img_allawayxeffiexmc_effiebed_stage_2:
    "bg mcxsistereatingeffie_1"
    pause 0.1
    "bg mcxsistereatingeffie_2"
    pause 0.2
    "bg mcxsistereatingeffie_4"
    pause 0.2
    "bg mcxsistereatingeffie_2"
    pause 0.1
    repeat

####################
## Stage 3
label lbl_mcxsister_eating_effie_3:
    scene img_allawayxeffiexmc_effiebed_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_mcxsister_eating_effie_menu
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_mcxsister_eating_effie_3

image img_allawayxeffiexmc_effiebed_stage_3:
    "bg mcxsistereatingeffie_1"
    pause 0.2
    "bg mcxsistereatingeffie_4"
    pause 0.2
    "bg mcxsistereatingeffie_2"
    pause 0.2
    repeat

####################
## Missionary Cum
label lbl_mcxsister_eating_effie_menu:
    call screen scr_mcxsister_eating_effie_menu

screen scr_mcxsister_eating_effie_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mcxsister_eating_effie_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mcxsister_eating_effie_cum")

# label lbl_mcxsister_eating_effie_cumchoice:
#     menu:
#         "Cum inside":
#             if hscene_xray == 0:
#                 jump lbl_mcxsister_eating_effie_cumin
#             else:
#                 jump lbl_mcxsister_eating_effie_cumin_0
#         "Cum on them":
#             jump lbl_mcxsister_eating_effie_cumout

####################
## Cum
label lbl_mcxsister_eating_effie_cum:
    scene bg mcxsistereatingeffie_4
    $ renpy.pause(1.5,hard=True)
    show bg mcxsistereatingeffie_5_1
    $ renpy.pause(0.4,hard=True)
    show bg mcxsistereatingeffie_5_2
    $ renpy.pause(0.4,hard=True)
    show bg mcxsistereatingeffie_5_3
    $ renpy.pause(0.4,hard=True)
    show bg mcxsistereatingeffie_5_4
    $ renpy.pause(0.4,hard=True)
    show bg mcxsistereatingeffie_5_5
    $ renpy.pause(0.4,hard=True)
    show bg mcxsistereatingeffie_5_6
    $ renpy.pause(1,hard=True)
    eff "Oh- fuck"
    eff "Oh fuck-"
    eff "Oooh fuuuuuck~"
    eff "Fuck fuck fuck-"
    eff "God- that felt so fucking good-"
    pov "{i}*Slurp slurp*{/i}"
    sis "{i}*Lick lick lick*{/i}"
    pov "{i}*Gulp*{/i}"
    sis "{i}*Sluuuurp*{/i}"
    eff "Oooh- my god.."
    eff "You two are amazing-"
    eff "You are welcome over ANY time."
    eff "Fuck-"
    eff "You're gonna make me squirt again if you keep trying to clean me up-"
    pov "{i}*Lick lick lick*{/i}"
    sis "{i}*Slurp slurp*{/i}"
    eff "Fuuuuuuuck-"

    scene black
    with fade
    $ renpy.pause()
    "After making Effie cum twice more..."
    scene bg effiehouseoutside_day
    with fade

    $ gtime = 1

    jump lbl_effiehouseoutside_day_setup
