####################
## Lashley Ribbon Mating Press
label lbl_lashley_ribbon_mating_press:
    ## PRE STORY
    scene black
    with fade
    $ renpy.pause()
    "At the door-"
    scene bg lashley_ribbonmatingpress_door_1
    with fade
    pov "Director Lashley!"
    pov "I didn't expect you to be right outside my house already."
    pov "Did we schedule a bible study session that I forgot about?"
    show bg lashley_ribbonmatingpress_door_2
    pri "Oh- no, [povname]. This was a last minute thing."
    show bg lashley_ribbonmatingpress_door_3
    pri "I woke up this morning with a single strong urge to be here."
    pri "I felt something was off, I sensed that you had something you're struggling with."
    show bg lashley_ribbonmatingpress_door_4
    pri "And I thought to myself, coming here to help you as important as attending church."
    pri "I couldn't just abandon one of my student to fulfil my own needs."
    show bg lashley_ribbonmatingpress_door_3
    pri "That isn't what God is about, it's about praising him through helping others."
    pri "So- with all that said."
    show bg lashley_ribbonmatingpress_door_2
    pri "I have a surprise for you that might help peak your interest."
    pri "I know you aren't a regular church-goer so I figured I needed something to grab your attention."
    show bg lashley_ribbonmatingpress_door_5
    with hpunch
    $ renpy.pause()
    pov "Oh my God! Di-"
    show bg lashley_ribbonmatingpress_door_6
    pri "[povname]! What did we talk about using the Lord's name in vain."
    show bg lashley_ribbonmatingpress_door_7
    pov "I'm sorry- I just wasn't prepared for that."
    show bg lashley_ribbonmatingpress_door_8
    pri "Well? Are you going to keep gawking me or should we start our little spiritual healing session?"
    show bg lashley_ribbonmatingpress_door_5
    pov "Come right in!"

label lbl_lashley_ribbon_mating_press_0:
    jump lbl_lashley_ribbon_mating_press_1

####################
## Stage 1
label lbl_lashley_ribbon_mating_press_1:
    scene img_lashley_ribbon_mating_press_stage_1
    with fade

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_ribbon_mating_press_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_ribbon_mating_press_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_ribbon_mating_press_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_ribbon_mating_press_1

image img_lashley_ribbon_mating_press_stage_1:
    "bg lashley_ribbonmatingpress_1"
    pause 0.2
    "bg lashley_ribbonmatingpress_2"
    pause 0.2
    "bg lashley_ribbonmatingpress_3"
    pause 0.2
    "bg lashley_ribbonmatingpress_4"
    pause 0.2
    "bg lashley_ribbonmatingpress_5"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_lashley_ribbon_mating_press_2:
    scene img_lashley_ribbon_mating_press_stage_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_lashley_ribbon_mating_press_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_ribbon_mating_press_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_ribbon_mating_press_2

image img_lashley_ribbon_mating_press_stage_2:
    "bg lashley_ribbonmatingpress_1"
    pause 0.2
    "bg lashley_ribbonmatingpress_2"
    pause 0.2
    "bg lashley_ribbonmatingpress_4"
    pause 0.2
    "bg lashley_ribbonmatingpress_5"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_lashley_ribbon_mating_press_3:
    scene img_lashley_ribbon_mating_press_stage_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_lashley_ribbon_mating_press_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_lashley_ribbon_mating_press_3

image img_lashley_ribbon_mating_press_stage_3:
    "bg lashley_ribbonmatingpress_1"
    pause 0.2
    "bg lashley_ribbonmatingpress_4"
    pause 0.1
    "bg lashley_ribbonmatingpress_5"
    pause 0.2
    repeat

####################
## Menu
label lbl_lashley_ribbon_mating_press_menu:
    call screen scr_lashley_ribbon_mating_press_menu

screen scr_lashley_ribbon_mating_press_menu():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashley_ribbon_mating_press_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_lashley_ribbon_mating_press_cum")

####################
## Cum
label lbl_lashley_ribbon_mating_press_cum:
    if skill_sta <= 7:
        scene img_lashley_ribbon_mating_press_stage_1
    elif skill_sta <= 14:
        scene img_lashley_ribbon_mating_press_stage_2
    else:
        scene img_lashley_ribbon_mating_press_stage_3
    pov "I- I- I'm gonna-"
    pri "Yes, [povname]. Release your sins."
    pri "{i}*Pants*{/i} I can take it all for you."
    pri "I can free you from your shackles."
    pri "I can be your saviour to fill and defile."
    pri "{i}*Moans*{/i}"
    pri "Don't worry- I can take it all."
    pri "Don't- {i}*gasps*{/i} -pull out of me-"
    pri "Just let it all out."
    pov "Euunngghh-!"
    scene bg lashley_ribbonmatingpress_4
    $ renpy.pause(0.8,hard=True)
    show bg lashley_ribbonmatingpress_6_1
    $ renpy.pause(0.3,hard=True)
    show bg lashley_ribbonmatingpress_6_2
    $ renpy.pause(0.3,hard=True)
    show bg lashley_ribbonmatingpress_6_3
    $ renpy.pause(0.3,hard=True)
    show bg lashley_ribbonmatingpress_6_4
    $ renpy.pause(0.3,hard=True)
    show bg lashley_ribbonmatingpress_6_5
    $ renpy.pause(0.3,hard=True)
    show bg lashley_ribbonmatingpress_6_6
    $ renpy.pause(0.3,hard=True)
    show bg lashley_ribbonmatingpress_6_7
    $ renpy.pause(0.3,hard=True)
    show bg lashley_ribbonmatingpress_6_8
    $ renpy.pause(1,hard=True)
    pov "{i}*Pants*{/i}"
    pri "{i}*Moans*{/i}"
    pov "Fu--"
    pri "Ah-!"
    pov "Fuu---n times-!"
    pov "{i}*Huff*{/i} Wouldn't you agree?"
    pri "Hm- you did amazing, [povname]."
    pri "Don't you feel better?"
    pov "I really do."
    pri "I'm glad to hear. It's unhealthy to keep pent up frustration."
    pri "It consumes your mind and taints your reality."
    pri "A clear head, means a clear vision of the Lord."
    pov "Heh- yeah. Sure, amen to that."
    pov "What about you, are you going to be okay after I- y'know- in you?"
    pri "Don't worry about me, [povname]. I'm protected and safe, always am."
    pri "Spiritually and physically, I know you're about to ask."
    pov "When- can we do this again?"
    pri "Addiction is also a sin, [povname]. While I am happy to be here for you, you shouldn't rely on me too heavily."
    pri "Continue to pray and keep a level head."
    pov "{i}*Exhale*{/i} Alright- noted. Until next time then."
    pri "Let's clean up. Bless your heart, [povname]."

    jump lbl_mylivingroom_day_setup
