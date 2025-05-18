## Work At IceCreampy ##
label lbl_working_at_icecreampy:
    "How many shifts do you want to work?"

    menu:
        "One shift - Earn $40":
            scene bg job_icecreampy_1
            with fade
            $ renpy.pause()
            $ gtime += 1
            $ inventory.money += 40
            if gtime == 1:
                scene bg mall_day
                with fade
                $ renpy.notify("Current Balance: $[inventory.money]")

                jump lbl_mall_day_setup
            else:
                scene bg townmap_night
                with fade
                stop music fadeout 2.0
                $ renpy.notify("Current Balance: $[inventory.money]")

                jump lbl_townmap_setup
        "Two shifts - Earn $90" if gtime == 0:
            ## Temporary Walk in Fridge Cuddle Fuck for Warmth H-Scene
            if day == 1 or day == 5:
                ala "Hey, [povname]. Can you give me a hand with this tub of icecream?"
                ala "It's kinda heavy, like kinda reaaally heavy."
                menu:
                    "Sure":
                        pov "Sure, be right  with you."
                        ala "I'm just in the walk-in freezer."
                        jump lbl_alanna_cuddle_fuck_pre

                    "Just leave it":
                        pov "Just leave it, I'm really busy out here at the moment."
                        ala "Ugh, fine."
                        pass

            scene bg job_icecreampy_1
            with fade
            $ renpy.pause()
            $ gtime += 2
            $ inventory.money += 90
            scene bg townmap_night
            with fade
            stop music fadeout 2.0
            $ renpy.notify("Current Balance: $[inventory.money]")

            jump lbl_townmap_setup
        "I don't want to work.":
            jump lbl_mall_day_setup
