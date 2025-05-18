###############
## Setup
## Story Path
label lbl_stuffstore_day_setup:
    jump lbl_stuffstore_day

###############
## Room Navigation
## This is the map for mall during the day
label lbl_stuffstore_day:

    scene bg stuffstore_day
    if insexworld == 0:
        show btn stuffstore_day_grundlesam_idle
    else:
        show btn stuffstore_daysexworld_grundlesam_idle
    call screen scr_stuffstore_day

screen scr_stuffstore_day():
    if insexworld == 0:
        imagebutton auto "btn stuffstore_day_grundlesam_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_stuffstore_day_grundlesam")
    else:
        imagebutton auto "btn stuffstore_daysexworld_grundlesam_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_stuffstore_day_grundlesam")
    imagebutton auto "btn stuffstore_day_mall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_setup")
    use hud_overlay

###############
## Labels
label lbl_stuffstore_counter_check:
    if store_counter == 1:
        show counter stuffstore at right
        with dissolve
    else:
        pass
    return

## Stores
################################################################################
## GRUNDLE SAM'S ##
#######################
## WOLF ##
label lbl_stuffstoremenu_wolf:
    scene bg stuffstore_day
    call screen scr_stuffstoremenu_wolf

screen scr_stuffstoremenu_wolf():
    add "bg stuffstoremenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_wolf"), Jump("lbl_stuffstore_day")]

## Totem Category
    add "img stuffstoremenu_wolf"
    imagebutton auto "btn stuffstoremenu_owl_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_wolf"), Show("scr_stuffstoremenu_owl")]
    imagebutton auto "btn stuffstoremenu_elk_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_wolf"), Show("scr_stuffstoremenu_elk")]
    imagebutton auto "btn stuffstoremenu_rabbit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_wolf"), Show("scr_stuffstoremenu_rabbit")]
    imagebutton auto "btn stuffstoremenu_bear_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_wolf"), Show("scr_stuffstoremenu_bear")]

## Items
    imagebutton auto "btn menuskillitems_skillitem7_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem7")
    imagebutton auto "btn menuskillitems_skillitem2_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem2")


## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Skill Item 2
    hbox xpos 238 ypos 476 spacing 20:
        text "$60" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Skill Item 7
    hbox xpos 412 ypos 476 spacing 20:
        text "$320" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Skill Item 2
label lbl_stuffstoremenu_skillitem2:
    if inventory.money >= 60:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem2)
        $ renpy.notify("New Item Obtained: Totem #2")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_wolf

## Skill Item 7
label lbl_stuffstoremenu_skillitem7:
    if inventory.money >= 320:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem7)
        $ renpy.notify("New Item Obtained: Totem #7")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_wolf

#######################
## OWL ##
label lbl_stuffstoremenu_owl:
    scene bg stuffstore_day
    call screen scr_stuffstoremenu_owl

screen scr_stuffstoremenu_owl():
    add "bg stuffstoremenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_owl"), Jump("lbl_stuffstore_day")]

## Totem Category
    add "img stuffstoremenu_owl"
    imagebutton auto "btn stuffstoremenu_wolf_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_owl"), Show("scr_stuffstoremenu_wolf")]
    imagebutton auto "btn stuffstoremenu_elk_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_owl"), Show("scr_stuffstoremenu_elk")]
    imagebutton auto "btn stuffstoremenu_rabbit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_owl"), Show("scr_stuffstoremenu_rabbit")]
    imagebutton auto "btn stuffstoremenu_bear_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_owl"), Show("scr_stuffstoremenu_bear")]

## Items
    imagebutton auto "btn menuskillitems_skillitem8_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem8")
    imagebutton auto "btn menuskillitems_skillitem3_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem3")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Skill Item 3
    hbox xpos 238 ypos 476 spacing 20:
        text "$60" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Skill Item 8
    hbox xpos 412 ypos 476 spacing 20:
        text "$560" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Skill Item 3
label lbl_stuffstoremenu_skillitem3:
    if inventory.money >= 60:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem3)
        $ renpy.notify("New Item Obtained: Totem #3")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_owl

## Skill Item 8
label lbl_stuffstoremenu_skillitem8:
    if inventory.money >= 560:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem8)
        $ renpy.notify("New Item Obtained: Totem #8")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_owl

#######################
## ELK ##
label lbl_stuffstoremenu_elk:
    scene bg stuffstore_day
    call screen scr_stuffstoremenu_elk

screen scr_stuffstoremenu_elk():
    add "bg stuffstoremenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_elk"), Jump("lbl_stuffstore_day")]

## Totem Category
    add "img stuffstoremenu_elk"
    imagebutton auto "btn stuffstoremenu_wolf_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_elk"), Show("scr_stuffstoremenu_wolf")]
    imagebutton auto "btn stuffstoremenu_owl_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_elk"), Show("scr_stuffstoremenu_owl")]
    imagebutton auto "btn stuffstoremenu_rabbit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_elk"), Show("scr_stuffstoremenu_rabbit")]
    imagebutton auto "btn stuffstoremenu_bear_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_elk"), Show("scr_stuffstoremenu_bear")]

## Items
    imagebutton auto "btn menuskillitems_skillitem9_%s" xpos 531 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem9")
    imagebutton auto "btn menuskillitems_skillitem5_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem5")
    imagebutton auto "btn menuskillitems_skillitem1_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem1")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Skill Item 1
    hbox xpos 238 ypos 476 spacing 20:
        text "$50" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Skill Item 5
    hbox xpos 412 ypos 476 spacing 20:
        text "$70" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Skill Item 9
    hbox xpos 582 ypos 476 spacing 20:
        text "$560" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Skill Item 1
label lbl_stuffstoremenu_skillitem1:
    if inventory.money >= 50:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem1)
        $ renpy.notify("New Item Obtained: Totem #1")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_elk

## Skill Item 5
label lbl_stuffstoremenu_skillitem5:
    if inventory.money >= 70:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem5)
        $ renpy.notify("New Item Obtained: Totem #5")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_elk

## Skill Item 9
label lbl_stuffstoremenu_skillitem9:
    if inventory.money >= 560:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem9)
        $ renpy.notify("New Item Obtained: Totem #9")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_elk

#######################
## RABBIT ##
label lbl_stuffstoremenu_rabbit:
    scene bg stuffstore_day
    call screen scr_stuffstoremenu_rabbit

screen scr_stuffstoremenu_rabbit():
    add "bg stuffstoremenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_rabbit"), Jump("lbl_stuffstore_day")]

## Totem Category
    add "img stuffstoremenu_rabbit"
    imagebutton auto "btn stuffstoremenu_wolf_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_rabbit"), Show("scr_stuffstoremenu_wolf")]
    imagebutton auto "btn stuffstoremenu_owl_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_rabbit"), Show("scr_stuffstoremenu_owl")]
    imagebutton auto "btn stuffstoremenu_elk_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_rabbit"), Show("scr_stuffstoremenu_elk")]
    imagebutton auto "btn stuffstoremenu_bear_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_rabbit"), Show("scr_stuffstoremenu_bear")]

## Items
    imagebutton auto "btn menuskillitems_skillitem4_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem4")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Skill Item 4
    hbox xpos 238 ypos 476 spacing 20:
        text "$60" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Skill Item 4
label lbl_stuffstoremenu_skillitem4:
    if inventory.money >= 60:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem4)
        $ renpy.notify("New Item Obtained: Totem #4")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_rabbit

#######################
## BEAR ##
label lbl_stuffstoremenu_bear:
    scene bg stuffstore_day
    call screen scr_stuffstoremenu_bear

screen scr_stuffstoremenu_bear():
    add "bg stuffstoremenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_bear"), Jump("lbl_stuffstore_day")]

## Totem Category
    add "img stuffstoremenu_bear"
    imagebutton auto "btn stuffstoremenu_wolf_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_bear"), Show("scr_stuffstoremenu_wolf")]
    imagebutton auto "btn stuffstoremenu_owl_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_bear"), Show("scr_stuffstoremenu_owl")]
    imagebutton auto "btn stuffstoremenu_elk_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_bear"), Show("scr_stuffstoremenu_elk")]
    imagebutton auto "btn stuffstoremenu_rabbit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_stuffstoremenu_bear"), Show("scr_stuffstoremenu_rabbit")]

## Items
    imagebutton auto "btn menuskillitems_skillitem10_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem10")
    imagebutton auto "btn menuskillitems_skillitem6_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_stuffstoremenu_skillitem6")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Skill Item 6
    hbox xpos 238 ypos 476 spacing 20:
        text "$200" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Skill Item 10
    hbox xpos 412 ypos 476 spacing 20:
        text "$800" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Skill Item 6
label lbl_stuffstoremenu_skillitem6:
    if inventory.money >= 200:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem6)
        $ renpy.notify("New Item Obtained: Totem #6")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_bear

## Skill Item 10
label lbl_stuffstoremenu_skillitem10:
    if inventory.money >= 800:
        call lbl_stuffstore_day_tradetotem
        $ inventory.buy(Items.skillitem10)
        $ renpy.notify("New Item Obtained: Totem #10")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_stuffstoremenu_bear
