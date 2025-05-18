label lbl_the_polaroid:
#[Your Room, night - “The Polaroid”  - main_story #=67]
    scene bg thepolaroid_rest
    show eyes thepolaroid_closed
    show charexpression thepolaroid_sad
    show sheets thepolaroid_up
    #scene bg thepolaroid_1_sad
    with fade
    #"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    #"You lay back on your bed at night, the sound of a clock ticking ominously is the only companion you have. You are wide awake and staring at the ceiling unable to sleep, the clock reads 3:00 am."

    pov "…"
    pov "{i}All of this…{/i}"
    pov "{i}It wasn’t my fault, right?{/i}"

    #"You toss and turn in bed as you keep thinking back on the chaos around town."

    #show bg thepolaroid_temp2
    #with dissolve
    #$ renpy.pause(1,hard=True)
    #show bg thepolaroid_temp3
    #with dissolve
    #$ renpy.pause(1,hard=True)
    #show bg thepolaroid_temp2
    show charexpression thepolaroid_confused
    #with dissolve
    #$ renpy.pause(1,hard=True)
    #scene bg thepolaroid_1_confused
    pov "{i}All of this would have happened regardless of whether those maniacs sacrificed me or not…{/i}"
    pov "{i}Right?{/i}"
    show eyes thepolaroid_clenched
    show charexpression thepolaroid_angry
    show phonelight thepolaroid
    pov "…"

    #"Your pondering is suddenly interrupted by a notification sound from your phone."

    #"{i}*Phone Notificaaaation*{/i}"

    #show bg thepolaroid_temp3
    show eyes thepolaroid_right
    show charexpression thepolaroid_bored
    hide phonelight
    pov "Hmm?"
    scene black with fade

    #"Picking it up and unlocking it, you are a bit surprise to see it’s from Effie."

    #(The following is a text conversation the Mc has with “Effie” who is actually Vi using a fake account to try to get the MC to lower his guard and exit the house for the usual kidnapping purposes)

    scene bg thepolaroid_text_1
    with dissolve
    $ renpy.pause()
    #eff "Hey."
    show bg thepolaroid_text_2
    $ renpy.pause()
    #eff "You up? :P"
    show bg thepolaroid_text_3
    $ renpy.pause()
    #pov "Yeah."
    show bg thepolaroid_text_4
    $ renpy.pause()
    # eff "What ya doin?"
    show bg thepolaroid_text_5
    $ renpy.pause()
    # pov "Just thinking."
    show bg thepolaroid_text_6
    $ renpy.pause()
    #eff "You want to have some fun?"
    show bg thepolaroid_text_7
    $ renpy.pause()
    # pov "Uh… I can’t really go out with everything that’s going on, you know this."
    show bg thepolaroid_text_8
    $ renpy.pause()
    # pov "Plus, doesn’t your father have you on lockdown too?"

    #"A few more moments pass and Effie replies by sending you a picture of the front of your house."
    show bg thepolaroid_text_9
    $ renpy.pause()
    #eff "I am right outside, come out."

    #(In voice)
    pov "{i}What the hell?{/i}"

    #(Back to text)
    show bg thepolaroid_text_10
    $ renpy.pause()
    #pov "Effie, what are you doing? Go home before your father notices you are gone!"
    show bg thepolaroid_text_11
    $ renpy.pause()
    #eff "You want a nude?"
    show bg thepolaroid_text_12
    $ renpy.pause()
    #eff "Tits, Vag or Ass? Your pick."
    menu:
        "Tits":
            #"You receive a picture of Vi’s tits, which are of course, noticeably larger than Effie’s, along with paler. Some parts of her white dress can also be seen in the corners of the image along with a few strands of black hair."
            show bg thepolaroid_text_13_1
            $ renpy.pause()
            show bg thepolaroid_text_14_1
            $ renpy.pause()
            pov "Wow! Thi-"
            pov "This-"
            pov "They look..."
            pov "...different..?"

            show bg thepolaroid_text_14_1
            with hpunch
            "{i}*RIIIIIIIIINGGGGTONEEEE*{/i}"
            pov "Jesus fuck-!"

            scene bg thepolaroid_phone
            show eyes thepolaroid_normal
            show charexpression thepolaroid_confused
            show sheets thepolaroid_down
            with fade
            pov "Hey, Effie.."
            show charexpression thepolaroid_shocked
            idk "Like what you see?"
            show charexpression thepolaroid_confused_talk
            pov "Uhm.."
            pov "You're not Effie..."
            show charexpression thepolaroid_angry_talk
            pov "Who is this?"
            show charexpression thepolaroid_shocked
            idk "They are all yours and waiting for you, [povname]."
            idk "Come out and I’ll use them to milk your cock dry."
            show charexpression thepolaroid_angry_talk
            pov "Who the hell is this?!"
            show charexpression thepolaroid_shocked
            idk "Your personal titfuck machine for life if you come out right now,"
            idk "I’ll even let you suck on my nipples while I give you a handjob anytime you want~"
            idk "Or you can motorboat them as you jack off into my stomach."

        "Vag":
            #"Vi sends you a picture of her vagina, her skin pale and overall figure too different for her to be Effie. Maybe she has a bush? That I leave up to Gee-"
            show bg thepolaroid_text_13_3
            $ renpy.pause()
            show bg thepolaroid_text_14_3
            $ renpy.pause()
            pov "Wow! Thi-"
            pov "This-"
            pov "Is this Effie..?"
            pov "It looks... fake?"

            show bg thepolaroid_text_14_3
            with hpunch
            "{i}*RIIIIIIIIINGGGGTONEEEE*{/i}"
            pov "Jesus fuck-!"

            scene bg thepolaroid_phone
            show eyes thepolaroid_normal
            show charexpression thepolaroid_confused
            show sheets thepolaroid_down
            with fade
            pov "Hey, Effie.."
            show charexpression thepolaroid_shocked
            idk "I am soaking wet over here, [povname]"
            show charexpression thepolaroid_confused_talk
            pov "Uhm.."
            pov "You're not Effie..."
            show charexpression thepolaroid_angry_talk
            pov "Who is this?"
            show charexpression thepolaroid_shocked
            idk "Get out here and pound me until my insides take the shape of your dick~"
            idk "I want all of your load inside me~"
            show charexpression thepolaroid_angry_talk
            pov "What the hell?!"
            pov "Who is this?!"
            show charexpression thepolaroid_shocked
            idk "Your future onahole wife if you come out right now."
            idk "I’ll use my pussy to pump you dry of cum every day and night for the rest of your life if you do~"
            idk "Or sit on your face like a throne and suck you off in the process."

        "Ass":
            #"Vi takes a picture of her ass, using her hand to lift up her dress for you to see her properly, her skin way to pale for it to be Effie, not to mention the fact her ass and waist are definitely bigger than hers-"
            show bg thepolaroid_text_13_2
            $ renpy.pause()
            show bg thepolaroid_text_14_2
            $ renpy.pause()
            pov "Wow! Thi-"
            pov "This-"
            pov "Is this Effie..?"
            pov "Her butt looks... bigger... and... really really pale...?"

            show bg thepolaroid_text_14_2
            with hpunch
            "{i}*RIIIIIIIIINGGGGTONEEEE*{/i}"
            pov "Jesus fuck-!"

            scene bg thepolaroid_phone
            show eyes thepolaroid_normal
            show charexpression thepolaroid_confused
            show sheets thepolaroid_down
            with fade
            pov "Hey, Effie.."
            show charexpression thepolaroid_shocked
            idk "This fat ass is begging for you to give it a good spank, [povname]."
            show charexpression thepolaroid_confused_talk
            pov "Uhm.."
            pov "You're not Effie..."
            show charexpression thepolaroid_angry_talk
            pov "Who is this?"
            show charexpression thepolaroid_angry
            idk "Why don’t you come out and we can see how well my ass bounces against you when you thrust that giant nightstick of yours into my cunt?"
            idk "I’ll even let you use the back door~"
            show charexpression thepolaroid_angry_talk
            pov "What the hell?!"
            pov "Who the hell are you?!"
            show charexpression thepolaroid_shocked
            idk "Your very own sentient sexdoll if you come out right now."
            idk "I’ll let you write all you want on my ass and pump me full of cum everyday until you get sick of me and start using the rest of my holes~"
            idk "You can even hold me over your legs and spank this fat ass to your heart’s desire!"

        # "What the hell are you talking about?":
        #     #"Effie takes a moment but you receive a picture of an open mouth with the tongue out as if begging for a load of cum, the skin is far too pale for it to be Effie and the several strands of black hair (which conveniently cover any sign of her being a robot) give yet another clue-"
        #     pov "What-?"
        #     pov "Is this-?"
        #     pov "This doesn't look like.. Effie..."
        #
        #     show bg thepolaroid_temp4
        #     with hpunch
        #     "{i}*RIIIIIIIIINGGGGTONEEEE*{/i}"
        #     pov "Jesus fuck-!"
        #
        #     show bg thepolaroid_temp5
        #     pov "Hey, Effie.."
        #
        #     idk "I need you inside of me, [povname]."
        #
        #     pov "Uhm.."
        #     pov "You're not Effie..."
        #     pov "Who is this?"
        #
        #     idk "My mouth is in severe need for a good dick to ravage it down to the throat."
        #     idk "All you have to do is come out of the house and I’ll give you the blowjob of a lifetime."
        #     idk "I need to feel your cock using my throat like a cheap toy~"
        #
        #     pov "What the hell is this?!"
        #     pov "Who are you?!"
        #
        #     idk "I am your slutty wet hole waiting to be filled with that beast of a cock you have."
        #     idk "All I want is to suck on that dick and drink your cum until the day I die!"
        #     idk "I can even take it down to the base and stay there, you know?~"

    #=RESULT END#=
    show charexpression thepolaroid_angry
    idk "All this and more, you just need to come outside and play~"
    show charexpression thepolaroid_angry_talk
    pov "Look, whoever you are- I don't know how you got this number-"
    pov "You're creeping me the fuck out."
    pov "I'm hanging u-"

    #"You are now visibly freaked out and panicking."
    show charexpression thepolaroid_shocked
    idk "Is that not enough for you?"
    idk "That’s okay! You’ll be ours either way~"
    idk "However I do want you to remember, I asked you nicely first~"
    idk "Now you left me no choice but to use force next time~"
    show charexpression thepolaroid_shocked_talk
    pov "What the hell do you want?!"
    show charexpression thepolaroid_shocked
    idk "You’ll see, you hot stuff~"
    idk "But in the meantime, open the window for me, will you?"
    show charexpression thepolaroid_surprised
    idk "I left you a surprise!"
    show charexpression thepolaroid_angry_talk
    pov "What makes you think I’ll do anything you say?!"
    show charexpression thepolaroid_confused
    idk "Because my orders are to give you this nice gift!, maybe have sex with you if you were up for it too~"
    idk "But since you won’t come and have sex with me."
    idk "And you don’t want to take my gift, then…"
    show charexpression thepolaroid_shocked
    show eyes thepolaroid_shocked
    #"You suddenly hear a knock on your window."
    "{i}*Knock knock knock*{/i}"

    idk "MAYBE."
    idk "I."
    idk "SHOULD."

    scene bg thepolaroid_6
    with vpunch

    idk "COME."
    idk "IN?"
    show effect thepolaroid_vieyes with dissolve

    #"You stand up from the bed in a hurry, now standing in the opposite corner of the room while dropping the phone in the process as you scream at Vi."

    pov "AHHH! WHAT THE FUCKK!"

    #"You close your eyes tightly as if trying to wake up from a dream."

    #show bg thepolaroid_temp7
    scene bg thepolaroid_rest
    show eyes thepolaroid_shocked
    show charexpression thepolaroid_shocked
    show sheets thepolaroid_up
    pov "It's just a dream-"
    show eyes thepolaroid_clenched
    show charexpression thepolaroid_sad
    pov "-it's just a dream-"
    pov "--it's just a dream!"
    scene black with fade
    pov "."
    #"Several minutes of silence happen, no more messages come from the phone and there is not a single noise coming from outside your window."
    show bg thepolaroid_kiss
    show eyes thepolaroid_clenched
    show charexpression thepolaroid_confused
    show sheets thepolaroid_up
    with fade
    pov ".."
    show eyes thepolaroid_closed
    pov "..."
    show eyes thepolaroid_normal
    pov "...."
    show sheets thepolaroid_down with dissolve
    #"You slowly open your eyes to see VI gone and stuck on the window is a polaroid."

    scene bg thepolaroid_8
    with dissolve
    pov "{i}*Gulps*{/i}"
    pov "What the fuck-"
    pov "..."
    #show bg thepolaroid_temp9
    scene bg thepolaroid_calendar1
    pov "Wh-"
    pov "What's that-?"

    scene bg thepolaroid_photo
    pov "Is that- me...?"

    #show bg thepolaroid_temp9
    #$ renpy.pause(1,hard=True)
    #show bg thepolaroid_temp11
    #$ renpy.pause(0.6,hard=True)
    #show bg thepolaroid_temp12
    #$ renpy.pause(0.6,hard=True)
    scene bg thepolaroid_calendar1
    scene bg thepolaroid_calendar2 with dissolve
    scene bg thepolaroid_calendar3 with dissolve
    scene bg thepolaroid_calendar with dissolve
    with vpunch
    "{i}*Thud*{/i}"
    scene black with fade

    #"You are then met with the grim image of bright red letters that one could mistaken as blood at first (It’s lipstick) written all over your window that read in a creepy manner “SEE YOU SOON!” in the middle of it, a single polaroid picture that shows the MC sleeping in his bed, the white frame on the bottom of the picture has a noticeable red lipstick kiss mark followed by a signature by Xina herself."

    #"This proves to be too much for the Mc as he then faints on the spot, in the morning the letters are gone, but the polaroid remains as a grim reminder of what happened last night."

    $ main_story = 68

    jump lbl_mybedroom_night_sleep_1
