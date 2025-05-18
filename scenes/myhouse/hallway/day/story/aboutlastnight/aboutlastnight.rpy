## About Last Night ##
label lbl_about_last_night:

    scene bg myhallway_day
    with fade
    if (momdrama_good and momdrama_touch) == 0:
        jump lbl_about_last_night_g0t0_1
    elif (momdrama_good and momdrama_touch) == 1:
        jump lbl_about_last_night_g1t1_1
    elif momdrama_good == 0 and momdrama_touch == 1:
        jump lbl_about_last_night_g0t1_1
    elif momdrama_good == 1 and momdrama_touch == 0:
        jump lbl_about_last_night_g1t0_1

label lbl_about_last_night_g0t0_1:
    show pov embarrassed at left
    with dissolve
    show mum embarrassed_talk at right
    with dissolve
    mum "Oh, [povname]! How was your sleep?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "It was good."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "Sorry if I was a little cranky last night."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    if winc == 0:
        pov "It's alright, [missus]."
    else:
        pov "It's alright, Mom."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "It must've been the Korean drama and, y'know how I get really emotional so easily.. an-"
    show pov embarrassed_talk at left
    show mum sad at right
    if winc == 0:
        pov "[missus], it's okay, it's not your fault. I wasn't being a very good [povmumrole]."
    else:
        pov "Mom, it's okay, it's not your fault. I wasn't being a very good son."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "Don't say that, baby. You know I still love you very much."

    jump lbl_about_last_night_g0t_1

label lbl_about_last_night_g0t_1:
    show pov embarrassed_talk at left
    show mum embarrassed at right
    if winc == 0:
        pov "I know, [missus]."
    else:
        pov "I know, Mom."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Good."
    show pov neutral at left
    show mum neutral at right
    pov "..."
    show mum bored at right
    mum "..."
    show pov confused at left
    show mum confused_talk at right
    mum "Aaand-?"

    menu:
        "And I promise to be a better son." if winc == 1:
            show pov smirk_talk at left
            show mum smirk at right
            pov "And I promise to be a better son in the future."
            show pov neutral at left
            show mum smirk_talk at right
            mum "I couldn't ever ask for a better son that I who I already have."
            show pov bored_talk at left
            show mum smirk at right
            pov "Stop, Mom. You're making me blush."
            show pov neutral at left
            show mum neutral_talk at right
            mum "You can never have too much love from me."
            show mum shocked_talk at right
            mum "Oh?! [povname]."
            show pov confused_talk at left
            show mum embarrassed at right
            pov "Yeah?"

            jump lbl_about_last_night_end
        "And I promise to be a better [povmumrole]." if winc == 0:
            show pov smirk_talk at left
            show mum smirk at right
            pov "And I promise to be a better [povmumrole] in the future."
            show pov neutral at left
            show mum smirk_talk at right
            mum "I couldn't ever ask for a better [povmumrole] that I who I already have."
            show pov bored_talk at left
            show mum smirk at right
            pov "Stop, [missus]. You're making me blush."
            show pov neutral at left
            show mum neutral_talk at right
            mum "You can never have too much love from me."
            show mum shocked_talk at right
            mum "Oh?! [povname]."
            show pov confused_talk at left
            show mum embarrassed at right
            pov "Yeah?"

            jump lbl_about_last_night_end
        "And I love you too.":
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ renpy.notify("Your relationship with Mom has increased")
            show pov smirk_talk at left
            show mum smirk at right
            if winc == 0:
                pov "And I love you too, [missus]."
            else:
                pov "And I love you too, Mom."
            show pov confused at left
            show mum smirk_talk at right
            mum "Hehe, that's my boy. I trained you so well."
            show pov confused_talk at left
            show mum bored at right
            pov "You're evil."
            show pov embarrassed at left
            show mum bored_talk at right
            mum "What did you say?"
            show pov embarrassed_talk at left
            show mum confused at right
            pov "Nothing."
            show pov neutral at left
            show mum bored_talk at right
            mum "Uh-huh."
            show pov bored at left
            show mum shocked_talk at right
            mum "Oh, [povname]."
            show pov confused_talk at left
            show mum embarrassed at right
            pov "Yeah?"

            jump lbl_about_last_night_end
        "And I'll see you later.":
            if mum_points >= 1:
                $ mum_points -= 1
                if winc == 0:
                    $ renpy.notify("Your relationship with [missus] has decreased by 1")
                else:
                    $ renpy.notify("Your relationship with Mom has decreased by 1")
            else:
                $ mum_points = -0
            show pov confused_talk at left
            show mum bored at right
            pov "And I'll see you later?"
            show pov confused at left
            show mum angry_talk at right
            mum "Oh, really? Is that all? Fine."
            show mum confused_talk at right
            mum "Wait, [povname]. Before you go."
            show pov confused at left
            show mum embarrassed at right
            pov "Mmmm?"

            jump lbl_about_last_night_end

label lbl_about_last_night_g0t1_1:
    show pov embarrassed at left
    with dissolve
    show mum embarrassed_talk at right
    with dissolve
    mum "Morning, [povname].. How was your sleep?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "It was alright..."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "About last night..."
    show mum embarrassed_talk at right
    mum "This is a really awkward topic to be talking to you about."
    show pov embarrassed_talk at left
    show mum sad at right
    pov "Yeah. It really is. Can we possibly just drop it and forget it happened?"
    show pov sad at left
    show mum sad_talk at right
    mum "I'm really sorry, [povname]. It really is my fault, I shouldn't have even acted the way I acted to begin with."
    show pov sad_talk at left
    show mum sad at right
    pov "I'm the one who is at fault. It was entirely idiotic of me to-"
    show pov embarrassed_talk at left
    pov "Well... Y'know..? With my-"
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "I'm sorry, you're sorry. Let's just move on."
    show mum sad_talk at right
    if winc == 0:
        mum "And don't you dare speak a word about what happened to your [dadrole], or anyone for that matter."
    else:
        mum "And don't you dare speak a word about what happened to your father, or anyone for that matter."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    if winc == 0:
        pov "You don't have to tell me, [missus]. Just between us."
    else:
        pov "You don't have to tell me, Mom. Just between us."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "Thanks. I still love you, [povname]."

    jump lbl_about_last_night_g0t_1

label lbl_about_last_night_g1t0_1:
    show pov neutral at left
    with dissolve
    show mum neutral_talk at right
    with dissolve
    mum "Morning [povname]. How was your sleep, baby?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "It was good."
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "Hey, thanks for hanging out with me last night. We haven't spent time together since we moved here."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "It's no problem, and sorry about that. I've been very occupied around here, people to meet up with, responsibilities to tend to."
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "I know, I know. I can understand that. Just remember to save some time for me too."
    show pov neutral at left
    show mum sad_talk at right
    mum "I may sound clingy but this will probably be your last year at home before you move out for college."

    menu:
        "A bird's gotta leave its nest.":
            show pov embarrassed_talk at left
            show mum sad at right
            pov "A bird's gotta leave its nest eventually."
            show pov embarrassed at left
            show mum sad_talk at right
            if winc == 0:
                mum "That's what they all say. But it doesn't mean it doesn't hurt."
            else:
                mum "That's what they all say. But it doesn't mean it doesn't hurt the mother bird."
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "Don't worry, Mom. I won't disappear from you."
            show pov neutral at left
            show mum smirk_talk at right
            mum "You better not. Otherwise I'm going to hunt you down myself."
            show pov smirk_talk at left
            show mum bored at right
            pov "You better keep that promise. There's a possibility that I've been taken prisoner in someone's torture dungeon."
            show pov smirk at left
            show mum sad_talk at right
            mum "Don't say that, it scares me."
            show pov smirk_talk at left
            show mum neutral at right
            pov "I'm joking."
            show pov embarrassed at left
            show mum bored_talk at right
            mum "I'm not."
            show pov smirk_talk at left
            show mum embarrassed at right
            pov "I love you?"
            show pov neutral at left
            show mum smirk_talk at right
            mum "I love you too, baby."
            show pov confused at left
            show mum shocked_talk at right
            mum "Oh-! [povname]."
            show pov confused_talk at left
            show mum embarrassed at right
            pov "Yeah?"

            jump lbl_about_last_night_end
        "I'll always be there for you.":
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ renpy.notify("Your relationship with Mom has increased")
            show pov neutral_talk at left
            show mum embarrassed at right
            pov "I'll always be there for you when you need it."
            show pov neutral at left
            show mum smirk_talk at right
            mum "You always know the right things to say, I guess I raised you well."
            show pov bored at left
            mum "I'll pat myself on the back."
            show pov bored_talk at left
            show mum smirk at right
            pov "Sure, just give yourself all the credit. Hahaha."
            show pov smirk at left
            show mum neutral_talk at right
            mum "I am. And I love myself for it."
            show pov embarrassed_talk at left
            show mum embarrassed at right
            if winc == 0:
                pov "I love you too, [missus]."
            else:
                pov "I love you too, Mom."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "What did I ever do to deserve you?"
            show pov bored at left
            show mum smirk_talk at right
            mum "Oh, right! Raise you well! Hehehe."
            show pov bored_talk at left
            show mum smirk at right
            pov "I'll take it that you love me too."
            show pov smirk at left
            show mum neutral_talk at right
            mum "You already know I do, [povname]."
            show mum sad_talk at right
            mum "So so very very much much."
            show pov confused at left
            show mum shocked_talk at right
            mum "Oh! Hold on, before you go."
            show pov confused_talk at left
            show mum embarrassed at right
            pov "Yes?"

            jump lbl_about_last_night_end
        "It was bound to happen, you know that.":
            if mum_points >= 1:
                $ mum_points -= 1
                if winc == 0:
                    $ renpy.notify("Your relationship with [missus] has decreased by 1")
                else:
                    $ renpy.notify("Your relationship with Mom has decreased by 1")
            else:
                $ mum_points = -0
            show pov embarrassed_talk at left
            show mum bored at right
            pov "It was bound to happen, you know that."
            show pov sad at left
            show mum sad_talk at right
            mum "Well, obviously but you could've sugar-coated it a little just for me."
            show pov sad_talk at left
            show mum sad at right
            pov "Just being realistic here."
            show pov embarrassed at left
            show mum sad_talk at right
            mum "I guess."
            show pov neutral at left
            show mum embarrassed_talk at right
            mum "It's no point getting mad over that. I still love you."
            show pov neutral_talk at left
            show mum embarrassed at right
            if winc == 0:
                pov "I love you too, Mom."
            else:
                pov "I love you too, [missus]."
            show pov confused at left
            show mum sad_talk at right
            mum "Hey, [povname]. Before you go."
            show pov confused_talk at left
            show mum embarrassed at right
            pov "Yeah?"

            jump lbl_about_last_night_end

label lbl_about_last_night_g1t1_1:
    show pov neutral at left
    with dissolve
    show mum embarrassed_talk at right
    with dissolve
    mum "Hey, [povname]. How was your sleep, baby?"
    show pov neutral_talk at left
    show mum embarrassed at right
    if winc == 0:
        pov "Morning, [missus]. It was good. Yours?"
    else:
        pov "Morning, Mom. It was good. Yours?"
    show pov confused at left
    show mum embarrassed_talk at right
    mum "Mine was alright. I'm sorry about last night.."
    show pov confused_talk at left
    show mum sad at right
    pov "What are you sorry about?"
    show pov embarrassed at left
    show mum sad_talk at right
    if winc == 0:
        mum "If we were making too much noise, me and your [dadrole]."
    else:
        mum "If we were making too much noise, me and your father."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "Oh.."

    menu:
        "I didn't hear anything.":
            show pov embarrassed_talk at left
            show mum shocked at right
            pov "I didn't hear anything, I was fast asleep."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Oh, alright. Nevermind then. Just thought I'd apologise just in cas-"
            show mum sad_talk at right
            mum "Y'know what? Forget I even said anything."

            jump lbl_about_last_night_g1t1_2
        "It's okay.":
            show pov embarrassed_talk at left
            show mum embarrassed at right
            if winc == 0:
                pov "It's okay, [missus].."
                show pov embarrassed at left
                show mum sad_talk at right
                mum "I hope we didn't keep you up. It's kind of embarrassing.. now that I'm realising what I'm talking to you about."
                show pov embarrassed_talk at left
                show mum embarrassed at right
                pov "Hehe.. [missus], it's okay. I understand."
            else:
                pov "It's okay, Mom.."
                show pov embarrassed at left
                show mum sad_talk at right
                mum "I hope we didn't keep you up. It's kind of embarrassing.. now that I'm realising what I'm talking to you about."
                show pov embarrassed_talk at left
                show mum embarrassed at right
                pov "Hehe.. Mom, it's okay. I understand."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Good.. good."

            jump lbl_about_last_night_g1t1_2

label lbl_about_last_night_g1t1_2:
    show pov sad at left
    show mum embarrassed_talk at right
    mum "We should talk about what happened last night."
    show pov embarrassed_talk at left
    show mum sad at right
    pov "Which part."
    show pov sad at left
    show mum sad_talk at right
    mum "Don't act stupid, [povname]. You know exactly what we were doing last night."
    mum "It was incredibly wrong for me to be doing that to you. I'm really sorry."
    mum "And don't you dare take the blame, I'm supposed to be the mature one between us."
    show pov sad_talk at left
    show mum sad at right
    if winc == 0:
        pov "[missus]?"
    else:
        pov "Mom?"
    show pov embarrassed_talk at left
    show mum sad at right
    pov "I will never tell a living soul about it, alright? The secret is safe with me."
    show pov sad at left
    show mum sad_talk at right
    mum "It's not just that. It's the fact that it happened in the first place."
    mum "[povname], I was in a very, lonely, emotional, vulnerable state when you came into the living room."
    if winc == 0:
        mum "And- and when you were just so sweet to me when your [dadrole] wasn't."
    else:
        mum "And- and when you were just so sweet to me when your father wasn't."
    show mum sad at right
    mum "..."
    show pov embarrassed at left
    show mum sad_talk at right
    mum "I- I kind of just.. my brain wasn't functioning."

    menu:
        "We were both a little loopy.":
            show pov embarrassed_talk at left
            show mum sad at right
            if winc == 0:
                pov "It's just as awkward for me, [missus]. It was late and we were both a little loopy."
            else:
                pov "It's just as awkward for me, Mom. It was late and we were both a little loopy."
            pov "I'll forget it happened if you do."

            jump lbl_about_last_night_g1t1_3
        "We're both adults.":
            show pov embarrassed_talk at left
            show mum sad at right
            if winc == 0:
                pov "[missus], It's totally fine, we're both adults."
            else:
                pov "Mom, It's totally fine, we're both adults."
            show mum embarrassed at right
            pov "Let's just deal with this maturely and move on from it, okay?"
            pov "Anything that happened in that living room last night, stays in that living room. Okay?"

            jump lbl_about_last_night_g1t1_3

label lbl_about_last_night_g1t1_3:
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "Promise?"
    show pov neutral_talk at left
    show mum embarrassed at right
    pov "Promise."
    show pov neutral at left
    show mum embarrassed_talk at right
    mum "Thank you. Oh! Hold on, [povname]. While you're here.."
    show pov confused_talk at left
    show mum embarrassed at right
    pov "Mm? What is it?"

    jump lbl_about_last_night_end

label lbl_about_last_night_end:
    show pov confused at left
    show mum embarrassed_talk at right
    mum "I have a... little problem."
    show pov confused_talk at left
    show mum embarrassed at right
    pov "What is it?"
    show pov bored at left
    show mum embarrassed_talk at right
    mum "Well, it's about my computer."
    show pov bored_talk at left
    show mum sad at right
    pov "What did you do with it..?"
    show pov bored at left
    show mum confused_talk at right
    mum "I mean, I- didn't do anything. I don't think I did?"
    show pov bored_talk at left
    show mum sad at right
    pov "What virus did you accidentally install this time?"
    show pov confused at left
    show mum embarrassed_talk at right
    mum "It's not a virus. I swear."
    show pov bored at left
    show mum sad_talk at right
    mum "It's just that there's a lot of pop-up windows and stuff all over the screen making weird noises and showing really inappropriate pictures."
    show pov bored_talk at left
    show mum bored at right
    pov "So... a virus?"
    show pov smirk at left
    show mum confused_talk at right
    mum "If you insist on labelling it like that, then yes..."
    show pov smirk_talk at left
    show mum neutral at right
    pov "I'll have a look at it later, alright?"
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Thanks, honey. You're a lifesaver. You're like the Gill Bates of the computer world."
    show pov bored_talk at left
    show mum smirk at right
    pov "...I surprisingly get that a lot."
    $ mum_path = 2
    $ townmap_enabled = 1
    $ renpy.notify("New Objective: Fix Mom's Computer")

    jump lbl_myhallway_day_setup
