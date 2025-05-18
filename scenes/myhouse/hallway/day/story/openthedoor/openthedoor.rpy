## Open the Door ##
label lbl_open_the_door:
    if winc == 0:
        jump lbl_open_the_door_winc0

    scene bg cheermomup_1
    with fade
    "{i}*Knock knock*{/i}"
    show bg cheermomup_8
    pov "Mom?"
    show bg cheermomup_1
    mum "Yeah? I'm here."
    show bg cheermomup_8
    pov "Hehe... of course you are."
    show bg cheermomup_7
    pov "Did you get Webflicks working on the TV?"
    show bg cheermomup_1
    mum "Oh my God! I actually did!"
    show bg cheermomup_8
    pov "Really?!"
    show bg cheermomup_1
    mum "Oh, come now, [povname]. It wasn't that difficult."
    mum "You made it sound so much more complicated than it really was."
    show bg cheermomup_7
    pov "I mean, I didn't really but sure. Sorry about that."
    show bg cheermomup_4
    mum "Is there something wrong, baby?"
    show bg cheermomup_2
    pov "No, Mom. Nothing wrong on this side. I just came to drop off something."
    show bg cheermomup_4
    mum "Hm? What is it."
    show bg cheermomup_7
    pov "Don't tell me you forgot already."
    show bg cheermomup_1
    mum "Haha... sorry. My mind's been occupied with this show I'm watching."
    show bg cheermomup_8
    pov "I'm only going to give it to you if you let me in."
    show bg cheermomup_1
    mum "I-"
    show bg cheermomup_4
    mum "..."
    show bg cheermomup_3
    mum "No."
    show bg cheermomup_11
    pov "..."
    show bg cheermomup_12
    pov "What?"
    show bg cheermomup_13
    mum "No, [povname]. I can't let you in."

    menu:
        "Open the damn door!":
            show bg cheermomup_14
            with hpunch
            pov "Open the damn door, Mom! You've been in there for how frikkin long?"
            show bg cheermomup_12
            pov "... I miss you, Mom!"
            pov "Don't... don't shut me out!"
            show bg cheermomup_14
            pov "I'm your son for God's sake!"
            show bg cheermomup_12
            pov "Don't..."
            pov "Don't do this to me..."
            show bg cheermomup_11
            mum "..."
            mum "I'm sorry, [povname]... I don't want to do this to you."
            show bg cheermomup_12
            pov "Then why-?"
            show bg cheermomup_11
            mum "Because!"
            mum "{i}*Sniff*{/i} I... I..."
            mum "{i}*Sniff*{/i}"
            show bg cheermomup_13
            mum "Please, [povname]. Don't make me feel like this..."
            show bg cheermomup_14
            pov "You're still selfish. After the things I did for you."
            show bg cheermomup_13
            mum "[povname]... sweetie... please."
            pov "..."
            mum "[povname]?"
            pov "..."
        "You're not sick anymore.":
            show bg cheermomup_12
            pov "You're not sick anymore. You don't sound sick to me."
            pov "Please, Mom. Just let me in."
            show bg cheermomup_6
            pov "I don't care if I get sick, I just wanna see you."
            show bg cheermomup_11
            mum "I- I can't..."
            show bg cheermomup_14
            pov "What do you mean you can't?"
            show bg cheermomup_12
            pov "Mom... just open the door."
            show bg cheermomup_11
            mum "[povname]..."
            show bg cheermomup_14
            pov "Open the door, Mom."
            show bg cheermomup_13
            mum "I-"
            show bg cheermomup_14
            pov "Mom!"
            show bg cheermomup_13
            mum "..."
            show bg cheermomup_14
            with hpunch
            pov "Open this damn door!"
            show bg cheermomup_13
            mum "..."
            mum "I'm sorry..."
            mum "I'm doing this for you..."
            show bg cheermomup_14
            pov "You're doing this for yourself!"
        "After all the things I got for you?":
            show bg cheermomup_12
            pov "Even after all the things I got for you?"
            show bg cheermomup_11
            mum "..."
            mum "Honey, you know how grateful I am fo-"
            show bg cheermomup_12
            pov "No, no, no!"
            show bg cheermomup_14
            pov "No, you're not!"
            pov "If you were seriously grateful, you'd open this door and let me in!"
            show bg cheermomup_13
            mum "..."
            pov "..."
            show bg cheermomup_14
            with hpunch
            pov "Open this damn door!"
            show bg cheermomup_13
            mum "I can't let you in, [povname]!"
            show bg cheermomup_14
            pov "Why not!"
            show bg cheermomup_13
            mum "I just can't!"
            show bg cheermomup_14
            pov "Why are you shutting me out!"
            show bg cheermomup_13
            mum "I'm not!"
            show bg cheermomup_14
            pov "Yes, you fucking are! I'm your son for God's sake!"
            show bg cheermomup_14
            with hpunch
            pov "Let me in!"
            show bg cheermomup_13
            mum "... I- I'm sorry..."

    menu:
        "Leave the teddy bear by the door":
            if inventory.has_item(Items.teddybear3):
                $ cheermomup_doorbear = 3
                $ inventory.drop(Items.teddybear3)
                $ renpy.notify("You put the teddy bear by her door.")
            elif inventory.has_item(Items.teddybear2):
                $ cheermomup_doorbear = 2
                $ inventory.drop(Items.teddybear2)
                $ renpy.notify("You put the teddy bear by her door.")
            elif inventory.has_item(Items.teddybear1):
                $ cheermomup_doorbear = 1
                $ inventory.drop(Items.teddybear1)
                $ renpy.notify("You put the teddy bear by her door.")
        "Keep the teddy bear with you":
            $ renpy.notify("You keep the teddy bear with you.")
    $ mum_path = 15

    jump lbl_myhallway_day_setup

### NO WINC ###
label lbl_open_the_door_winc0:

    scene bg cheermomup_1
    with fade
    "{i}*Knock knock*{/i}"
    show bg cheermomup_8
    pov "[missus]?"
    show bg cheermomup_1
    mum "Yeah? I'm here."
    show bg cheermomup_8
    pov "Hehe... of course you are."
    show bg cheermomup_7
    pov "Did you get Webflicks working on the TV?"
    show bg cheermomup_1
    mum "Oh my God! I actually did!"
    show bg cheermomup_8
    pov "Really?!"
    show bg cheermomup_1
    mum "Oh, come now, [povname]. It wasn't that difficult."
    mum "You made it sound so much more complicated than it really was."
    show bg cheermomup_7
    pov "I mean, I didn't really but sure. Sorry about that."
    show bg cheermomup_4
    mum "Is there something wrong, baby?"
    show bg cheermomup_2
    pov "No, [missus]. Nothing wrong on this side. I just came to drop off something."
    show bg cheermomup_4
    mum "Hm? What is it."
    show bg cheermomup_7
    pov "Don't tell me you forgot already."
    show bg cheermomup_1
    mum "Haha... sorry. My mind's been occupied with this show I'm watching."
    show bg cheermomup_8
    pov "I'm only going to give it to you if you let me in."
    show bg cheermomup_1
    mum "I-"
    show bg cheermomup_4
    mum "..."
    show bg cheermomup_3
    mum "No."
    show bg cheermomup_11
    pov "..."
    show bg cheermomup_12
    pov "What?"
    show bg cheermomup_13
    mum "No, [povname]. I can't let you in."

    menu:
        "Open the damn door!":
            show bg cheermomup_14
            with hpunch
            pov "Open the damn door, [missus]! You've been in there for how frikkin long?"
            show bg cheermomup_12
            pov "... I miss you, [missus]!"
            pov "Don't... don't shut me out!"
            show bg cheermomup_14
            pov "I'm your [povmumrole] for God's sake!"
            show bg cheermomup_12
            pov "Don't..."
            pov "Don't do this to me..."
            show bg cheermomup_11
            mum "..."
            mum "I'm sorry, [povname]... I don't want to do this to you."
            show bg cheermomup_12
            pov "Then why-?"
            show bg cheermomup_11
            mum "Because!"
            mum "{i}*Sniff*{/i} I... I..."
            mum "{i}*Sniff*{/i}"
            show bg cheermomup_13
            mum "Please, [povname]. Don't make me feel like this..."
            show bg cheermomup_14
            pov "You're still selfish. After the things I did for you."
            show bg cheermomup_13
            mum "[povname]... sweetie... please."
            pov "..."
            mum "[povname]?"
            pov "..."
        "You're not sick anymore.":
            show bg cheermomup_12
            pov "You're not sick anymore. You don't sound sick to me."
            pov "Please, [missus]. Just let me in."
            show bg cheermomup_6
            pov "I don't care if I get sick, I just wanna see you."
            show bg cheermomup_11
            mum "I- I can't..."
            show bg cheermomup_14
            pov "What do you mean you can't?"
            show bg cheermomup_12
            pov "[missus]... just open the door."
            show bg cheermomup_11
            mum "[povname]..."
            show bg cheermomup_14
            pov "Open the door, [missus]."
            show bg cheermomup_13
            mum "I-"
            show bg cheermomup_14
            pov "[missus]!"
            show bg cheermomup_13
            mum "..."
            show bg cheermomup_14
            with hpunch
            pov "Open this damn door!"
            show bg cheermomup_13
            mum "..."
            mum "I'm sorry..."
            mum "I'm doing this for you..."
            show bg cheermomup_14
            pov "You're doing this for yourself!"
        "After all the things I got for you?":
            show bg cheermomup_12
            pov "Even after all the things I got for you?"
            show bg cheermomup_11
            mum "..."
            mum "Honey, you know how grateful I am fo-"
            show bg cheermomup_12
            pov "No, no, no!"
            show bg cheermomup_14
            pov "No, you're not!"
            pov "If you were seriously grateful, you'd open this door and let me in!"
            show bg cheermomup_13
            mum "..."
            pov "..."
            show bg cheermomup_14
            with hpunch
            pov "Open this damn door!"
            show bg cheermomup_13
            mum "I can't let you in, [povname]!"
            show bg cheermomup_14
            pov "Why not!"
            show bg cheermomup_13
            mum "I just can't!"
            show bg cheermomup_14
            pov "Why are you shutting me out!"
            show bg cheermomup_13
            mum "I'm not!"
            show bg cheermomup_14
            pov "Yes, you fucking are! I'm your [povmumrole] for God's sake!"
            show bg cheermomup_14
            with hpunch
            pov "Let me in!"
            show bg cheermomup_13
            mum "... I- I'm sorry..."

    menu:
        "Leave the teddy bear by the door":
            if inventory.has_item(Items.teddybear3):
                $ cheermomup_doorbear = 3
                $ inventory.drop(Items.teddybear3)
            elif inventory.has_item(Items.teddybear2):
                $ cheermomup_doorbear = 2
                $ inventory.drop(Items.teddybear2)
            elif inventory.has_item(Items.teddybear1):
                $ cheermomup_doorbear = 1
                $ inventory.drop(Items.teddybear1)
            $ renpy.notify("You put the teddy bear by her door.")
        "Keep the teddy bear with you":
            $ renpy.notify("You kept the teddy bear with you.")
    $ mum_path = 15

    jump lbl_myhallway_day_setup
