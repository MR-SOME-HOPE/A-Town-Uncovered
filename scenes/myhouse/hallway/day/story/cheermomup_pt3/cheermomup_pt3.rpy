## Cheer Mom Up Pt 3 - Go get a Teddy Bear ##
label lbl_cheermomup_pt3:
    default cheermomup_owe = 0
    if winc == 0:
        jump lbl_cheermomup_pt3_winc0
    show bg cheermomup_4
    "{i}*Knock knock*{/i}"
    show bg cheermomup_7
    pov "Mom?"
    show bg cheermomup_4
    mum "Mhmm? Is that you, [povname]?"
    show bg cheermomup_2
    pov "Yes, Mom. It's still me."
    show bg cheermomup_3
    mum "What is it?"
    show bg cheermomup_8
    pov "I got you a Smart TV Box."
    show bg cheermomup_3
    mum "I already have a TV."
    show bg cheermomup_2
    pov "No, a Smart TV Box, it's like a little box you connect to your TV so you can watch your Webflicks."
    show bg cheermomup_1
    mum "Oh!! Right right, that thing. Thank you so much, baby. How much do I owe you?"

    menu:
        "$100.":
            $ cheermomup_owe = 0
            show bg cheermomup_8
            pov "$100."
            show bg cheermomup_1
            mum "Hmm, that's not too bad actually. I think?"
            mum "Hold on while I go grab my wallet, okay?"
            show bg cheermomup_8
            pov "Sure thing."
            scene black
            with fade
            "She opened the door just enough for you to hand over the Smart TV Box through the crack."
            "Again, she was hiding out of sight from the crack of the door."
            "Only her hand was visible, open to receiving the box"
            $ inventory.drop(Items.smarttvbox)
            $ inventory.money += 100
            $ renpy.notify("You gave Mom the Smart Box TV")
            $ renpy.pause(3,hard=True)
            $ renpy.notify("Current Balance: $[inventory.money]")
            $ renpy.pause(3,hard=True)
            show bg cheermomup_8
            with fade
            pov "And while I'm here, do you want me to come in and set this up for you?"
        "$200.":
            $ cheermomup_owe = 1
            show bg cheermomup_8
            pov "$200."
            show bg cheermomup_4
            mum "Really? That much? Oh, gosh..."
            show bg cheermomup_10
            mum "I uh, I'll pay you back some other time okay?"
            show bg cheermomup_9
            pov "I'll hold you to it."
            scene black
            with fade
            "She opened the door just enough for you to hand over the Smart TV Box through the crack."
            "Again, she was hiding out of sight from the crack of the door."
            "Only her hand was visible, open to receiving the box"
            $ inventory.drop(Items.smarttvbox)
            $ renpy.notify("You gave Mom the Smart Box TV")
            show bg cheermomup_9
            with fade
            pov "So do you want me to come in and set this up for you?"
        "$300.":
            $ cheermomup_owe = 2
            show bg cheermomup_8
            pov "$300."
            show bg cheermomup_10
            mum "$300! Why is it so expensive?!"
            show bg cheermomup_7
            pov "I don't know, that's all they have there."
            show bg cheermomup_4
            mum "I can't pay you right now, I'll get it to you eventually, okay?"
            show bg cheermomup_9
            pov "No problem."
            scene black
            with fade
            "She opened the door just enough for you to hand over the Smart TV Box through the crack."
            "Again, she was hiding out of sight from the crack of the door."
            "Only her hand was visible, open to receiving the box"
            $ inventory.drop(Items.smarttvbox)
            $ renpy.notify("You gave Mom the Smart Box TV")
            scene bg cheermomup_9
            with fade
            pov "So do you want me to come in and set this up for you?"
        "You don't owe me anything.":
            $ cheermomup_owe = 0
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with Mom has increased")
            else:
                $ mum_points = 10
            show bg cheermomup_8
            pov "No need, Mom. Think of this as my get well gift to you?"
            show bg cheermomup_10
            mum "What? No, baby. I can't accept that. That thing must've costed an arm."
            show bg cheermomup_9
            pov "I insist, Mom. I wanna prove to you that I can not only take care of myself but of you as well."
            show bg cheermomup_10
            mum "..."
            mum "{i}*Sniff*{/i} Really?"
            scene black
            with fade
            "She opened the door just enough for you to hand over the Smart TV Box through the crack."
            "Again, she was hiding out of sight from the crack of the door."
            "Only her hand was visible, open to receiving the box"
            $ inventory.drop(Items.smarttvbox)
            $ renpy.notify("You gave Mom the Smart Box TV")
            scene bg myhallway_day
            with fade
            show bg cheermomup_8
            pov "Hehe, so um.. do you want me to come in and set this up for you?"
    show bg cheermomup_4
    mum "I actually want to try and do it myself."
    pov "..."
    mum "..."
    mum "Hello?"
    show bg cheermomup_7
    pov "Sorry, did you just say you want to set this up... yourself?"
    show bg cheermomup_10
    mum "Hahaha, I know I can be bad with technology but it's about time I at least tried."
    mum "Maybe I'll learn something along the way so I won't be so embarrassing to talk to about it."
    show bg cheermomup_8
    pov "Hahaha, you know what? You have yourself a challenge."
    pov "It'll be a good brain-stimulating exercise for you."
    pov "Nothing too complicated, just gotta plug in a few things, set up your settings, and you're good to go."
    show bg cheermomup_1
    pov "..."
    show bg cheermomup_7
    pov "Mom?"
    show bg cheermomup_4
    mum "Yeah? What? Sorry, I kinda blanked out for a second."
    show bg cheermomup_7
    pov "Are you okay?"
    show bg cheermomup_1
    mum "Yeah, it was just... that sounds sooo boring."
    show bg cheermomup_8
    pov "Hahahaha! Just get your butt into gear."
    show bg cheermomup_1
    mum "..."
    show bg cheermomup_4
    mum "Oh, [povname]?"
    show bg cheermomup_7
    pov "Yes?"
    show bg cheermomup_4
    mum "Um... it's a little out of the ordinary to ask this of you but..."
    show bg cheermomup_7
    pov "Uh huh...?"
    show bg cheermomup_4
    mum "Well, me being a grown woman and all, a mother to you no doubt..."
    show bg cheermomup_7
    pov "What... is it?"
    show bg cheermomup_4
    mum "..."
    show bg cheermomup_3
    mum "I want a teddy bear."
    show bg cheermomup_2
    pov "A teddy bear?"
    show bg cheermomup_10
    mum "To hold and make lo- cuddle. To cuddle with..."
    show bg cheermomup_9
    pov "Sure...?"
    pov "I'll go and see what I can find."
    show bg cheermomup_10
    mum "Thanks, honey. It doesn't have to be expensive or big either, just something that'll keep me company here."
    show bg cheermomup_8
    pov "Alright, you hang on tight. Good luck again, with that box."
    show bg cheermomup_1
    mum "I'm gonna need it. Ughh..."
    $ mum_path = 14

    jump lbl_myhallway_day_setup

### NO WINC ###
label lbl_cheermomup_pt3_winc0:
    show bg cheermomup_4
    "{i}*Knock knock*{/i}"
    show bg cheermomup_7
    pov "[missus]?"
    show bg cheermomup_4
    mum "Mhmm? Is that you, [povname]?"
    show bg cheermomup_2
    pov "Yes, [missus]. It's still me."
    show bg cheermomup_3
    mum "What is it?"
    show bg cheermomup_8
    pov "I got you a Smart TV Box."
    show bg cheermomup_3
    mum "I already have a TV."
    show bg cheermomup_2
    pov "No, a Smart TV Box, it's like a little box you connect to your TV so you can watch your Webflicks."
    show bg cheermomup_1
    mum "Oh!! Right right, that thing. Thank you so much, baby. How much do I owe you?"

    menu:
        "$100.":
            $ cheermomup_owe = 0
            show bg cheermomup_8
            pov "$100."
            show bg cheermomup_1
            mum "Hmm, that's not too bad actually. I think?"
            mum "Hold on while I go grab my wallet, okay?"
            show bg cheermomup_8
            pov "Sure thing."
            scene black
            with fade
            "She opened the door just enough for you to hand over the Smart TV Box through the crack."
            "Again, she was hiding out of sight from the crack of the door."
            "Only her hand was visible, open to receiving the box"
            $ inventory.drop(Items.smarttvbox)
            $ inventory.money += 100
            $ renpy.notify("You gave Mom the Smart Box TV")
            $ renpy.pause(3,hard=True)
            $ renpy.notify("Current Balance: $[inventory.money]")
            $ renpy.pause(3,hard=True)
            show bg cheermomup_8
            with fade
            pov "And while I'm here, do you want me to come in and set this up for you?"
        "$200.":
            $ cheermomup_owe = 1
            show bg cheermomup_8
            pov "$200."
            show bg cheermomup_4
            mum "Really? That much? Oh, gosh..."
            show bg cheermomup_10
            mum "I uh, I'll pay you back some other time okay?"
            show bg cheermomup_9
            pov "I'll hold you to it."
            scene black
            with fade
            "She opened the door just enough for you to hand over the Smart TV Box through the crack."
            "Again, she was hiding out of sight from the crack of the door."
            "Only her hand was visible, open to receiving the box"
            $ inventory.drop(Items.smarttvbox)
            $ renpy.notify("You gave Mom the Smart Box TV")
            show bg cheermomup_9
            with fade
            pov "So do you want me to come in and set this up for you?"
        "$300.":
            $ cheermomup_owe = 2
            show bg cheermomup_8
            pov "$300."
            show bg cheermomup_10
            mum "$300! Why is it so expensive?!"
            show bg cheermomup_7
            pov "I don't know, that's all they have there."
            show bg cheermomup_4
            mum "I can't pay you right now, I'll get it to you eventually, okay?"
            show bg cheermomup_9
            pov "No problem."
            scene black
            with fade
            "She opened the door just enough for you to hand over the Smart TV Box through the crack."
            "Again, she was hiding out of sight from the crack of the door."
            "Only her hand was visible, open to receiving the box"
            $ inventory.drop(Items.smarttvbox)
            $ renpy.notify("You gave Mom the Smart Box TV")
            scene bg cheermomup_9
            with fade
            pov "So do you want me to come in and set this up for you?"
        "You don't owe me anything.":
            $ cheermomup_owe = 0
            if mum_points <= 9:
                $ mum_points += 1
                $ renpy.notify("Your relationship with [missus] has increased")
            else:
                $ mum_points = 10
            show bg cheermomup_8
            pov "No need, Mom. Think of this as my get well gift to you?"
            show bg cheermomup_10
            mum "What? No, baby. I can't accept that. That thing must've cost an arm and a leg."
            show bg cheermomup_9
            pov "I insist, Mom. I wanna prove to you that I can not only take care of myself but of you as well."
            show bg cheermomup_10
            mum "..."
            mum "{i}*Sniff*{/i} Really?"
            scene black
            with fade
            "She opened the door just enough for you to hand over the Smart TV Box through the crack."
            "Again, she was hiding out of sight from the crack of the door."
            "Only her hand was visible, open to receiving the box"
            $ inventory.drop(Items.smarttvbox)
            $ renpy.notify("You gave Mom the Smart Box TV")
            scene bg myhallway_day
            with fade
            show bg cheermomup_8
            pov "Hehe, so um.. do you want me to come in and set this up for you?"
    show bg cheermomup_4
    mum "I actually want to try and do it myself."
    pov "..."
    mum "..."
    mum "Hello?"
    show bg cheermomup_3
    pov "Sorry, did you just say you want to set this up... yourself?"
    show bg cheermomup_10
    mum "Hahaha, I know I can be bad with technology but it's about time I at least tried."
    mum "Maybe I'll learn something along the way so I won't be so embarrassing to talk to about it."
    show bg cheermomup_8
    pov "Hahaha, you know what? You have yourself a challenge."
    pov "It'll be a good brain-stimulating exercise for you."
    pov "Nothing too complicated, just gotta plug in a few things, set up your settings, and you're good to go."
    show bg cheermomup_1
    pov "..."
    show bg cheermomup_7
    pov "[missus]?"
    show bg cheermomup_4
    mum "Yeah? What? Sorry, I kinda blanked out for a second."
    show bg cheermomup_7
    pov "Are you okay?"
    show bg cheermomup_1
    mum "Yeah, it was just... that sounds sooo boring."
    show bg cheermomup_8
    pov "Hahahaha! Just get your butt into gear."
    show bg cheermomup_1
    mum "..."
    show bg cheermomup_4
    mum "Oh, [povname]?"
    show bg cheermomup_7
    pov "Yes?"
    show bg cheermomup_4
    mum "Um... it's a little out of the ordinary to ask this of you but..."
    show bg cheermomup_7
    pov "Uh huh...?"
    show bg cheermomup_4
    mum "Well, me being a grown woman and all, a [mumrole] to you no doubt..."
    show bg cheermomup_7
    pov "What... is it?"
    show bg cheermomup_4
    mum "..."
    show bg cheermomup_3
    mum "I want a teddy bear."
    show bg cheermomup_2
    pov "A teddy bear?"
    show bg cheermomup_10
    mum "To hold and make lo- cuddle. To cuddle with..."
    show bg cheermomup_9
    pov "Sure...?"
    pov "I'll go and see what I can find."
    show bg cheermomup_10
    mum "Thanks, honey. It doesn't have to be expensive or big either, just something that'll keep me company here."
    show bg cheermomup_8
    pov "Alright, you hang on tight. Good luck again, with that box."
    show bg cheermomup_1
    mum "I'm gonna need it. Ughh..."
    $ mum_path = 14

    jump lbl_myhallway_day_setup
