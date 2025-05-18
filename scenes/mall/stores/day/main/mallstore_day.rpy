###############
## Setup
## Story Path
label lbl_mallstores_day_setup:
    jump lbl_mallstores_day

###############
## Room Navigation
## This is the map for mallstores during the day
label lbl_mallstores_day:
    scene bg mallstores_day
    call screen scr_mallstores_day

screen scr_mallstores_day():
    imagebutton auto "btn mallstores_day_mainarea_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_setup")
    #imagebutton auto "btn mallstores_day_bahlsenkoch_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mallstores_bahlsenkoch")
    imagebutton auto "btn mallstores_day_buy050_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mallstores_buy050")
    imagebutton auto "btn mallstores_day_mockingjay_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mallstores_mockingjay")
    imagebutton auto "btn mallstores_day_munchiewunchie_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mallstores_munchiewunchie")
    imagebutton auto "btn mallstores_day_stemptation_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mallstores_stemptation")
    imagebutton auto "btn mallstores_day_tequila_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mallstores_tequila")

    imagebutton auto "btn mallstores_day_gacha_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mallstores_gacha")
    use hud_overlay

###############
## Labels
## Stores
################################################################################
## TEQUILA ##
label lbl_mallstores_tequila:
    scene bg mallstores_day
    call screen scr_mallstores_tequila

screen scr_mallstores_tequila():
    add "bg mallstores_tequilamenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_mallstores_tequila"), Jump("lbl_mallstores_day")]

## Items
    imagebutton auto "btn menuitems_redwine_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_tequila_redwine")
    imagebutton auto "btn menuitems_whitewine_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_tequila_whitewine")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Red Wine
    hbox xpos 232 ypos 476 spacing 20:
        text "$100" color "403b36" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # White Wine
    hbox xpos 406 ypos 476 spacing 20:
        text "$100" color "403b36" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Red Wine
label lbl_tequila_redwine:
    if inventory.has_item(Items.fakeid):
        if inventory.money >= 100:
            $ inventory.buy(Items.redwine)
            $ renpy.notify("New Item Obtained: Red Wine")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    else:
        "I'm not allowed to purchase alcohol without a valid ID."

    call screen scr_mallstores_tequila

## Red Wine
label lbl_tequila_whitewine:
    if inventory.has_item(Items.fakeid):
        if inventory.money >= 100:
            $ inventory.buy(Items.whitewine)
            $ renpy.notify("New Item Obtained: White Wine")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    else:
        "I'm not allowed to purchase alcohol without a valid ID."

    call screen scr_mallstores_tequila

################################################################################
## MOCKINGJAY ##
label lbl_mallstores_mockingjay:
    scene bg mallstores_day
    call screen scr_mallstores_mockingjay

screen scr_mallstores_mockingjay():
    add "bg mallstores_mockingjaymenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_mallstores_mockingjay"), Jump("lbl_mallstores_day")]

## Items
    imagebutton auto "btn menuitems_kidsbible_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_mockingjay_kidsbible")
    imagebutton auto "btn menuitems_bible_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_mockingjay_bible")
    imagebutton auto "btn menuitems_drawinganatomy_%s" xpos 531 ypos 312 focus_mask True action Jump("lbl_mockingjay_drawinganatomy")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Kids' Bible
    hbox xpos 238 ypos 476 spacing 20:
        text "$60" color "403b36" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Bible
    hbox xpos 412 ypos 476 spacing 20:
        text "$90" color "403b36" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Drawing Anatomy
    hbox xpos 586 ypos 476 spacing 20:
        text "$150" color "403b36" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Kids' Bible
label lbl_mockingjay_kidsbible:
    if inventory.money >= 60:
        $ inventory.buy(Items.kidsbible)
        $ renpy.notify("New Item Obtained: Kids' Bible")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_mockingjay

## Bible
label lbl_mockingjay_bible:
    if inventory.money >= 90:
        $ inventory.buy(Items.bible)
        $ renpy.notify("New Item Obtained: Bible")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_mockingjay
## Drawing Anatomy
label lbl_mockingjay_drawinganatomy:
    if inventory.money >= 150:
        $ inventory.buy(Items.drawinganatomy)
        $ renpy.notify("New Item Obtained: Drawing Anatomy")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_mockingjay

################################################################################
## STEMPTATION ##
label lbl_mallstores_stemptation:
    scene bg mallstores_day
    call screen scr_mallstores_stemptation

screen scr_mallstores_stemptation():
    add "bg mallstores_stemptationmenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_mallstores_stemptation"), Jump("lbl_mallstores_day")]

## Items
    imagebutton auto "btn menuitems_essentialoilpeppermint_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_stemptation_essentialoilpeppermint")
    imagebutton auto "btn menuitems_essentialoilcitrus_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_stemptation_essentialoilcitrus")
    imagebutton auto "btn menuitems_essentialoillavender_%s" xpos 531 ypos 312 focus_mask True action Jump("lbl_stemptation_essentialoillavender")
    imagebutton auto "btn menuitems_flowersunflowers_%s" xpos 708 ypos 312 focus_mask True action Jump("lbl_stemptation_flowersunflowers")
    imagebutton auto "btn menuitems_flowerlillies_%s" xpos 885 ypos 312 focus_mask True action Jump("lbl_stemptation_flowerlillies")
    imagebutton auto "btn menuitems_flowerroses_%s" xpos 1062 ypos 312 focus_mask True action Jump("lbl_stemptation_flowerroses")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Essential Oil Peppermint
    hbox xpos 238 ypos 476 spacing 20:
        text "$40" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Essential Oil Citrus
    hbox xpos 412 ypos 476 spacing 20:
        text "$40" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Essential Oil Lavender
    hbox xpos 582 ypos 476 spacing 20:
        text "$40" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Sunflowers
    hbox xpos 759 ypos 476 spacing 20:
        text "$90" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Lillies
    hbox xpos 942 ypos 476 spacing 20:
        text "$90" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Roses
    hbox xpos 1118 ypos 476 spacing 20:
        text "$90" color "66812f" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Essential Oil Peppermint
label lbl_stemptation_essentialoilpeppermint:
    if inventory.money >= 40:
        $ inventory.buy(Items.essentialoilpeppermint)
        $ renpy.notify("New Item Obtained: Peppermint Essential Oil")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_stemptation

## Essential Oil Citrus
label lbl_stemptation_essentialoilcitrus:
    if inventory.money >= 40:
        $ inventory.buy(Items.essentialoilcitrus)
        $ renpy.notify("New Item Obtained: Citrus Essential Oil")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_stemptation

## Essential Oil Lavender
label lbl_stemptation_essentialoillavender:
    if inventory.money >= 40:
        $ inventory.buy(Items.essentialoillavender)
        $ renpy.notify("New Item Obtained: Lavender Essential Oil")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_stemptation

## Sunflowers
label lbl_stemptation_flowersunflowers:
    if inventory.money >= 90:
        $ inventory.buy(Items.flowersunflowers)
        $ renpy.notify("New Item Obtained: Bouquet of Sunflowers")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_stemptation

## Lillies
label lbl_stemptation_flowerlillies:
    if inventory.money >= 90:
        $ inventory.buy(Items.flowerlilies)
        $ renpy.notify("New Item Obtained: Bouquet of Lillies")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_stemptation

## Roses
label lbl_stemptation_flowerroses:
    if inventory.money >= 90:
        $ inventory.buy(Items.flowerroses)
        $ renpy.notify("New Item Obtained: Bouquet of Roses")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_stemptation

################################################################################
## BUY-050 ##
label lbl_mallstores_buy050:
    scene bg mallstores_day
    call screen scr_mallstores_buy050

screen scr_mallstores_buy050():
    add "bg mallstores_buy050menu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_mallstores_buy050"), Jump("lbl_mallstores_day")]

## Items
    imagebutton auto "btn menuitems_hairbands_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_buy050_hairbands")
    imagebutton auto "btn menuitems_sockslightning_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_buy050_sockslightning")
    imagebutton auto "btn menuitems_socksflamingo_%s" xpos 531 ypos 312 focus_mask True action Jump("lbl_buy050_socksflamingo")
    imagebutton auto "btn menuitems_socksclouds_%s" xpos 708 ypos 312 focus_mask True action Jump("lbl_buy050_socksclouds")
    imagebutton auto "btn menuitems_hairdyegreen_%s" xpos 885 ypos 312 focus_mask True action Jump("lbl_buy050_hairdyegreen")
    imagebutton auto "btn menuitems_videogameaction_%s" xpos 1062 ypos 312 focus_mask True action Jump("lbl_buy050_videogameaction")
    imagebutton auto "btn menuitems_videogameshooter_%s" xpos 1239 ypos 312 focus_mask True action Jump("lbl_buy050_videogameshooter")
    imagebutton auto "btn menuitems_videogamedatingsim_%s" xpos 1416 ypos 312 focus_mask True action Jump("lbl_buy050_videogamedatingsim")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Hair Bands
    hbox xpos 238 ypos 476 spacing 20:
        text "$20" color "c560ab" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Socks Lightning
    hbox xpos 412 ypos 476 spacing 20:
        text "$40" color "c560ab" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Socks Flamingo
    hbox xpos 587 ypos 476 spacing 20:
        text "$40" color "c560ab" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Socks Clouds
    hbox xpos 765 ypos 476 spacing 20:
        text "$40" color "c560ab" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Green Hair Dye
    hbox xpos 942 ypos 476 spacing 20:
        text "$65" color "c560ab" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Video Game - Action
    hbox xpos 1112 ypos 476 spacing 20:
        text "$100" color "c560ab" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Video Game - Shooter
    hbox xpos 1292 ypos 476 spacing 20:
        text "$100" color "c560ab" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Video Game - Dating Sim
    hbox xpos 1472 ypos 476 spacing 20:
        text "$100" color "c560ab" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Hair Bands
label lbl_buy050_hairbands:
    if inventory.money >= 20:
        $ inventory.buy(Items.hairbands)
        $ renpy.notify("New Item Obtained: Hairbands")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_buy050

## Lightning Socks
label lbl_buy050_sockslightning:
    if inventory.money >= 40:
        $ inventory.buy(Items.sockslightning)
        $ renpy.notify("New Item Obtained: Fluffy Lightning Socks")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_buy050

## Flamingo Socks
label lbl_buy050_socksflamingo:
    if inventory.money >= 40:
        $ inventory.buy(Items.socksflamingo)
        $ renpy.notify("New Item Obtained: Fluffy Flamingo Socks")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_buy050

## Lightning Socks
label lbl_buy050_socksclouds:
    if inventory.money >= 40:
        $ inventory.buy(Items.socksclouds)
        $ renpy.notify("New Item Obtained: Fluffy Clouds Socks")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_buy050

## Green Hair Dye
label lbl_buy050_hairdyegreen:
    if inventory.money >= 65:
        $ inventory.buy(Items.hairdyegreen)
        $ renpy.notify("New Item Obtained: Green Hair Dye")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_buy050

## Video Game - Action
label lbl_buy050_videogameaction:
    if inventory.money >= 100:
        $ inventory.buy(Items.videogameaction)
        $ renpy.notify("New Item Obtained: Action Video Game")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_buy050

## Video Game - Shooter
label lbl_buy050_videogameshooter:
    if inventory.money >= 100:
        $ inventory.buy(Items.videogameshooter)
        $ renpy.notify("New Item Obtained: Shooter Video Game")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_buy050

## Video Game - Dating Sim
label lbl_buy050_videogamedatingsim:
    if inventory.money >= 100:
        $ inventory.buy(Items.videogamedatingsim)
        $ renpy.notify("New Item Obtained: Dating Sim Video Game")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_buy050

################################################################################
## MUNCHIE WUNCHIE ##
label lbl_mallstores_munchiewunchie:
    scene bg mallstores_day
    call screen scr_mallstores_munchiewunchie

screen scr_mallstores_munchiewunchie():
    add "bg mallstores_munchiewunchiemenu"

## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_mallstores_munchiewunchie"), Jump("lbl_mallstores_day")]

## Items
    imagebutton auto "btn menuitems_pepperostrawberry_%s" xpos 178 ypos 312 focus_mask True action Jump("lbl_munchiewunchie_pepperostrawberry")
    imagebutton auto "btn menuitems_pepperopeanutbutter_%s" xpos 354 ypos 312 focus_mask True action Jump("lbl_munchiewunchie_pepperopeanutbutter")
    imagebutton auto "btn menuitems_pepperochocolate_%s" xpos 531 ypos 312 focus_mask True action Jump("lbl_munchiewunchie_pepperochocolate")
    imagebutton auto "btn menuitems_rainbowlollipop_%s" xpos 708 ypos 312 focus_mask True action Jump("lbl_munchiewunchie_rainbowlollipop")
    imagebutton auto "btn menuitems_premiumchocnutsmix_%s" xpos 885 ypos 312 focus_mask True action Jump("lbl_munchiewunchie_premiumchocnutsmix")
    imagebutton auto "btn menuitems_coffeecapsuleboxset_%s" xpos 1062 ypos 312 focus_mask True action Jump("lbl_munchiewunchie_coffeecapsuleboxset")
    imagebutton auto "btn menuitems_chocolatebox_%s" xpos 1239 ypos 312 focus_mask True action Jump("lbl_munchiewunchie_chocolatebox")

## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Item Price
    # Pepper-o Strawberry
    hbox xpos 238 ypos 476 spacing 20:
        text "$15" color "a04040" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Pepper-o Peanut Butter
    hbox xpos 412 ypos 476 spacing 20:
        text "$15" color "a04040" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Pepper-o Chocolate
    hbox xpos 582 ypos 476 spacing 20:
        text "$15" color "a04040" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Rainbow Lollipop
    hbox xpos 767 ypos 476 spacing 20:
        text "$30" color "a04040" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Premium Choc Nuts Mix
    hbox xpos 942 ypos 476 spacing 20:
        text "$30" color "a04040" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Coffee Capsule Boxset
    hbox xpos 1112 ypos 476 spacing 20:
        text "$100" color "a04040" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Chocolate box
    hbox xpos 1292 ypos 476 spacing 20:
        text "$100" color "a04040" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Buy Items
## Pepper-o Strawberry
label lbl_munchiewunchie_pepperostrawberry:
    if inventory.money >= 15:
        $ inventory.buy(Items.pepperostrawberry)
        $ renpy.notify("New Item Obtained: Strawberry Pepper-o")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_munchiewunchie

## Pepper-o Peanut Butter
label lbl_munchiewunchie_pepperopeanutbutter:
    if inventory.money >= 15:
        $ inventory.buy(Items.pepperopeanutbutter)
        $ renpy.notify("New Item Obtained: Peanut Butter Pepper-o")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_munchiewunchie

## Pepper-o Chocolate
label lbl_munchiewunchie_pepperochocolate:
    if inventory.money >= 15:
        $ inventory.buy(Items.pepperochocolate)
        $ renpy.notify("New Item Obtained: Chocolate Pepper-o")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_munchiewunchie

## Rainbow Lollipop
label lbl_munchiewunchie_rainbowlollipop:
    if inventory.money >= 30:
        $ inventory.buy(Items.rainbowlollipop)
        $ renpy.notify("New Item Obtained: Rainbow Lollipop")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_munchiewunchie

## Premium Choc Nuts Mix
label lbl_munchiewunchie_premiumchocnutsmix:
    if inventory.money >= 30:
        $ inventory.buy(Items.premiumchocnutsmix)
        $ renpy.notify("New Item Obtained: Premium Chocolate & Nuts Mix")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_munchiewunchie

## Coffee Capsule Boxset
label lbl_munchiewunchie_coffeecapsuleboxset:
    if inventory.money >= 100:
        $ inventory.buy(Items.coffeecapsuleboxset)
        $ renpy.notify("New Item Obtained: Coffee Capsule Boxset")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_munchiewunchie

## Chocolate Box
label lbl_munchiewunchie_chocolatebox:
    if inventory.money >= 100:
        $ inventory.buy(Items.chocolatebox)
        $ renpy.notify("New Item Obtained: Chocolate Box")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_munchiewunchie

################################################################################
## BAHLSENKOCH ##
label lbl_mallstores_bahlsenkoch:
    scene bg mallstores_day
    call screen scr_mallstores_bahlsenkoch

screen scr_mallstores_bahlsenkoch():
    add "bg mallstores_bahlsenkochmenu"
    # add "img inconstruction" # Fixed

    ## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_mallstores_bahlsenkoch"), Jump("lbl_mallstores_day")]

    ## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

################################################################################
## GACHA ##
label lbl_mallstores_gacha:
    scene bg mallstores_day
    call screen scr_mallstores_gacha

screen scr_mallstores_gacha():
    add "bg mallstores_gachamenu"

    ## Exit
    imagebutton auto "btn mallstores_exit_%s" xpos 0 ypos 0 focus_mask True action [Hide("scr_mallstores_gacha"), Jump("lbl_mallstores_day")]

    ## Lever
    imagebutton auto "btn mallstores_gachalever_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_gacha_leverpull")

    ## Money
    hbox xpos 250 ypos 157 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Gacha Machine
label lbl_gacha_leverpull:
    if inventory.money >= 10:
        $ gachamachine = renpy.random.randint(1,3)
        if gachamachine == 1:
            $ inventory.buy(Items.gachayellow)
            $ renpy.notify("New Item Obtained: Yellow Gacha Capsule")
        elif gachamachine == 2:
            $ inventory.buy(Items.gachapink)
            $ renpy.notify("New Item Obtained: Pink Gacha Capsule")
        else:
            $ inventory.buy(Items.gachablue)
            $ renpy.notify("New Item Obtained: Blue Gacha Capsule")
    else:
        pov "{i}I don't have enough money for that at the moment.{/i}"

    call screen scr_mallstores_gacha
