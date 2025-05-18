## Second Camgurl Stream ##
label lbl_second_camgurl_stream:
    default secondcamgurlstream_donate = 0
    default secondcamgurlstream_squirtforus = 0

    scene bg secondcamgurlstream_1
    with fade
    $ renpy.pause(0.7,hard=True)
    show bg secondcamgurlstream_2
    $ renpy.pause(0.7,hard=True)
    show bg secondcamgurlstream_1
    $ renpy.pause(0.7,hard=True)
    show bg secondcamgurlstream_2
    $ renpy.pause(0.7,hard=True)
    pov "Oh- wow... caught the stream just in time."
    show bg secondcamgurlstream_1
    sis "{i}*Pants*{/i}"
    show bg secondcamgurlstream_2
    "{i}*Ding*{/i}"
    show bg secondcamgurlstream_1
    "{i}*Ding ding*{/i}"
    show bg secondcamgurlstream_2
    "{i}*Di-ding dingding*{/i}"
    show bg secondcamgurlstream_1
    "{i}*Ding dingdi-ding*{/i}"
    show bg secondcamgurlstream_4
    sis "Oh my God... thank you.. Guys..."
    show bg secondcamgurlstream_3
    sis "K-keep the donations coming if you wanna s-see me- cumming..."
    show bg secondcamgurlstream_4
    sis "Hehee-"
    show bg secondcamgurlstream_2
    sis "Ahh... Fuck..."
    show bg secondcamgurlstream_3
    sis "Thank you, BigJeff- Thank you, x3_Badboy- Thank you, KwazzyTee-"
    show bg secondcamgurlstream_2
    pov "{i}Oh, I'm definitely gonna make her cum.{/i}"

    menu:
        "Donate nothing, you broke-ass" if inventory.money <= 9:
            jump lbl_second_camgurl_stream_2
        "Donate $10" if inventory.money >= 10:
            $ inventory.money -= 10
            $ renpy.notify("Current Balance: $[inventory.money]")
            if skill_luc >= 20:
                $ skill_luc -= 5
                $ secondcamgurlstream_donate = 5

                jump lbl_second_camgurl_stream_1
            else:
                jump lbl_second_camgurl_stream_2
        "Donate $20" if inventory.money >= 20:
            $ inventory.money -= 20
            $ renpy.notify("Current Balance: $[inventory.money]")
            if skill_luc >= 16:
                $ skill_luc -= 4
                $ secondcamgurlstream_donate = 4

                jump lbl_second_camgurl_stream_1
            else:
                jump lbl_second_camgurl_stream_2
        "Donate $50" if inventory.money >= 50:
            $ inventory.money -= 50
            $ renpy.notify("Current Balance: $[inventory.money]")
            if skill_luc >= 12:
                $ skill_luc -= 3
                $ secondcamgurlstream_donate = 3

                jump lbl_second_camgurl_stream_1
            else:
                jump lbl_second_camgurl_stream_2
        "Donate $100" if inventory.money >= 100:
            $ inventory.money -= 100
            $ renpy.notify("Current Balance: $[inventory.money]")
            if skill_luc >= 8:
                $ skill_luc -= 2
                $ secondcamgurlstream_donate = 2

                jump lbl_second_camgurl_stream_1
            else:
                jump lbl_second_camgurl_stream_2
        "Donate $200" if inventory.money >= 200:
            $ inventory.money -= 200
            $ renpy.notify("Current Balance: $[inventory.money]")
            if skill_luc >= 4:
                $ skill_luc -= 1
                $ secondcamgurlstream_donate = 1

                jump lbl_second_camgurl_stream_1
            else:
                jump lbl_second_camgurl_stream_2
        "Donate $500" if inventory.money >= 500:
            $ inventory.money -= 500
            $ renpy.notify("Current Balance: $[inventory.money]")

            jump lbl_second_camgurl_stream_1

label lbl_second_camgurl_stream_1:
    show bg secondcamgurlstream_1
    sis "Thank- Th- Mm..."
    show bg secondcamgurlstream_2
    sis "Ah.. ahh.. Oh my God... I'm cumming-"
    show bg secondcamgurlstream_1
    sis "Guys, I'm cum-"
    show bg secondcamgurlstream_5
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_6
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_7
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_8
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_9
    sis "Fucckk! Fuck- fuck- fuck-"
    show bg secondcamgurlstream_10
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_11
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_12
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_13
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_14
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_15
    sis "Oh- fuck- oh my God..."
    show bg secondcamgurlstream_16
    sis "I- I'm sorry-"
    show bg secondcamgurlstream_15
    sis "Sorry I cussed..."
    show bg secondcamgurlstream_16
    sis "Fuck-"
    show bg secondcamgurlstream_17
    sis "Oops, I made a little mess."
    show bg secondcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg secondcamgurlstream_19
    $ renpy.pause(0.5,hard=True)
    show bg secondcamgurlstream_20
    $ renpy.pause(0.5,hard=True)
    show bg secondcamgurlstream_21
    sis "{i}*gulps* *pants*{/i}"
    show bg secondcamgurlstream_24
    sis "Wh-who? Which one of you made me cum?"
    show bg secondcamgurlstream_20
    sis "..."
    sis "Mm..."
    sis "[usname]?"
    show bg secondcamgurlstream_23
    sis "[usname], you naughty, naughty man."
    show bg secondcamgurlstream_22
    sis "Look what you did to poor, little me."
    show bg secondcamgurlstream_23
    sis "You must be so proud of yourself, aren't you? Hehehehe~"
    show bg secondcamgurlstream_24
    sis "I'll definitely remember your name."
    show bg secondcamgurlstream_23
    sis "I love you, [usname]. I dedicate tonight's squirt to you~"
    $ secondcamgurlstream_squirtforus = 1

    jump lbl_second_camgurl_stream_end

label lbl_second_camgurl_stream_2:
    show bg secondcamgurlstream_1
    $ renpy.pause(0.7,hard=True)
    show bg secondcamgurlstream_2
    $ renpy.pause(0.7,hard=True)
    show bg secondcamgurlstream_1
    $ renpy.pause(0.7,hard=True)
    show bg secondcamgurlstream_2
    $ renpy.pause(0.7,hard=True)
    sis "{i}*Pants*{/i}"
    show bg secondcamgurlstream_3
    sis "I- Oh my God... thank you, guys so much for all the- the donations."
    show bg secondcamgurlstream_4
    sis "It's really buzzing hard inside me..."
    show bg secondcamgurlstream_1
    sis "Mm..."
    show bg secondcamgurlstream_2
    sis "I- It's-"
    show bg secondcamgurlstream_1
    sis "Mmm... fuck.. Fuck..."
    show bg secondcamgurlstream_2
    sis "Oh my God, I'm gonna cum.."
    show bg secondcamgurlstream_3
    sis "Who's doing that?"
    show bg secondcamgurlstream_2
    sis "Who's-"
    show bg secondcamgurlstream_5
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_6
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_7
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_8
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_9
    sis "Fucckk! Fuck- fuck- fuck-"
    show bg secondcamgurlstream_10
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_11
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_12
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_13
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_14
    $ renpy.pause(0.2,hard=True)
    show bg secondcamgurlstream_15
    sis "Oh- fuck- oh my God..."
    show bg secondcamgurlstream_16
    sis "I- I'm sorry-"
    show bg secondcamgurlstream_15
    sis "Sorry I cussed..."
    show bg secondcamgurlstream_16
    sis "Fuck-"
    show bg secondcamgurlstream_17
    sis "Oops, I made a little mess."
    show bg secondcamgurlstream_18
    $ renpy.pause(0.5,hard=True)
    show bg secondcamgurlstream_19
    $ renpy.pause(0.5,hard=True)
    show bg secondcamgurlstream_20
    $ renpy.pause(0.5,hard=True)
    show bg secondcamgurlstream_21
    sis "{i}*gulps* *pants*{/i}"
    show bg secondcamgurlstream_22
    sis "Wh-who? Which one of you made me cum?"
    show bg secondcamgurlstream_20
    sis "..."
    sis "Mm..."
    sis "Chestnutt?"
    show bg secondcamgurlstream_23
    sis "Naww, Chestnutt, you're too generous, man."
    show bg secondcamgurlstream_24
    sis "You made me cum last time as well!"

    jump lbl_second_camgurl_stream_end

label lbl_second_camgurl_stream_end:
    show bg secondcamgurlstream_23
    sis "And to all of you, thank you so much for all your heartfelt donations."
    sis "I hope many of you came with me, I'd love to see the mess you made. Remember to send them as a PM~"
    sis "I hope we broke the world record for the most people who came at the same time."
    show bg secondcamgurlstream_24
    sis "Hehehe~ Just kidding, joke, joke."
    show bg secondcamgurlstream_23
    sis "{i}*Pants*{/i}"
    show bg secondcamgurlstream_24
    sis "This toy took me a while to set up but it was definitely worth it!"
    show bg secondcamgurlstream_23
    sis "I'd love to try this one again sometime."
    sis "Anyway, thank you all for coming along to my stream."
    sis "Get it? Cumming?"
    show bg secondcamgurlstream_24
    sis "Sorry I had to leave with a bad taste in your mouths, hahaha~"
    sis "I'm going to turn to my private stream for my top donators. I can't wait to see you all in there!"
    show bg secondcamgurlstream_25
    sis "Byee~"
    sis ".."
    sis "..."
    sis "Why isn't it- oh, ther-"
    show bg firstcamgurlstream_0_2
    $ renpy.pause()
    pov "{i}Goddamnit. I'm never going to get into her private streams.{/i}"
    pov "{i}I definitely should ask her about this in the box fort. Even if I have to force it out of her.{/i}"
    pov "{i}There's no way I'm letting this go.{/i}"
    $ sister_path = 15
    if secondcamgurlstream_donate == 1:
        $ renpy.notify("You used a Luck Point")
    elif secondcamgurlstream_donate == 2:
        $ renpy.notify("You used 2 Luck Points")
    elif secondcamgurlstream_donate == 3:
        $ renpy.notify("You used 3 Luck Points")
    elif secondcamgurlstream_donate == 4:
        $ renpy.notify("You used 4 Luck Points")
    elif secondcamgurlstream_donate == 5:
        $ renpy.notify("You used 5 Luck Points")

    jump lbl_mybedroom_day_setup
