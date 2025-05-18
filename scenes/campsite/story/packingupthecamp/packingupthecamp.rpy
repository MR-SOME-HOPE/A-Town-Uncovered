## Packing Up The Camp
label lbl_packing_up_the_camp:
    scene black
    with fade
    $ renpy.pause()
    "The next morning after the campsite has been packed up..."

    scene bg campsite_1
    with fade

    show pov embarrassed_talk at left
    show sis neutral at Position(xpos=1300)
    show mumc neutral at right
    with dissolve
    pov "{i}*Phew*{/i} Awesome."
    pov "Thanks for helping me pack up the campsite this time, girls."
    show pov smirk_talk
    show sis smirk
    show mumc neutral
    pov "Glad you didn’t run off to the hot springs and leave me to do it myself."

    show pov bored
    show sis smirk_talk
    show mumc neutral
    sis "Oh- but we were so close to doing it though."

    show pov neutral
    show sis smirk
    show mumc embarrassed_talk
    mum "Shush, [sister]."
    show pov shocked
    mum "That’s supposed to be a secret!"

    show pov sad_talk
    show mumc smirk
    pov "Hey!"

    show pov sad
    show sis smirk
    show mumc smirk_talk
    mum "We’re kidding!"

    show pov bored
    show sis smirk_talk
    show mumc smirk
    sis "We’re not kidding."

    show sis smirk
    show mumc neutral_talk
    mum "We’re kidding!!"

    show sis smirk_talk
    show mumc bored
    sis "We’re not kidding."

    show sis smirk
    show mumc shocked_talk
    mum "Stop confusing him!"

    show pov neutral_talk
    show sis smirk
    show mumc embarrassed
    pov "I know she’s just being a dweeb."

    show pov neutral
    show sis neutral
    show mumc confused_talk
    mum "Alright. We didn’t forget anything, did we? I want you guys to double-triple check everywhere."

    show pov neutral
    show sis bored_talk
    show mumc neutral
    if winc == 0:
        sis "Already am, [missus]."
    else:
        sis "Already am, mom."

    show pov neutral_talk
    show sis confused
    pov "I don’t see anything, everything’s clear and the firepit is safe."

    show pov confused
    show sis confused
    show mumc confused_talk
    mum "Did you pee on it?"

    show mumc confused
    pov "..."
    show pov confused_talk
    pov "Should I?"

    show pov confused
    show mumc confused_talk
    mum "Nooo..."
    mum "No?"

    show pov confused_talk
    show mumc confused
    pov "Idunno-"

    show pov confused
    show sis neutral_talk
    show mumc confused
    sis "I think we’re good here then."
    show pov sad
    show sis embarrassed
    show mumc embarrassed
    sis "Car’s packed."
    sis "Let’s go home..."
    show sis sad_talk
    show mumc sad
    sis "{i}*Sigh*{/i}"

    show sis sad
    show mumc sad_talk
    mum "Everything alright, dear?"

    show pov embarrassed
    show sis sad_talk
    show mumc embarrassed
    sis "I’m gonna miss this place."

    show pov embarrassed
    show sis sad
    show mumc embarrassed_talk
    mum "It’s not going anywhere, hehehe."

    show sis sad_talk
    show mumc embarrassed
    sis "I know, it’s just. I didn’t expect to have such a good time and now we’re leaving and ughhh.."
    sis "Yeah, I’m just gonna miss it."
    show sis embarrassed_talk
    show mumc neutral
    sis "Let’s come back here soon, okay? Seriously."
    show pov neutral
    show sis neutral_talk
    show mumc shocked
    sis "Or like- more other adventures."
    if winc == 0:
        sis "As a household!"
    else:
        sis "As a family!"
    show sis embarrassed_talk
    show mumc embarrassed
    sis "I’m already thinking of other stuff we can do and go to!"

    show sis embarrassed
    show mumc embarrassed_talk
    mum "Make a list for us, dear."
    mum "I’m so happy you enjoyed the trip."
    mum "I enjoyed it myself and I can’t wait for the next one."

    show pov neutral_talk
    show mumc embarrassed
    pov "Ditto."
    show pov embarrassed_talk
    pov "You guys are the best."
    pov "I love you both."

    show pov embarrassed
    show sis embarrassed_talk
    show mumc sad
    sis "I- love you guys too."

    show pov shocked
    show sis shocked
    show mumc sad_talk
    mum "I LOVE MY BABIES! SO MUCH!"
    show pov embarrassed
    show sis embarrassed
    mum "Get in the car before I become a cring mess!"

    show pov confused
    show sis embarrassed_talk
    show mumc embarrassed
    sis "Hey, [povname]..."
    sis "I uh-"
    sis "Not gonna lie..."
    sis "I’m..."
    show pov smirk
    sis "I’m kinda horny since last night."
    sis "Are you feeling energized… or...?"

    show pov smirk_talk
    show sis embarrassed
    show mumc embarrassed
    pov "Yeah, we can do it on the way home."
    pov "If-"
    if winc == 0:
        pov "It’s okay with [missus], of course?"

        show pov neutral
        show sis sad_talk
        show mumc confused
        sis "Can we, [missus]?! Please!"
    else:
        pov "It’s okay with mom, of course?"

        show pov neutral
        show sis sad_talk
        show mumc confused
        sis "Can we, mom?! Please!"

    show sis shocked
    show mumc smirk_talk
    mum "Oh, alright. Just don’t make a mess, okay?"
    show pov smirk
    show sis neutral
    show mumc bored_talk
    mum "You make a mess, you not only clean it up but you clean the whole car."
    mum "Got it?!"

    show pov neutral_talk
    show mumc neutral
    if winc == 0:
        pov "Yes, [missus]."
    else:
        pov "Yes, mom."

    show pov smirk
    show sis smirk_talk
    show mumc neutral
    sis "Yaaaaay, hurry, let’s go, [povname]."
    
    $ mumsiscamp_path = 14

    jump lbl_fun_ride_home_from_camp

