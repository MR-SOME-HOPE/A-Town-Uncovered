## Parking with Allaway ##
default parkingwithallaway_action = 0
#default parking_with_allaway_bj_counter = 0
label lbl_parking_with_allaway:
    "She parked right outside your place and you both sit in silence."
    scene bg parkingwithallaway_1
    with fade
    $ renpy.pause(1.4,hard=True)
    show bg parkingwithallaway_2
    $ renpy.pause(0.7,hard=True)
    show bg parkingwithallaway_3
    pov "Thanks, Miss."
    show bg parkingwithallaway_4
    pov "For driving me back home, that is."
    show bg parkingwithallaway_5
    mis "You're most definitely welcome."
    mis "Thanks for spending some time with me tonight."
    show bg parkingwithallaway_6
    mis "Usually I don't mind being alone, maybe even prefer it but..."
    show bg parkingwithallaway_5
    mis "I guess my brain was ready to spend the night with someone."
    show bg parkingwithallaway_7
    pov "Who knew it would be me."
    show bg parkingwithallaway_5
    mis "It's funny you say that because I had this feeling, when I left the house that I'd run into somewhere along the way."
    show bg parkingwithallaway_8
    mis "Some weird, intuition I had."
    mis "You've been around me very frequently as of recently."
    show bg parkingwithallaway_9
    mis "Are you always this close with your teachers?"
    show bg parkingwithallaway_10

    menu:
        "I never liked any other teacher.":
            show bg parkingwithallaway_11
            pov "I never liked any other teacher."
            show bg parkingwithallaway_12
            mis "Is that because they're not as beautiful and funny as me?"
            show bg parkingwithallaway_13
            mis "Hahaha, no. I'm not beautiful and funny, just ignore me."
            show bg parkingwithallaway_14
            pov "No, you're on the right page, I just never found any of them as attractive as you, in all ways."
            show bg parkingwithallaway_15
            mis "Stop, [povname]. You're making me blush..."
        "I was always friendly with my teachers.":
            show bg parkingwithallaway_11
            pov "I was always friendly with my teachers."
            show bg parkingwithallaway_13
            mis "Friendly, like you are with me?"
            show bg parkingwithallaway_14
            pov "Oh, no. Definitely not, you're on a whole ‘nother' league."
            show bg parkingwithallaway_15
            mis "Stop, [povname]. You're making me blush..."
        "What do you mean?":
            show bg parkingwithallaway_16
            pov "What do you mean?"
            show bg parkingwithallaway_13
            mis "Y'know..."
            mis "The whole, interest in me... thing."
            show bg parkingwithallaway_15
            mis "Oh God, I'm making myself blush just thinking about it."
    show bg parkingwithallaway_17
    pov "Is it working?"
    show bg parkingwithallaway_12
    mis "You courting me?"
    show bg parkingwithallaway_7
    pov "I feel like it is."
    pov "You're very chill about the whole idea now compared to when you'd squirm and scold me."
    show bg parkingwithallaway_18
    mis "If you didn't notice, the scolding didn't work."
    show bg parkingwithallaway_8
    mis "And if you can't beat ‘em..."
    show bg parkingwithallaway_17
    pov "Join them?"
    show bg parkingwithallaway_9
    mis "I was gonna say..."
    show bg parkingwithallaway_10
    mis "..."
    show bg parkingwithallaway_12
    mis "Yeah.."
    show bg parkingwithallaway_5
    mis "And between you and me, I've grown to enjoy your company, especially tonight."
    show bg parkingwithallaway_19
    pov "I'm not coming off as desperate, am I?"
    show bg parkingwithallaway_20
    mis "A little."
    show bg parkingwithallaway_21
    mis "But I'm a little desperate myself so I guess that's another thing we have in common."
    show bg parkingwithallaway_22
    pov "You know what? I'll take that as a compliment and a win."
    show bg parkingwithallaway_23
    mis "I didn't mean it to come off as mean."
    show bg parkingwithallaway_24
    mis "I-"
    show bg parkingwithallaway_25
    mis "I do like you, [povname]. And even if you're not the exact my ideal type, the why, vulnerable feeling when I'm with you must mean something."
    show bg parkingwithallaway_26
    pov "Hmm."

    menu:
        "Do you want to come inside?":
            show bg parkingwithallaway_27
            pov "Do you want to come inside?"
            show bg parkingwithallaway_28
            mis "Oh! No.. I can't, [povname]. I'm assuming you don't live alone?"
            show bg parkingwithallaway_29
            mis "No, I... I can't risk being seen."
            show bg parkingwithallaway_30
            mis "I hope you still understand that."
            show bg parkingwithallaway_31
            pov "For sure, Miss. How silly of me to ask. I was just, trying to fill in the silence I felt coming."
            show bg parkingwithallaway_32
            mis "..."
        "I guess I best get inside.":
            show bg parkingwithallaway_27
            pov "I guess I best get inside."
            if winc == 0:
                pov "My [dadrole]s would be wondering what this old truck is parked outside our house for."
            else:
                pov "My parents would be wondering what this old truck is parked outside our house for."
            show bg parkingwithallaway_30
            mis "Oh, yeah. Sure."
            mis "I- uhm... I'll see you, [povname]."
            show bg parkingwithallaway_29
            mis "See you... in class."
            show bg parkingwithallaway_32
            mis "Mhmm!"
            mis "..."

    menu:
        "Kiss her":
            #"You lean in for a kiss and she leans in as well, shy but needy for it."
            show bg parkingwithallaway_33
            $ renpy.pause(0.7,hard=True)
            show bg parkingwithallaway_34
            $ renpy.pause(2.0,hard=True)
            show bg parkingwithallaway_35
            $ renpy.pause(1.0,hard=True)
            if missallaway_points >= 7:
                show bg parkingwithallaway_36
                menu:
                    "Let her give you a BJ":
                        jump lbl_parking_with_allaway_bj
                    "Stop her":
                        show bg parkingwithallaway_37
                        pov "Wait, as much as want it, I don't think this is the best idea right now."
                        show bg parkingwithallaway_38
                        mis "Whoa, look at you! It's like our roles have been reversed."
                        show bg parkingwithallaway_39
                        mis "... Alright, [povname]. I'll stop."
                        show bg parkingwithallaway_40
                        pov "Maybe another time, somewhere... more private?"
                        show bg parkingwithallaway_41
                        mis "Mhmm, good idea."
                        show bg parkingwithallaway_7
                        pov "G-goodnight, Miss Allaway."
                        show bg parkingwithallaway_8
                        mis "Goodnight, [povname]."
                        #"You exit the car, leaving Allaway alone, watching you until you safely get inside."
                        $ parkingwithallaway_action = 1
                        jump lbl_parking_with_allaway_end
            else:
                jump lbl_parking_with_allaway_end
        "Exit the truck":
            #"You exit the car, leaving Allaway alone, watching you until you safely get inside."
            jump lbl_parking_with_allaway_end


label lbl_parking_with_allaway_end:
    show bg parkingwithallaway_42
    $ renpy.pause(0.7,hard=True)
    show bg parkingwithallaway_43
    $ renpy.pause(1.4,hard=True)
    show bg parkingwithallaway_44
    $ renpy.pause(0.7,hard=True)
    show bg parkingwithallaway_45
    $ renpy.pause(1.4,hard=True)
    show bg parkingwithallaway_46
    $ renpy.pause(0.7,hard=True)
    $ missallaway_path = 15
    $ gtime = 3

    scene bg mylivingroom_night
    with fade
    $ renpy.pause(1.5)

    jump lbl_mylivingroom_night_setup

label lbl_parking_with_allaway_bj:
    #$ parking_with_allaway_bj_counter = 0
    scene bg parkingwithallaway_bj_1
    with fade
    $ renpy.pause(0.5,hard=True)
    show bg parkingwithallaway_bj_2
    $ renpy.pause(0.3,hard=True)
    show bg parkingwithallaway_bj_3
    $ renpy.pause(0.3,hard=True)
    show bg parkingwithallaway_bj_4
    $ renpy.pause(0.5,hard=True)
    jump lbl_parking_with_allaway_bj_1

label lbl_parking_with_allaway_bj_reset:
    #$ parking_with_allaway_bj_counter = 0
    jump lbl_parking_with_allaway_bj_1

####################
## BJ Stage 1
label lbl_parking_with_allaway_bj_1:
    scene img_parking_with_allaway_bj_stage_1
    #$ parking_with_allaway_bj_counter += 1
    #show bg parkingwithallaway_bj_1
    #$ renpy.pause(0.3,hard=True)
    #show bg parkingwithallaway_bj_2
    #$ renpy.pause(0.1,hard=True)
    #show bg parkingwithallaway_bj_3
    #$ renpy.pause(0.1,hard=True)
    #show bg parkingwithallaway_bj_4
    #$ renpy.pause(0.3,hard=True)
    #if skill_sta <= 7 and parking_with_allaway_bj_counter == 4:
    #    jump lbl_parking_with_allaway_bj_menu
    #elif skill_sta <= 14 and parking_with_allaway_bj_counter == 6:
    #    jump lbl_parking_with_allaway_bj_2
    #elif skill_sta <= 20 and parking_with_allaway_bj_counter == 8:
    #    jump lbl_parking_with_allaway_bj_2
    #else:
    #    jump lbl_parking_with_allaway_bj_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_parking_with_allaway_bj_menu
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_parking_with_allaway_bj_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_parking_with_allaway_bj_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_parking_with_allaway_bj_1

image img_parking_with_allaway_bj_stage_1:
    "bg parkingwithallaway_bj_1"
    pause 0.3
    "bg parkingwithallaway_bj_2"
    pause 0.1
    "bg parkingwithallaway_bj_3"
    pause 0.1
    "bg parkingwithallaway_bj_4"
    pause 0.3
    repeat

####################
## BJ Stage 2
label lbl_parking_with_allaway_bj_2:
    scene img_parking_with_allaway_bj_stage_2
    #$ parking_with_allaway_bj_counter += 1
    #show bg parkingwithallaway_bj_1
    #$ renpy.pause(0.3,hard=True)
    #show bg parkingwithallaway_bj_3
    #$ renpy.pause(0.1,hard=True)
    #show bg parkingwithallaway_bj_4
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 14 and parking_with_allaway_bj_counter == 14:
    #    jump lbl_parking_with_allaway_bj_menu
    #elif skill_sta <= 20 and parking_with_allaway_bj_counter == 16:
    #    jump lbl_parking_with_allaway_bj_3
    #else:
    #    jump lbl_parking_with_allaway_bj_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_parking_with_allaway_bj_menu

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_parking_with_allaway_bj_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_parking_with_allaway_bj_2

image img_parking_with_allaway_bj_stage_2:
    "bg parkingwithallaway_bj_1"
    pause 0.3
    "bg parkingwithallaway_bj_3"
    pause 0.1
    "bg parkingwithallaway_bj_4"
    pause 0.2
    repeat
####################
## BJ Stage 3
label lbl_parking_with_allaway_bj_3:
    scene img_parking_with_allaway_bj_stage_3
    #$ parking_with_allaway_bj_counter += 1
    #show bg parkingwithallaway_bj_1
    #$ renpy.pause(0.2,hard=True)
    #show bg parkingwithallaway_bj_3
    #$ renpy.pause(0.1,hard=True)
    #show bg parkingwithallaway_bj_4
    #$ renpy.pause(0.2,hard=True)
    #if skill_sta <= 20 and parking_with_allaway_bj_counter == 24:
    #    jump lbl_parking_with_allaway_bj_menu
    #else:
    #    jump lbl_parking_with_allaway_bj_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_parking_with_allaway_bj_menu

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_parking_with_allaway_bj_3

image img_parking_with_allaway_bj_stage_3:
    "bg parkingwithallaway_bj_1"
    pause 0.2
    "bg parkingwithallaway_bj_3"
    pause 0.1
    "bg parkingwithallaway_bj_4"
    pause 0.2
    repeat

label lbl_parking_with_allaway_bj_menu:
    #show bg parkingwithallaway_bj_1
    call screen scr_parking_with_allaway_bj_cumchoice

screen scr_parking_with_allaway_bj_cumchoice():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parking_with_allaway_bj_reset")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parking_with_allaway_bj_cum")

label lbl_parking_with_allaway_bj_cum:
    pov "Ah- Miss... I'm about to c-"
    scene bg parkingwithallaway_bj_4
    $ renpy.pause(0.2,hard=True)
    show bg parkingwithallaway_47
    with fade
    $ renpy.pause(1.4,hard=True)
    show bg parkingwithallaway_48
    mis "Ah-ah-ah. Not in my truck, mister."
    mis "Hehehe~"
    show bg parkingwithallaway_49
    pov "Noo.. Miss... don't tease me like that."
    show bg parkingwithallaway_50
    mis "I'm sorry, [povname]. I can help you out but you've got to finish the assignment yourself."
    show bg parkingwithallaway_51
    pov "You're not seriously playing the teacher's card, are you?"
    show bg parkingwithallaway_52
    mis "I didn't become one for nothing."
    mis "But yeah, no mess in here tonight."
    show bg parkingwithallaway_53
    pov "Can't you swallow."
    show bg parkingwithallaway_54
    mis "Can't you stop whining like a little bitch?"
    show bg parkingwithallaway_55
    mis "Sorry! I didn't mean for that to come out..."
    show bg parkingwithallaway_57
    pov "Hahaha, it's okay. I think I deserve that."
    show bg parkingwithallaway_56
    pov "I think..."
    show bg parkingwithallaway_58
    mis "C'mon, get out of here. Your parents might be watching from their window."
    mis "I don't know which window is theirs."
    show bg parkingwithallaway_59
    pov "Oh, shit... fuck..."
    show bg parkingwithallaway_7
    pov "You're right, I- uh better go.."
    pov "Goodnight!"
    show bg parkingwithallaway_12
    mis "Hehe, goodnight, [povname]."
    $ parkingwithallaway_action = 2
    jump lbl_parking_with_allaway_end
