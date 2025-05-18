###############
## Setup
## Image
image btn_retailstore_section_day_hdcamera_idle2:
    "/scenes/mall/retailstore/day/main/assets/button/btn_retailstore_section_day_hdcamera_idle.png"
image btn_retailstore_section_day_lightingequipment_idle2:
    "/scenes/mall/retailstore/day/main/assets/button/btn_retailstore_section_day_lightingequipment_idle.png"

###############
## Room Navigation
## This is the map for retailstore electronics section
label lbl_retailstore_electronics_day:
    scene bg retailstore_electronics_day
    show btn_retailstore_section_day_antivirus_idle2
    show btn_retailstore_section_day_smarttvbox_idle2
    show btn_retailstore_section_day_vrheadset_idle2
    show btn_retailstore_section_day_hdcamera_idle2
    show btn_retailstore_section_day_lightingequipment_idle2
    show btn_retailstore_section_day_clothing_idle2:
        xpos 1500 ypos 420
    show btn_retailstore_section_day_misc_idle2:
        xpos 1500 ypos 220
    show btn_retailstore_section_day_mall_idle2
    with fade
    call screen scr_retailstore_electronics_day

screen scr_retailstore_electronics_day():
    use hud_overlay

## Exits
    imagebutton auto "btn retailstore_section_day_retailstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_day_setup")
    imagebutton auto "btn retailstore_section_day_mall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_setup")

## Retail Store Navigation
    imagebutton auto "btn retailstore_section_day_misc_%s" xpos 1500 ypos 220 focus_mask True action Jump("lbl_retailstore_misc_day")
    imagebutton auto "btn retailstore_section_day_clothing_%s" xpos 1500 ypos 420 focus_mask True action Jump("lbl_retailstore_clothing_day")

## Items
    imagebutton auto "btn retailstore_section_day_antivirus_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_antivirus")
    imagebutton auto "btn retailstore_section_day_smarttvbox_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_smarttvbox")
    imagebutton auto "btn retailstore_section_day_vrheadset_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_vrheadset")
    imagebutton auto "btn retailstore_section_day_hdcamera_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_hdcamera")
    imagebutton auto "btn retailstore_section_day_lightingequipment_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_lightingequipment")


## Item Price
    # Antivirus
    hbox xpos 752 ypos 252 spacing 20:
        text "$120" color "1e1a1a" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Smart TV Box
    hbox xpos 1034 ypos 377 spacing 20:
        text "$200" color "1e1a1a" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # VR Headset
    hbox xpos 835 ypos 593 spacing 20:
        text "$900" color "1e1a1a" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # HD Camera
    hbox xpos 1038 ypos 499 spacing 20:
        text "$600" color "1e1a1a" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Lighting Equipment
    hbox xpos 812 ypos 807 spacing 20:
        text "$600" color "1e1a1a" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Money
    hbox xpos 200 ypos 843 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Electronics Items
## Antivirus CD ##
label lbl_retailstore_section_day_antivirus:
    if inventory.has_item(Items.antiviruscd) or mum_path >= 4:
        pov "{i}I already bought that item, I don't need another at the moment.{/i}"
    elif mum_path in (3, 3.5):
        if inventory.money >= 120:
            $ inventory.buy(Items.antiviruscd)
            $ renpy.notify("New Item Obtained: Antivirus CD")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    else:
        pov "Why buy overpriced anti-virus software in a package. Everyone has internet these days."
    call screen scr_retailstore_electronics_day

## Smart TV Box ##
label lbl_retailstore_section_day_smarttvbox:
    if inventory.has_item(Items.smarttvbox) or mum_path >= 14:
        pov "{i}I already bought that item, I don't need another at the moment.{/i}"
    else:
        if inventory.money >= 200:
            $ inventory.buy(Items.smarttvbox)
            $ renpy.notify("New Item Obtained: Smart TV Box")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    call screen scr_retailstore_electronics_day

## VR Headset ##
label lbl_retailstore_section_day_vrheadset:

    if edward_vr_path < 2:
        pov "{i}I'm not sure what use I have for that right now.{/i}"
    elif edward_vr_path == 2:
        if inventory.has_item(Items.vrheadset):
            pov "{i}I already bought that item, I don't need another at the moment.{/i}"
        elif inventory.money >= 900:
            $ inventory.buy(Items.vrheadset)
            $ renpy.notify("New Item Obtained: VR Headset")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    elif edward_vr_path > 2:
        pov "{i}It's the same version I have aready, just unmodded. I don't need another.{/i}"
    call screen scr_retailstore_electronics_day

## HD Camera ##
label lbl_retailstore_section_day_hdcamera:
    if inventory.has_item(Items.hdcamera):
        pov "{i}I already bought that item, I don't need another at the moment.{/i}"
    else:
        if inventory.money >= 600:
            $ inventory.buy(Items.hdcamera)
            $ renpy.notify("New Item Obtained: HD Camera")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    call screen scr_retailstore_electronics_day

## Lighting Equipment ##
label lbl_retailstore_section_day_lightingequipment:
    if inventory.has_item(Items.lightingequipment):
        pov "{i}I already bought that item, I don't need another at the moment.{/i}"
    else:
        if inventory.money >= 600:
            $ inventory.buy(Items.lightingequipment)
            $ renpy.notify("New Item Obtained: Lighting Equipment")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    call screen scr_retailstore_electronics_day

###############
## This is the map for retailstore misc section
label lbl_retailstore_misc_day:

    scene bg retailstore_misc_day
    show btn_retailstore_section_day_teddybear1_idle2
    show btn_retailstore_section_day_teddybear2_idle2
    show btn_retailstore_section_day_teddybear3_idle2
    show btn_retailstore_section_day_clothing_idle2:
        xpos 1500 ypos 420
    show btn_retailstore_section_day_electronics_idle2:
        xpos 1500 ypos 220
    show btn_retailstore_section_day_mall_idle2
    with fade
    call screen scr_retailstore_misc_day

screen scr_retailstore_misc_day():
    use hud_overlay

## Exits
    imagebutton auto "btn retailstore_section_day_retailstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_day_setup")
    imagebutton auto "btn retailstore_section_day_mall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_setup")

## Retail Store Navigation
    imagebutton auto "btn retailstore_section_day_electronics_%s" xpos 1500 ypos 220 focus_mask True action Jump("lbl_retailstore_electronics_day")
    imagebutton auto "btn retailstore_section_day_clothing_%s" xpos 1500 ypos 420 focus_mask True action Jump("lbl_retailstore_clothing_day")

## Items
    imagebutton auto "btn retailstore_section_day_teddybear1_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_teddybear1")
    imagebutton auto "btn retailstore_section_day_teddybear2_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_teddybear2")
    imagebutton auto "btn retailstore_section_day_teddybear3_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_teddybear3")

## Item Price
    # Tiny Teddy Bear
    hbox xpos 680 ypos 359 spacing 20:
        text "$40" color "1e1a1a" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Normal Teddy Bear
    hbox xpos 727 ypos 586 spacing 20:
        text "$80" color "1e1a1a" size 40 font "fonts/KGSorryNotSorryChub.ttf"
    # Large Teddy Bear
    hbox xpos 762 ypos 747 spacing 20:
        text "$190" color "1e1a1a" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Money
    hbox xpos 200 ypos 843 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Misc Items
## Tiny Teddy Bear ##
label lbl_retailstore_section_day_teddybear1:
    if inventory.has_item(Items.teddybear1) or mum_path >= 15:
        pov "{i}I already have that item, I don't need another at the moment.{/i}"
    else:
        if inventory.money >= 40:
            $ inventory.buy(Items.teddybear1)
            $ renpy.notify("New Item Obtained: Tiny Teddy Bear")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    call screen scr_retailstore_misc_day

## Normal Teddy Bear ##
label lbl_retailstore_section_day_teddybear2:
    if inventory.has_item(Items.teddybear2) or mum_path >= 15:
        pov "{i}I already bought that item, I don't need another at the moment.{/i}"
    else:
        if inventory.money >= 80:
            $ inventory.buy(Items.teddybear2)
            $ renpy.notify("New Item Obtained: Normal Teddy Bear")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    call screen scr_retailstore_misc_day

## Large Teddy Bear ##
label lbl_retailstore_section_day_teddybear3:
    if inventory.has_item(Items.teddybear3) or mum_path >= 15:
        pov "{i}I already have that item, I don't need another at the moment.{/i}"
    else:
        if inventory.money >= 190:
            $ inventory.buy(Items.teddybear3)
            $ renpy.notify("New Item Obtained: Large Teddy Bear")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    call screen scr_retailstore_misc_day

###############
## This is the map for retailstore clothing section
label lbl_retailstore_clothing_day:

    scene bg retailstore_clothing_day
    show btn_retailstore_section_day_suit_idle2
    show btn_retailstore_section_day_misc_idle2:
        xpos 1500 ypos 420
    show btn_retailstore_section_day_electronics_idle2:
        xpos 1500 ypos 220
    show btn_retailstore_section_day_mall_idle2
    with fade
    call screen scr_retailstore_clothing_day

screen scr_retailstore_clothing_day():
    use hud_overlay

## Exits
    imagebutton auto "btn retailstore_section_day_retailstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_day_setup")
    imagebutton auto "btn retailstore_section_day_mall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_setup")

## Retail Store Navigation
    imagebutton auto "btn retailstore_section_day_electronics_%s" xpos 1500 ypos 220 focus_mask True action Jump("lbl_retailstore_electronics_day")
    imagebutton auto "btn retailstore_section_day_misc_%s" xpos 1500 ypos 420 focus_mask True action Jump("lbl_retailstore_misc_day")

## Items
    imagebutton auto "btn retailstore_section_day_suit_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_suit")

## Item Price
    # Suit
    hbox xpos 765 ypos 330 spacing 20:
        text "$500" color "1e1a1a" size 40 font "fonts/KGSorryNotSorryChub.ttf"

## Money
    hbox xpos 200 ypos 843 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Clothing Items
## Suit ##
label lbl_retailstore_section_day_suit:
    if inventory.has_item(Items.suit) or mum_path >= 27:
        pov "{i}I already have that item, I don't need another at the moment.{/i}"
    else:
        if inventory.money >= 500:
            $ inventory.buy(Items.suit)
            $ renpy.notify("New Item Obtained: Suit")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    call screen scr_retailstore_clothing_day

###############
## This is the map for retailstore gift card rack
label lbl_retailstore_giftcard_day:

    scene bg retailstore_giftcard_day
    show btn_retailstore_section_day_giftcardwebflix_idle2
    show btn_retailstore_section_day_giftcardcamgurl_idle2
    # show btn_retailstore_section_day_misc_idle2:
    #     xpos 1500 ypos 420
    # show btn_retailstore_section_day_electronics_idle2:
    #     xpos 1500 ypos 220
    # show btn_retailstore_section_day_mall_idle2
    # with fade
    call screen scr_retailstore_giftcard_day

screen scr_retailstore_giftcard_day():
    use hud_overlay

## Exits
    imagebutton auto "btn retailstore_section_day_retailstore_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_day_setup")
    imagebutton auto "btn retailstore_section_day_mall_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_mall_day_setup")

## Retail Store Navigation
    # imagebutton auto "btn retailstore_section_day_electronics_%s" xpos 1500 ypos 220 focus_mask True action Jump("lbl_retailstore_electronics_day")
    # imagebutton auto "btn retailstore_section_day_misc_%s" xpos 1500 ypos 420 focus_mask True action Jump("lbl_retailstore_misc_day")

## Items
    imagebutton auto "btn retailstore_section_day_giftcardwebflix_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_giftcardwebflix")
    imagebutton auto "btn retailstore_section_day_giftcardcamgurl_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_retailstore_section_day_giftcardcamgurl")

## Item Price

## Money
    hbox xpos 200 ypos 843 spacing 20:
        text "$[inventory.money]" color "1e1a1a" size 90 font "fonts/KGSorryNotSorryChub.ttf"

## Gift Card Items
## $100 Webflix Giftcard ##
label lbl_retailstore_section_day_giftcardwebflix:
    if inventory.has_item(Items.giftcardwebflix):
        pov "{i}I already have that item, I don't need another at the moment.{/i}"
    else:
        if inventory.money >= 100:
            $ inventory.buy(Items.giftcardwebflix)
            $ renpy.notify("New Item Obtained: $100 Webflix Giftcard")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    call screen scr_retailstore_giftcard_day

## $100 Camgurl Giftcard ##
label lbl_retailstore_section_day_giftcardcamgurl:
    if inventory.has_item(Items.giftcardcamgurl):
        pov "{i}I already have that item, I don't need another at the moment.{/i}"
    else:
        if inventory.money >= 100:
            $ inventory.buy(Items.giftcardcamgurl)
            $ renpy.notify("New Item Obtained: $100 Camgurl Giftcard")
        else:
            pov "{i}I don't have enough money for that at the moment.{/i}"
    call screen scr_retailstore_giftcard_day
