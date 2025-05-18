## Trapped and Teased ##
label lbl_trapped_and_teased_revisit:
    $ vrheadset_revisitcounter = 0
    jump lbl_trapped_and_teased_revisit_1

label lbl_trapped_and_teased_revisit_1:
    show bg trappedwithallaway_55
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_56
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_55
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_56
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_55
    $ renpy.pause(0.8,hard=True)
    show bg trappedwithallaway_56
    $ renpy.pause(0.8,hard=True)
    mis "Mm... your hand is warm..."
    show bg trappedwithallaway_55
    mis "Has- has it always been this warm..?"
    show bg trappedwithallaway_56
    pov "You like it don't you?"
    show bg trappedwithallaway_55
    mis "Mmm.."
    show bg trappedwithallaway_56
    pov "I want to hear you say it."
    show bg trappedwithallaway_55
    mis "I- I shouldn't..."
    show bg trappedwithallaway_56
    pov "Ah- that's not it."
    show bg trappedwithallaway_55
    mis "I- I like it, [povname]... it feels nice."
    show bg trappedwithallaway_56
    mis "Ahh... yeeahh.. Oh... yeah..."
    show bg trappedwithallaway_55
    mis "That's the spot, [povname]..."
    show bg trappedwithallaway_56
    $ vrheadset_revisitcounter = 0
    jump lbl_trapped_and_teased_revisit_1_1

label lbl_trapped_and_teased_revisit_0:
    $ vrheadset_revisitcounter = 0
    jump lbl_trapped_and_teased_revisit_1_1

####################
## Stage 1
label lbl_trapped_and_teased_revisit_1_1:
    $ vrheadset_revisitcounter += 1
    show bg trappedwithallaway_55
    $ renpy.pause(0.4,hard=True)
    show bg trappedwithallaway_56
    $ renpy.pause(0.4,hard=True)
    jump lbl_trapped_and_teased_revisit_counter
####################
## Stage 2
label lbl_trapped_and_teased_revisit_1_2:
    $ vrheadset_revisitcounter += 1
    show bg trappedwithallaway_55
    $ renpy.pause(0.2,hard=True)
    show bg trappedwithallaway_56
    $ renpy.pause(0.2,hard=True)
    jump lbl_trapped_and_teased_revisit_counter

####################
## Stage 3
label lbl_trapped_and_teased_revisit_1_3:
    $ vrheadset_revisitcounter += 1
    show bg trappedwithallaway_55
    $ renpy.pause(0.1,hard=True)
    show bg trappedwithallaway_56
    $ renpy.pause(0.1,hard=True)
    jump lbl_trapped_and_teased_revisit_counter


label lbl_trapped_and_teased_revisit_counter:
    if 30 <= vrheadset_revisitcounter <= 59:
        jump lbl_trapped_and_teased_revisit_1_2
    elif 60 <= vrheadset_revisitcounter <= 89:
        jump lbl_trapped_and_teased_revisit_1_3
    elif vrheadset_revisitcounter >= 90:
        call screen scr_trapped_and_teased_revisit
    else:
        jump lbl_trapped_and_teased_revisit_1_1

screen scr_trapped_and_teased_revisit():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_trapped_and_teased_revisit_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_trapped_and_teased_revisit_1_4")


####################
## Cum or Not
label lbl_trapped_and_teased_revisit_1_4:
    show bg trappedwithallaway_57
    with vpunch
    mis "Oh- fucckk!"
    show bg trappedwithallaway_58
    mis "Oh, fuck..."
    show bg trappedwithallaway_59
    mis "Fuck fuckity fuck!"
    show bg trappedwithallaway_60
    $ renpy.pause(0.5,hard=True)
    show bg trappedwithallaway_61
    $ renpy.pause(0.5,hard=True)
    show bg trappedwithallaway_62
    $ renpy.pause(0.5,hard=True)
    show bg trappedwithallaway_63
    $ renpy.pause(0.5,hard=True)
    mis "Oh God, that felt so good."
    show bg trappedwithallaway_62
    mis "I fucking needed that."
    mis "Shit... what a fucking mess."
    mis "..."
    mis "Excuse my French, [povname]."
    pov "Hahaha, you can speak all the French you want. I find it so hot and unlike you."
    mis "..."
    mis "C'mon. Let's get some sleep. We may be stuck in the classroom but we still need to get some shut eye."
    pov "Right. Good idea. I guess next time you can return the favour."
    mis "Ha. Good one, [povname]. In your dreams. As if this will ever happen again."
    mis "I hope..."
    scene black
    with fade
    $ renpy.pause (1,hard=True)
    jump lbl_vrheadset_character_selection
