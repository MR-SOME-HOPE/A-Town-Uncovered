## Director Office Chair Sex
default principalofficechairsex_firsttimedone = 0
#default principal_office_chair_sex_counter = 0

label lbl_principal_office_chair_sex:
    if principalofficechairsex_firsttimedone == 0:
        pass
    else:
        jump lbl_principal_office_chair_sex_intro2

    scene bg principaloffice_day
    show pov neutral_talk at left
    with dissolve
    show pri neutral at right
    with dissolve
    pov "Hey, I was wondering if you could help me decipher a dream I had last night."
    show pov neutral at left
    show pri neutral_talk at right
    pri "Everything happens for a reason, even when it hasn't happened yet."
    show pri neutral_talk at right
    pri "What did you see in your dreams last night, [povname]?"
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "Well, it was between you and me. We were... naked."
    show pov embarrassed at left
    show pri shocked_talk at right
    pri "Naked?! Um-"
    show pov shocked_talk at left
    show pri shocked at right
    pov "In God's intended state, shameless."
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "Oh, of course. That is very true."
    show pov embarrassed at left
    pri "Please, carry on."
    show pov embarrassed_talk at left
    show pri embarrassed at right
    pov "Y-yeah! It was actually a re-imagined version of Adam and Eve instead it was- us..."
    show pov neutral at left
    show pri embarrassed_talk at right
    pri "I see... I'm going to need a- little more... detail."
    show pov embarrassed_talk at left
    show pri confused at right
    pov "Uh- hehe.. you know how God is with his creation."
    show pov embarrassed at left
    show pri confused_talk at right
    pri "Uh-huh?"
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "How as essentially living beings, we have to reproduce and start populating the word with the image of God."
    show pov embarrassed_talk at left
    show pri shocked_talk at right
    pri "Oh- wow.. um.. okay."
    show pov embarrassed at left
    show pri embarrassed_talk at right
    pri "That's- {i}*gulp*{/i} I wasn't expecting it to go there, [povname]."
    show pov neutral at left
    pri "Nevertheless, God gave us dreams for a reason and I'm sure there's a valid reason I was in yours with you."
    show pov smirk at left
    pri "Uh- naked... and.. that thing.."
    show pov embarrassed_talk at left
    show pri sad at right
    pov "I couldn't stop thinking about it's meaning."
    show pov sad_talk at left
    pov "I'm sure he's guiding me towards-"
    show pov embarrassed_talk at left
    show pri embarrassed at right
    pri "..."
    show pri shocked at right
    pov "You."
    show pov embarrassed at left
    show pri shocked_talk at right
    pri "W-why me?"
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "Because-"
    show pov neutral_talk at left
    show pri embarrassed at right
    pov "God loves you."
    show pov embarrassed_talk at left
    pov "God loves every one of his children."
    show pri shocked at right
    pov "We should... make more love."
    show pov shocked at left
    show pri sad_talk at right
    pri "[povname]! That is-"
    show pov shocked_talk at left
    show pri sad at right
    pov "You said it yourself, God put these types of dream in my head for a reason."
    show pov sad_talk at left
    pov "If it's not for us to praise him the way he wants us to, then what..?"
    show pov sad at left
    show pri sad_talk at right
    pri "I- He- You- I- I don't know... that is not the type of-"
    show pov confused at left
    pri "That is a sin."
    show pov smirk_talk at left
    show pri sad at right
    pov "He works in mysterious ways."
    show pov embarrassed at left
    pri "..."
    show pov embarrassed_talk at left
    show pri shocked at right
    pov "Let's just do it, Director Lashley."
    show pov shocked_talk at left
    show pri confused at right
    pov "God has a heart as big as... well, as big as He himself."
    show pov neutral_talk at left
    show pri embarrassed at right
    pov "I'm sure we can ask for forgiveness and state that it's an honest mistake."
    show pov embarrassed at left
    show pri sad_talk at right
    pri "I-"
    show pov smirk_talk at left
    show pri sad at right
    pov "One could say it's just as bad as to disobey him by not going through with this."
    pov "Either way, we must follow our animalistic instincts. The one that God once gave us to thrive."
    show pov smirk at left
    pri "..."
    show pov confused at left
    show pri sad_talk at right
    pri "Y-"
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "You're right, [povname]..."
    show pov neutral at left
    pri "You're absolutely right."
    show pov embarrassed at left
    show pri shocked_talk at right
    pri "2 John 1:16 says it so."
    show pov embarrassed_talk at left
    show pri neutral at right
    pov "Exactly... John 1:16. That verse. I love that- that verse."
    show pov embarrassed at left
    show pri neutral at right
    pri "..."
    show pov smirk at left
    show pri embarrassed_talk at right
    pri "Please go ahead and lock the door, [povname]."
    scene black
    with fade
    $ renpy.pause(1.5)

    $ principalofficechairsex_firsttimedone = 1

    jump lbl_principal_office_chair_sex_pre

label lbl_principal_office_chair_sex_intro2:
    scene bg principaloffice_day
    show pov embarrassed_talk at left
    with dissolve
    show pri neutral at right
    with dissolve
    pov "Hey, Director Lashley?"
    show pov embarrassed at left
    show pri neutral_talk at right
    pri "Yes, [povname]. How can I help you today?"
    show pov sad_talk at left
    show pri confused at right
    pov "I- had that dream again."
    show pov sad at left
    pri "..."
    show pov embarrassed at left
    show pri embarrassed_talk at right
    pri "{i}That{/i} dream?"
    show pri sad at right
    pov "Mhmm..."
    show pov neutral at left
    show pri neutral_talk at right
    pri "{i}*Inhale*{/i} Say no more, He has a reason for everything."
    show pov smirk_talk at left
    show pri embarrassed at right
    pov "Great, I'll go lock the door!"

    if hscene_xray == 0:
        scene bg principalofficechairsex_1
        with fade

        jump lbl_principal_office_chair_sex_0
    else:
        scene bg principalofficechairsex_anal_1_0
        with fade

        jump lbl_principal_office_chair_sex_0

####################
## Missionary Pre
label lbl_principal_office_chair_sex_pre:
    if hscene_xray == 0:
        scene bg principalofficechairsex_1
        with fade
    else:
        scene bg principalofficechairsex_anal_1_0
        with fade
    pri "Ah- [povname]."
    pri "It hurts..."
    pri "Take it out-!"
    pov "Anything worth doing won't come easy, Director Lashley."
    pri "Take it ou-!"
    pov "How about you pull yourself off me?"
    if hscene_xray == 0:
        show bg principalofficechairsex_1
        $ renpy.pause(0.5,hard=True)
        show bg principalofficechairsex_2
        $ renpy.pause(0.5,hard=True)
        show bg principalofficechairsex_3
        $ renpy.pause(0.5,hard=True)
        show bg principalofficechairsex_4
        $ renpy.pause(0.8,hard=True)
        show bg principalofficechairsex_1
        with vpunch
    else:
        show bg principalofficechairsex_anal_1_0
        $ renpy.pause(0.5,hard=True)
        show bg principalofficechairsex_anal_2_0
        $ renpy.pause(0.5,hard=True)
        show bg principalofficechairsex_anal_3_0
        $ renpy.pause(0.5,hard=True)
        show bg principalofficechairsex_anal_4_0
        $ renpy.pause(0.5,hard=True)
        show bg principalofficechairsex_anal_5_0
        $ renpy.pause(0.5,hard=True)
        with vpunch
    pri "Ahh-owww!"
    pri "Ow- ow- ow..."
    pri "Are you holding me down..?"
    pov "... No?"
    pov "Why would I hold you down?"
    pov "Give it some time... you'll get used to it.."
    pri "I-I don't think I want to."
    pov "Here, I'll ease you in, just leave yourself in my hands."
    pov "I promise I won't hurt you."

    jump lbl_principal_office_chair_sex_0

label lbl_principal_office_chair_sex_0:
    #$ principal_office_chair_sex_counter = 0
    if hscene_xray == 0:
        jump lbl_principal_office_chair_sex_1
    else:
        jump lbl_principal_office_chair_sex_1_0

####################
## Stage 1
label lbl_principal_office_chair_sex_1:
    scene img_principal_office_chair_sex_stage_1
    #$ principal_office_chair_sex_counter += 1
    #show bg principalofficechairsex_1
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_2
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_3
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_4
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_5
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and principal_office_chair_sex_counter == 4:
    #    jump lbl_principal_office_chair_sex_cum
    #elif skill_sta <= 14 and principal_office_chair_sex_counter == 6:
    #    jump lbl_principal_office_chair_sex_2
    #elif skill_sta <= 20 and principal_office_chair_sex_counter == 8:
    #    jump lbl_principal_office_chair_sex_2
    #else:
    #    jump lbl_principal_office_chair_sex_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_principal_office_chair_sex_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_1

image img_principal_office_chair_sex_stage_1:
    "bg principalofficechairsex_1"
    pause 0.2
    "bg principalofficechairsex_2"
    pause 0.2
    "bg principalofficechairsex_3"
    pause 0.2
    "bg principalofficechairsex_4"
    pause 0.2
    "bg principalofficechairsex_5"
    pause 0.2
    repeat

####################
## Stage 1 XRAY
label lbl_principal_office_chair_sex_1_0:
    scene img_principal_office_chair_sex_stage_1_0
    #$ principal_office_chair_sex_counter += 1
    #show bg principalofficechairsex_anal_1_0
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_anal_2_0
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_anal_3_0
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_anal_4_0
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_anal_5_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and principal_office_chair_sex_counter == 4:
    #    jump lbl_principal_office_chair_sex_cum
    #elif skill_sta <= 14 and principal_office_chair_sex_counter == 6:
    #    jump lbl_principal_office_chair_sex_2_0
    #elif skill_sta <= 20 and principal_office_chair_sex_counter == 8:
    #    jump lbl_principal_office_chair_sex_2_0
    #else:
    #    jump lbl_principal_office_chair_sex_1_0
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_principal_office_chair_sex_2_0

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_2_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_1_0

image img_principal_office_chair_sex_stage_1_0:
    "bg principalofficechairsex_anal_1_0"
    pause 0.2
    "bg principalofficechairsex_anal_2_0"
    pause 0.2
    "bg principalofficechairsex_anal_3_0"
    pause 0.2
    "bg principalofficechairsex_anal_4_0"
    pause 0.2
    "bg principalofficechairsex_anal_5_0"
    pause 0.2
    repeat

####################
## Stage 2
label lbl_principal_office_chair_sex_2:
    scene img_principal_office_chair_sex_stage_2
    #$ principal_office_chair_sex_counter += 1
    #show bg principalofficechairsex_6
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_7
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_8
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_9
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and principal_office_chair_sex_counter == 14:
    #    jump lbl_principal_office_chair_sex_cum
    #elif skill_sta <= 20 and principal_office_chair_sex_counter == 16:
    #    jump lbl_principal_office_chair_sex_3
    #else:
    #    jump lbl_principal_office_chair_sex_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_principal_office_chair_sex_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_2

image img_principal_office_chair_sex_stage_2:
    "bg principalofficechairsex_6"
    pause 0.2
    "bg principalofficechairsex_7"
    pause 0.2
    "bg principalofficechairsex_8"
    pause 0.2
    "bg principalofficechairsex_9"
    pause 0.2
    repeat

####################
## Stage 2 XRAY
label lbl_principal_office_chair_sex_2_0:
    scene img_principal_office_chair_sex_stage_2_0
    #$ principal_office_chair_sex_counter += 1
    #show bg principalofficechairsex_anal_6_0
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_anal_7_0
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_anal_8_0
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_anal_9_0
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and principal_office_chair_sex_counter == 14:
    #    jump lbl_principal_office_chair_sex_cum
    #elif skill_sta <= 20 and principal_office_chair_sex_counter == 16:
    #    jump lbl_principal_office_chair_sex_3_0
    #else:
    #    jump lbl_principal_office_chair_sex_2_0
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_principal_office_chair_sex_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_3_0

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_2_0

image img_principal_office_chair_sex_stage_2_0:
    "bg principalofficechairsex_anal_6_0"
    pause 0.2
    "bg principalofficechairsex_anal_7_0"
    pause 0.2
    "bg principalofficechairsex_anal_8_0"
    pause 0.2
    "bg principalofficechairsex_anal_9_0"
    pause 0.2
    repeat

####################
## Stage 3
label lbl_principal_office_chair_sex_3:
    scene img_principal_office_chair_sex_stage_3
    #$ principal_office_chair_sex_counter += 1
    #show bg principalofficechairsex_10
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_11
    #$ renpy.pause(0.1,hard=True)
    #show bg principalofficechairsex_12
    #$ renpy.pause(0.1,hard=True)
    #show bg principalofficechairsex_13
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and principal_office_chair_sex_counter == 24:
    #    jump lbl_principal_office_chair_sex_cum
    #else:
    #    jump lbl_principal_office_chair_sex_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_3

image img_principal_office_chair_sex_stage_3:
    "bg principalofficechairsex_10"
    pause 0.2
    "bg principalofficechairsex_11"
    pause 0.1
    "bg principalofficechairsex_12"
    pause 0.1
    "bg principalofficechairsex_13"
    pause 0.1
    repeat

####################
## Stage 3 XRAY
label lbl_principal_office_chair_sex_3_0:
    scene img_principal_office_chair_sex_stage_3_0
    #$ principal_office_chair_sex_counter += 1
    #show bg principalofficechairsex_anal_10_0
    #$ renpy.pause(0.2,hard=True)
    #show bg principalofficechairsex_anal_11_0
    #$ renpy.pause(0.1,hard=True)
    #show bg principalofficechairsex_anal_12_0
    #$ renpy.pause(0.1,hard=True)
    #show bg principalofficechairsex_anal_13_0
    #$ renpy.pause(0.1,hard=True)
    #if skill_sta <= 20 and principal_office_chair_sex_counter == 24:
    #    jump lbl_principal_office_chair_sex_cum
    #else:
    #    jump lbl_principal_office_chair_sex_3_0
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_principal_office_chair_sex_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_principal_office_chair_sex_3_0

image img_principal_office_chair_sex_stage_3_0:
    "bg principalofficechairsex_anal_10_0"
    pause 0.2
    "bg principalofficechairsex_anal_11_0"
    pause 0.1
    "bg principalofficechairsex_anal_12_0"
    pause 0.1
    "bg principalofficechairsex_anal_13_0"
    pause 0.1
    repeat

####################
## Missionary Cum
label lbl_principal_office_chair_sex_cum:
    jump lbl_principal_office_chair_sex_cum_2

label lbl_principal_office_chair_sex_cum_2:
    #if hscene_xray == 0:
    #    scene bg principalofficechairsex_1
    #else:
    #    scene bg principalofficechairsex_anal_1_0
    call screen scr_principal_office_chair_sex_cum_2

screen scr_principal_office_chair_sex_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_principal_office_chair_sex_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_principal_office_chair_sex_cumchoice")

label lbl_principal_office_chair_sex_cumchoice:
    if hscene_xray == 0:
        jump lbl_principal_office_chair_sex_cumin
    else:
        jump lbl_principal_office_chair_sex_cumin_0

####################
## Cum In
label lbl_principal_office_chair_sex_cumin:
    scene bg principalofficechairsex_14_0
    $ renpy.pause(1.5,hard=True)
    show bg principalofficechairsex_14_1
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_14_2
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_14_3
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_14_4
    $ renpy.pause(1,hard=True)
    pri "{i}*Pants*{/i}"
    pov "Mmm.. fuckk..."
    pri "Ah!"
    pri "[povname]!"
    pri "I can't believe you just said that!"
    pov "Oop- {i}*Exhale*{/i} sorry... I just-"
    pov "That felt so good."
    pri "{i}*Pants*{/i} O- of course, [povname]."
    pri "Why'd you think God made us like this."
    pri "Do you think he'd make it so... pleasurable if it was a sin...?"
    pov "No, of course not. He knows what he's doing."
    pri "{i}*Pants*{/i} Dear... Lord, thank you for this blessed day."
    pri "Thank you for- {i}*pants*{/i} [povname]- and reaching out to him in his dream."
    pri "Bless him with more pleasant dreams, I know you will. Amen."
    pov "Yeah, thanks Big G."
    pri "Let's... clean ourselves up and-"
    pri "[povname]? Let's keep this between us, okay?"
    pri "This is no one else's business except yours, mine, and the-"
    pri "Almighty."
    pov "I won't tell another soul, don't worry."
    pov "Who do you think I am."
    scene black
    with fade
    $ renpy.pause(1.5)
    "After cleaning up..."
    scene bg principaloffice_day
    with fade

    jump lbl_principaloffice_day_setup

####################
## Cum In XRAY
label lbl_principal_office_chair_sex_cumin_0:
    scene bg principalofficechairsex_anal_14_0
    $ renpy.pause(1.5,hard=True)
    show bg principalofficechairsex_anal_14_1
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_2
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_3
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_4
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_5
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_6
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_7
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_8
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_9
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_10
    $ renpy.pause(0.4,hard=True)
    show bg principalofficechairsex_anal_14_11
    $ renpy.pause(1,hard=True)
    pri "{i}*Pants*{/i}"
    pov "Mmm.. fuckk..."
    pri "Ah!"
    pri "[povname]!"
    pri "I can't believe you just said that!"
    pov "Oop- {i}*Exhale*{/i} sorry... I just-"
    pov "That felt so good."
    pri "{i}*Pants*{/i} O- of course, [povname]."
    pri "Why'd you think God made us like this."
    pri "Do you think he'd make it so... pleasurable if it was a sin...?"
    pov "No, of course not. He knows what he's doing."
    pri "{i}*Pants*{/i} Dear... Lord, thank you for this blessed day."
    pri "Thank you for- {i}*pants*{/i} [povname]- and reaching out to him in his dream."
    pri "Bless him with more pleasant dreams, I know you will. Amen."
    pov "Yeah, thanks Big G."
    pri "Let's... clean ourselves up and-"
    pri "[povname]? Let's keep this between us, okay?"
    pri "This is no one else's business except yours, mine, and the-"
    pri "Almighty."
    pov "I won't tell another soul, don't worry."
    pov "Who do you think I am."
    scene black
    with fade
    $ renpy.pause(1.5)
    "After cleaning up..."
    scene bg principaloffice_day
    with fade

    jump lbl_principaloffice_day_setup

####################
## Cum Out
label lbl_principal_office_chair_sex_cumout:
    show bg allawaybedroommish_5_0#NOTE make scene not show when replacing this line
    $ renpy.pause(0.6,hard=True)
    show bg allawaybedroommish_5_1
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_2
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_3
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_4
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_5
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_6
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_7
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_8
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_9
    $ renpy.pause(0.3,hard=True)
    show bg allawaybedroommish_5_10
    $ renpy.pause(0.8,hard=True)
    mis "Jesus Christ, [povname]. {i}*Pants*{/i} Look at the frikkin' mess you made."
    pov "I know, {i}*pants*{/i} I call it art."
    mis "Am I a canvas now?"
    pov "You're part of my masterpiece."
    mis "{i}*Pants*{/i} It's so.. hot..."
    mis "And sticky..."
    pov "{i}*Pants*{/i} Am I in trouble?"
    mis "If I give you detention, I'm afraid what I'll do with you."
    pov "Is that a threat or a proposal?"
    mis "Hehehe~ {i}*pants*{/i} Maybe both?"
    mis "Now... get off me and get me some towels. I think 5 big ones will suffice."

    jump lbl_principaloffice_day_setup
