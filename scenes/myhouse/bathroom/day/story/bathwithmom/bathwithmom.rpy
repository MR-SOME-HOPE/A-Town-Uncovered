## Bath with Mom ##
label lbl_bath_with_mom:
    default bathwithmom_eyereveal = 0
    #default bathwithmom_counter = 0

    scene bg bathwithmom_1
    pov "..."
    if winc == 0:
        pov "[missus]?"
    else:
        pov "Mom?"
    show bg bathwithmom_2
    mum "..."
    show bg bathwithmom_3
    mum "Hey, [povname]..."
    mum "Care to join me?"

    menu:
        "I'm still mad at you.":
            show bg bathwithmom_4
            with dissolve
            pov "I'm still mad at you for shutting me out for so long. Literally."
            show bg bathwithmom_5
            mum "I know, I know. How selfish of me, right?"
            show bg bathwithmom_4
            pov "Yeah, it actually was."
            pov "Like, you've literally scolded me about not being there for you 24/7..."
            pov "And there you were, trapped in your room away from me."
        "Do you realise how much I've missed you?":
            show bg bathwithmom_6
            with dissolve
            pov "Do you realise how much I've missed you?"
            show bg bathwithmom_7
            mum "I know, honey. I'm sorry I made you feel lonely."
            show bg bathwithmom_6
            pov "And not only that, you purposely did it knowingly."
            pov "..."
            pov "All I wanted was to be with you and you shut me out like I was nobody."
    show bg bathwithmom_5
    mum "I know, [povname]. I- I hope you can forgive me."
    show bg bathwithmom_4
    pov "{i}*Sigh*{/i}"

    menu:
        "Join you, you say?":
            show bg bathwithmom_6
            pov "Join you, you say?"
            show bg bathwithmom_7
            mum "If that isn't too much to ask."
            show bg bathwithmom_6
            if winc == 0:
                pov "I'd love to, [missus]."
            else:
                pov "I'd love to, Mom."

            jump lbl_bath_with_mom_1
        "I'll just leave you to your bath.":
            show bg bathwithmom_4
            pov "I'll just leave you to your bath. I'm not in the mood."
            show bg bathwithmom_5
            mum "Well... okay, if you insist."
            show bg bathwithmom_7
            mum "I love you..."

            menu:
                "I love you too.":
                    show bg bathwithmom_6
                    if winc == 0:
                        pov "I love you too, [missus]. Don't think I don't."
                    else:
                        pov "I love you too, Mom. Don't think I don't."
                "I know.":
                    show bg bathwithmom_4
                    if winc == 0:
                        pov "I know, [missus]. I'll talk to you another time."
                    else:
                        pov "I know, Mom. I'll talk to you another time."
            $ mum_path = 17

            jump lbl_myhallway_day_setup

label lbl_bath_with_mom_1:

    scene bg bathwithmom_8
    with fade
    $ renpy.pause(3,hard=True)
    show bg bathwithmom_9
    $ renpy.pause()
    show bg bathwithmom_10
    mum "I just want to say that I'm really sorry for trapping myself in my room."
    if winc == 0:
        mum "I know you didn't deserve a [mumrole] like that but..."
    else:
        mum "I know you didn't deserve a mother like that but..."
    show bg bathwithmom_11
    mum "..."
    show bg bathwithmom_12
    mum "But... uh..."
    $ bathwithmom_eyereveal = 1

    menu:
        "Wait for her to finish":
            show bg bathwithmom_11
            pov "..."
            show bg bathwithmom_12
            mum "I... don't know if I should tell you."
            show bg bathwithmom_10
            mum "Not because I don't want to..."
            mum "It's because I'm afraid you might do something stupid."
            show bg bathwithmom_12
            if winc == 0:
                mum "I don't want to tear this household apart."
            else:
                mum "I don't want to tear this family apart."
            show bg bathwithmom_11
            mum "..."
            show bg bathwithmom_12
            if winc == 0:
                mum "Your [dadrole] and I..."
            else:
                mum "Your father and I..."
            show bg bathwithmom_11
            pov "..."
            show bg bathwithmom_10
            mum "Well... Just promise you won't overreact."

            menu:
                "If he hurt you, I can't promise I won't be furious.":
                    show bg bathwithmom_9
                    pov "If he hurt you at all, I can't promise I won't be furious with him."
                    mum "..."
                    show bg bathwithmom_11
                    pov "Did he hurt you?!"
                    show bg bathwithmom_9
                    mum "..."
                    show bg bathwithmom_13
                    $ renpy.pause(2,hard=True)
                    show bg bathwithmom_14
                    $ renpy.pause()
                    show bg bathwithmom_14
                    with hpunch
                    pov "That fucking mo-"
                    show bg bathwithmom_15
                    mum "[povname]! Please, please PLEASE!"
                    show bg bathwithmom_12
                    mum "Just let it go."
                    show bg bathwithmom_11
                    pov "How the fuck am I supposed to let it go?!"
                    show bg bathwithmom_9
                    pov "You've got a fucking black eye!"
                "I'll try not to.":
                    show bg bathwithmom_9
                    pov "I'll try not to..."
                    mum "..."
                    show bg bathwithmom_10
                    mum "Promise?"
                    show bg bathwithmom_9
                    pov "{i}*Sigh*{/i} I promise..."
                    show bg bathwithmom_10
                    mum "You better..."
                    show bg bathwithmom_13
                    $ renpy.pause(2,hard=True)
                    show bg bathwithmom_14
                    $ renpy.pause()
                    show bg bathwithmom_14
                    with hpunch
                    pov "That fucking mo-"
                    show bg bathwithmom_15
                    mum "You promised, [povname]!"
                    show bg bathwithmom_11
                    if winc == 0:
                        pov "[missus]! I don't know if you've noticed but you've got a fucking black eye!"
                    else:
                        pov "Mom! I don't know if you've noticed but you've got a fucking black eye!"
                    pov "You can't tell me that I don't want to kill him right now!"

            jump lbl_bath_with_mom_2
        "You don't have to tell me anything.":
            show bg bathwithmom_9
            if winc == 0:
                pov "[missus]."
            else:
                pov "Mom."
            pov "You don't have to tell me anything you don't want to."
            pov "There are some things better kept to ourselves."
            pov "Agree?"
            show bg bathwithmom_16
            mum "I guess, yeah. Thanks, honey."
            show bg bathwithmom_17
            if winc == 0:
                pov "I mean, it must be quite a secret to keep it from your own naked [povmumrole], ain't it?"
            else:
                pov "I mean, it must be quite a secret to keep it from your own naked son, ain't it?"
            show bg bathwithmom_18
            mum "Hehehe..."
            show bg bathwithmom_11
            mum "..."
            show bg bathwithmom_10
            mum "But I just can't keep it from you forever."
            mum "No secrets between us, remember?"
            show bg bathwithmom_13
            $ renpy.pause(2,hard=True)
            show bg bathwithmom_14
            $ renpy.pause()
            show bg bathwithmom_14
            with hpunch
            pov "What the fuck!?"
            if winc == 0:
                pov "[dadname] did that to you?!"
            else:
                pov "Dad did that to you?!"
            show bg bathwithmom_12
            mum "It's nothing to be too worked up about, [povname]."
            show bg bathwithmom_16
            mum "It's healing up now."
            mum "No more pain."
            show bg bathwithmom_11
            if winc == 0:
                pov "[missus]! That's fucked up! How could you let him do that to you?"
            else:
                pov "Mom! That's fucked up! How could you let him do that to you?"
            pov "Let alone hide it from me?"
            if savemomfromdad_tackle == 1:
                pov "I can knock him out and give him two black eyes if you want me to."
                show bg bathwithmom_10
                mum "[povname]... Just because you got him the first time, doesn't mean you should do it again."
                mum "I don't like violence in this house."
                show bg bathwithmom_11
                if winc == 0:
                    pov "Have you seen your eye, [missus]? He deserves double."
                else:
                    pov "Have you seen your eye, Mom? He deserves double."
            elif savemomfromdad_tackle == 0:
                pov "I'll dislocate his fucking jaw, I don't care."
                show bg bathwithmom_10
                mum "[povname]. Not to bring it up but you failed the first time. I don't think you should be talking like that."
                show bg bathwithmom_17
                pov "Hey! I saved you from him, didn't I?"
            else:
                pov "I'll fucking kill him!"
                show bg bathwithmom_10
                mum "[povname]..."
                if winc == 0:
                    mum "I don't want to hear you say those words ever again. He's your [dadrole] for crying out loud."
                else:
                    mum "I don't want to hear you say those words ever again. He's your dad for crying out loud."
                show bg bathwithmom_9
                pov "Does it look like I care? The only thing I care about is you."

            jump lbl_bath_with_mom_2

label lbl_bath_with_mom_2:
    show bg bathwithmom_9
    mum "..."
    show bg bathwithmom_10
    mum "I locked myself in there to hide it from you and [sister]."
    mum "I didn't want you two worrying and taking sides."
    show bg bathwithmom_9
    if winc == 0:
        pov "[missus]!"
    else:
        pov "Mom!"
    pov "Tell me you're not serious with that logic."
    show bg bathwithmom_11
    pov "Aren't we all in this together? How could we ever forgive him?"
    pov "I know I can never forgive him now!"
    pov "And to think that I actually respected him before."
    show bg bathwithmom_16
    mum "[povname]... It's alright."
    mum "Scars and wounds heal."
    mum "I'll be okay."
    show bg bathwithmom_9
    pov "It is still unacceptable."
    show bg bathwithmom_16
    mum "Hey, how about this?"
    mum "If he ever does this to me again, kick his teeth in for me."
    show bg bathwithmom_19
    pov "You fuckin' bet I will, that bastard deserves it right now."
    show bg bathwithmom_10
    mum "Just... please. Let this go for now. I rather not linger on this subject for longer than it has been on my face."
    show bg bathwithmom_11
    pov "..."

    menu:
        "At least it looks like it'll be healed soon.":
            show bg bathwithmom_19
            pov "At least it looks like it'll be healed soon."
            show bg bathwithmom_18
            mum "Yeah..."
        "You still look pretty to me." if skill_cha >= 3:
            if skill_cha >= 3:
                $ skill_cha -= 3
            else:
                $ skill_cha = 0
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("You used 5 Charisma Points\nYour relationship with [missus] has increased")
            else:
                $ renpy.notify("You used 5 Charisma Points\nYour relationship with Mom has increased")
            show bg bathwithmom_19
            pov "You still look pretty to me."
            show bg bathwithmom_16
            mum "Thanks, sweetie."
        "You still look beautiful as ever." if skill_cha >= 5:
            if skill_cha >= 5:
                $ skill_cha -= 5
            else:
                $ skill_cha = 0
            if mum_points <= 8:
                $ mum_points += 2
            else:
                $ mum_points = 10
            if winc == 0:
                $ renpy.notify("You used 5 Charisma Points\nYour relationship with [missus] has increased by 2")
            else:
                $ renpy.notify("You used 5 Charisma Points\nYour relationship with Mom has increased by 2")
            show bg bathwithmom_19
            if winc == 0:
                pov "You still look beautiful as ever, [missus]"
            else:
                pov "You still look beautiful as ever, mom"
            show bg bathwithmom_16
            mum "That really means a lot, honey."
    show bg bathwithmom_17
    mum "..."
    show bg bathwithmom_18
    mum "The tub used to have a lot more space when you were younger."
    show bg bathwithmom_19
    pov "Either this tub is smaller than the one back home, or I've grown a lot since then."
    show bg bathwithmom_20
    mum "Hmm.. I think it must be the smaller tub."
    show bg bathwithmom_21
    pov "Haha, yeah."
    show bg bathwithmom_18
    mum "Damn, I really miss that tub back home."
    mum "That was definitely my home away from home..."
    show bg bathwithmom_16
    mum "At home..."
    show bg bathwithmom_19
    pov "I miss back home."
    pov "It was a lot simpler back then, everything was a lot simpler."
    show bg bathwithmom_18
    if winc == 0:
        mum "I remember our household being a lot happier."
    else:
        mum "I remember our family being a lot happier."
    show bg bathwithmom_17
    pov "Man, adulthood really screwed us over, didn't it?"
    show bg bathwithmom_20
    mum "The transition isn't the most welcoming, I'll tell you that."
    show bg bathwithmom_16
    mum "But believe me, it'll get better with time."
    show bg bathwithmom_19
    pov "Let's hope so."
    show bg bathwithmom_21
    pov "Hehe..."
    show bg bathwithmom_22
    pov "Hehehe..."
    mum "..."
    show bg bathwithmom_23
    mum "Are you okay there?"
    show bg bathwithmom_21
    pov "Hmm? Yeah, I was just wondering how crowded it'd be if [sister] joined us."
    show bg bathwithmom_20
    mum "Well, aren't you a perv?"
    show bg bathwithmom_21
    pov "What? No. You know what I mean... just think about the tight fit."
    show bg bathwithmom_20
    if winc == 0:
        mum "Now, now, [povname]. Let's not talk about how tight your [sisrole] is."
    else:
        mum "Now, now, [povname]. Let's not talk about how tight your sister is."
    show bg bathwithmom_21
    if winc == 0:
        pov "[missus]! C'mon, I wasn't even-"
    else:
        pov "Mom! C'mon, I wasn't even-"
    show bg bathwithmom_24
    mum "I bet you're now wondering about how tight I am..."
    show bg bathwithmom_25
    if winc == 0:
        pov "[missus]..."
    else:
        pov "M-mom..."
    pov "You're the perverted one here..."
    show bg bathwithmom_26
    mum "I'm not the one with a boner."
    show bg bathwithmom_25
    pov "A bone- what? I don't hav-"
    show bg bathwithmom_27
    with hpunch
    $ renpy.pause()
    show bg bathwithmom_28
    with vpunch
    $ renpy.pause()
    pov "..."
    show bg bathwithmom_29
    mum "I'm sorry, did I leave you speechless?"
    show bg bathwithmom_28
    pov "..."
    pov "Hm.. wh- what?"
    show bg bathwithmom_30
    mum "Hehehe, you're so cute."
    show bg bathwithmom_28
    mum "..."
    show bg bathwithmom_29
    mum "Hey, since you've already accused me of being a pervert."
    show bg bathwithmom_31
    mum "Do you want to masturbate together?"

    menu:
        "Why not?":
            show bg bathwithmom_32
            pov "Sure, why not. It'll be a good bonding moment."
            show bg bathwithmom_31
            mum "Mhmm. Exactly."
            show bg bathwithmom_32
            if winc == 0:
                pov "Just you and me, [mumrole] and her [povmumrole]."
            else:
                pov "Just you and me, mother and her son."
            pov "Jerking it."
            show bg bathwithmom_29
            mum "Are you feeling awkward?"
            show bg bathwithmom_32
            pov "What? No. How could I feel anymore awkward than what this is."
            show bg bathwithmom_29
            mum "Take a deep breath, baby. Baths are meant to relieve stress."
            show bg bathwithmom_32
            pov "{i}*Deep inhale*{/i}"
            pov "{i}*Exhale*{/i}"

            jump lbl_bath_with_mom_3
        "Just masturbating?":
            show bg bathwithmom_33
            pov "Just masturbating? Can't I fuck you already?"
            show bg bathwithmom_34
            mum "Ugh, you boys these days have no class."
            show bg bathwithmom_32
            pov "I have class..."
            show bg bathwithmom_33
            pov "From Monday to Friday."
            pov "Hahahahaha!"
            mum "..."
            show bg bathwithmom_34
            mum "I don't know how to feel about everything you just said."
            show bg bathwithmom_33
            pov "So can we fu-"
            show bg bathwithmom_34
            mum "No."
            show bg bathwithmom_29
            mum "Just-"
            mum "Shut your mouth and stroke your dick for me."
            show bg bathwithmom_28
            if winc == 0:
                pov "Jeez... fine, [missus]."
            else:
                pov "Jeez... fine, Mom."

            jump lbl_bath_with_mom_3
        "Not really...":
            show bg bathwithmom_33
            pov "Not really... It's a little awkward, don't you think?"
            show bg bathwithmom_35
            mum "Don't you love me?"
            show bg bathwithmom_36
            if winc == 0:
                pov "I do! I just, what does that have to d-? You're my [mumrole], [missus]."
            else:
                pov "I do! I just, what does that have to d-? You're my mom, Mom."
                show bg bathwithmom_37
                mum "You came out this vagina."
            show bg bathwithmom_38
            mum "Let's do it. It'll be fun."

            menu:
                "It's still a no.":
                    show bg bathwithmom_33
                    pov "It's still a no, unfortunately."
                    show bg bathwithmom_39
                    mum "{i}*sigh*{/i} Alright. I honestly thought you were gonna be up for it."
                    show bg bathwithmom_40
                    mum "Wasn't this what you were hoping for?"
                    show bg bathwithmom_39
                    mum "Y'know what, don't answer that. I shouldn't be asking you that."
                    show bg bathwithmom_42
                    pov "I-"
                    show bg bathwithmom_41
                    mum "Ah ah ah.. shhhh. No talking. Let me just lay here and relax."
                    show bg bathwithmom_42
                    pov "..."
                    show bg bathwithmom_8
                    $ renpy.pause()
                    scene black
                    with fade
                    "Later..."
                    scene bg myhallway_day
                    with fade
                    $ mum_path = 17

                    jump lbl_myhallway_day_setup
                "I never expected to be peer-pressured by my own mom." if winc == 1:
                    show bg bathwithmom_32
                    pov "Jeez, I never expected to be peer-pressured by my own mom into masturbating together."
                    show bg bathwithmom_30
                    mum "Consider yourself lucky. From the amount of mother-son incest pornographies on the intern-"
                    show bg bathwithmom_32
                    pov "What? Mothe-"
                    show bg bathwithmom_29
                    mum "Huh? What? Shhh, let's just do it."

                    jump lbl_bath_with_mom_3
                "I never expected to be peer-pressured by my [mumrole]." if winc == 0:
                    show bg bathwithmom_32
                    pov "Jeez, I never expected to be peer-pressured by my own [mumrole] into masturbating together."
                    show bg bathwithmom_30
                    mum "Consider yourself lucky. From the amount of [mumrole]-[povmumrole] pornographies on the intern-"
                    show bg bathwithmom_32
                    pov "What? [missus]-"
                    show bg bathwithmom_29
                    mum "Huh? What? Shhh, let's just do it."

                    jump lbl_bath_with_mom_3

label lbl_bath_with_mom_3:
    show bg bathwithmom_51
    mum "Match my speed, okay, baby?"
    show bg bathwithmom_44
    pov "Alright."
    show bg bathwithmom_51
    mum "I don't want you cumming too prematurely."
    show bg bathwithmom_44
    pov "Pssh, talk for yourself. I can last forever."
    show bg bathwithmom_59_1
    mum "Jus- shhh!"
    #$ bathwithmom_counter = 0

    jump lbl_bath_with_mom_3_1

label lbl_bath_with_mom_3_1: ## Stage 1 - Slow warm up
#    $ bathwithmom_counter += 1
#    show bg bathwithmom_43
#    $ renpy.pause(0.5,hard=True)
#    show bg bathwithmom_44
#    $ renpy.pause(0.5,hard=True)

#    jump lbl_bath_with_mom_3_counter
    scene img_bath_with_mom_3_1

    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_bath_with_mom_3_counter
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_bath_with_mom_3_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_bath_with_mom_3_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_bath_with_mom_3_1
image img_bath_with_mom_3_1:
    "bg bathwithmom_43"
    pause 0.5
    "bg bathwithmom_44"
    pause 0.5
    repeat

label lbl_bath_with_mom_3_2: ## Stage 2 - Getting into it
#    $ bathwithmom_counter += 1
#    show bg bathwithmom_45
#    $ renpy.pause(0.4,hard=True)
#    show bg bathwithmom_46
#    $ renpy.pause(0.4,hard=True)

#    jump lbl_bath_with_mom_3_counter
    scene img_bath_with_mom_3_2

    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_bath_with_mom_3_counter
    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_bath_with_mom_3_3
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_bath_with_mom_3_2

image img_bath_with_mom_3_2:
    "bg bathwithmom_45"
    pause 0.4
    "bg bathwithmom_46"
    pause 0.4
    repeat

label lbl_bath_with_mom_3_3: ## Stage 3 - Almost there
#    $ bathwithmom_counter += 1
#    show bg bathwithmom_47
#    $ renpy.pause(0.3,hard=True)
#    show bg bathwithmom_48
#    $ renpy.pause(0.3,hard=True)

#    jump lbl_bath_with_mom_3_counter
    scene img_bath_with_mom_3_3

    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_bath_with_mom_3_counter
    else:
        $ renpy.pause(10,hard=True)
        jump lbl_bath_with_mom_3_3


image img_bath_with_mom_3_3:
    "bg bathwithmom_47"
    pause 0.3
    "bg bathwithmom_48"
    pause 0.3
    repeat


label lbl_bath_with_mom_3_counter:
    #if skill_sta <= 5 and bathwithmom_counter == 5:
    #    jump lbl_bath_with_mom_4_1
    #elif skill_sta <= 10:
    #    if bathwithmom_counter <= 5:
    #        jump lbl_bath_with_mom_3_1
    #    elif bathwithmom_counter <= 10:
    #        jump lbl_bath_with_mom_3_2
    #    elif bathwithmom_counter == 16:
    #        jump lbl_bath_with_mom_4_2
    #elif skill_sta <= 15:
    #    if bathwithmom_counter <= 6:
    #        jump lbl_bath_with_mom_3_1
    #    elif bathwithmom_counter <= 12:
    #        jump lbl_bath_with_mom_3_2
    #    elif bathwithmom_counter <= 18:
    #        jump lbl_bath_with_mom_3_3
    #    elif bathwithmom_counter <= 25:
    #        jump lbl_bath_with_mom_4_3
    #elif skill_sta >= 16:
    #    call screen scr_bathwithmom_masturbate
    #else:
    #    jump lbl_bath_with_mom_3_1
    if skill_sta <= 7:
        #$ renpy.pause(10,hard=True)
        jump lbl_bath_with_mom_4_1
    elif skill_sta <= 14:
        #$ renpy.pause(15,hard=True)
        jump lbl_bath_with_mom_4_2

    elif skill_sta <= 20:
        #$ renpy.pause(20,hard=True)
        call screen scr_bathwithmom_masturbate

    else:
        #$ renpy.pause(10,hard=True)
        jump lbl_bath_with_mom_3_1


screen scr_bathwithmom_masturbate():
    imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_bath_with_mom_4_4")
    imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_bath_with_mom_4_3")

label lbl_bath_with_mom_4_1:
    scene bg bathwithmom_52_1
    pov "Oh, fuuck...!"
    show bg bathwithmom_52_2
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_3
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_4
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_5
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_6
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_7
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_8
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_52_9
    $ renpy.pause()
    show bg bathwithmom_53
    mum "Last forever, did you say?"
    show bg bathwithmom_54
    pov "I- was... just so... turned on!"
    show bg bathwithmom_55
    mum "Yeah, nice save there, [povname]."
    show bg bathwithmom_56
    mum "Hehehe, it's alright. I'll finish myself off some other time."
    show bg bathwithmom_57
    pov "I'd be more than happy to just watch you."
    show bg bathwithmom_58
    mum "No, no. It's alright. I'll survive."

    jump lbl_bath_with_mom_5

label lbl_bath_with_mom_4_2:
    scene bg bathwithmom_59_1
    if winc == 0:
        pov "[missus]... I- I'm gonna cum..."
    else:
        pov "Mom... I- I'm gonna cum..."
    show bg bathwithmom_59_2
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_3
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_4
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_5
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_6
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_7
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_8
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_59_9
    $ renpy.pause()
    show bg bathwithmom_60
    mum "{i}*pant*{/i} Oh... you... we... were supposed... {i}*gulp*{/i} to cum... together."
    show bg bathwithmom_54
    pov "Sorry... I... fuck... I was just so ready to cum on you."
    show bg bathwithmom_60
    mum "It's... alright... ugh fuck. Edging is making my clit so fucking sensitive..."
    show bg bathwithmom_61
    mum "Sorry... language."
    show bg bathwithmom_57
    pov "Don't you wanna cum?"
    show bg bathwithmom_58
    mum "Hmm? No.. no... it's alright. My body feels so good right now."

    jump lbl_bath_with_mom_5

label lbl_bath_with_mom_4_3:
    scene bg bathwithmom_62_1
    pov "Fucck!"
    mum "Oh, fuck... baby!"
    show bg bathwithmom_62_2
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_3
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_4
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_5
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_6
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_7
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_8
    $ renpy.pause(0.3,hard=True)
    show bg bathwithmom_62_9
    $ renpy.pause()
    show bg bathwithmom_63
    $ renpy.pause(2,hard=True)
    show bg bathwithmom_64
    pov "That felt..."
    show bg bathwithmom_63
    mum "Soo..."
    show bg bathwithmom_64
    pov "Fuc-"
    show bg bathwithmom_63
    mum "Good..."
    show bg bathwithmom_64
    pov "Heh... yeah..."
    if mum_points <= 9:
        $ mum_points += 1
    else:
        $ mum_points = 10
    if winc == 0:
        $ renpy.notify("Your relationship with [missus] has increased")
    else:
        $ renpy.notify("Your relationship with Mom has increased")

    jump lbl_bath_with_mom_5

label lbl_bath_with_mom_4_4:
    scene bg bathwithmom_49
    if winc == 0:
        pov "Fuck... [missus]... stop..."
    else:
        pov "Fuck... Mom... stop..."
    show bg bathwithmom_50
    pov "Slow down..."
    show bg bathwithmom_49
    pov "Don't cum yet."
    show bg bathwithmom_50
    pov "I- I want to keep edging."
    show bg bathwithmom_51
    mum "Y-yeah... Me- me too."
    #$ bathwithmom_counter = 0

    jump lbl_bath_with_mom_3_1

label lbl_bath_with_mom_5:
    scene bg bathwithmom_65
    mum "I love you, [povname]. Thank you for coming in here with me."
    mum "Your company was really all I needed."
    show bg bathwithmom_57
    pov "I'll be there for you when you need it. Remember that."
    pov "Burn it in your brain."
    show bg bathwithmom_66
    mum "Oh, don't you worry about that. I will."
    show bg bathwithmom_57
    mum "..."
    show bg bathwithmom_65
    mum "Hey, [povname]?"
    show bg bathwithmom_67
    pov "Mhmm?"
    show bg bathwithmom_65
    mum "Thanks... for everything. I don't know what I'd do without you."
    show bg bathwithmom_55

    scene black
    with fade
    "Afterwards..."

    scene bg myhallway_day
    with fade
    #mum "Have you ever gotten a facial before?"
    #show bg bathwithmom_68
    #pov "A facial? What do you mea-"
    #show bg bathwithmom_8
    #$ renpy.pause(2,hard=True)
    #show bg bathwithmom_69_1
    #$ renpy.pause(0.3,hard=True)
    #show bg bathwithmom_69_2
    #$ renpy.pause(0.3,hard=True)
    #show bg bathwithmom_70
    #mum "HAHAHAHA!"
    #show bg bathwithmom_71
    #pov "MOM! WHAT THE HELL?!"
    #show bg bathwithmom_72
    #pov "{i}*cough cough cough*{/i}"
    #show bg bathwithmom_73
    #mum "Nyehehehe!"
    $ mum_path = 17

    jump lbl_myhallway_day_setup
