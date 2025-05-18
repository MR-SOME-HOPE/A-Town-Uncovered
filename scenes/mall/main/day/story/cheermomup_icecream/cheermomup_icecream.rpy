## Cheer Mom Up - Icecream ##
label lbl_cheermomup_icecream:
    default cheermomup_icecream_exception = 0
    default cheermomup_icecream_10dollar = 0
    default cheermomup_icecream_20dollar = 0
    default cheermomup_icecream_30dollar = 0
    default cheermomup_icecream_visit = 0

    scene bg mall_day_icecreampy
    if cheermomup_icecream_visit == 0:
        $ cheermomup_icecream_visit = 1
        show pov neutral_talk at left
        with dissolve
        show ala bored at right
        call lbl_icecreampy_counter_check
        with dissolve
        pov "Hey, Alanna."
        show pov neutral at left
        show ala bored_talk at right
        ala "Hey, [povname]. You here to work or what?"

        menu:
            "Work.":
                jump lbl_working_at_icecreampy
            "Buy Icecream.":
                show pov neutral_talk at left
                show ala bored at right
                pov "Actually, no. I can't at the moment. I'm here to grab a tub of icecream."
                show pov bored at left
                show ala bored_talk at right
                ala "We're an icecream parlour. We don't sell tubs of icecream."
                ala "You either grab a cone or a cup or get."
                ala "Thank you, please come ag-"
                show pov smirk_talk at left
                show ala bored at right
                pov "C'mon, Alanna."

                jump lbl_cheermomup_icecream_1
    elif cheermomup_icecream_visit == 1:
        show pov neutral_talk at left
        with dissolve
        show ala bored at right
        with dissolve
        pov "Hey, Alanna."
        show pov neutral at left
        show ala bored_talk at right
        ala "Hey, [povname]. You here for work or you still want some icecream?"

        menu:
            "Work.":
                jump lbl_working_at_icecreampy
            "Buy Icecream.":
                show pov neutral_talk at left
                show ala bored at right
                pov "I'm here for the icecream."
                show pov bored at left
                show ala bored_talk at right
                ala "Well, we still don't sell tubs."

                jump lbl_cheermomup_icecream_1
    else:
        show pov neutral_talk at left
        show ala bored at right
        pov "Hey again."
        show pov neutral at left
        show ala bored_talk at right
        ala "Did you decide on a flavour?"

        jump lbl_cheermomup_icecream_4

label lbl_cheermomup_icecream_1:

    menu:
        "Can't you make an exception for me?" if cheermomup_icecream_exception == 0:
            show pov smirk_talk at left
            show ala bored at right
            pov "We work together, I'm sure you can make an exception for me."
            if alanna_points >= 5:
                show pov neutral at left
                show ala neutral_talk at right
                ala "Fine. I guess I can do it just for you."
                show pov neutral_talk at left
                show ala neutral at right
                pov "Really?! Thank you so much! That means a lot to me."
                show pov neutral at left
                show ala bored_talk at right
                ala "Yeah, yeah, don't start taking your clothes off and celebrating, it's just icecream."
                show pov confused_talk at left
                show ala neutral at right
                pov "Yeah, no. I get ya. I'm chill."

                jump lbl_cheermomup_icecream_3
            else:
                show pov smirk at left
                show ala bored at right
                ala "..."
                show pov bored at left
                show ala bored_talk at right
                ala "Does it look like I care if you work with me?"
                show pov embarrassed_talk at left
                show ala bored at right
                pov "I mean... yeah... I thought.. y'know.. we were cool and all."
                show pov embarrassed at left
                show ala bored_talk at right
                ala "I've got a college degree and this is what it got me. I ain't cool."
                show ala smirk_talk at right
                ala "This icecream freezer is though. Hehe. Get it?"
                ala "Cause... cause it's coo-"
                show ala bored_talk at right
                ala "Sorry, it had to be done."
                show ala bored at right
                pov "..."
                show pov embarrassed_talk at left
                show ala bored at right
                pov "Yeah.. haha... sure. Cool."
                $ cheermomup_icecream_exception = 1

                jump lbl_cheermomup_icecream_1
        "I'll pay you for your trouble.":
            show pov neutral_talk at left
            show ala confused at right
            pov "I'll even pay you for your trouble."
            show pov neutral at left
            show ala confused_talk at right
            ala "How much are we talking?"

            jump lbl_cheermomup_icecream_2
        "I'll come back later.":
            show pov bored_talk at left
            show ala bored at right
            pov "I'll come back later. Maybe there's another icecream store here that'll give me better service."
            show pov bored at left
            show ala bored_talk at right
            ala "We're the only one in this mall but sure, please come again."

            jump lbl_mall_day_setup

label lbl_cheermomup_icecream_2:

    menu:
        "$10?" if cheermomup_icecream_10dollar == 0:
            show pov confused_talk at left
            show ala confused at right
            pov "How does $10 sound?"
            if skill_luc >= 15 and skill_cha >= 15:
                show pov neutral at left
                show ala neutral_talk at right
                ala "Yeah, that works for me."

                jump lbl_cheermomup_icecream_3
            else:
                show pov bored at left
                show ala bored_talk at right
                ala "Well, aren't you a cheapskate."
                $ cheermomup_icecream_10dollar = 1

                jump lbl_cheermomup_icecream_2
        "$20?" if cheermomup_icecream_20dollar == 0:
            show pov confused_talk at left
            show ala confused at right
            pov "How does half my shift sound? $20?"
            if skill_luc >= 10 and skill_cha >= 10:
                show pov neutral at left
                show ala neutral_talk at right
                ala "Yeah, that sounds good to me."

                jump lbl_cheermomup_icecream_3
            else:
                show pov bored at left
                show ala bored_talk at right
                ala "That's it? C'mon, [povname]. You're killing me here."
                $ cheermomup_icecream_20dollar = 1

                jump lbl_cheermomup_icecream_2
        "$30?" if cheermomup_icecream_30dollar == 0:
            show pov confused_talk at left
            show ala confused at right
            pov "I'm really pulling my balls here but what about $30?"
            if skill_luc >= 5 and skill_cha >= 5:
                show pov neutral at left
                show ala smirk_talk at right
                ala "Yeah, that'll be great."

                jump lbl_cheermomup_icecream_3
            else:
                show pov bored at left
                show ala bored_talk at right
                ala "Close, but not quite there, [povname]."
                $ cheermomup_icecream_30dollar = 1

                jump lbl_cheermomup_icecream_2
        "$40?":
            show pov sad_talk at left
            show ala smirk at right
            pov "I don't know why I'm even offering this much for a frikkin tub of iceceam."
            pov "But you can't dare say no to $40."
            show pov embarrassed at left
            show ala smirk_talk at right
            ala "Yeah, how could anyone ever say no to this deal?"

            jump lbl_cheermomup_icecream_3

label lbl_cheermomup_icecream_3:
    show pov confused at left
    show ala confused_talk at right
    ala "So what will it be?"
    show pov confused_talk at left
    show ala confused at right
    pov "I beg your pardon?"
    show pov confused at left
    show ala bored_talk at right
    ala "Flavour. What flavour are you looking for?"
    show pov shocked_talk at left
    show ala bored at right
    pov "Oh! Oh, right, duh. Well... um... what do you recommend?"
    show pov bored at left
    show ala bored_talk at right
    ala "Don't you work here?"
    show pov embarrassed_talk at left
    show ala bored at right
    pov "Yeah but, I never got to try ALL the flavours."
    show pov neutral_talk at left
    show ala confused at right
    pov "What's the richest, creamiest one available?"
    show pov confused at left
    show ala smirk_talk at right
    ala "Richest and creamiest one you say?"
    ala "Hmmm. Gimme a second while I head to the back."
    hide ala smirk talk
    with dissolve
    hide counter icecreampy
    with dissolve
    $ renpy.pause(1,hard=True)
    show ala smirk_talk at right
    call lbl_icecreampy_counter_check
    with dissolve
    show pov confused at left
    ala "This one is my own creation. I've been experimenting on it while you were managing the front."
    show pov confused_talk at left
    show ala neutral at right
    pov "Your own creation?"
    show pov confused at left
    show ala neutral_talk at right
    ala "Yup! And may I say, it is frikkin amazin'!"
    show pov confused_talk at left
    show ala smirk at right
    pov "What's in it."
    show pov confused at left
    show ala smirk_talk at right
    ala "Wha- well... friend. That right there is a trade secret."
    ala "I can't be letting you steal my ticket to millions."
    show pov confused_talk at left
    show ala confused at right
    pov "Has our manager approved this?"
    show pov confused at left
    show ala smirk_talk at right
    ala "Uhh no. That's why I've kept it at the back."
    show pov confused_talk at left
    show ala bored at right
    pov "I- don't know..."
    show pov bored at left
    show ala bored_talk at right
    ala "Don't be a party pooper, [povname]."
    show ala confused_talk at right
    ala "What, you don't trust me? I know how to make icecream."
    show pov embarrassed at left
    ala "It's not like I'm just adding random ingredients in here without thinking."
    show pov embarrassed_talk at left
    show ala sad at right
    pov "I wasn't saying you were."
    show pov embarrassed at left
    show ala sad_talk at right
    ala "Well, I'm not."
    show ala sad at right
    pov "..."
    show ala confused_talk at right
    ala "Seriously, I feel really uncomfortable that you're putting me on the spot like this."
    show pov confused_talk at left
    show ala embarrassed at right
    pov "I didn't say anything."
    show pov bored at left
    show ala embarrassed_talk at right
    ala "Right."
    show pov bored_talk at left
    show ala neutral at right
    pov "Fine, how much for a tub of it?"
    show pov shocked at left
    show ala neutral_talk at right
    ala "$40"
    show pov shocked_talk at left
    show ala bored at right
    pov "$40 for a tub of icecream?! You're crazy."
    show pov bored at left
    show ala bored_talk at right
    ala "Hey, kiddo. It's $5 for 2 scoops and a cone. This tub could easily get you like, more than 20 proper scoops."
    ala "I ain't no genius but that's value."
    ala "Plus, it's a seasonal, limited time flavour."
    show pov bored_talk at left
    show ala bored at right
    pov "How much for a regular, non-seasonal flavour then?"
    show pov neutral at left
    show ala bored_talk at right
    ala "Eh... $25?"

label lbl_cheermomup_icecream_4:

    menu:
        "Experimental flavour." if inventory.money >= 40:
            show pov neutral_talk at left
            show ala shocked at right
            pov "I'll take your experimental flavour."
            show pov neutral at left
            show ala neutral_talk at right
            ala "Awesome! I promise, it'll blow your mind."
            show pov embarrassed_talk at left
            show ala confused at right
            if winc == 0:
                pov "Oh, it's not for me, it's for my [mumrole]."
            else:
                pov "Oh, it's not for me, it's for my mom."
            show pov confused at left
            show ala confused_talk at right
            if winc == 0:
                ala "You still live with your [mumrole]?"
            else:
                ala "You still live with your mom?"
            show pov confused_talk at left
            show ala shocked at right
            pov "I'm still a student."
            show pov confused at left
            show ala shocked_talk at right
            ala "Ahh right, right. I forgot. I always pictured you a little more.. ‘mature' than that."
            show pov confused_talk at left
            show ala neutral at right
            pov "Thanks?"
            show pov neutral at left
            show ala neutral_talk at right
            ala "Anyways, thanks for coming! Let me know how she likes it!"
            $ inventory.buy(Items.icecream4)
            if alanna_points <= 8:
                $ alanna_points += 2
            else:
                $ alanna_points = 10
            $ renpy.notify("New Item Obtained: Alanna's Icecream")
            $ renpy.pause(3,hard=True)
            $ renpy.notify("Your relationship with Alanna has increased by 2")
            $ renpy.pause(3,hard=True)

            jump lbl_mall_day_setup
        "Triple Fudge Delight." if inventory.money >= 25:
            show pov neutral_talk at left
            show ala sad at right
            pov "I'll take fudge delight."
            $ inventory.buy(Items.icecream1)

            jump lbl_cheermomup_icecream_5
        "Rare Velvet." if inventory.money >= 25:
            show pov neutral_talk at left
            show ala sad at right
            pov "I'll take rare velvet."
            $ inventory.buy(Items.icecream2)

            jump lbl_cheermomup_icecream_5
        "Creme Fatale." if inventory.money >= 25:
            show pov neutral_talk at left
            show ala sad at right
            pov "I'll take creme fatale."
            $ inventory.buy(Items.icecream3)

            jump lbl_cheermomup_icecream_5
        "I don't have any money." if inventory.money < 25:
            show pov embarrassed_talk at left
            show ala bored at right
            pov "I don't have any money..."
            show pov sad at left
            show ala confused_talk at right
            ala "That's... fucking sad."
            show pov embarrassed_talk at left
            show ala bored at right
            pov "I'll just work a shift right now."
            show pov sad at left
            show ala bored_talk at right
            ala "Yeah, good idea."
            scene bg job_icecreampy_1
            with dissolve
            $ renpy.pause()
            $ gtime += 1
            $ inventory.money += 40
            if gtime == 1:
                scene bg mall_day_icecreampy
                show ala bored at right
                show pov neutral at left
                with fade
                $ renpy.notify("Current Balance: $[inventory.money]")

                jump lbl_cheermomup_icecream_4
            else:
                scene bg townmap_night
                with fade
                $ renpy.notify("Current Balance: $[inventory.money]")
                $ cheermomup_icecream_visit = 2

                jump lbl_townmap_setup

label lbl_cheermomup_icecream_5:
    show pov embarrassed at left
    show ala sad_talk at right
    ala "Oh. Alright then."
    show ala embarrassed_talk at right
    ala "I guess you can try my icecream some other time?"

    menu:
        "Of course.":
            show pov neutral_talk at left
            show ala neutral at right
            if winc == 0:
                pov "Of course, Alanna. I'll have some of it myself. It's just, this icecream isn't for me, it's for my [mumrole]."
            else:
                pov "Of course, Alanna. I'll have some of it myself. It's just, this icecream isn't for me, it's for my mom."
            show pov embarrassed_talk at left
            show ala shocked at right
            pov "She's a little under the weather at the moment."
            show pov neutral at left
            show ala shocked_talk at right
            ala "Oh, sorry to hear that. I do wish her well soon."
            show ala embarrassed_talk at right
            ala "And thanks, [povname]."
            show ala neutral_talk at right
            ala "Here you go. That'll be $25."
            show pov neutral_talk at left
            show ala neutral at right
            pov "Thanks."
            show pov neutral at left
            show ala neutral_talk at right
            ala "Please come again!"
            $ alanna_points += 1
            $ renpy.notify("Your relationship with Alanna has increased")
            $ renpy.pause(3,hard=True)
        "Maybe.":
            show pov embarrassed_talk at left
            show ala embarrassed at right
            pov "Maybe, we'll see."
            show pov embarrassed at left
            show ala embarrassed_talk at right
            ala "Alright... Sure thing, no problem."
            show pov embarrassed_talk at left
            show ala sad at right
            pov "It's nothing personal."
            show pov embarrassed at left
            show ala embarrassed_talk at right
            ala "Yeah, no. Of course not."
            ala "Don't worry about it."
            show pov embarrassed_talk at left
            show ala sad at right
            pov "Don't you have anyone else to give it to?"
            show pov sad at left
            show ala sad_talk at right
            ala "No, not really. And I can't give out taste samples because if I get caught selling this, I'll get fired for sure."
            show pov embarrassed at left
            show ala embarrassed_talk at right
            ala "Anyway, here's your icecream."
            show pov embarrassed_talk at left
            show ala embarrassed at right
            pov "Thanks, Alanna."
            show pov embarrassed at left
            show ala embarrassed_talk at right
            ala "Please come again."
        "Yeah... no.":
            show pov bored_talk at left
            show ala sad at right
            pov "Yeah... no. I don't think so."
            show pov confused at left
            show ala sad_talk at right
            ala "Wow. You're just gonna straight up say that?"
            ala "Not even gonna sugar coat the denial?"
            show pov confused_talk at left
            show ala sad at right
            pov "Look, I just really don't know what you've done with the icecream."
            pov "The rule is that if we are to make more icecream, we have to strictly follow the recipe."
            show pov confused at left
            show ala sad_talk at right
            ala "Yeah, I hear you, [povname]. I get it."
            show ala sad at right
            ala "..."
            show ala sad_talk at right
            ala "Here's your icecream."
            show pov embarrassed_talk at left
            show ala sad at right
            pov "Thanks, Alanna."
            show pov embarrassed at left
            ala "..."
            $ alanna_points -= 1
            $ renpy.notify("Your relationship with Alanna has decreased")
            $ renpy.pause(3,hard=True)

    jump lbl_cheermomup_icecream_6

label lbl_cheermomup_icecream_6:
    if inventory.has_item(Items.icecream1):
        $ renpy.notify("New Item Obtained: Triple Fudge Delight Icecream")
    elif inventory.has_item(Items.icecream2):
        $ renpy.notify("New Item Obtained: Rare Velvet Icecream")
    elif inventory.has_item(Items.icecream3):
        $ renpy.notify("New Item Obtained: Creme Fatale Icecream")

    jump lbl_mall_day_setup
