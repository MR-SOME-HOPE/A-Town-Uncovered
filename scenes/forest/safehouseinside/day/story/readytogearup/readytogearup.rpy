## Ready To Gear Up
label lbl_ready_to_gear_up:
    ### NO GOING BACK

    ## Everyone is present at the Safehouse
    ## CG of the box of BDSM gear
    scene black
    with fade
    "Everyone is looking at the box of BDSM Gear"

    pov "Alright, everyone."
    pov "This wasn’t cheap-"
    pov "I made a deal with Hazel down at the adult store for some…"
    pov "Returned items and this is what they gave me."

    edw "Wait- returned?"
    edw "You mean… these all have potentially been worn?"

    col "Not potentially."
    col "Most definitely have been worn."

    eff "Ew…"
    eff "Can’t we like wipe them down with alcohol or something."
    eff "It’s all leather and latex, we can’t quite put it in the wash."
    eff "Wait, can we?"

    jac "It is highly inadvisable."

    eff "And how would you know?"

    jac "Bro, it’s just common sense."
    jac "Not everything has to be a weird secret of mine."

    edw "Yeah, uh- I’ll find some ."

    col "It’s weird but the best way to clean and sanitize them is with warm, soapy water."
    col "Rubbing alcohol will ruin that shit."

    edw "Oh yeah, because the last thing I want is to ruin something I’m gonna keep forever."

    eff "I’m not keeping this."

    jac "I meaaaaan…"
    jac "Maybe."

    edw "I’ll grab some rubbing alcohol, there should be somewhere in here."

    pov "Look guys, once we go down, it’ll be pretty hectic."
    pov "There’s no knowing if shit will go down and we’ll have to be fully present in the moment."
    pov "We can wait a while but we should go through with this soon."
    pov "Does everyone understand?"

    col "Yup."

    eff "Loud and clear."

    jac "Crystal."

    "Once you proceed with this, you’ll have to commit to the main story until the very end."
    "We suggest you save your game here as the town won’t be the same after everything is over."
    "Are you ready to proceed?"

    ## If the player chooses to proceed, keep going.
    menu:
        "Proceed":
            jump lbl_ready_to_gear_up_2
        "Come back later":
            pov "Actually, we'll come back to this at another time."
            pov "Make sure you're ready to go."

            $ main_story = 171.5

            scene bg forest_day
            with fade

            jump lbl_forest_day_setup

label lbl_ready_to_gear_up_2:
    scene bg forestsafehouseinside_day
    with fade

    ## SPRITES (normal)
    show pov confused_talk at left
    show col confused at Position(xpos=1000)
    show jac embarrassed at Position(xpos=1300)
    show eff bored at Position(xpos=1500)
    show edw embarrassed at Position(xpos=1800)
    with dissolve
    pov "We also may need to put this gear on now because it’s kind of complicated."
    show pov embarrassed_talk at left
    pov "We definitely won’t have time to change into it when we get there."
    show pov embarrassed at left
    show eff embarrassed_talk at Position(xpos=1500)
    eff "That’s true."
    show jac confused_talk at Position(xpos=1300)
    show eff embarrassed at Position(xpos=1500)
    jac "Okay but… we’re gonna stand out like a sore thumb on the way there."
    show jac confused at Position(xpos=1300)
    show edw embarrassed_talk at Position(xpos=1800)
    edw "I’ve got some cloaks in my bag."
    show col smirk_talk at Position(xpos=1000)
    show edw embarrassed at Position(xpos=1800)
    col "Why do you have cloaks in your bag?"
    show col confused_talk at Position(xpos=1000)
    col "Like, enough for all of us?"
    show pov confused at left
    show col confused at Position(xpos=1000)
    show edw embarrassed_talk at Position(xpos=1800)
    edw "Y-yeah…"
    show col bored at Position(xpos=1000)
    edw "I brought them in case…"
    show col bored_talk at Position(xpos=1000)
    show edw embarrassed at Position(xpos=1800)
    col "Stripping in front of us and that sudden narrow escape really scarred you, didn’t it?"
    show col embarrassed at Position(xpos=1000)
    show jac smirk at Position(xpos=1300)
    show edw bored_talk at Position(xpos=1800)
    edw "To the core."
    edw "I do not like being in my birthday suit…"
    show jac smirk_talk at Position(xpos=1300)
    jac "That’s valid."
    show pov embarrassed at left
    show col smirk at Position(xpos=1000)
    show jac neutral_talk at Position(xpos=1300)
    show eff smirk at Position(xpos=1500)
    jac "It’s not even your birthday."
    show pov neutral at left
    show jac smirk at Position(xpos=1300)
    show edw smirk_talk at Position(xpos=1800)
    eff "Thanks, Edward. Really smart and thoughtful, as always."
    show pov neutral_talk at left
    show edw neutral at Position(xpos=1800)
    pov "Yeah, thanks."
    show pov embarrassed_talk at left
    show col bored at Position(xpos=1000)
    pov "Alright, everyone. Find something that’s your size and get into it."
    show pov smirk_talk at left
    show eff bored at Position(xpos=1500)
    pov "We’re probably gonna look stupid but it’s for the greater good."
    show pov embarrassed_talk at left
    show eff bored_talk at Position(xpos=1500)
    eff "We’ve seen each other naked. No shame."
    show pov embarrassed at left
    show eff smirk at Position(xpos=1500)
    show edw smirk_talk at Position(xpos=1800)
    edw "Speak for yourself."

    scene black
    with fade
    $ renpy.pause()
    "They all change into the BDSM gear and put cloaks on to hide them..."

    scene bg forestsafehouseinside_day
    with fade

    ## SPRITES (cloak - povcl, effcl, colcl, jaccl, edwcl)
    show povcl shocked at left
    show colcl smirk_talk at Position(xpos=1000)
    show jaccl shocked at Position(xpos=1300)
    show effcl smirk at Position(xpos=1500)
    show edwcl embarrassed at Position(xpos=1800)
    with dissolve
    col "Is- are these cloaks from that anime…?"
    show colcl smirk at Position(xpos=1000)
    show jaccl smirk_talk at Position(xpos=1300)
    jac "Weeb."
    show colcl smirk_talk at Position(xpos=1000)
    show jaccl neutral at Position(xpos=1300)
    col "Hey, I didn’t say they’re bad. I like that anime…"
    show povcl embarrassed at left
    show colcl smirk at Position(xpos=1000)
    show effcl neutral_talk at Position(xpos=1500)
    eff "I have no idea what you guys are talking about."
    show povcl embarrassed_talk at left
    show effcl bored at Position(xpos=1500)
    pov "It doesn’t matter."
    pov "What matters is that we’re ready to go."
    show povcl shocked_talk at left
    show edwcl embarrassed at Position(xpos=1800)
    pov "Any last minute mind-changing?"
    show povcl smirk_talk at left
    pov "I need everyone’s full focus and support on this mission."
    show povcl confused_talk at left
    show jaccl bored at Position(xpos=1300)
    show effcl confused at Position(xpos=1500)
    pov "…"
    show povcl embarrassed_talk at left
    pov "Alright, team. Let’s head out."

    ## SCENE END

    $ main_story = 172

    jump lbl_revise_the_final_plan
