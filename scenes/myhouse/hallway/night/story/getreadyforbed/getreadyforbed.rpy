## Get Ready For Bed ##
label lbl_get_ready_for_bed:
## 1 = Less than $300, more than 7 points
## 2 = Less than $300, less than 7 points
## 3 = Less than $500, more than 7 points
## 4 = Less than $500, less than 7 points
## 5 = More than $500, Pay ALL or Less than 7 points
## 6 = More than $500, Pay SPLIT
    if dinnerdatewithmom_outcome == 1:
        show povf sad at left
        with dissolve
        show mumf bored_talk at right
        with dissolve
        mum "I guess I should say thanks for taking me out."
        show povf sad_talk at left
        show mumf bored at right
        pov "I hope you're not too mad about me not being able to pay for the entire meal."
        show povf sad at left
        show mumf bored_talk at right
        mum "It's kind of a bummer but it's alright, as long as you pay it back."
        mum "This was supposed to be your treat after all."
        show povf embarrassed_talk at left
        show mumf bored at right
        pov "Don't worry, Mom. I promise I'll get the money to you."
        show mumf embarrassed_talk at right
        mum "Thanks, we should get to bed, it's late."
    elif dinnerdatewithmom_outcome == 2:
        show povf sad at left
        with dissolve
        show mumf bored_talk at right
        with dissolve
        mum "I guess I should say thanks for taking me out but.."
        show povf sad_talk at left
        show mumf bored at right
        pov "I know, Mom. I'm sorry I didn't have enough money tonight."
        show povf sad at left
        show mumf bored_talk at right
        mum "Well, it was nice while it lasted."
        mum "You will pay me back right? This was supposed to be your treat."
        show povf embarrassed_talk at left
        show mumf bored at right
        pov "I will, I will. Don't you worry about a thing. I'll make up all the costs as I promised I would."
        show mumf embarrassed_talk at right
        mum "Good, we should get to bed, it's late."
    elif dinnerdatewithmom_outcome == 3:
        show povf embarrassed at left
        with dissolve
        show mumf neutral_talk at right
        with dissolve
        mum "Thank you for taking me out to dinner, sweetie. It was really, really nice."
        show povf sad_talk at left
        show mumf embarrassed at right
        pov "Sorry I was short on cash, Mom. I didn't think tonight would be {i}that{/i} expensive."
        show povf embarrassed at left
        show mumf embarrassed_talk at right
        mum "I'm still glad you thought to bring as much as you did tonight."
        mum "It must've been quite a shock seeing that bill."
        show mumf neutral_talk at right
        mum "Hehehehe. Welcome to being an adult with high class."
        show povf embarrassed_talk at left
        show mumf neutral at right
        pov "Don't expect this to be a common occurance."
        pov "I'll pay you back when I can."
        show mumf embarrassed_talk at right
        mum "Thanks, we should get to bed, it's late."
    elif dinnerdatewithmom_outcome == 4:
        show povf embarrassed at left
        with dissolve
        show mumf embarrassed_talk at right
        with dissolve
        mum "Thanks for taking me out to dinner."
        show povf sad_talk at left
        show mumf embarrassed at right
        pov "Sorry I was short on cash, Mom. I didn't think tonight would be {i}that{/i} expensive."
        show povf embarrassed at left
        show mumf embarrassed_talk at right
        mum "It's okay, at least you managed to cut most of the expense."
        mum "It must've been quite a shock seeing that bill."
        show povf embarrassed_talk at left
        show mumf embarrassed at right
        pov "Heh.. to be honest, yeah. I thought'd it'd be a lot cheaper than that."
        pov "I'll pay you back when I can, Mom."
        show mumf embarrassed_talk at right
        mum "Good, we should get to bed, it's late."
    elif dinnerdatewithmom_outcome == 5:
        show povf neutral at left
        with dissolve
        show mumf neutral_talk at right
        with dissolve
        mum "Thank you so much for taking me out to dinner, honey. It is definitely a night to remember."
        show povf smirk_talk at left
        show mumf embarrassed at right
        pov "It was my pleasure, Mom. A woman like you deserves to be treated like a queen."
        show povf smirk at left
        show mumf embarrassed_talk at right
        mum "Oh, stop. You're spoiling me. Don't spend all your money on me, baby."
        show mumf sad_talk at right
        mum "And don't look at me like that... I- It's turning m-"
        mum "Uhmm.."
        show mumf embarrassed_talk at right
        mum "We should get to bed, it's late."
    elif dinnerdatewithmom_outcome == 6:
        show povf neutral at left
        with dissolve
        show mumf embarrassed_talk at right
        with dissolve
        mum "Thank you so much for taking me out to dinner, honey. It is was an absolutely amazing."
        show povf neutral_talk at left
        show mumf smirk at right
        if winc == 0:
            pov "It was my pleasure, [missus] but I should be thanking you for sharing the bill."
        else:
            pov "It was my pleasure, Mom but I should be thanking you for sharing the bill."
        show povf embarrassed at left
        show mumf neutral_talk at right
        mum "Oh, don't even worry about it. You proved to me that you were capable of treating me."
        mum "I didn't want you to go into debt."
        show mumf smirk_talk at right
        mum "You massage my chest and I'll massage yours, am I right?"
        show povf smirk_talk at left
        show mumf smirk at right
        pov "I guess if you put it that way.."
        show povf smirk at left
        mum "Hehehe~"
        show mumf embarrassed_talk at right
        mum "We should get to bed, it's late."
    show povf embarrassed_talk at left
    show mumf embarrassed at right
    pov "Oh, hehe.. yeah."
    show povf embarrassed at left
    show mumf embarrassed_talk at right
    mum "..."
    mum "Goodnight, baby."
    mum "I love you..."
    if dinnerdatewithmom_outcome >= 5:
        show mumf sad_talk at right
        mum "So so much."
    show povf embarrassed_talk at left
    show mumf embarrassed at right
    if winc == 0:
        pov "I love you too, [missus]."
    else:
        pov "I love you too, Mom."
    $ mum_path = 28
    $ townmap_enabled = 0

    jump lbl_myhallway_night_setup
