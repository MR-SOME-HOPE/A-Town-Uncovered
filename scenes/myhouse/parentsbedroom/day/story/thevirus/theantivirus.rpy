## The Antivirus ##
label lbl_the_antivirus:
    if winc == 0:
        jump lbl_the_antivirus_winc0

    scene black
    with fade
    $ inventory.drop(Items.antiviruscd)
    "After installing the antivirus CD and running the scanner"

    scene bg thevirus_4_1
    with fade
    mum "Hey, how's the computer?"
    pov "It's almost done with the scan."
    mum "What's the scan for?"
    pov "It detects viruses and gets rid of them for you."
    mum "Oh, really? That's quite helpful."
    pov "I had to go out and buy an antivirus CD because the virus was messing with the wifi connectivity."

    menu:
        "You owe me $120.":
            pov "You owe me $120."
            mum "Oh, really..? Well.. I guess it is my laptop after all. I should've taken better care of it."
            mum "I'll give you the money now."
            pov "Great, thanks."
            $ inventory.money += 120
            $ renpy.notify("Current Balance: $[inventory.money]")
        "It was cheap.":
            pov "Luckily it was quite cheap."
            mum "Luckily."
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
    show bg thevirus_4_2
    pov "Oh, it's done!"
    mum "Can I have it back now?"
    pov "Hold on, let me just finish up."

    scene bg thevirus_4_2
    call screen scr_the_antivirus_1_0

screen scr_the_antivirus_1_0():
    add "bg thevirus_4_2"
    imagebutton auto "btn thevirus_done1_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_the_antivirus_1_1")

label lbl_the_antivirus_1_1:
    show bg thevirus_2_13
    with dissolve
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_12
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_11
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_10
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_9
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_8
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_7
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_6
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_5
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_4
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_3
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_2
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_1
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_1
    $ renpy.pause(1,hard=True)
    show bg thevirus_5
    with dissolve
    $ renpy.pause()
    show bg thevirusbed_1
    $ renpy.pause()

    menu:
        "Read the title":
            show bg thevirusbed_2
            pov "Mom... fucks son..."
            show bg thevirusbed_3
            mum "What?! What the hell is that?!"
            show bg thevirusbed_3
            mum "That.. that scanner must not have properly scanned this computer."
            show bg thevirusbed_4
            pov "Did you downlo-"
            show bg thevirusbed_5
            mum "They must've left this.. uh.. virus here."
            show bg thevirusbed_6
            mum "How rude of them."
            show bg thevirusbed_7
            pov "Who's them?"
            show bg thevirusbed_8
            mum "I- I don't know? THEM! The people who created the virus."
            show bg thevirusbed_9
            pov "You probab-"
            show bg thevirusbed_14
            mum "Sorry, let me just take this off your hands. Don't worry, I can rescan and- uh- or delete it myself."
        "Is this how you got the virus?":
            show bg thevirusbed_10
            pov "Mom... Is this how you got the viru-"
            show bg thevirusbed_3
            mum "What?! No?! I- I don't even know how this got here."
            show bg thevirusbed_4
            pov "Mom..?"
            show bg thevirusbed_11
            mum "Don't look at me like that, I know what I did and didn't do."
            show bg thevirusbed_12
            mum "I didn't download... ‘Mom fucks.... Son...”"
            show bg thevirusbed_14
            mum "Look, give it to me. I know how to delete. I'll do a rescan to make sure it has gotten rid of everthing."
        "Stay silent":
            show bg thevirusbed_13
            pov "..."
            show bg thevirusbed_14
            mum "Uhhh- I'll just take that back now..."
            pov "..."
            show bg thevirusbed_11
            mum "Don't look at me like that, you're misunderstanding."
            show bg thevirusbed_12
            mum "I- I didn't download this video."
            show bg thevirusbed_11
            mum "I swear I didn't! Don't judge me like that, I know you are."
            show bg thevirusbed_12
            mum "The scanner probably missed deleting this... uh.. virus."
            show bg thevirusbed_14
            mum "So, I'll just be taking that, thank you very much."

    menu:
        "I didn't know you watched porn.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
            show bg thevirusbed_15
            pov "I didn't know you watched porn..."
            show bg thevirusbed_16
            mum "It's not porn!"
            show bg thevirusbed_17
            pov "It's called ‘Mom fucks s-‘"
            show bg thevirusbed_16
            mum "I know what it's called!"
            show bg thevirusbed_18
            mum "It's- It's a... I- I don't know what it is! It's not mine!"
            show bg thevirusbed_19
            pov "A virus doesn't usually just download porn videos on people's compute-"
            show bg thevirusbed_20
            mum "I said it's not porn!"
            show bg thevirusbed_21
            mum "Just... thank you for fixing my computer for me but I can handle it from here."
        "Why are you watching this?":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
            show bg thevirusbed_15
            pov "Why are you watching this..?"
            show bg thevirusbed_22
            mum "What? I didn't watch this! It was probably... your Dad! Yeah."
            show bg thevirusbed_23
            mum "He must've some sort of fantasy of us or something..."
            show bg thevirusbed_19
            pov "But it's on your lapto-"
            show bg thevirusbed_20
            mum "I haven't watched it!"
            show bg thevirusbed_21
            mum "Just... thank you for fixing my computer for me but I can handle it from here."
        "It's nothing to be embarrassed about.":
            if mum_points <= 3:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with Mom has decreased")
                show bg thevirusbed_24
                pov "Mom, it's nothing to be embarrassed about..."
                show bg thevirusbed_25
                mum "What? I'm not embarrassed. I didn't download this video."
                mum "The virus must've implanted it and played it by itself."
                show bg thevirusbed_24
                pov "I don't think viruses generally do th-"
                show bg thevirusbed_20
                mum "Well, it certainly wasn't me! It was probably you, wasn't it?"
                show bg thevirusbed_19
                pov "I just fixed the computer."
                show bg thevirusbed_16
                mum "Well, good but it wasn't me, I swear."
                show bg thevirusbed_26
                mum "Just... thank you for fixing my computer for me but I can handle it from here."
            elif mum_points >= 4:
                show bg thevirusbed_24
                pov "Mom, it's nothing to be embarrassed about..."
                show bg thevirusbed_25
                mum "What? I'm not embarrassed..."
                show bg thevirusbed_27
                pov "Mom, we're both adults remember? You know I watch porn. And it's okay if you do too."
                show bg thevirusbed_28
                mum "It's a little awkward if you say it like that..."
                show bg thevirusbed_29
                pov "Mom. Weren't you the one going on about how you're my mother and that there shouldn't be anything to hide between us?"
                show bg thevirusbed_30
                mum "It was I."
                show bg thevirusbed_29
                pov "Well..?"
                show bg thevirusbed_31
                mum "Well, what? You want to watch this pornographic video with me?"

                menu:
                    "Why not?":
                        show bg thevirusbed_24
                        pov "Why not?"
                        show bg thevirusbed_33
                        mum "[povname]. I'm still your mother, you know that right?"
                        show bg thevirusbed_27
                        pov "Right.. sorry. What was I thinking?"
                    "That's not what I meant.":
                        show bg thevirusbed_32
                        pov "No, I mean, It's just fine that you do what you want to do."
                        show bg thevirusbed_34
                        mum "..."
                        show bg thevirusbed_30
                        mum "Thanks for being so mature about this."
                        show bg thevirusbed_35
                        pov "Don't sweat about it, Mom."
                        show bg thevirusbed_36
                        mum "And thanks, for saving my computer's life."
        "Do you have a fetish for me?":
            if mum_points <= 3:
                show bg thevirusbed_32
                pov "Do you have a fetish for me..?"
                show bg thevirusbed_16
                mum "[povname]! Wh-what are you even asking that for?!"
                show bg thevirusbed_20
                mum "Of course I don't have a ‘fetish' for you. You're my son."
                show bg thevirusbed_37
                pov "Yeah but, you have mother-son porn on ther-"
                show bg thevirusbed_20
                mum "I- I didn't put it there! I swear to God."
                mum "I'm not the type to watch pornography."
                show bg thevirusbed_21
                mum "Just... thank you for fixing my computer for me but I can handle it from here."
            elif mum_points >= 4:
                show bg thevirusbed_32
                pov "Do you have a fetish for me..?"
                show bg thevirusbed_22
                mum "[povname]! Wh-what are you even asking that for?"
                show bg thevirusbed_16
                mum "I'm your very own mother, not some fantasy woman who says she's your mother."
                show bg thevirusbed_37
                pov "I'm just asking, person to person."
                show bg thevirusbed_38
                mum "Well, you shouldn't be asking me those things, it's very wrong."
                show bg thevirusbed_21
                mum "And even if I did, it's ALL just a fantasy, understand?"
                show bg thevirusbed_28
                mum "You say you're old enough to understand but to you, there's still this blurry line between what can happen and what should stay inside your head."
                show bg thevirusbed_27
                pov "Alright, alright, Mom. I get it. Sorry I asked."
                show bg thevirusbed_39
                mum "I love you, [povname]. Don't think I don't."
                mum "Just not in that way."
                show bg thevirusbed_40
                pov "Heheh.. mom, it's okay. I didn't expect you to anyway. I'm just joking around."
                show bg thevirusbed_36
                mum "Heh.. But thank you again, for saving my laptop's life."
        "It's better if you scan it 3 times." if skill_cha >= 5:
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg thevirusbed_27
            pov "Alright. It's better if you scan it 3 times, just to be on the safe side."
            pov "Antivirus scans tend to miss a couple of things the first time around, I'm sure that was just one of them."
            show bg thevirusbed_30
            mum "Ye- yeah. Thanks, honey. I'll do as you say, just to be on the safe side."
    show bg thevirusbed_43
    mum "And um.. don't tell your father about this."

    menu:
        "Your secret is safe with me.":
            show bg thevirusbed_29
            pov "Sure, your secret is safe with me."
            show bg thevirusbed_30
            mum "Thanks, dear. I love you."
            show bg thevirusbed_42
            pov "Love you too, Mom."
        "About the porn?":
            show bg thevirusbed_19
            pov "About the porn?"
            show bg thevirusbed_16
            mum "What? No. About the computer."
            show bg thevirusbed_18
            mum "This is the third time he had to buy me a new one."
            show bg thevirusbed_27
            pov "Oh- right right. Yeah, you need to be a bit more careful with it."
            show bg thevirusbed_30
            mum "Anyways, thank you, dear. I love you."
            show bg thevirusbed_42
            pov "I love you too, Mom."
        "About the computer?":
            show bg thevirusbed_44
            pov "About the computer?"
            show bg thevirusbed_18
            mum "Yeah, this is the third time he had to buy me a new one."
            show bg thevirusbed_35
            pov "Don't worry, the secret is safe with me."
            show bg thevirusbed_45
            mum "Great, thanks dear. I love you."
            show bg thevirusbed_30
            pov "I love you too, Mom."
    $ mum_path = 4

    jump lbl_parentsbedroom_day_setup

### NO WINC ###
label lbl_the_antivirus_winc0:

    scene black
    with fade
    $ inventory.drop(Items.antiviruscd)
    "After installing the antivirus CD and running the scanner"

    scene bg thevirus_4_1
    with fade
    mum "Hey, how's the computer?"
    pov "It's almost done with the scan."
    mum "What's the scan for?"
    pov "It detects viruses and gets rid of them for you."
    mum "Oh, really? That's quite helpful."
    pov "I had to go out and buy an antivirus CD because the virus was messing with the wifi connectivity."

    menu:
        "You owe me $120.":
            pov "You owe me $120."
            mum "Oh, really..? Well.. I guess it is my laptop after all. I should've taken better care of it."
            mum "I'll give you the money now."
            pov "Great, thanks."
            $ inventory.money += 120
            $ renpy.notify("Current Balance: $[inventory.money]")
        "It was cheap.":
            pov "Luckily it was quite cheap."
            mum "Luckily."
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
    show bg thevirus_4_2
    pov "Oh, it's done!"
    mum "Can I have it back now?"
    pov "Hold on, let me just finish up."

    scene bg thevirus_4_2
    call screen scr_the_antivirus_1_0_winc0

screen scr_the_antivirus_1_0_winc0():
    add "bg thevirus_4_2"
    imagebutton auto "btn thevirus_done1_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_the_antivirus_1_1_winc0")

label lbl_the_antivirus_1_1_winc0:
    show bg thevirus_2_13
    with dissolve
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_12
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_11
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_10
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_9
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_8
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_7
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_6
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_5
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_4
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_3
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_2
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_2_1
    $ renpy.pause(0.1,hard=True)
    show bg thevirus_1
    $ renpy.pause(1,hard=True)
    if winc == 0:
        show bg thevirus_5_winc
    else:
        show bg thevirus_5
    with dissolve
    $ renpy.pause()
    show bg thevirusbed_1
    $ renpy.pause()

    menu:
        "Read the title":
            show bg thevirusbed_2
            pov "Milf... fucks young..."
            show bg thevirusbed_3
            mum "What?! What the hell is that?!"
            show bg thevirusbed_3
            mum "That.. that scanner must not have properly scanned this computer."
            show bg thevirusbed_4
            pov "Did you downlo-"
            show bg thevirusbed_5
            mum "They must've left this.. uh.. virus here."
            show bg thevirusbed_6
            mum "How rude of them."
            show bg thevirusbed_7
            pov "Who's them?"
            show bg thevirusbed_8
            mum "I- I don't know? THEM! The people who created the virus."
            show bg thevirusbed_9
            pov "You probab-"
            show bg thevirusbed_14
            mum "Sorry, let me just take this off your hands. Don't worry, I can rescan and- uh- or delete it myself."
        "Is this how you got the virus?":
            show bg thevirusbed_10
            pov "[missus]... Is this how you got the viru-"
            show bg thevirusbed_3
            mum "What?! No?! I- I don't even know how this got here."
            show bg thevirusbed_4
            pov "[missus]..?"
            show bg thevirusbed_11
            mum "Don't look at me like that, I know what I did and didn't do."
            show bg thevirusbed_12
            mum "I didn't download... ‘Milf fucks.... young...”"
            show bg thevirusbed_14
            mum "Look, give it to me. I know how to delete. I'll do a rescan to make sure it has gotten rid of everthing."
        "Stay silent":
            show bg thevirusbed_13
            pov "..."
            show bg thevirusbed_14
            mum "Uhhh- I'll just take that back now..."
            pov "..."
            show bg thevirusbed_11
            mum "Don't look at me like that, you're misunderstanding."
            show bg thevirusbed_12
            mum "I- I didn't download this video."
            show bg thevirusbed_11
            mum "I swear I didn't! Don't judge me like that, I know you are."
            show bg thevirusbed_12
            mum "The scanner probably missed deleting this... uh.. virus."
            show bg thevirusbed_14
            mum "So, I'll just be taking that, thank you very much."

    menu:
        "I didn't know you watched porn.":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
            show bg thevirusbed_15
            pov "I didn't know you watched porn..."
            show bg thevirusbed_16
            mum "It's not porn!"
            show bg thevirusbed_17
            pov "It's called ‘Milf fucks y-‘"
            show bg thevirusbed_16
            mum "I know what it's called!"
            show bg thevirusbed_18
            mum "It's- It's a... I- I don't know what it is! It's not mine!"
            show bg thevirusbed_19
            pov "A virus doesn't usually just download porn videos on people's compute-"
            show bg thevirusbed_20
            mum "I said it's not porn!"
            show bg thevirusbed_21
            mum "Just... thank you for fixing my computer for me but I can handle it from here."
        "Why are you watching this?":
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
            show bg thevirusbed_15
            pov "Why are you watching this..?"
            show bg thevirusbed_22
            mum "What? I didn't watch this! It was probably... your [dadrole]! Yeah."
            show bg thevirusbed_23
            mum "He must've some sort of fantasy of us or something..."
            show bg thevirusbed_19
            pov "But it's on your lapto-"
            show bg thevirusbed_20
            mum "I haven't watched it!"
            show bg thevirusbed_21
            mum "Just... thank you for fixing my computer for me but I can handle it from here."
        "It's nothing to be embarrassed about.":
            if mum_points <= 3:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with [missus] has decreased")
                show bg thevirusbed_24
                pov "[missus], it's nothing to be embarrassed about..."
                show bg thevirusbed_25
                mum "What? I'm not embarrassed. I didn't download this video."
                mum "The virus must've implanted it and played it by itself."
                show bg thevirusbed_24
                pov "I don't think viruses generally do th-"
                show bg thevirusbed_20
                mum "Well, it certainly wasn't me! It was probably you, wasn't it?"
                show bg thevirusbed_19
                pov "I just fixed the computer."
                show bg thevirusbed_16
                mum "Well, good but it wasn't me, I swear."
                show bg thevirusbed_26
                mum "Just... thank you for fixing my computer for me but I can handle it from here."
            elif mum_points >= 4:
                show bg thevirusbed_24
                pov "[missus], it's nothing to be embarrassed about..."
                show bg thevirusbed_25
                mum "What? I'm not embarrassed..."
                show bg thevirusbed_27
                pov "[missus], we're both adults remember? You know I watch porn. And it's okay if you do too."
                show bg thevirusbed_28
                mum "It's a little awkward if you say it like that..."
                show bg thevirusbed_29
                pov "[missus]. Weren't you the one going on about how you're my [mumrole] and that there shouldn't be anything to hide between us?"
                show bg thevirusbed_30
                mum "It was I."
                show bg thevirusbed_29
                pov "Well..?"
                show bg thevirusbed_31
                mum "Well, what? You want to watch this pornographic video with me?"

                menu:
                    "Why not?":
                        show bg thevirusbed_24
                        pov "Why not?"
                        show bg thevirusbed_33
                        mum "[povname]. I'm still your [mumrole], you know that right?"
                        show bg thevirusbed_27
                        pov "Right.. sorry. What was I thinking?"
                    "That's not what I meant.":
                        show bg thevirusbed_32
                        pov "No, I mean, It's just fine that you do what you want to do."
                        show bg thevirusbed_34
                        mum "..."
                        show bg thevirusbed_30
                        mum "Thanks for being so mature about this."
                        show bg thevirusbed_35
                        pov "Don't sweat about it, [missus]."
                        show bg thevirusbed_36
                        mum "And thanks, for saving my computer's life."
        "Do you have a fetish for me?":
            if mum_points <= 3:
                show bg thevirusbed_32
                pov "Do you have a fetish for me..?"
                show bg thevirusbed_16
                mum "[povname]! Wh-what are you even asking that for?!"
                show bg thevirusbed_20
                mum "Of course I don't have a ‘fetish' for you. You're my [povmumrole]."
                show bg thevirusbed_37
                pov "Yeah but, you have [mumrole]-[povmumrole] porn on ther-"
                show bg thevirusbed_20
                mum "I- I didn't put it there! I swear to God."
                mum "I'm not the type to watch pornography."
                show bg thevirusbed_21
                mum "Just... thank you for fixing my computer for me but I can handle it from here."
            elif mum_points >= 4:
                show bg thevirusbed_32
                pov "Do you have a fetish for me..?"
                show bg thevirusbed_22
                mum "[povname]! Wh-what are you even asking that for?"
                show bg thevirusbed_16
                mum "I'm your very own [mumrole], not some fantasy woman who says she's your [mumrole]."
                show bg thevirusbed_37
                pov "I'm just asking, person to person."
                show bg thevirusbed_38
                mum "Well, you shouldn't be asking me those things, it's very wrong."
                show bg thevirusbed_21
                mum "And even if I did, it's ALL just a fantasy, understand?"
                show bg thevirusbed_28
                mum "You say you're old enough to understand but to you, there's still this blurry line between what can happen and what should stay inside your head."
                show bg thevirusbed_27
                pov "Alright, alright, [missus]. I get it. Sorry I asked."
                show bg thevirusbed_39
                mum "I love you, [povname]. Don't think I don't."
                mum "Just not in that way."
                show bg thevirusbed_40
                pov "Heheh.. [missus], it's okay. I didn't expect you to anyway. I'm just joking around."
                show bg thevirusbed_36
                mum "Heh.. But thank you again, for saving my laptop's life."
        "It's better if you scan it 3 times." if skill_cha >= 5:
            if mum_points <= 9:
                $ mum_points += 1
            else:
                $ mum_points = 10
            $ renpy.notify("Your relationship with [missus] has decreased")
            show bg thevirusbed_27
            pov "Alright. It's better if you scan it 3 times, just to be on the safe side."
            pov "Antivirus scans tend to miss a couple of things the first time around, I'm sure that was just one of them."
            show bg thevirusbed_30
            mum "Ye- yeah. Thanks, honey. I'll do as you say, just to be on the safe side."
    show bg thevirusbed_43
    mum "And um.. don't tell your [dadrole] about this."

    menu:
        "Your secret is safe with me.":
            show bg thevirusbed_29
            pov "Sure, your secret is safe with me."
            show bg thevirusbed_30
            mum "Thanks, dear. I love you."
            show bg thevirusbed_42
            pov "Love you too, [missus]."
        "About the porn?":
            show bg thevirusbed_19
            pov "About the porn?"
            show bg thevirusbed_16
            mum "What? No. About the computer."
            show bg thevirusbed_18
            mum "This is the third time he's had to buy me a new one."
            show bg thevirusbed_27
            pov "Oh- right right. Yeah, you need to be a bit more careful with it."
            show bg thevirusbed_30
            mum "Anyways, thank you, dear. I love you."
            show bg thevirusbed_42
            pov "I love you too, [mumrole]."
        "About the computer?":
            show bg thevirusbed_44
            pov "About the computer?"
            show bg thevirusbed_18
            mum "Yeah, this is the third time he's had to buy me a new one."
            show bg thevirusbed_35
            pov "Don't worry, the secret is safe with me."
            show bg thevirusbed_45
            mum "Great, thanks dear. I love you."
            show bg thevirusbed_30
            pov "I love you too, [mumrole]."
    $ mum_path = 4

    jump lbl_parentsbedroom_day_setup
