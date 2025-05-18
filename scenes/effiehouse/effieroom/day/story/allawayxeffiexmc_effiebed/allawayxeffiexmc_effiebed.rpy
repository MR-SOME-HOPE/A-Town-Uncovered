## Allaway x Effie x MC Effie Bed
default allawayxeffiexmceffiebed_firsttimedone = 0
#default allawayxeffiexmc_effiebed_counter = 0

label lbl_allawayxeffiexmc_effiebed:
    $ gtime = 1
    $ effie_funlater = 0
    if allawayxeffiexmceffiebed_firsttimedone == 0:
        pass
    else:
        jump lbl_allawayxeffiexmc_effiebed_intro2

    scene bg effiehouseoutside_day
    show pov neutral at left
    with dissolve
    show eff neutral_talk at right
    with dissolve
    eff "Hey! [povname]."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Oh? Effie. You're off early today."
    show pov neutral at left
    show eff neutral_talk at right
    eff "Yeah, it got pretty quiet so I decided to close up a tad earlier for today."
    show pov neutral_talk at left
    show eff neutral at right
    pov "Awesome!"
    show pov shocked at left
    mis "Uh- hi..."
    show pov shocked_talk at left
    pov "Miss Allaway?"
    show pov shocked at left
    show misc embarrassed at Position(xpos=1300) zorder 1
    show eff neutral_talk at right
    eff "Miss Allaway! You came!"
    show misc confused_talk at Position(xpos=1300)
    show eff neutral at right
    mis "Of course I came, you told me to come..?"
    show pov shocked_talk at left
    show misc embarrassed at Position(xpos=1300)
    show eff smirk at right
    pov "You asked her to come?"
    show pov confused at left
    show misc embarrassed_talk at Position(xpos=1300)
    mis "For- tutoring."
    show misc shocked at Position(xpos=1300)
    show eff smirk_talk at right
    eff "Oh hush, Miss Allaway. You don't have to lie to [povname]."
    show pov shocked at left
    show eff neutral_talk at right
    eff "We're all here for the same reason."
    show eff neutral at right
    pov "..."
    show eff confused at right
    mis "..."
    show eff bored at right
    eff "..."
    show pov embarrassed_talk at left
    show misc embarrassed at Position(xpos=1300)
    show eff confused at right
    pov "And that would be..?"
    show pov shocked at left
    show eff smirk_talk at right
    eff "You don't have to be shy with Miss Allaway, [povname]."
    show misc shocked at Position(xpos=1300)
    eff "I thought you two were close, I've seen you guys alone together before."
    show misc shocked_talk at Position(xpos=1300)
    show eff smirk at right
    mis "You have?!"
    show pov sad at left
    show misc sad at Position(xpos=1300)
    show eff smirk_talk at right
    eff "Don't worry, your secret is safe with me."
    show misc sad_talk at Position(xpos=1300)
    show eff neutral at right
    mis "Effie! Why is this the first I'm hearing of this?"
    show pov confused at left
    show misc angry at Position(xpos=1300)
    show eff embarrassed_talk at right
    eff "I just didn't think it was something that needed to be brough up until now."
    show pov embarrassed at left
    show misc sad at Position(xpos=1300)
    show eff embarrassed at right
    pov "..."
    show eff embarrassed_talk at right
    eff "C'mon, you two."
    show eff smirk_talk at right
    eff "Let's get our asses inside."
    show pov shocked at left
    show misc shocked at Position(xpos=1300)
    show eff smirk_talk at right
    eff "I can feel the sexual tension between all of us and honestly, I'm so fucking wet right not."
    show misc sad_talk at Position(xpos=1300)
    show eff confused at right
    mis "I-"
    show pov embarrassed_talk at left
    show misc sad at Position(xpos=1300)
    pov "Miss?"
    show pov embarrassed at left
    show misc sad_talk at Position(xpos=1300)
    mis "[povname]?"
    show pov embarrassed_talk at left
    show misc sad at Position(xpos=1300)
    pov "I really don't know what to say but..."
    show pov neutral_talk at left
    show misc shocked at Position(xpos=1300)
    show eff smirk at right
    pov "Let's get fucking naked!"
    show pov shocked at left
    show misc angry_talk at Position(xpos=1300)
    show eff shocked at right
    mis "Not so fucking loud you too! The neighbours will hear-"
    show pov embarrassed at left
    show misc bored at Position(xpos=1300)
    show eff smirk_talk at right
    eff "It'll be a lot safer to scream and moan in my room, trust."
    show pov shocked at left
    show misc sad_talk at Position(xpos=1300)
    show eff smirk at right
    mis "I know, I know, you're right."
    show misc embarrassed at Position(xpos=1300)
    show eff smirk at right
    pov "..."
    show pov shocked_talk at left
    pov "I must be fucking dreaming but this is the best day of my life."
    scene black
    with fade
    $ renpy.pause()

    $ allawayxeffiexmceffiebed_firsttimedone = 1

    jump lbl_allawayxeffiexmc_effiebed_pre

label lbl_allawayxeffiexmc_effiebed_intro2:
    scene bg effiehouseoutside_day
    show pov neutral at left
    with dissolve
    show eff neutral_talk at right
    with dissolve
    pov "Yo!"
    show pov smirk_talk at left
    show eff neutral at right
    pov "Finished early again today?"
    show pov neutral at left
    show eff embarrassed_talk at right
    eff "Yup, another quiet day with not a lot of customers."
    show pov confused_talk at left
    show eff neutral at right
    pov "Is Miss Allaway coming?"
    show pov smirk at left
    show eff smirk_talk at right
    eff "How do you know?"
    show pov smirk_talk at left
    show eff smirk at right
    pov "Just an educated guess."
    show pov neutral at left
    show eff confused_talk at right
    eff "Yeah, she's always a little late."
    show pov neutral_talk at left
    show eff shocked at right
    pov "Ooh- speak of the devil."
    show pov neutral at left
    show misc embarrassed_talk at Position(xpos=1300) zorder 1
    show eff smirk at right
    mis "Hey, you two. Sorry if I kept you waiting."
    mis "Wanted to make sure no one was around the area to spot us."
    show misc bored at Position(xpos=1300)
    show eff smirk_talk at right
    eff "And why would you care about that, Miss Allaway?"
    eff "We're just having a private tutoring session to work on our team assignment."
    show pov embarrassed at left
    show misc bored_talk at Position(xpos=1300)
    show eff smirk at right
    mis "I'm here aren't I? Don't sass me girl."
    show pov smirk_talk at left
    show misc embarrassed at Position(xpos=1300)
    show eff neutral at right
    pov "Why don't we take this inside before it turns into a full on cat-fight."

    jump lbl_allawayxeffiexmc_effiebed_0

####################
## Missionary Pre
label lbl_allawayxeffiexmc_effiebed_pre:
    if hscene_xray == 0:
        scene bg allawayxeffiexmc_effiebed_1
        with fade
    else:
        scene bg allawayxeffiexmc_effiebed_1_0
        with fade

    jump lbl_allawayxeffiexmc_effiebed_0

label lbl_allawayxeffiexmc_effiebed_0:
    #$ allawayxeffiexmc_effiebed_counter = 0
    if hscene_xray == 0:
        jump lbl_allawayxeffiexmc_effiebed_1
    else:
        jump lbl_allawayxeffiexmc_effiebed_1_0

####################
## Stage 1
label lbl_allawayxeffiexmc_effiebed_1:
    scene img_allawayxeffiexmc_effiebed_stage_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_2
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_2
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_1

image img_allawayxeffiexmc_effiebed_stage_1:
    "bg allawayxeffiexmc_effiebed_1"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_2"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_3"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_6"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_allawayxeffiexmc_effiebed_1_0:
    scene img_allawayxeffiexmc_effiebed_stage_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_2_0
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_2_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_1_0

image img_allawayxeffiexmc_effiebed_stage_1_0:
    "bg allawayxeffiexmc_effiebed_1_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_2_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_3_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_6_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_allawayxeffiexmc_effiebed_2:
    scene img_allawayxeffiexmc_effiebed_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_3
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_2

image img_allawayxeffiexmc_effiebed_stage_2:
    "bg allawayxeffiexmc_effiebed_1"
    pause 0.1
    "bg allawayxeffiexmc_effiebed_2"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_6"
    pause 0.1
    repeat

####################
## Stage 2 XRAY
label lbl_allawayxeffiexmc_effiebed_2_0:
    scene img_allawayxeffiexmc_effiebed_stage_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_cum
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_3_0
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_2_0

image img_allawayxeffiexmc_effiebed_stage_2_0:
    "bg allawayxeffiexmc_effiebed_1_0"
    pause 0.1
    "bg allawayxeffiexmc_effiebed_2_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_6_0"
    pause 0.1
    repeat

####################
## Stage 3
label lbl_allawayxeffiexmc_effiebed_3:
    scene img_allawayxeffiexmc_effiebed_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_3

image img_allawayxeffiexmc_effiebed_stage_3:
    "bg allawayxeffiexmc_effiebed_6"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5"
    pause 0.2
    repeat

####################
## Stage 3 XRAY
label lbl_allawayxeffiexmc_effiebed_3_0:
    scene img_allawayxeffiexmc_effiebed_stage_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_cum
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allawayxeffiexmc_effiebed_3_0

image img_allawayxeffiexmc_effiebed_stage_3_0:
    "bg allawayxeffiexmc_effiebed_6_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_4_0"
    pause 0.2
    "bg allawayxeffiexmc_effiebed_5_0"
    pause 0.2
    repeat

####################
## Missionary Cum
label lbl_allawayxeffiexmc_effiebed_cum:
    jump lbl_allawayxeffiexmc_effiebed_cum_2

label lbl_allawayxeffiexmc_effiebed_cum_2:
    #if hscene_xray == 0:
    #    scene bg allawayxeffiexmc_effiebed_1
    #else:
    #    scene bg allawayxeffiexmc_effiebed_1_0
    call screen scr_allawayxeffiexmc_effiebed_cum_2

screen scr_allawayxeffiexmc_effiebed_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allawayxeffiexmc_effiebed_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allawayxeffiexmc_effiebed_cumchoice")

label lbl_allawayxeffiexmc_effiebed_cumchoice:
    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_allawayxeffiexmc_effiebed_cumin
            else:
                jump lbl_allawayxeffiexmc_effiebed_cumin_0
        "Cum on them":
            jump lbl_allawayxeffiexmc_effiebed_cumout

####################
## Cum In
label lbl_allawayxeffiexmc_effiebed_cumin:
    scene bg allawayxeffiexmc_effiebed_8_0
    $ renpy.pause(1.5,hard=True)
    show bg allawayxeffiexmc_effiebed_8_1
    $ renpy.pause(0.4,hard=True)
    show bg allawayxeffiexmc_effiebed_8_2
    $ renpy.pause(0.4,hard=True)
    show bg allawayxeffiexmc_effiebed_8_3
    $ renpy.pause(0.4,hard=True)
    show bg allawayxeffiexmc_effiebed_8_4
    $ renpy.pause(0.4,hard=True)
    show bg allawayxeffiexmc_effiebed_8_5
    $ renpy.pause(1,hard=True)
    mis "Ohhh- fuck..."
    mis "Oh- sh-shit..."
    pov "{i}*Pants*{/i}"
    eff "Fuck that looks so fucking hot..."
    eff "Mmm.. I'm so jealous..."
    pov "Cumming in your pussy feels so good, Miss."
    mis "{i}*Pants*{/i} Oh God.. my legs..."
    mis "I feel so full of your cum, [povname]."
    eff "It's seeped out, Miss Allaway."
    eff "[povname] really is the god of cum."
    pov "You girls are making me blush."
    eff "Hehehe~"
    mis "I'm such a mess right now."
    mis "Effie you weren't kidding about being dripping wet, my tongue couldn't keep up."
    pov "You both did great, mind cleaning me up Effie?"
    mis "No- don't pull out."
    mis "Maybe I'm crazy but I feel really comfortable like this."
    eff "Then keep on licking, Miss."
    scene black
    with fade
    $ renpy.pause()
    "After chilling together until the sun goes down..."
    scene bg effiehouseoutside_night
    with fade

    $ gtime = 2

    jump lbl_effiehouseoutside_night_setup

####################
## Cum In XRAY
label lbl_allawayxeffiexmc_effiebed_cumin_0:
    scene bg allawayxeffiexmc_effiebed_2
    $ renpy.pause(0.2,hard=True)
    show bg allawayxeffiexmc_effiebed_3
    $ renpy.pause(0.2,hard=True)
    show bg allawayxeffiexmc_effiebed_7_0
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_8
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_9
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_10
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_11
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_7_12
    $ renpy.pause(0.3,hard=True)
    mis "Ohhh- fuck..."
    mis "Oh- sh-shit..."
    pov "{i}*Pants*{/i}"
    eff "Fuck that looks so fucking hot..."
    eff "Mmm.. I'm so jealous..."
    pov "Cumming in your pussy feels so good, Miss."
    mis "{i}*Pants*{/i} Oh God.. my legs..."
    mis "I feel so full of your cum, [povname]."
    eff "It's seeped out, Miss Allaway."
    eff "[povname] really is the god of cum."
    pov "You girls are making me blush."
    eff "Hehehe~"
    mis "I'm such a mess right now."
    mis "Effie you weren't kidding about being dripping wet, my tongue couldn't keep up."
    pov "You both did great, mind cleaning me up Effie?"
    mis "No- don't pull out."
    mis "Maybe I'm crazy but I feel really comfortable like this."
    eff "Then keep on licking, Miss."
    scene black
    with fade
    $ renpy.pause()
    "After chilling together until the sun goes down..."
    scene bg effiehouseoutside_night
    with fade

    $ gtime = 2

    jump lbl_effiehouseoutside_night_setup

####################
## Cum Out
label lbl_allawayxeffiexmc_effiebed_cumout:
    pov "Ahh- I'm cumming-"
    scene bg allawayxeffiexmc_effiebed_9_0
    $ renpy.pause(0.6,hard=True)
    show bg allawayxeffiexmc_effiebed_9_1
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_2
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_3
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_4
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_5
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_6
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_7
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_8
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_9
    $ renpy.pause(0.3,hard=True)
    show bg allawayxeffiexmc_effiebed_9_10
    $ renpy.pause(0.8,hard=True)
    eff "[povname]!"
    mis "Holy shit, why is there so much-?"
    eff "You almost got me in the face-"
    pov "{i}*Pants*{/i}"
    pov "Guys-"
    pov "Can you-"
    pov "I just busted my entire load all over you-"
    pov "{i}*Pants*{/i} Give me some fucking slack."
    eff "Hmm.."
    mis "My pussy is completely covered with your cum..."
    eff "And how much I just want to bury my face and push it inside you with my tongue, Miss Allaway."
    mis "Don't tease me like that Effie.."
    mis "If you're gonna do it, just do it."
    mis "You're driving me crazy."
    pov "Mind cleaning me up, Effie?"
    eff "Bitch please, your cock looks spotless apart from that glistening highlight."
    mis "Here's an idea, [povname]. Why don't you take your mouth and clean both of us up."
    pov "No, thanks. I'll just go ahead and quickly grab some tissues."
    eff "Ughh- use the old towel, [povname]. Tissues won't cut this."
    pov "Hold tight, you don't want it getting everywhere."
    show bg allawayxeffiexmc_effiebed_9_11
    with dissolve
    mis "Effie? Can you see if it's going inside me."
    eff "Miss Allaway, there's no doubt it's going in."
    mis "Damn, can I borrow a pill?"
    scene black
    with fade
    $ renpy.pause()
    "A few towels later..."
    scene bg effiehouseoutside_night
    with fade

    $ gtime = 2

    jump lbl_effiehouseoutside_night_setup
