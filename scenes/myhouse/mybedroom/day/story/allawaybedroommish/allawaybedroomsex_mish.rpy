####################
## Allaway Bedroom Sex
default allawaybedroomsex_sneakherin = 0
#default allaway_bedroom_mish_counter = 0

label lbl_allaway_bedroom_sex:

    $ allawaybedroomsex_sneakherin = 0

    jump lbl_allaway_bedroom_mish

####################
## Missionary Pre
label lbl_allaway_bedroom_mish:
    scene bg allawaybedroommish_1
    with fade
    $ renpy.pause(0.4, hard=True)
    show bg allawaybedroommish_2
    $ renpy.pause(0.2, hard=True)
    show bg allawaybedroommish_3
    $ renpy.pause(0.2, hard=True)
    show bg allawaybedroommish_4
    $ renpy.pause(0.2, hard=True)
    mis "Ah- Not too fast, [povname]."
    mis "Go slow."
    mis "I want to feel all of you deep inside me."
    show bg allawaybedroommish_2
    pov "Anything you say, Miss Allaway."
    show bg allawaybedroommish_1
    mis "Mm... I love it when you still call me 'Miss Allaway'."
    show bg allawaybedroommish_2
    pov "I just can't believe I'm fucking my teacher in my very own room."
    show bg allawaybedroommish_3
    mis "I can't fucking believe either."
    show bg allawaybedroommish_4
    mis "Fuck my brains out, or I'll fail you."
    show bg allawaybedroommish_2
    pov "Looks like I have no choice but to do as you say."

    jump lbl_allaway_bedroom_mish_0

label lbl_allaway_bedroom_mish_0:
    #$ allaway_bedroom_mish_counter = 0
    if hscene_xray == 0:
        jump lbl_allaway_bedroom_mish_1
    else:
        #jump lbl_allaway_bedroom_mish_1_0 ## XRAY NOT AVAILABLE YET#
        jump lbl_allaway_bedroom_mish_1

####################
## Missionary Stage 1
label lbl_allaway_bedroom_mish_1:
    scene img_allaway_bedroom_mish_stage_1
    #$ allaway_bedroom_mish_counter += 1
    #show bg allawaybedroommish_1
    #$ renpy.pause(0.2,hard=True)
    #show bg allawaybedroommish_2
    #$ renpy.pause(0.2,hard=True)
    #show bg allawaybedroommish_3
    #$ renpy.pause(0.2,hard=True)
    #show bg allawaybedroommish_4
    #$ renpy.pause(0.2,hard=True)
    #show bg allawaybedroommish_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 7 and allaway_bedroom_mish_counter == 4:
    #    jump lbl_allaway_bedroom_mish_cum
    #elif skill_sta <= 14 and allaway_bedroom_mish_counter == 6:
    #    jump lbl_allaway_bedroom_mish_2
    #elif skill_sta <= 20 and allaway_bedroom_mish_counter == 8:
    #    jump lbl_allaway_bedroom_mish_2
    #else:
    #    jump lbl_allaway_bedroom_mish_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_bedroom_mish_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_bedroom_mish_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_bedroom_mish_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_bedroom_mish_1

image img_allaway_bedroom_mish_stage_1:
    "bg allawaybedroommish_1"
    pause 0.2
    "bg allawaybedroommish_2"
    pause 0.2
    "bg allawaybedroommish_3"
    pause 0.2
    "bg allawaybedroommish_4"
    pause 0.2
    "bg allawaybedroommish_2"
    pause 0.2
    repeat

####################
## Missionary Stage 2
label lbl_allaway_bedroom_mish_2:
    scene img_allaway_bedroom_mish_stage_2
    #$ allaway_bedroom_mish_counter += 1
    #show bg allawaybedroommish_1
    #$ renpy.pause(0.2,hard=True)
    #show bg allawaybedroommish_2
    #$ renpy.pause(0.2,hard=True)
    #show bg allawaybedroommish_4
    #$ renpy.pause(0.2,hard=True)
    #show bg allawaybedroommish_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and allaway_bedroom_mish_counter == 14:
    #    jump lbl_allaway_bedroom_mish_cum
    #elif skill_sta <= 20 and allaway_bedroom_mish_counter == 16:
    #    jump lbl_allaway_bedroom_mish_3
    #else:
    #    jump lbl_allaway_bedroom_mish_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_allaway_bedroom_mish_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_bedroom_mish_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_bedroom_mish_2

image img_allaway_bedroom_mish_stage_2:
    "bg allawaybedroommish_1"
    pause 0.2
    "bg allawaybedroommish_2"
    pause 0.2
    "bg allawaybedroommish_4"
    pause 0.2
    "bg allawaybedroommish_2"
    pause 0.2
    repeat

####################
## Missionary Stage 3
label lbl_allaway_bedroom_mish_3:
    scene img_allaway_bedroom_mish_stage_3
    #$ allaway_bedroom_mish_counter += 1
    #show bg allawaybedroommish_1
    #$ renpy.pause(0.1,hard=True)
    #show bg allawaybedroommish_4
    #$ renpy.pause(0.1,hard=True)
    #show bg allawaybedroommish_2
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and allaway_bedroom_mish_counter == 24:
    #    jump lbl_allaway_bedroom_mish_cum
    #else:
    #    jump lbl_allaway_bedroom_mish_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_allaway_bedroom_mish_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_allaway_bedroom_mish_3

image img_allaway_bedroom_mish_stage_3:
    "bg allawaybedroommish_1"
    pause 0.1
    "bg allawaybedroommish_4"
    pause 0.1
    "bg allawaybedroommish_2"
    pause 0.2
    repeat

####################
## Missionary Cum
label lbl_allaway_bedroom_mish_cum:
    jump lbl_allaway_bedroom_mish_cum_2

label lbl_allaway_bedroom_mish_cum_2:
    #if hscene_xray == 0:
    #    scene bg allawaybedroommish_1
    #else:
        #scene bg mombedroomhscene_mish_13_0
    #    scene bg allawaybedroommish_1
    call screen scr_allaway_bedroom_mish_cum_2

screen scr_allaway_bedroom_mish_cum_2():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_bedroom_mish_0")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_allaway_bedroom_mish_cumchoice")

label lbl_allaway_bedroom_mish_cumchoice:

    menu:
        "Cum inside":
            if hscene_xray == 0:
                jump lbl_allaway_bedroom_mish_cumin
            else:
                #jump lbl_allaway_bedroom_mish_cumin_0
                jump lbl_allaway_bedroom_mish_cumin
        "Cum on her":
            jump lbl_allaway_bedroom_mish_cumout

####################
## Missionary Cum In
label lbl_allaway_bedroom_mish_cumin:
    scene bg allawaybedroommish_2
    $ renpy.pause(0.2,hard=True)
    show bg allawaybedroommish_3
    $ renpy.pause(0.6,hard=True)
    show bg allawaybedroommish_4
    $ renpy.pause(0.6,hard=True)
    show bg allawaybedroommish_3
    $ renpy.pause(0.6,hard=True)
    show bg allawaybedroommish_4
    $ renpy.pause(0.6,hard=True)
    show bg allawaybedroommish_3
    $ renpy.pause(0.6,hard=True)
    show bg allawaybedroommish_4
    $ renpy.pause(0.6,hard=True)
    mis "Oh my.. did you... why..."
    mis "You weren't even wearing- {i}*pants*{/i}"
    mis "-a condom- {i}*pants*{/i}"
    pov "Sorry... it's kind of a habit."
    mis "..."
    mis "I'm gonna have to get a Plan B pill on the way back."
    pov "Did- did I... does that mean I failed the class?"
    mis "Hehe, don't worry, [povname]. You passed with flying colours."
    pov "Awesome, {i}*pants*{/i}"
    pov "Double awesome."
    scene black
    with fade
    $ renpy.pause(1.5)
    "After cleaning up..."

    jump lbl_allaway_bedroom_mish_post

####################
## Missionary Cum Out
label lbl_allaway_bedroom_mish_cumout:
    scene bg allawaybedroommish_5_0
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

    #jump lbl_mybedroom_night_sleep
    scene black
    with fade
    $ renpy.pause(1.5)
    "After cleaning up..."

    jump lbl_allaway_bedroom_mish_post

####################
## Missionary Next
label lbl_allaway_bedroom_mish_post:
    scene bg mybedroom_day
    with fade
    show povn neutral at left
    with dissolve
    show misn confused at right
    with dissolve
    mis "..."
    show povn confused at left
    show misn confused_talk at right
    mis "So... how do you expect to sneak me out?"
    show povn confused at left
    show misn confused at right
    pov "..."
    show povn confused_talk at left
    show misn bored at right
    pov "Uhm..."
    show povn embarrassed_talk at left
    pov "Out the window...?"
    show povn embarrassed at left
    show misn bored_talk at right
    mis "Are you serious?"
    mis "We're on the second story."
    show povn confused_talk at left
    show misn bored at right
    pov "Uh..."
    show povn smirk_talk at left
    show misn confused at right
    pov "Okay, here's the plan. You get your pantyhose back on and I'll go check outside to see if the coast is clear."
    show povn confused at left
    show misn confused_talk at right
    mis "Don't you need to get some pants on as well?"
    mis "Or is your family like... comfortable with the nudity thing?"
    if mum_points >= 7 or sister_points >= 7:
        show povn embarrassed_talk at left
        show misn confused at right
        pov "Haha... that's funny, what makes you-"
        pov "What? Nope. Just a normal, ordinary, family with nothing weird going on."
    else:
        show povn smirk_talk at left
        show misn confused at right
        pov "Haha, right; pants. No, not that close."
        show povn neutral_talk at left
        show misn neutral at right
        pov "New plan; pants first then recon."
    scene black
    with fade
    $ renpy.pause(1.5)
    "After getting dressed at checking the house for family members."
    if 0 <= date <= 4 or 10 <= date <= 14 or 20 <= date <= 24 or date == 30:
        scene bg mybedroom_day
        with fade
        show pov neutral_talk at left
        with dissolve
        show mis neutral at right
        with dissolve
        pov "Good news, the coast is clear."
        show mis confused at right
        pov "At least on the way out. They might be somewhere else for now."
        show pov shocked_talk at left
        show mis bored at right
        pov "But you gotta be quick. I suggest just cutting straight out the backyard from the kitchen."
        show pov shocked at left
        show mis angry_talk at right
        mis "At least come with me, you asshole."
        mis "Don't just tell me what to do while you hide here in your room."
        show pov embarrassed_talk at left
        show mis bored at right
        pov "Alright, alright. {i}*Sigh*{/i} Let's go."
        scene black
        with fade
        $ renpy.pause()
        "After sneaking Miss Allaway out the backyard..."
        if mowed_lawn == 1:
            scene bg mydiningroom_day
            with fade
        else:
            scene bg mydiningroom_day_grassy
            with fade

        jump lbl_mydiningroom_day_setup

    else:
        scene bg mybedroom_day
        with fade
        show pov embarrassed_talk at left
        with dissolve
        show mis shocked at right
        with dissolve
        pov "Bad... news... there's people in the house."
        show pov sad_talk at left
        pov "And it'll be impossible to get you outside."
        show pov confused_talk at left
        show mis angry at right
        pov "You're going to have to either jump out the window or stay low in here for a bit."
        show pov sad at left
        show mis angry_talk at right
        mis "You've got to be shitting me, [povname]. I have to get back to university!"
        show pov embarrassed_talk at left
        show mis angry at right
        pov "I know, I know..."
        show pov sad_talk at left
        pov "Fuck..."
        show pov embarrassed at left
        show mis sad_talk at right
        mis "{i}*Sigh*{/i}"
        show pov smirk_talk at left
        show mis bored at right
        pov "Wanna get naked again?"
        show pov embarrassed at left
        mis "..."
        show pov sad at left
        show mis bored_talk at right
        mis "I hate you."
        show pov smirk at left
        mis "But yeah, might as well."
        if missallaway_points >= 1:
            $ missallaway_points -= 1
        else:
            $ missallaway_points = 0
        $ renpy.notify("Relationship with Miss Allaway Decreased")
        jump lbl_mybedroom_day_setup
