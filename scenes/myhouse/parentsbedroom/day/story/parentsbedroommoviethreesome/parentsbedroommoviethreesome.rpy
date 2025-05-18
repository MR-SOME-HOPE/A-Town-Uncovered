## Parents Bedroom Movie Threesome
default parentsbedroommovie_threesome = 0
default parentsbedroommovie_threesome_horny_mom = False
default parentsbedroommovie_threesome_horny_sis = False

label lbl_parents_bedroom_movie_threesome:
    $ main_story = 80
    $ mumsis_path = 1
    $ max_phone_objectives += 1

    ###########################################################
    ##"mum = [mum_path], sis = [sister_path]"

    #if (mum_path <= 21 or mum_points <= 6) and (sister_path <= 31 or sister_points <= 6):
    #    jump lbl_parents_bedroom_movie_threesome_0
    #elif (mum_path >= 22 and mum_points >= 7) and (sister_path <= 31 or sister_points <= 6):
    #    jump lbl_parents_bedroom_movie_threesome_mom
    #elif (mum_path <= 21 or mum_points <= 6) and (sister_path >= 32 and sister_points >= 7):
    #    jump lbl_parents_bedroom_movie_threesome_sis
    #else:
        #$ parentsbedroommovie_threesome = 1
    #    if date <= 14:
    #        jump lbl_parents_bedroom_movie_threesome_mom
    #    else:
    #        jump lbl_parents_bedroom_movie_threesome_sis
    if (mum_path >= 22 and mum_points >= 7):
        $ parentsbedroommovie_threesome_horny_mom = True

    if (sister_path >= 32 and sister_points >= 7):
        $ parentsbedroommovie_threesome_horny_sis = True

    if not parentsbedroommovie_threesome_horny_mom and not parentsbedroommovie_threesome_horny_sis:
        jump lbl_parents_bedroom_movie_threesome_0

    elif parentsbedroommovie_threesome_horny_mom and parentsbedroommovie_threesome_horny_sis:
        if date <= 14:
            jump lbl_parents_bedroom_movie_threesome_mom
        else:
            jump lbl_parents_bedroom_movie_threesome_sis

    elif parentsbedroommovie_threesome_horny_mom:
        jump lbl_parents_bedroom_movie_threesome_mom

    elif parentsbedroommovie_threesome_horny_sis:
        jump lbl_parents_bedroom_movie_threesome_sis


## NO ROMANCE
label lbl_parents_bedroom_movie_threesome_0:
    scene bg qualityfamilytime_6
    with fade
    pov "{i}They are sleeping away without a care in the world…{/i}"
    pov "..."
    pov "{i}When was the last time I was able to do that?{/i}"

    #-The Mc looks worried as thoughts of Xina and the Sex World go back into his head-

    show bg qualityfamilytime_6_1
    pov "{i}Jacob said Grundle may have some information I could use...{/i}"
    pov "{i}Anything I can find that may help me know what I’m dealing cannot be ignored.{/i}"
    pov "{i}She must have made mistakes somewhere. Others must have noticed it too. I have to ask, and find out as much as I can before planning what to do next…{/i}"
    pov "{i}Know your enemy, and all that…{/i}"

    #-The Mc once again looks at Missus and Jane sleeping-

    pov "{i}I have to keep them safe...{/i}"
    tv "{i}A hero can be anyone.{/i}"
    tv "{i}Even a man doing something as simple and reassuring as: putting a coat around a young boy's shoulders.{/i}"
    show bg qualityfamilytime_6
    tv "{i}To let him know the world hadn’t ended.{/i}"
    pov "God damn. That line is still good!"
    scene black with fade
    $ renpy.pause()
    "You fall asleep watching movies..."

    jump lbl_falling_asleep_after_movie_or_threesome

label lbl_falling_asleep_after_movie_or_threesome:

    $ gtime = 0
    $ newspaper = 0
    call lbl_misc_restart
    call lbl_skill_items
    call lbl_next_date
    play music "audio/music/a_family_home.ogg"
    if day <= 5:
        $ day += 1
        if day == 1:
            $ renpy.notify("Tuesday Morning")
        elif day == 2:
            $ renpy.notify("Wednesday Morning")
        elif day == 3:
            $ renpy.notify("Thursday Morning")
        elif day == 4:
            $ renpy.notify("Friday Morning")
        elif day == 5:
            $ renpy.notify("Saturday Morning")
        elif day == 6:
            $ renpy.notify("Sunday Morning")
    elif day == 6:
        $ day = 0
        if day == 0:
            $ renpy.notify("Monday Morning")
    jump lbl_waking_up_alone

## MOM
label lbl_parents_bedroom_movie_threesome_mom:
    $ parentsbedroommovie_threesome = 1
    scene bg qualityfamilytime_3
    with fade
    tv "{i}If that plane leaves the ground and you are not with him, you’ll regret it.{/i}"
    tv "{i}Maybe not today, maybe not tomorrow, but soon. And for the rest of your life.{/i}"
    tv "{i}But what about us?{/i}"
    tv "{i}We’ll always have that brothel in Amsterdam.{/i}"
    tv "{i}We didn’t have it. We lost it until you came to Enus and Benus’ house of Weenuhs.{/i}"
    tv "{i}We got it back last night.{/i}"
    tv "{i}When I said I would never leave you…{/i}"
    tv "{i}And you never will.{/i}"
    mum "{i}*Sniff*{/i}"
    show bg qualityfamilytime_3_1
    mum "Oh lord, that scene always gets me all teared up."
    show bg qualityfamilytime_3_2
    pov "It’s a good scene, but I still think they should have named the place something else."
    show bg qualityfamilytime_3_3
    mum "The forties was a weird era; but their romance classics hold up, to this day."

    #-Missus then turns to look at the sleeping form of Jane before smiling-

    show bg qualityfamilytime_3_4
    mum "Look at her, it was her idea to have this movie marathon, and she is out for the count."
    show bg qualityfamilytime_3_5
    pov "Well, she never was one for these old-timey romantic movies."
    show bg qualityfamilytime_3_6
    mum "It’s a good thing, then, that I have my big, strong softy of a man to watch them with."
    show bg qualityfamilytime_3_7
    pov "I’d watch anything if it made you happy."
    show bg qualityfamilytime_3_6
    mum "And I love you because of that."

    show bg qualityfamilytime_4
    pov "Woah, there. You sure we should be doing this now?"
    pov "What if she wakes up?"
    show bg qualityfamilytime_4_1
    mum "Well, we are just going to have to be careful, then, won’t we?"
    mum "Don’t act as if the possibility of getting caught doesn’t excite you."
    show bg qualityfamilytime_4_2
    pov "W-Well, I-"

    #-she lowers her hand to grab the bulge in the mc’s pants-
    show bg qualityfamilytime_4_3
    mum "You can lie to me all you want, but this cock is very clearly telling me to give it some attention."
    show bg qualityfamilytime_4_4
    pov "Well, you are not wrong…"
    show bg qualityfamilytime_4_3
    mum "Now, as much as I want to ride you - cowgirl style - until this bed breaks, let’s try not wake your [povsisrole] and stick to foreplay, okay?"
    show bg qualityfamilytime_4_4
    pov "And what do you have in mind?"
    show bg qualityfamilytime_4_3
    mum "Well, young man, these big breasts of mine aren’t going to suck themselves - and I expect you have been practicing how to work those fingers."
    mum "I’ve certainly been researching new ways to make my hand choke your cock out."
    show bg qualityfamilytime_4_4
    pov "Oh boy."

    jump lbl_parents_bedroom_movie_momhscene

## SIS
label lbl_parents_bedroom_movie_threesome_sis:
    $ parentsbedroommovie_threesome = 2
    scene bg qualityfamilytime_7
    with fade
    tv "{i}Hello… My name Is Enrique Mountain… You fucked my father… Prepare to die...{/i}"
    tv "{i}*Swords clashing*{/i}"
    tv "{i}Hello! My name Is Enrique Mountain. You fucked my father. Prepare to die.{/i}"
    tv "{i}Stop saying that!{/i}"
    tv "{i}*More swords clashing*{/i}"
    show bg qualityfamilytime_7_1
    sis "Dude, here comes the best part!"
    show bg qualityfamilytime_7_2
    pov "Shut up! Sshut up! Don’t ruin it!"
    show bg qualityfamilytime_7
    tv "{i}Hello! My name Is Enrique Mountain. You fucked my father, Prepare to die!{/i}"
    tv "{i}Now, offer me money.{/i}"
    tv "{i}Yes…{/i}"
    tv "{i}Tits too, promise me that.{/i}"
    tv "{i}All the women I have and more. Please…{/i}"
    tv "{i}Offer me everything I ask for.{/i}"
    tv "{i}Anything you want.{/i}"
    show bg qualityfamilytime_7_1
    sis "Here it comes, here it comes!"
    show bg qualityfamilytime_7
    tv "{i}*Sword clash*{/i}"
    tv "{i}Urk-!{/i}"
    tv "{i}I want my father’s butt virginity back, you son of a bitch.{/i}"
    show bg qualityfamilytime_7_3
    sis "Ohhhh!"
    pov "Suck on that, you six fingered cock sucker!"
    sis "On your mustached face!"

    #-You and sister celebrate for a moment before minding Missus in bed with you
    show bg qualityfamilytime_7_4
    mum "Mmnnn..."
    show bg qualityfamilytime_7_5
    pov "Woah, easy there, [sister]. Lets not wake [missus] up."
    show bg qualityfamilytime_7_6
    sis "My bad, my bad."
    show bg qualityfamilytime_7_7
    sis "I just love this movie so much."
    show bg qualityfamilytime_7_8
    pov "Don’t we all?"

    #-You and sister then turn to look at the sleeping Missus-

    show bg qualityfamilytime_7_9
    sis "Look at her."
    sis "She was so excited about the idea of us having a family night; and she is the first to pass out."
    show bg qualityfamilytime_7_10
    pov "Figures..."
    pov "At least she had a good time, for while it lasted."
    show bg qualityfamilytime_7_9
    sis "That’s true."

    show bg qualityfamilytime_5
    pov "Mm!"
    show bg qualityfamilytime_5_1
    pov "Woah there, you think it’s a good idea to do this here?"
    pov "What if she wakes up?"
    show bg qualityfamilytime_5_2
    sis "Well, in that case you are going to have to be very quiet, then. Won’t you, mister?"
    sis "You haven’t given me much attention lately, and I plan to get some now."
    show bg qualityfamilytime_5_3
    pov "Still… She is right there and-"
    show bg qualityfamilytime_5_2
    sis "Don’t act as if you don’t want this as well."
    sis "There is quite the large bulge - with my name on it - in your pants that is saying otherwise."
    show bg qualityfamilytime_5_3
    pov "Alright, fair enough."
    show bg qualityfamilytime_5_2
    sis "Hehehe, alright."
    sis "As much as I’m sure you want me to ride you - reverse cowgirl style - until we break the bed; I’m not about to wake up [missus]."
    sis "So instead, you are going to do something for me. Then something to me."
    show bg qualityfamilytime_5_3
    pov "Which is?"
    show bg qualityfamilytime_5_2
    sis "It’s dinner time, Dead Pirate Juarez."

    jump lbl_parents_bedroom_movie_sisterhscene

## MOM H-SCENE
label lbl_parents_bedroom_movie_momhscene:
    scene black
    with fade
    $ renpy.pause

    scene bg qualityfamilytime_momhscene_1
    with fade
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_3
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_1
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_3
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_1
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause()
    show bg qualityfamilytime_momhscene_3
    mum "Mmm.. honey. I can't believe we're doing this..."
    show bg qualityfamilytime_momhscene_2
    mum "R-right next to [sister]."

label lbl_parents_bedroom_movie_momhscene_0:
    $ qualityfamilytime_momhscene_counter = 0

label lbl_parents_bedroom_movie_momhscene_1:
    $ qualityfamilytime_momhscene_counter += 1
    show bg qualityfamilytime_momhscene_1
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_3
    $ renpy.pause(0.4,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.3,hard=True)
    if skill_sta <= 7 and qualityfamilytime_momhscene_counter == 4:
        if parentsbedroommovie_threesome_horny_sis:
            jump lbl_parents_bedroom_movie_momhscene_sisterjoins
        else:
            jump lbl_parents_bedroom_movie_momhscene_cum
    elif skill_sta <= 14 and qualityfamilytime_momhscene_counter == 6:
        jump lbl_parents_bedroom_movie_momhscene_2
    elif skill_sta <= 20 and qualityfamilytime_momhscene_counter == 8:
        jump lbl_parents_bedroom_movie_momhscene_2
    else:
        jump lbl_parents_bedroom_movie_momhscene_1

label lbl_parents_bedroom_movie_momhscene_2:
    $ qualityfamilytime_momhscene_counter += 1
    show bg qualityfamilytime_momhscene_1
    $ renpy.pause(0.2,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.2,hard=True)
    show bg qualityfamilytime_momhscene_3
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.3,hard=True)
    if skill_sta <= 14 and qualityfamilytime_momhscene_counter == 14:
        if parentsbedroommovie_threesome_horny_sis:
            jump lbl_parents_bedroom_movie_momhscene_sisterjoins
        else:
            jump lbl_parents_bedroom_movie_momhscene_cum
    elif skill_sta <= 20 and qualityfamilytime_momhscene_counter == 16:
        jump lbl_parents_bedroom_movie_momhscene_3
    else:
        jump lbl_parents_bedroom_movie_momhscene_2

label lbl_parents_bedroom_movie_momhscene_3:
    $ qualityfamilytime_momhscene_counter += 1
    show bg qualityfamilytime_momhscene_1
    $ renpy.pause(0.2,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.2,hard=True)
    show bg qualityfamilytime_momhscene_3
    $ renpy.pause(0.2,hard=True)
    show bg qualityfamilytime_momhscene_2
    $ renpy.pause(0.2,hard=True)
    if skill_sta <= 20 and qualityfamilytime_momhscene_counter == 24:
        if parentsbedroommovie_threesome_horny_sis:
            jump lbl_parents_bedroom_movie_momhscene_sisterjoins
        else:
            jump lbl_parents_bedroom_movie_momhscene_cum
    else:
        jump lbl_parents_bedroom_movie_momhscene_3

label lbl_parents_bedroom_movie_momhscene_cum:
    call screen scr_parents_bedroom_movie_momhscene_cum

screen scr_parents_bedroom_movie_momhscene_cum():
    if not parentsbedroommovie_threesome_horny_sis:
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_momhscene_cumout")
    else:
        imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_momhscene_sisterjoins")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_momhscene_0")

label lbl_parents_bedroom_movie_momhscene_cumout:
    show bg qualityfamilytime_momhscene_4_1
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_4_2
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_4_3
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_4_4
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_4_5
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_momhscene_4_6
    $ renpy.pause()
    mum "{i}*Whisper*{/i} Oh my gosh, sweetie! You came-."
    mum "Just- don't move too much, I don't need you messing up the bedsheets or getting it on your [povsisrole]'s arm."
    mum "I'll grab you something to clean up with. I think it's best you head to bed, baby."
    mum "I love you."
    pov "I love you too, [missus]."
    scene black
    with fade
    $ renpy.pause()
    $ gtime = 3

    scene bg myhallway_night
    with fade

    jump lbl_myhallway_night_setup

label lbl_parents_bedroom_movie_momhscene_finish:
    sis "Mmmm.."
    mum "[povname]- stop- I think [sister]'s about to wake up."
    pov "Oh-"
    mum "Seriously stop- we should get out of here before she sees what we're doing."
    pov "{i}*Muffled*{/i} Nawww..."

    scene black
    with fade
    $ renpy.pause()

    $ gtime = 3

    scene bg myhallway_night
    with fade

    jump lbl_myhallway_night_setup

## SISTER H-SCENE
label lbl_parents_bedroom_movie_sisterhscene:
    jump lbl_parents_bedroom_movie_sisterhscene_0

label lbl_parents_bedroom_movie_sisterhscene_0:
    $ qualityfamilytime_sisterhscene_counter = 0

    jump lbl_parents_bedroom_movie_sisterhscene_1

label lbl_parents_bedroom_movie_sisterhscene_0_2:
    $ qualityfamilytime_sisterhscene_counter = 8

    jump lbl_parents_bedroom_movie_sisterhscene_1

label lbl_parents_bedroom_movie_sisterhscene_0_3:
    $ qualityfamilytime_sisterhscene_counter = 18

    jump lbl_parents_bedroom_movie_sisterhscene_1

label lbl_parents_bedroom_movie_sisterhscene_1:
    $ qualityfamilytime_sisterhscene_counter += 1
    show bg qualityfamilytime_sisterhscene_1
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_2
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_3
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_2
    $ renpy.pause(0.3,hard=True)
    if skill_sta <= 7 and qualityfamilytime_sisterhscene_counter == 6:
        if parentsbedroommovie_threesome_horny_mom:
            jump lbl_parents_bedroom_movie_sisterhscene_momjoins
        else:
            jump lbl_parents_bedroom_movie_sisterhscene_finish
    elif skill_sta <= 14 and qualityfamilytime_sisterhscene_counter == 8:
        jump lbl_parents_bedroom_movie_sisterhscene_1_2
    elif skill_sta <= 20 and qualityfamilytime_sisterhscene_counter == 10:
        jump lbl_parents_bedroom_movie_sisterhscene_1_2
    else:
        jump lbl_parents_bedroom_movie_sisterhscene_1

label lbl_parents_bedroom_movie_sisterhscene_1_2:
    call screen scr_parents_bedroom_movie_sisterhscene_1_2

screen scr_parents_bedroom_movie_sisterhscene_1_2():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_sisterhscene_2")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_sisterhscene_0")

label lbl_parents_bedroom_movie_sisterhscene_2:
    $ qualityfamilytime_sisterhscene_counter += 1
    show bg qualityfamilytime_sisterhscene_4
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_5
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_6
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_5
    $ renpy.pause(0.3,hard=True)
    if skill_sta <= 14 and qualityfamilytime_sisterhscene_counter == 16:
        if parentsbedroommovie_threesome_horny_mom:
            jump lbl_parents_bedroom_movie_sisterhscene_momjoins
        else:
            jump lbl_parents_bedroom_movie_sisterhscene_finish
    elif skill_sta <= 20 and qualityfamilytime_sisterhscene_counter == 18:
        jump lbl_parents_bedroom_movie_sisterhscene_2_2
    else:
        jump lbl_parents_bedroom_movie_sisterhscene_2

label lbl_parents_bedroom_movie_sisterhscene_2_2:
    call screen scr_parents_bedroom_movie_sisterhscene_2_2

screen scr_parents_bedroom_movie_sisterhscene_2_2():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_sisterhscene_3")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_sisterhscene_0_2")

label lbl_parents_bedroom_movie_sisterhscene_3:
    $ qualityfamilytime_sisterhscene_counter += 1
    show bg qualityfamilytime_sisterhscene_7
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_8
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_9
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_8
    $ renpy.pause(0.3,hard=True)
    if skill_sta <= 20 and qualityfamilytime_sisterhscene_counter == 26:
        if parentsbedroommovie_threesome_horny_mom:
            jump lbl_parents_bedroom_movie_sisterhscene_momjoins
        else:
            jump lbl_parents_bedroom_movie_sisterhscene_3_2
    else:
        jump lbl_parents_bedroom_movie_sisterhscene_3

label lbl_parents_bedroom_movie_sisterhscene_3_2:
    call screen scr_parents_bedroom_movie_sisterhscene_3_2

screen scr_parents_bedroom_movie_sisterhscene_3_2():
    if not parentsbedroommovie_threesome_horny_mom:
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_sisterhscene_cum")
    else:
        imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_sisterhscene_momjoins")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_sisterhscene_0_3")

label lbl_parents_bedroom_movie_sisterhscene_cum:
    show bg qualityfamilytime_sisterhscene_8
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_9
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_sisterhscene_10_1
    sis "[povname]-!"
    show bg qualityfamilytime_sisterhscene_10_2
    $ renpy.pause(0.6,hard=True)
    show bg qualityfamilytime_sisterhscene_10_3
    $ renpy.pause(0.6,hard=True)
    show bg qualityfamilytime_sisterhscene_10_4
    $ renpy.pause(0.6,hard=True)
    show bg qualityfamilytime_sisterhscene_10_5
    $ renpy.pause(0.6,hard=True)
    show bg qualityfamilytime_sisterhscene_10_6
    $ renpy.pause(0.6,hard=True)
    sis "{i}*Pants*{/i}"
    sis "Fuck-"
    show bg qualityfamilytime_sisterhscene_10_7
    sis "Oh damn- that felt so fucking good, [povname]."
    sis "You should have your pussy licked sometime, shit's pre- good."
    pov "I'll consider having a go sometime."
    sis "C'mon, we should get outta here before [missus] wakes up."
    pov "She's definitely out like a light."
    sis "Thank God for that. Your tongue was making a lot of noise."
    pov "Hehehe~"
    scene black
    with fade
    $ renpy.pause()

    $ gtime = 3

    scene bg myhallway_night
    with fade

    jump lbl_myhallway_night_setup

label lbl_parents_bedroom_movie_sisterhscene_finish:
    mum "Mmmm.."
    sis "[povname]- stop- I think [missus]'s about to wake up."
    pov "Oh-"
    sis "Seriously stop- we should get out of here before she sees what we're doing."
    pov "{i}*Muffled*{/i} Nawww..."

    scene black
    with fade
    $ renpy.pause()

    $ gtime = 3

    scene bg myhallway_night
    with fade

    jump lbl_myhallway_night_setup

## SISTER JOINS
label lbl_parents_bedroom_movie_momhscene_sisterjoins:
    scene bg qualityfamilytime_prethreesome_1
    sis "Mmmmum.."
    mum "Oh- stop- stop- [povname]..!"
    show bg qualityfamilytime_prethreesome_2
    pov "[missus]! You're the one that's on me."
    show bg qualityfamilytime_prethreesome_3
    sis "What- what's going on here?!"
    show bg qualityfamilytime_prethreesome_4
    mum "Honey~ I was just-"
    show bg qualityfamilytime_prethreesome_5
    sis "Mom? Why are you on top of [povname]?"
    show bg qualityfamilytime_prethreesome_4
    mum "I-"
    show bg qualityfamilytime_prethreesome_6
    sis "It looks fun..."
    show bg qualityfamilytime_prethreesome_7
    pov "Uh-"
    show bg qualityfamilytime_prethreesome_8
    mum "No- this isn't- You are mistaken."
    show bg qualityfamilytime_prethreesome_3
    sis "[missus], I can see his stupid dick out."
    show bg qualityfamilytime_prethreesome_6
    sis "Look, it's just us in here. I won't tell a soul."
    show bg qualityfamilytime_prethreesome_7
    mum "[sister]..."
    show bg qualityfamilytime_prethreesome_9
    mum "You know what: it IS just us in here, right?"
    mum "And it's family night."
    mum "Why don't we do something fun, as a trio?"
    show bg qualityfamilytime_prethreesome_10
    pov "I- what- do you have in mind, [missus]?"
    show bg qualityfamilytime_prethreesome_0
    mum "I have this. Your [sisrole] gave it to me when she first started working at that sex shop."
    sis "I remember that. You still have some left over?"
    mum "I was saving it for a special ocassion."
    sis "Can I try it?"
    mum "Sure, baby. Lemme just get undressed and get it ready for you."
    mum "Oh- screw it, I think we all should get undressed and try it."
    pov "Really?"
    sis "I'm down, I shotgun eating out [missus]!"
    mum "Welp, [povname], looks like you're my dinner tonight and [sister]'s yours."
    pov "I'm not complaining~"

    jump lbl_parents_bedroom_movie_threesomehscene

## MOM JOINS
label lbl_parents_bedroom_movie_sisterhscene_momjoins:
    scene bg qualityfamilytime_prethreesome_11
    mum "Mmmm.."
    show bg qualityfamilytime_prethreesome_12
    sis "[povname]- stop- I think [missus]'s about to wake u-."
    show bg qualityfamilytime_prethreesome_13
    mum "What's that slurping soun'-"
    mum "Whatcha eatin-"
    mum "..."
    mum "Ummm?!"
    show bg qualityfamilytime_prethreesome_14
    sis "[missus]!"
    show bg qualityfamilytime_prethreesome_15
    pov "I- it's not what it looks like-!"
    show bg qualityfamilytime_prethreesome_13
    mum "Uh-huh, and what does it look like?"
    show bg qualityfamilytime_prethreesome_14
    sis "I- he-"
    show bg qualityfamilytime_prethreesome_13
    mum "It looks like I'm left out, that's what it looks like to me."
    show bg qualityfamilytime_prethreesome_15
    pov "I- you- huh...?"
    show bg qualityfamilytime_prethreesome_14
    sis "[missus]?"
    show bg qualityfamilytime_prethreesome_15
    pov "What are you saying..?"
    show bg qualityfamilytime_prethreesome_13
    mum "I'm saying that we should be spending family night together."
    show bg qualityfamilytime_prethreesome_0
    mum "Thanks for the little gift, [sister]. It actually tastes pretty good."
    pov "You gave [missus] flavoured lube? Hmm... warermelon."
    sis "I work at a sex store; it's one of the free swag I could give her."
    pov "One of-?"
    mum "Now now, don't be so judgy, [povname]. It's perfectly normal."
    if winc == 1:
        mum "Now, which one of you wants to have a taste of mommy's pussy?"
    else:
        mum "Now, which one of you wants to have a taste of your [povmumrole] pussy?"
    pov "Me!"
    mum "..."
    if winc == 1:
        mum "[sister], care to help mommy?"
    else:
        mum "[sister], care to help your [povmumrole]?"
    pov "But-"
    mum "[povname], don't be selfish. I'm sure [sister] doesn't want you to jump ship."
    mum "I'll pour some onto hers and then some onto your cock too, [povname]."
    pov "Mine too?"
    mum "Of course, I'm hungry too."
    mum "C'mon, honeybears: take off your clothes now."

    jump lbl_parents_bedroom_movie_threesomehscene

## THREESOME H-SCENE
label lbl_parents_bedroom_movie_threesomehscene:
    $ parentsbedroommovie_threesome = 3
    scene black
    with fade
    $ renpy.pause()
    "A few clothes later..."
    scene bg qualityfamilytime_threesomehscene_1
    with fade

    jump lbl_parents_bedroom_movie_threesomehscene_0

label lbl_parents_bedroom_movie_threesomehscene_0:
    $ qualityfamilytime_threesomehscene_counter = 0

    jump lbl_parents_bedroom_movie_threesomehscene_1

label lbl_parents_bedroom_movie_threesomehscene_0_2:
    if skill_sta <= 14:
        $ qualityfamilytime_threesomehscene_counter = 8
    else:
        $ qualityfamilytime_threesomehscene_counter = 10

    jump lbl_parents_bedroom_movie_threesomehscene_2

label lbl_parents_bedroom_movie_threesomehscene_0_3:
    $ qualityfamilytime_threesomehscene_counter = 18

    jump lbl_parents_bedroom_movie_threesomehscene_3

label lbl_parents_bedroom_movie_threesomehscene_1:
    $ qualityfamilytime_threesomehscene_counter += 1
    show bg qualityfamilytime_threesomehscene_1
    $ renpy.pause(0.4,hard=True)
    show bg qualityfamilytime_threesomehscene_2
    $ renpy.pause(0.4,hard=True)
    show bg qualityfamilytime_threesomehscene_3
    $ renpy.pause(0.4,hard=True)
    show bg qualityfamilytime_threesomehscene_2
    $ renpy.pause(0.5,hard=True)
    if skill_sta <= 7 and qualityfamilytime_threesomehscene_counter == 6:
        jump lbl_parents_bedroom_movie_threesomehscene_finish
    elif skill_sta <= 14 and qualityfamilytime_threesomehscene_counter == 8:
        jump lbl_parents_bedroom_movie_threesomehscene_1_2
    elif skill_sta <= 20 and qualityfamilytime_threesomehscene_counter == 10:
        jump lbl_parents_bedroom_movie_threesomehscene_1_2
    else:
        jump lbl_parents_bedroom_movie_threesomehscene_1

label lbl_parents_bedroom_movie_threesomehscene_1_2:
    call screen scr_parents_bedroom_movie_threesomehscene_1_2

screen scr_parents_bedroom_movie_threesomehscene_1_2():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_threesomehscene_finish")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_threesomehscene_0")

label lbl_parents_bedroom_movie_threesomehscene_2:
    $ qualityfamilytime_threesomehscene_counter += 1
    show bg qualityfamilytime_threesomehscene_1
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_threesomehscene_2
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_threesomehscene_3
    $ renpy.pause(0.3,hard=True)
    show bg qualityfamilytime_threesomehscene_2
    $ renpy.pause(0.4,hard=True)
    if skill_sta <= 14 and qualityfamilytime_threesomehscene_counter == 16:
        jump lbl_parents_bedroom_movie_threesomehscene_finish
    elif skill_sta <= 20 and qualityfamilytime_threesomehscene_counter == 18:
        jump lbl_parents_bedroom_movie_threesomehscene_2_2
    else:
        jump lbl_parents_bedroom_movie_threesomehscene_2

label lbl_parents_bedroom_movie_threesomehscene_2_2:
    call screen scr_parents_bedroom_movie_threesomehscene_2_2

screen scr_parents_bedroom_movie_threesomehscene_2_2():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_threesomehscene_finish")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_threesomehscene_0")

label lbl_parents_bedroom_movie_threesomehscene_3:
    $ qualityfamilytime_threesomehscene_counter += 1
    show bg qualityfamilytime_threesomehscene_1
    $ renpy.pause(0.2,hard=True)
    show bg qualityfamilytime_threesomehscene_2
    $ renpy.pause(0.2,hard=True)
    show bg qualityfamilytime_threesomehscene_3
    $ renpy.pause(0.2,hard=True)
    show bg qualityfamilytime_threesomehscene_2
    $ renpy.pause(0.3,hard=True)
    if skill_sta <= 20 and qualityfamilytime_threesomehscene_counter == 26:
        jump lbl_parents_bedroom_movie_threesomehscene_3_2
    else:
        jump lbl_parents_bedroom_movie_threesomehscene_3

label lbl_parents_bedroom_movie_threesomehscene_3_2:
    call screen scr_parents_bedroom_movie_threesomehscene_3_2

screen scr_parents_bedroom_movie_threesomehscene_3_2():
    imagebutton auto "btn hscene_next_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_threesomehscene_finish")
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_parents_bedroom_movie_threesomehscene_0")

label lbl_parents_bedroom_movie_threesomehscene_finish:
    scene black
    with fade
    $ renpy.pause()
    "You all kept going at it until you all fall asleep with each other..."

    jump lbl_falling_asleep_after_movie_or_threesome
