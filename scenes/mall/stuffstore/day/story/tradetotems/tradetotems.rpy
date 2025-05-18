## Grundle Sam Stuff Store Trade Totems ##
label lbl_stuffstore_day_grundlesam_trade:

    menu:
        "$10 - Skill Item 1 (All skills +1)":
            if inventory.has_item(Items.skillitem1):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 10:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem1)
                    $ renpy.notify("New Item Obtained: Totem #1")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "$20 - Skill Item 2 (CHA +2, Other skills +1)":
            if inventory.has_item(Items.skillitem2):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 20:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem2)
                    $ renpy.notify("New Item Obtained: Totem #2")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "$20 - Skill Item 3 (INT +2, Other skills +1)":
            if inventory.has_item(Items.skillitem3):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 20:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem3)
                    $ renpy.notify("New Item Obtained: Totem #3")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "$20 - Skill Item 4 (LUC +2, Other skills +1)":
            if inventory.has_item(Items.skillitem4):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 20:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem4)
                    $ renpy.notify("New Item Obtained: Totem #4")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "$30 - Skill Item 5 (STA/STR +2, Other skills +1)":
            if inventory.has_item(Items.skillitem5):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 20:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem5)
                    $ renpy.notify("New Item Obtained: Totem #5")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "Next Items":
            jump lbl_stuffstore_day_grundlesam_trade_2
        "I don't want to purchase anything.":
            jump lbl_stuffstore_day

label lbl_stuffstore_day_grundlesam_trade_2:

    menu:
        "$50 - Skill Item 6 (All skills +3)":
            if inventory.has_item(Items.skillitem6):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 50:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem6)
                    $ renpy.notify("New Item Obtained: Totem #6")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "$100 - Skill Item 7 (CHA/LUC/STR +5, INT/STA +3)":
            if inventory.has_item(Items.skillitem7):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 100:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem7)
                    $ renpy.notify("New Item Obtained: Totem #7")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "$100 - Skill Item 8 (INT/STA/STR +5, CHA/INT +3)":
            if inventory.has_item(Items.skillitem8):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 100:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem8)
                    $ renpy.notify("New Item Obtained: Totem #8")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "$100 - Skill Item 9 (CHA/INT/STA +5, LUC/STR +3)":
            if inventory.has_item(Items.skillitem9):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 100:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem9)
                    $ renpy.notify("New Item Obtained: Totem #9")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "$200 - Skill Item 10 (All skills +5)":
            if inventory.has_item(Items.skillitem10):
                pov "{i}I already bought that item, I don't need another at the moment.{/i}"
            else:
                if inventory.money >= 200:
                    call lbl_stuffstore_day_tradetotem
                    $ inventory.buy(Items.skillitem10)
                    $ renpy.notify("New Item Obtained: Totem #10")
                else:
                    pov "{i}I don't have enough money for that at the moment.{/i}"

            jump lbl_stuffstore_day
        "Previous Items":
            jump lbl_stuffstore_day_grundlesam_trade
        "I don't want to purchase anything.":
            jump lbl_stuffstore_day

label lbl_stuffstore_day_tradetotem:
    if inventory.has_item(Items.skillitem1) or inventory.has_item(Items.skillitem2) or inventory.has_item(Items.skillitem3) or inventory.has_item(Items.skillitem4) or inventory.has_item(Items.skillitem5):
        $ inventory.drop(Items.skillitem1)
        $ inventory.drop(Items.skillitem2)
        $ inventory.drop(Items.skillitem3)
        $ inventory.drop(Items.skillitem4)
        $ inventory.drop(Items.skillitem5)
    elif inventory.has_item(Items.skillitem6) or inventory.has_item(Items.skillitem7) or inventory.has_item(Items.skillitem8) or inventory.has_item(Items.skillitem9) or inventory.has_item(Items.skillitem10):
        $ inventory.drop(Items.skillitem6)
        $ inventory.drop(Items.skillitem7)
        $ inventory.drop(Items.skillitem8)
        $ inventory.drop(Items.skillitem9)
        $ inventory.drop(Items.skillitem10)
    return
