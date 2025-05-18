## Cheer Mom Up Pt 2 - Go get a Smart TV Box ##
label lbl_cheermomup_pt2:
    if winc == 0:
        jump lbl_cheermomup_pt2_winc0

    scene bg cheermomup_1
    with fade
    "{i}*Knock knock*{/i}"
    show bg cheermomup_2
    pov "Mom?"
    show bg cheermomup_1
    mum "Yeah? Honey, is that you?"
    show bg cheermomup_8
    pov "Yeah, it's me, Mom!"
    pov "I've got the icecream for you!"
    show bg cheermomup_2
    mum "Really?! I'll come to the door and grab it off you."
    show bg cheermomup_8
    pov "You don't have to get outta bed, I can bring it to you."
    show bg cheermomup_10
    mum "I have to unlock the door anyway, hold on."

    scene black
    with fade
    "She opened the door just enough for you to hand over the icecream through the crack."
    "You couldn't see her through the crack as she was out of sight."
    "Only her hand was visible peeking from out behind the door."
    $ renpy.notify("You gave Mom the Icecream")

    scene bg cheermomup_5
    with fade
    $ renpy.pause()
    show bg cheermomup_9
    pov "Um... how is it?"
    if inventory.has_item(Items.icecream4):
        $ inventory.drop(Items.icecream4)
        show bg cheermomup_4
        mum "It tastes... I- I can't describe it... what flavour is this?"
        show bg cheermomup_2
        pov "Uhh... what do you think it is?"
        show bg cheermomup_3
        mum "I don't know... It's very vanilla but it's got a kick to it."
        show bg cheermomup_10
        mum "It's not the greatest thing I've put in my mouth but damn.. why is it so addicting?"
        show bg cheermomup_9
        pov "Addicting? Mom?! Are you okay?"
        show bg cheermomup_4
        mum "{i}*Lick lick lick*{/i}"
        show bg cheermomup_7
        pov "Mom?"
        show bg cheermomup_3
        mum "{i}*Sluurrp*{/i} Mmm..."
    elif inventory.has_item(Items.icecream1):
        $ inventory.drop(Items.icecream1)
        show bg cheermomup_2
        pov "That's what you wanted, right?"
        show bg cheermomup_3
        mum "Mhmm... my gawhd... ish shuper shticky fo' shome reaashon."
        show bg cheermomup_7
        pov "It sounds like you just ate a spoonful of glue."
        show bg cheermomup_10
        mum "{i}*gulp*{/i} No, no. It's really good. {i}*lick*{/i}"
        mum "{i}*lick lick* *gulp*{/i} Mmmahhh! Ngyumm..."
    elif inventory.has_item(Items.icecream2):
        $ inventory.drop(Items.icecream2)
        show bg cheermomup_1
        mum "Mmm, this one's pretty. Red Velvet is it?"
        show bg cheermomup_8
        pov "It's ‘Rare Velvet' actually."
        show bg cheermomup_3
        mum "What's so rare about it?"
        show bg cheermomup_2
        pov "I have no idea."
        show bg cheermomup_4
        mum "Mmm! *lick* It's really good, [povname]. Good choice."
        show bg cheermomup_10
        mum "{i}*lick lick lick*{/i} Mmmmh.."
    elif inventory.has_item(Items.icecream3):
        $ inventory.drop(Items.icecream3)
        show bg cheermomup_4
        mum "Ooohuhu! I like this one. Does this one have any alcohol in it?"
        show bg cheermomup_7
        pov "I don't know. It shouldn't though."
        show bg cheermomup_1
        mum "Hmmm.. whatever it is, it... {i}*gulp*{/i}"
        show bg cheermomup_10
        mum "Mmmm.. {i}*lick lick*{/i} mhmm..."
        show bg cheermomup_9
        pov "Mom?"
        show bg cheermomup_10
        mum "Hmm? Sorry.. this one's weirdly making me sleepy."
        show bg cheermomup_7
        pov "Are you alright?"
        show bg cheermomup_4
        mum "Yeah, don't worry about me."
        show bg cheermomup_2
        pov "You sure?"
        show bg cheermomup_3
        mum "{i}*slurrrp*{/i} Nyumm.. {i}*lick*{/i}"
    show bg cheermomup_7
    pov "Uhh.."
    show bg cheermomup_2
    pov "I guess I'll leave you to that."
    show bg cheermomup_4
    mum "[povname]! Wait, hold on. Could you by any chance set up WebFlicks for me?"
    show bg cheermomup_2
    pov "Can't you watch it on your laptop?"
    show bg cheermomup_3
    mum "No, I meant, I wanna watch it on the TV."
    show bg cheermomup_2
    pov "You just gotta hook up the laptop to the-"
    show bg cheermomup_3
    mum "But I wanna.. y'know. Actually use my laptop with the TV on in the background."
    pov "..."
    show bg cheermomup_4
    mum "Please? Isn't there like a box thingy that you can get?"
    show bg cheermomup_7
    pov "{i}*sigh*{/i} I'll see what I can find."
    show bg cheermomup_1
    mum "Thanks, honey."
    $ mum_path = 13

    jump lbl_myhallway_day_setup

### NO WINC ###
label lbl_cheermomup_pt2_winc0:

    scene bg cheermomup_1
    with fade
    "{i}*Knock knock*{/i}"
    show bg cheermomup_2
    pov "[missus]?"
    show bg cheermomup_1
    mum "Yeah? Honey, is that you?"
    show bg cheermomup_8
    pov "Yeah, it's me, Mom!"
    pov "I've got the icecream for you!"
    show bg cheermomup_2
    mum "Really?! I'll come to the door and grab it off you."
    show bg cheermomup_8
    pov "You don't have to get outta bed, I can bring it to you."
    show bg cheermomup_10
    mum "I have to unlock the door anyway, hold on."

    scene black
    with fade
    "She opened the door just enough for you to hand over the icecream through the crack."
    "You couldn't see her through the crack as she was out of sight."
    "Only her hand was visible peeking from out behind the door."
    $ renpy.notify("You gave Mom the Icecream")

    scene bg cheermomup_5
    with fade
    $ renpy.pause()
    show bg cheermomup_9
    pov "Um... how is it?"
    if inventory.has_item(Items.icecream4):
        $ inventory.drop(Items.icecream4)
        show bg cheermomup_4
        mum "It tastes... I- I can't describe it... what flavour is this?"
        show bg cheermomup_2
        pov "Uhh... what do you think it is?"
        show bg cheermomup_3
        mum "I don't know... It's very vanilla but it's got a kick to it."
        show bg cheermomup_10
        mum "It's not the greatest thing I've put in my mouth but damn.. why is it so addicting?"
        show bg cheermomup_9
        pov "Addicting? [missus]?! Are you okay?"
        show bg cheermomup_4
        mum "{i}*Lick lick lick*{/i}"
        show bg cheermomup_7
        pov "[missus]?"
        show bg cheermomup_3
        mum "{i}*Sluurrp*{/i} Mmm..."
    elif inventory.has_item(Items.icecream1):
        $ inventory.drop(Items.icecream1)
        show bg cheermomup_2
        pov "That's what you wanted, right?"
        show bg cheermomup_3
        mum "Mhmm... my gawhd... ish shuper shticky fo' shome reaashon."
        show bg cheermomup_7
        pov "It sounds like you just ate a spoonful of glue."
        show bg cheermomup_10
        mum "{i}*gulp*{/i} No, no. It's really good. {i}*lick*{/i}"
        mum "{i}*lick lick* *gulp*{/i} Mmmahhh! Ngyumm..."
    elif inventory.has_item(Items.icecream2):
        $ inventory.drop(Items.icecream2)
        show bg cheermomup_1
        mum "Mmm, this one's pretty. Red Velvet is it?"
        show bg cheermomup_8
        pov "It's ‘Rare Velvet' actually."
        show bg cheermomup_3
        mum "What's so rare about it?"
        show bg cheermomup_2
        pov "I have no idea."
        show bg cheermomup_4
        mum "Mmm! *lick* It's really good, [povname]. Good choice."
        show bg cheermomup_10
        mum "{i}*lick lick lick*{/i} Mmmmh.."
    elif inventory.has_item(Items.icecream3):
        $ inventory.drop(Items.icecream3)
        show bg cheermomup_4
        mum "Ooohuhu! I like this one. Does this one have any alcohol in it?"
        show bg cheermomup_7
        pov "I don't know. It shouldn't though."
        show bg cheermomup_1
        mum "Hmmm.. whatever it is, it... {i}*gulp*{/i}"
        show bg cheermomup_10
        mum "Mmmm.. {i}*lick lick*{/i} mhmm..."
        show bg cheermomup_9
        pov "[missus]?"
        show bg cheermomup_10
        mum "Hmm? Sorry.. this one's weirdly making me sleepy."
        show bg cheermomup_7
        pov "Are you alright?"
        show bg cheermomup_4
        mum "Yeah, don't worry about me."
        show bg cheermomup_2
        pov "You sure?"
        show bg cheermomup_3
        mum "{i}*slurrrp*{/i} Nyumm.. {i}*lick*{/i}"
    show bg cheermomup_7
    pov "Uhh.."
    show bg cheermomup_2
    pov "I guess I'll leave you to that."
    show bg cheermomup_4
    mum "[povname]! Wait, hold on. Could you by any chance set up WebFlicks for me?"
    show bg cheermomup_2
    pov "Can't you watch it on your laptop?"
    show bg cheermomup_3
    mum "No, I meant, I wanna watch it on the TV."
    show bg cheermomup_2
    pov "You just gotta hook up the laptop to the-"
    show bg cheermomup_3
    mum "But I wanna.. y'know. Actually use my laptop with the TV on in the background."
    pov "..."
    show bg cheermomup_4
    mum "Please? Isn't there like a box thingy that you can get?"
    show bg cheermomup_7
    pov "{i}*sigh*{/i} I'll see what I can find."
    show bg cheermomup_1
    mum "Thanks, honey."
    $ mum_path = 13

    jump lbl_myhallway_day_setup
