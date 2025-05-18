## Foridiots.com - Learn New Skills (Parody of For Dummies) ##
default know_lockpick = 0

label lbl_mybedroompc_foridiots:
    call screen scr_mybedroompc_foridiots

screen scr_mybedroompc_foridiots():
    add "img mybedroompc_foridiots" align (0.5,0.407)
    imagebutton auto "btn mybedroompc_foridiots_virus_%s" xpos 285 ypos 192 focus_mask True action Jump("lbl_foridiots_virus")
    imagebutton auto "btn mybedroompc_foridiots_lockpick_%s" xpos 574 ypos 192 focus_mask True action Jump("lbl_foridiots_lockpick")
    imagebutton auto "btn mybedroompc_foridiots_model_%s" xpos 863 ypos 192 focus_mask True action Jump("lbl_foridiots_model")
    imagebutton auto "btn mybedroompc_windowclose_%s" xpos 1784 ypos 89 focus_mask True action Jump("lbl_mybedroom_desk_1")

label lbl_foridiots_virus:
    if mum_path == 3:
        if skill_int >= 3:
            if gtime <= 1:
                scene bg researchpc_1
                with fade
                $ renpy.pause()
            else:
                scene bg researchpc_2
                with fade
                $ renpy.pause()
            $ skill_int -= 3
            $ renpy.notify("You used 3 Intelligence Points\nYou've learnt how to fix a buggy computer.")
            if inventory.has_item(Items.antiviruscd):
                pov "{i}I have the CD, now I know what to do to install it safely and properly.{/i}"
            else:
                pov "{i}I just need to grab myself an Anti-virus Disk since I can't even download one from her laptop.{/i}"
            $ mum_path = 3.5
        else:
            $ renpy.notify("You Need 3 Intelligence Points")
            # "Developer Note: I have continuously getting reports that this does not work even if you have 3 INT points."
            # "Developer Note: I have tested this every single time it's reported and it's always worked fine."
            # "Developer Note: Do not mistake the gray bars in your Skill Bar as points, the Points are the coloured bars."
            # "Developer Note: If you need to get more INT points, visit Grundle Sam at the mall and obtain a totem to passively earn points as you sleep."
            # "Developer Note: If doing this still does not work, please provide me with a video or screen shots so I can actually see it break."

        jump lbl_mybedroom_desk_1
    else:
        pov "{i}My computer is fine as it is. I could use my time for better things.{/i}"
        pov "{i}Like porn.{/i}"

        jump lbl_mybedroompc_foridiots

    jump lbl_mybedroompc_foridiots

label lbl_foridiots_lockpick:
    if know_lockpick == 0:
        if skill_int >= 6:
            if gtime <= 1:
                scene bg researchpc_1
                with fade
                $ renpy.pause()
            else:
                scene bg researchpc_2
                with fade
                $ renpy.pause()
            $ skill_int -= 6
            $ renpy.notify("You used 6 Intelligence Points\nYou've learnt how to pick a locked door.")
            $ know_lockpick = 1
            ## SISTER
            if sister_path == 7.5:
                $ sister_path = 8.5
        else:
            $ renpy.notify("You Need 6 Intelligence Points")

            jump lbl_mybedroom_desk_1
    else:
        pov "{i}Could be useful if I decide to go rogue.{/i}"
        ## SISTER
        if sister_path == 7.5:
            $ sister_path = 8.5

        jump lbl_mybedroompc_foridiots

label lbl_foridiots_model:
    default model_level = 0
    default strength_used = 0
    if hitomi_path == 4.5:# and model_level == 0:
        #if skill_str >= 5:
        if gtime <= 1:
            scene bg researchpc_1
            with fade
            $ renpy.pause()
        else:
            scene bg researchpc_2
            with fade
            $ renpy.pause()
        #$ model_level += 1
        #if skill_str >= 10:
        #    $ model_level += 1
        #if skill_str >= 15:
        #    $ model_level += 1
        #$ strength_used = model_level * 5
        #$ skill_str -= strength_used
        #$ renpy.notify("You used [strength_used] Strength Points\nYou've learnt how to model.")
        $ renpy.notify("You've learnt how to model.")
        $ hitomi_path = 5
        $ model_level = 1
        #else:
        #    $ renpy.notify("You Need 5 Strength Points")

        jump lbl_mybedroom_desk_1
    elif model_level > 0:
        #if model_level == 3:
        pov "{i}I've learned all I can here.{/i}"
        #else:
        #    pov "{i}I've learned all I can here for now.{/i}"

        jump lbl_mybedroompc_foridiots
    else:
        pov "{i}Become a model? Nah.{/i}"

        jump lbl_mybedroompc_foridiots
