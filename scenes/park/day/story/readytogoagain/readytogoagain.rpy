## Ready To Go Again#
label lbl_ready_to_go_again:
    scene bg park_day
    with fade
    show pov smirk_talk at left
    show jac shocked at Position(xpos=1200)
    show edw confused at Position(xpos=1700)
    with dissolve
    pov "Hey, boys."
    show pov neutral_talk
    show jac shocked
    show edw shocked
    pov "I’m ready to head in."

    show pov neutral
    show jac neutral
    show edw confused_talk
    edw "Ah- speak of the devil!"

    show pov neutral
    show jac smirk_talk
    show edw neutral
    jac "There’s our number one agent."
    jac "Are you all ready to go?"

    show pov confused
    show jac embarrassed
    show edw confused_talk
    edw "This is it, [povname]."
    show edw bored_talk
    edw "This is now or never."
    edw "Whatever awaits you on the other side, is gonna change tomorrow."
    show edw sad_talk
    edw "Are you sure you’re ready to enter the lion’s den?"
    show edw bored

    "Important" "Please save your game on a different file so you can come back and do other activities! You can't go back from here."

    menu:
        "I’m ready to go.":
            show pov neutral_talk
            show jac neutral
            show edw neutral
            pov "I'm ready to go."
            show pov embarrassed_talk
            pov "Effie needs me. I can’t imagine how scared she is."
            show pov bored_talk
            pov "Ready me up."

            show pov neutral
            show edw bored_talk
            edw "Okay, soldier."
            show edw confused_talk
            edw "I’m gonna attach a few things to your body, okay?"
            show edw bored_talk
            edw "They’re really small and undetectable unless you are actively looking for them."
            edw "They need to be since you’ll be mostly naked in the sex world."
            edw "Would that be a fair assumption?"

            show pov confused_talk
            show edw bored
            pov "Mmm.. I guess so."

            show pov smirk
            show jac smirk_talk
            jac "Damn... maybe I should head in too."

            show jac bored
            show edw bored_talk
            edw "Jacob. It’s too dangerous for you to go."
            edw "You’ll be more a liability than an asset."

            show jac bored_talk
            show edw bored
            jac "You don’t have to say it like that."
            jac "Maybe next time, aye? When there isn’t the danger of it."

            show pov smirk_talk
            show jac confused
            pov "If you wanna walk around naked so much just go to the beach, Jacob."
            pov "You basically walk past there everyday to Hendai’s anyway."

            show pov smirk
            show jac embarrassed_talk
            jac "So true. But it isn’t the same."

            show pov confused_talk
            show jac neutral
            show edw confused
            pov "Anyway."
            pov "Go on, Edward."

            show pov confused
            show edw bored_talk
            edw "This ‘mole’ is actually an updated version of the vitals tracking, more accurate, but more importantly, more discreet."
            edw "Leave it on your nape and try not to scratch it off."
            edw "Now, if my theory is correct about this parallel world, when you enter the other side, you should see the other us at the park as well."
            edw "And if all is right, we should see the other you appear here too."
            edw "What happens after that is beyond me."

            show pov confused_talk
            show edw smirk
            pov "Hopefully so, this parallel universe shit is convoluted as fuck."

            show pov smirk
            show jac confused_talk
            jac "Pssh, you’re telling me."
            jac "I still can’t get over the fact that there IS a parallel universe."

            show pov neutral
            show jac confused
            show edw bored_talk
            edw "There are weirder things in the world."

            show pov embarrassed_talk
            show jac neutral
            pov "Anyway, is that all for gadgets?"

            show pov neutral
            show edw embarrassed_talk
            edw "It’s all we really need. A working camera is still in the works."

            show jac smirk_talk
            show edw bored
            jac "Aka, he doesn’t know how to make it not look like pure static noise."

            show jac smirk
            show edw bored_talk
            edw "It’s-"
            edw "Getting there..."

            show pov embarrassed_talk
            show edw confused
            pov "I’ll be fine without it, I can just describe to you what I see if I ever need your assistance."

            show pov neutral
            show jac neutral
            show edw neutral_talk
            edw "Sounds good."

            show pov embarrassed_talk
            show edw neutral
            pov "*Sigh* Alright."
            pov "I’ll head off then, wish me luck."

            show pov embarrassed
            show jac embarrassed_talk
            jac "Hey, be safe, okay?"
            jac "Get our Effie back to us in one piece."

            show jac embarrassed
            show edw embarrassed_talk
            edw "Godspeed, man."
            edw "The sex world awai-"

            stop music fadeout 1.0

            show pov shocked
            show jac shocked
            show edw shocked
            "*SIRRREEEEEEENNNNNN WHEEERRINGGGG*"

            show edw shocked_talk
            edw "What the hell?"

            show jac shocked_talk
            show edw shocked
            jac "Is that the warning siren?"
            jac "Is there a tsunami?!"

            show jac shocked
            show edw shocked_talk
            edw "Shit-"
            edw "Worst."
            edw "Look"

            scene bg readytogoagain_9
            with fade
            $ renpy.pause()

            jac "Are those?"

            pov "VIs."

            scene bg readytogoagain_10
            edw "They’re invading..."
            edw "Who- how?"
            edw "Already?!"
            
            jac "Fuck- we should’ve hurried."

            edw "There’s no time to waste, [povname]."
            edw "Get in and get outta here!"

            jac "Go, dude! GO!"

            pov "See you when I see you."

            scene bg readytogoagain_1
            $ renpy.pause(1.5,hard=True)
            show bg readytogoagain_2
            $ renpy.pause(1.5,hard=True)
            show bg readytogoagain_3
            $ renpy.pause(2.5,hard=True)

            show bg readytogoagain_4
            $ renpy.pause(2,hard=True)
            show bg readytogoagain_5
            $ renpy.pause(1.5,hard=True)
            show bg readytogoagain_6
            $ renpy.pause(1.5,hard=True)
            show bg readytogoagain_7
            $ renpy.pause(1.2,hard=True)
            show bg readytogoagain_8
            $ renpy.pause(1.2,hard=True)
            scene black

            $ main_story = 126

            $ townmap_enabled = 0

            scene bg park_day
            with fade

            jump lbl_hurry_to_the_office_building

        "Give me a bit.":
            show pov embarrassed_talk
            show jac confused
            show edw confused
            pov "Give me a bit."
            pov "There are some things I have to take care first."
            pov "I’m sure Effie will be okay."

            show pov embarrassed
            show jac confused_talk
            jac "Yeah, sure. Effie will be fine, she’s a strong girl."
            show jac smirk_talk
            jac "Edward actually managed to get a reading on her vitals after the software update and some dimensional hacker magic."
            jac "She seems to be in good condition."
            show jac confused_talk
            jac "Annoyed and... ovulating...?"
            jac "Edward?"

            show jac confused
            show edw embarrassed_talk
            edw "She’s good."
            edw "Just come to the park and give us a call when you’re ready."

            $ main_story = 125.1

            jump lbl_park_day

label lbl_ready_to_go_again_call:
    menu:
        "Call Jacob and Edward?"
        "Call them":
            "{i}*Riiing*{/i}"
            pov "{i}Hey, guys. Meet me at the park pronto."
            scene black
            with fade
            $ renpy.pause()

            "When Jacob and Edward arrives..."

            scene bg park_day
            with fade

            jump lbl_ready_to_go_again

        "No.":
            jump lbl_park_day
            