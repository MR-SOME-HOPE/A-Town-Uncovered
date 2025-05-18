label lbl_bath_with_mom_3_revisit:
    show bg bathwithmom_51
    mum "Match my speed, okay, baby?"
    show bg bathwithmom_44
    pov "Alright."
    show bg bathwithmom_51
    mum "I don't want you cumming too prematurely."
    show bg bathwithmom_44
    pov "Pssh, talk for yourself. I can last forever."
    show bg bathwithmom_59_1
    mum "Jus- shhh!"
    $ vrheadset_revisitcounter = 0

    jump lbl_bath_with_mom_3_revisit_1

label lbl_bath_with_mom_3_revisit_1: ## Stage 1 - Slow warm up
    $ vrheadset_revisitcounter += 1
    show bg bathwithmom_43
    $ renpy.pause(0.5,hard=True)
    show bg bathwithmom_44
    $ renpy.pause(0.5,hard=True)

    jump lbl_bath_with_mom_3_revisit_counter

label lbl_bath_with_mom_3_revisit_2: ## Stage 2 - Getting into it
    $ vrheadset_revisitcounter += 1
    show bg bathwithmom_45
    $ renpy.pause(0.4,hard=True)
    show bg bathwithmom_46
    $ renpy.pause(0.4,hard=True)

    jump lbl_bath_with_mom_3_revisit_counter

label lbl_bath_with_mom_3_revisit_3: ## Stage 3 - Almost there
    $ vrheadset_revisitcounter += 1
    show bg bathwithmom_47
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_48
    $ renpy.pause(0.3,hard=True)

    jump lbl_bath_with_mom_3_revisit_counter

label lbl_bath_with_mom_3_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_bath_with_mom_3_revisit_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_bath_with_mom_3_revisit_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_bathwithmom_masturbate_revisit
    else:
        jump lbl_bath_with_mom_3_revisit_1


screen scr_bathwithmom_masturbate_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_bath_with_mom_4_revisit_4")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_bath_with_mom_4_revisit_3")

label lbl_bath_with_mom_4_revisit_1:
    show bg bathwithmom_52_1
    pov "Oh, fuuck...!"
    show bg bathwithmom_52_2
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_3
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_4
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_5
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_6
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_7
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_8
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_9
    $ renpy.pause()
    show bg bathwithmom_53
    mum "Last forever, did you say?"
    show bg bathwithmom_54
    pov "I- was... just so... turned on!"
    show bg bathwithmom_55
    mum "Yeah, nice save there, [povname]."
    show bg bathwithmom_56
    mum "Hehehe, it's alright. I'll finish myself off some other time."
    show bg bathwithmom_57
    pov "I'd be more than happy to just watch you."
    show bg bathwithmom_58
    mum "No, no. It's alright. I'll survive."

    jump lbl_bath_with_mom_5_revisit

label lbl_bath_with_mom_4_revisit_2:
    show bg bathwithmom_59_1
    if winc == 0:
        pov "[missus]... I- I'm gonna cum..."
    else:
        pov "Mom... I- I'm gonna cum..."
    show bg bathwithmom_59_2
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_3
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_4
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_5
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_6
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_7
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_8
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_9
    $ renpy.pause()
    show bg bathwithmom_60
    mum "{i}*pant*{/i} Oh... you... we... were supposed... {i}*gulp*{/i} to cum... together."
    show bg bathwithmom_54
    pov "Sorry... I... fuck... I was just so ready to cum on you."
    show bg bathwithmom_60
    mum "It's... alright... ugh fuck. Edging is making my clit so fucking sensitive..."
    show bg bathwithmom_61
    mum "Sorry... language."
    show bg bathwithmom_57
    pov "Don't you wanna cum?"
    show bg bathwithmom_58
    mum "Hmm? No.. no... it's alright. My body feels so good right now."

    jump lbl_bath_with_mom_5_revisit

label lbl_bath_with_mom_4_revisit_3:
    show bg bathwithmom_62_1
    pov "Fucck!"
    mum "Oh, fuck... baby!"
    show bg bathwithmom_62_2
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_3
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_4
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_5
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_6
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_7
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_8
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_9
    $ renpy.pause()
    show bg bathwithmom_63
    $ renpy.pause(2,hard=True)
    show bg bathwithmom_64
    pov "That felt..."
    show bg bathwithmom_63
    mum "Soo..."
    show bg bathwithmom_64
    pov "Fuc-"
    show bg bathwithmom_63
    mum "Good..."
    show bg bathwithmom_64
    pov "Heh... yeah..."
    jump lbl_bath_with_mom_5_revisit

label lbl_bath_with_mom_4_revisit_4:
    show bg bathwithmom_49
    if winc == 0:
        pov "Fuck... [missus]... stop..."
    else:
        pov "Fuck... Mom... stop..."
    show bg bathwithmom_50
    pov "Slow down..."
    show bg bathwithmom_49
    pov "Don't cum yet."
    show bg bathwithmom_50
    pov "I- I want to keep edging."
    show bg bathwithmom_51
    mum "Y-yeah... Me- me too."
    $ vrheadset_revisitcounter = 0

    jump lbl_bath_with_mom_3_revisit_1

label lbl_bath_with_mom_5_revisit:
    show bg bathwithmom_65
    mum "I love you, [povname]. Thank you for coming in here with me."
    mum "Your company was really all I needed."
    show bg bathwithmom_57
    pov "I'll be there for you when you need it. Remember that."
    pov "Burn it in your brain."
    show bg bathwithmom_66
    mum "Oh, don't you worry about that. I will."
    show bg bathwithmom_57
    mum "..."
    show bg bathwithmom_65
    mum "Hey, [povname]?"
    show bg bathwithmom_67
    pov "Mhmm?"
    show bg bathwithmom_65
    mum "Thanks... for everything. I don't know what I'd do without you."
    show bg bathwithmom_55

    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
