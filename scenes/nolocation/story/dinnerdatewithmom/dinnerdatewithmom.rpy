## Dinner Date with Mom ##
default dinnerdatewithmom_owe = 0
default dinnerdatewithmom_outcome = 0

label lbl_dinner_date_with_mom:
    $ mum_points = 5

## 1 = Less than $300, more than 7 points

## 2 = Less than $300, less than 7 points

## 3 = Less than $500, more than 7 points

## 4 = Less than $500, less than 7 points

## 5 = More than $500, Pay ALL or Less than 7 points

## 6 = More than $500, Pay SPLIT
    if winc == 0:
        jump lbl_dinner_date_with_mom_winc0

    scene bg dinnerdatewithmom_1
    with fade
    $ renpy.pause()
    show bg dinnerdatewithmom_2
    mum "Wow, honey. Are you sure you're okay to eat here? This place looks like it costs a fortune..."
    show bg dinnerdatewithmom_3
    mum "These teeny breadsticks must be at least $10 each..."
    show bg dinnerdatewithmom_4
    pov "Mom, please, don't worry about it. Let's just clear our minds of it and enjoy the moment. Together."
    show bg dinnerdatewithmom_5
    mum "Okay, sweetie. This is honestly the most romantic thing anyone has done for me in a really long time."
    mum "I can't remember the last time your father..."
    show bg dinnerdatewithmom_6
    mum "Y'know, forget about your father. This is about us, right?"
    show bg dinnerdatewithmom_7
    pov "A night for just us. No Dad, no [sister], no interference."
    show bg dinnerdatewithmom_8
    mum "..."
    pov "What?"
    show bg dinnerdatewithmom_9
    mum "Hm? Nothing. I'm just admiring how good you look in that suit. You really do grow up so fast."
    mum "Like a real man now."
    show bg dinnerdatewithmom_10
    $ renpy.pause(1,hard=True)
    show bg dinnerdatewithmom_11
    pov "..."

    menu:
        "You think so?":
            pov "You really think so?"
            show bg dinnerdatewithmom_12
            mum "120 percent."
            show bg dinnerdatewithmom_11
            pov "Thanks, Mom."
        "You don't look too bad yourself." if skill_cha >= 3:
            pov "You don't look too bad yourself."
            show bg dinnerdatewithmom_13
            mum "Oh, I just threw this on. It's not that impressive."
            show bg dinnerdatewithmom_7
            pov "It looks good on you."
        "You don't look a year over 20." if skill_cha >= 6:
            $ skill_cha -= 3
            $ mum_points += 1
            $ renpy.notify("You used 3 Charisma Points\nYour relationship with Mom has increased")
            show bg dinnerdatewithmom_4
            pov "You don't look a year over 20."
            show bg dinnerdatewithmom_5
            mum "Oh, stop, that's not true."
            show bg dinnerdatewithmom_4
            pov "I'm serious, Mom. I feel weird even calling you ‘mom' to be frank with you."
            show bg dinnerdatewithmom_2
            mum "Hehe, really though? I'm starting to worry about wrinkles forming on my-"
            show bg dinnerdatewithmom_14
            pov "You look great, Mom."
        "You are the most stunning woman." if skill_cha >= 9:
            $ skill_cha -= 5
            $ mum_points += 2
            $ renpy.notify("You used 5 Charisma Points\nYour relationship with Mom has increased by 2")
            show bg dinnerdatewithmom_14
            pov "You are the most stunning woman."
            show bg dinnerdatewithmom_12
            mum "...in this room?"
            show bg dinnerdatewithmom_7
            pov "No."
            show bg dinnerdatewithmom_15
            mum "...that you've ever seen?"
            show bg dinnerdatewithmom_16
            pov "No."
            show bg dinnerdatewithmom_17
            mum "...in the world?"
            show bg dinnerdatewithmom_11
            pov "No, just. Stunning. Period."
            show bg dinnerdatewithmom_12
            mum "You're too much, [povname]."
    show bg dinnerdatewithmom_11
    $ renpy.pause()
    pov "I don't know about you but I'm ready to order mains."
    show bg dinnerdatewithmom_12
    mum "That makes two of us."
    show bg dinnerdatewithmom_18
    with fade
    pov "What are you craving for?"
    show bg dinnerdatewithmom_19
    mum "It all looks so good! Oh, gosh- it's how much?"
    show bg dinnerdatewithmom_20
    pov "Mom."
    show bg dinnerdatewithmom_21
    mum "Okay okay, I'll try not to cry."
    show bg dinnerdatewithmom_22
    mum "How about the Chef's Seafood Special?"
    show bg dinnerdatewithmom_23
    pov "Sounds good to me."
    show bg dinnerdatewithmom_24
    mum "How's about a bottle of chardonnay to go with that?"
    show bg dinnerdatewithmom_25
    pov "Whatever you want, Mom."
    show bg dinnerdatewithmom_26
    mum "Hehehe~"

    scene black
    with fade
    $ renpy.pause(1,hard=True)

    scene bg dinnerdatewithmom_27
    with fade
    mum "And then your sister said, I don't know Mom, we don't have a dog!"
    show bg dinnerdatewithmom_28
    pov "Oh my God, really? That's so bad."
    show bg dinnerdatewithmom_29
    mum "I love her to death but she can be so clueless sometimes."
    show bg dinnerdatewithmom_30
    pov "She's a weird one that is."
    pov "At least you raised one of us right."
    if mum_points >= 6:
        show bg dinnerdatewithmom_31
        mum "I raised the most beautiful boy in the world. I'm so happy to be here with you tonight."
        show bg dinnerdatewithmom_27
        mum "But don't get me wrong. [sister] is just as important to me as you are."
        show bg dinnerdatewithmom_33
        pov "You just love me a little more, right?"
        show bg dinnerdatewithmom_34
        mum "..." ##GRIN
        show bg dinnerdatewithmom_31
        mum "[sister] may be weird but you're definitely a smug one."
        show bg dinnerdatewithmom_32
        mum "At the end of the day, I consider myself lucky to have had twins."
    else:
        show bg dinnerdatewithmom_35
        mum "Hey! I raised two amazing children, thank you very much, young man. And it hasn't been easy."
        show bg dinnerdatewithmom_36
        pov "I can't imagine how hard it was for you, raising us twins. It's not like anyone expects twins when going for a child."
        show bg dinnerdatewithmom_29
        mum "Tell me about it. But I've always considered myself lucky."
    show bg dinnerdatewithmom_27
    mum "I mean, how often can a mother say that they are a mother of twins?"
    mum "To be honest with you, it brings up a lot of interest and conversations."
    if sister_points <= 3:
        show bg dinnerdatewithmom_30
        pov "All in all, being a twin, at least for me, isn't that bad."
        pov "Sure, we fight, we bicker, and yell till your ears bleed."
        pov "But there isn't anyone I would rather argue with than her."
    elif sister_points <= 7:
        show bg dinnerdatewithmom_30
        pov "I'm glad I'm a twin, jokes aside."
        pov "I can't imagine growing up without [sister]. She really brought out the fun in my life."
        pov "Would I consider her my ‘best friend'? That's a little too sappy to confirm."
        pov "But would I turn my back on her? Hell no."
    else:
        show bg dinnerdatewithmom_30
        pov "Yeah, I actually am really glad that I'm a twin."
        pov "[sister] is definitely a pain in my butt, but I can assure you that I'm a pain in hers too."
        pov "Maybe the term ‘best friend' may be pushing it but imagining a childhood without her just depresses me."
    show bg dinnerdatewithmom_29
    mum "You're a good brother. Arguments and immaturity aside. I can tell you really care for her."
    mum "Protect her, okay, [povname]?"
    show bg dinnerdatewithmom_30
    pov "I will, Mom. I don't hate her that much."
    show bg dinnerdatewithmom_37
    mum "I know, but I'm just telling you. If anything happens, it's her over me."
    mum "I can't continue living knowing my babies have suffered."
    show bg dinnerdatewithmom_38
    pov "Damn, Mom. Why are you so dark all of a sudden?"
    mum "..."
    show bg dinnerdatewithmom_32
    mum "Sorry, a Korean Drama flashed in my mind."
    show bg dinnerdatewithmom_30
    pov "Hehehe, fair enough."
    show bg dinnerdatewithmom_39
    mum "Oh, no..."
    show bg dinnerdatewithmom_40
    pov "What's wrong?"
    show bg dinnerdatewithmom_37
    mum "I'm out of wine. How about another for your dear old Mom?"
    show bg dinnerdatewithmom_30
    pov "Sure thing. I'll just flag someone down."

    scene black
    with fade
    $ renpy.pause(1,hard=True)

    scene bg dinnerdatewithmom_28
    with fade

    menu:
        "Nougat!":
            show bg dinnerdatewithmom_41
            pov "Nougat!"
            show bg dinnerdatewithmom_42
            mum "HAHAHAHAHA!"
            show bg dinnerdatewithmom_43
            mum "Oh my God! Nougat?"
        "A Lebanese midget!":
            show bg dinnerdatewithmom_41
            pov "A Lebanese midget!"
            show bg dinnerdatewithmom_42
            mum "HAHAHAHAHA!"
            show bg dinnerdatewithmom_43
            mum "Oh my God! A Lebanese midget?"
        "Nizzle fizzle, fo... hizzle drizzle!!":
            show bg dinnerdatewithmom_41
            pov "Nizzle fizzle, fo... hizzle drizzle!"
            show bg dinnerdatewithmom_42
            mum "HAHAHAHAHA!"
            show bg dinnerdatewithmom_43
            mum "Oh my God! Fizzle hizzle fo drizzle pizzle?!"
    show bg dinnerdatewithmom_42
    mum "That is frikkin hilarious."
    show bg dinnerdatewithmom_44
    pov "Yeah, Jacob told me that one."
    show bg dinnerdatewithmom_45
    mum "Jacob? Who's this Jacob? Your friend from university?"
    show bg dinnerdatewithmom_44
    pov "Yeah, he's a little... special."
    show bg dinnerdatewithmom_45
    mum "Nawww, my baby has a special wittle friend."
    show bg dinnerdatewithmom_44
    pov "Oh, c'mon, Mom. He's alright. Just made a weird first impression."
    show bg dinnerdatewithmom_45
    mum "How IS university, by the way? If you do not mind me asking."

    menu:
        "It's great.":
            show bg dinnerdatewithmom_46
            pov "University's great so far."
            pov "I really like my lecturers, made a nice set of friends."
            pov "The work's not too shabby."
            pov "Uni's... Uni's good."
            show bg dinnerdatewithmom_47
            mum "That's great to hear, honey. I'm glad you're liking it so far."
        "It's alright.":
            show bg dinnerdatewithmom_46
            pov "University's alright so far."
            pov "The teachers are fine, friends are pretty a'ight."
            pov "The work's pretty ‘meh', to be honest."
            pov "Uni's... just, y'know, fine."
            show bg dinnerdatewithmom_47
            mum "That's good to hear, honey. I'm sure it'll pick up later on."
        "It's not so good.":
            show bg dinnerdatewithmom_48
            pov "University's not so good so far."
            pov "The teachers are crap, my friends; pretty ‘eh'."
            pov "The work is mind-numbing, generously speaking."
            pov "Uni's... the worst."
            show bg dinnerdatewithmom_49
            mum "I'm sorry to hear, honey. Maybe the tides will turn, eventually."
    show bg dinnerdatewithmom_50
    mum "Not everyone has that great of an experience with university."
    show bg dinnerdatewithmom_49
    mum "I sure didn't."
    show bg dinnerdatewithmom_46
    pov "Grandma and Grandpa were strict about studies?"
    show bg dinnerdatewithmom_45
    mum "Strict doesn't even define it, boy. You have it lucky, y'know, being raised in a western culture, and all."
    show bg dinnerdatewithmom_51
    mum "That does not mean you can get away with bad grades, mister!"
    show bg dinnerdatewithmom_52
    pov "C'mon, Mom. I'm here to have a nice dinner, not be lectured by you."
    show bg dinnerdatewithmom_51
    mum "I'm still your mother... I can do what I want."
    show bg dinnerdatewithmom_47
    mum "I love you."
    show bg dinnerdatewithmom_46
    pov "I love you too, Mom."
    show bg dinnerdatewithmom_52
    pov "But you're drunk."
    show bg dinnerdatewithmom_49
    mum "Not THAT drunk."
    show bg dinnerdatewithmom_45
    mum "Heh."
    show bg dinnerdatewithmom_43
    mum "Hehe."
    show bg dinnerdatewithmom_51
    mum "DRRRRRR-Unk."
    show bg dinnerdatewithmom_41
    pov "..."
    pov "Want desser-"
    show bg dinnerdatewithmom_42
    mum "YES!"
    show bg dinnerdatewithmom_53
    mum "‘F' yeah."

    scene black
    with fade
    $ renpy.pause(1,hard=True)
    show bg dinnerdatewithmom_54
    $ renpy.pause()
    show bg dinnerdatewithmom_55
    mum "You know, honey, I don't think you understand how much I really do cherish my moments with you."
    mum "You're quite the treasure."
    show bg dinnerdatewithmom_56
    mum "Who would have thought that my own son would bring me to such a luxurious restaurant."
    mum "For what reason? It's goddamn adorable."
    show bg dinnerdatewithmom_55
    mum "I must be the luckiest mom in the history of mothers."
    show bg dinnerdatewithmom_54
    pov "Mom, please."
    show bg dinnerdatewithmom_55
    mum "I love you, honeypuff."
    show bg dinnerdatewithmom_54
    pov "I love you too."
    show bg dinnerdatewithmom_55
    mum "Hehe, you're soooooo cute. I love you three."
    show bg dinnerdatewithmom_54
    pov "Mom, please, you've had too much to drink."
    show bg dinnerdatewithmom_56
    mum "Am I? Psssh No? Psssh... PSSSSSSHHHHHSHSHShhsuu!"
    mum "How could you even say that? I don't drink."
    show bg dinnerdatewithmom_58
    mum "Maybe on special ocassions..."
    show bg dinnerdatewithmom_57
    mum "..."
    show bg dinnerdatewithmom_55
    mum "Today."
    mum "Today is a special occasion."
    show bg dinnerdatewithmom_54
    mum "..."
    show bg dinnerdatewithmom_59
    mum "How about just one more glass for your dear old Mommy, poppins?"

    menu:
        "Fine.":
            $ mum_points += 1
            $ renpy.notify("Your relationship with Mom has increased")
            $ dinnerdatewithmom_drink = 1
            show bg dinnerdatewithmom_57
            pov "{i}*Sigh*{/i}"
            show bg dinnerdatewithmom_54
            pov "Alright, but just one more glass, okay? We'll be getting a taxi home anyway."
        "No.":
            show bg dinnerdatewithmom_57
            pov "No, Mom, you've had too much. I love you too much to see you any worse than this."
            pov "No matter how funny and giddy you are now, at any moment, you can drop."
            show bg dinnerdatewithmom_58
            mum "Awh. Poo-poo head."
            show bg dinnerdatewithmom_60
            mum "You're so sweet. I lovvvee yoooou."
            show bg dinnerdatewithmom_61
            pov "Love y-"
            show bg dinnerdatewithmom_58
            mum "But screw you too. This is supposed to be my night."

    scene black
    with fade
    $ renpy.pause()
    show bg dinnerdatewithmom_62
    pov "Waiter, could we please have the check? I think we're done here."
    wai "How was your date, sir, madam?"
    show bg dinnerdatewithmom_63
    mum "HA! He called you ‘madam'. Hahaha!"
    show bg dinnerdatewithmom_64
    mum "Date. Oh, it was such a delight. This cutiepie right here is my favourite person in the world."
    show bg dinnerdatewithmom_63
    mum "You know how these nights end."
    show bg dinnerdatewithmom_65
    if skill_int <= 6:
        pov "Mom! Don't... say that."
        show bg dinnerdatewithmom_62
        wai "..."
        wai "I'll go get you and your... mother the bill."
        show bg dinnerdatewithmom_66
        with dissolve
        mum "You idiot. Hahaha, now he knows we're related."
        show bg dinnerdatewithmom_67
        pov "Oh... sh-"
        show bg dinnerdatewithmom_68
        mum "Language, mister."
    elif skill_int <= 13:
        pov "Moooom... moom- mon- Moni-.... Monique. {i}*Clears throat*{/i}"
        pov "Babe, maybe you should quiet down a little."
        show bg dinnerdatewithmom_63
        mum "Oh, did you hear that?! He called me ‘babe'!"
        show bg dinnerdatewithmom_62
        wai "Yes, enthralling."
        wai "I'll go get your bill, sir."
        show bg dinnerdatewithmom_68
        mum "Oh, he was referring ‘madam' to me. That's uncomfortable."
        show bg dinnerdatewithmom_69
        mum "Am I really that old?"
    elif skill_int >= 14:
        pov "{i}*Clears throat*{/i}"
        pov "Honey, have some class, will you please?"
        show bg dinnerdatewithmom_63
        mum "Oh! How adorable, he called me ‘honey'!"
        show bg dinnerdatewithmom_62
        wai "I'm absolutely ecstatic for you, madam."
        wai "I'll get that bill for you, sir. I won't be a moment."
        show bg dinnerdatewithmom_68
        mum "Hehe, I- will- get- that- bill- for- you- si-i-ir."
        show bg dinnerdatewithmom_66
        mum "That fellow sounds like a robot."
        show bg dinnerdatewithmom_67
        pov "Shhh."
    show bg dinnerdatewithmom_62
    with dissolve
    wai "Here's your bill, sir."
    show bg dinnerdatewithmom_70
    with dissolve
    $ renpy.pause()
    if inventory.money <= 299:
        if mum_points >= 7:
            $ dinnerdatewithmom_outcome = 1
            show bg dinnerdatewithmom_71
            pov "Oh... um. I might have underestimated tonight's dinner..."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "5... 500..."
            show bg dinnerdatewithmom_74
            mum "Oh... wow! That's... a whole heap of chicken nuggets."
            show bg dinnerdatewithmom_73
            pov "Y-yeah..."
            show bg dinnerdatewithmom_71
            pov "Um... I- don't have that much money..."
            show bg dinnerdatewithmom_72
            mum "Oh? Really? How much do you have?"
            show bg dinnerdatewithmom_73
            pov "$[inventory.money]."
            show bg dinnerdatewithmom_66
            mum "Y'know what. I'm the real adult here. I've enjoyed myself more than I imagined."
            mum "I'll pay the remaining."
            show bg dinnerdatewithmom_67
            pov "Sorry, Mom..."
            show bg dinnerdatewithmom_66
            mum "Oh, don't worry about it, [povname]. It's just money."
            mum "Your dad's money. HAHAHA!"
            mum "As you said, ‘don't let it ruin our night.'"
            show bg dinnerdatewithmom_67
            pov "I really am sorry, Mom. I'll pay you back."
            show bg dinnerdatewithmom_66
            mum "You better, sweetie-poo."
        else:
            $ dinnerdatewithmom_outcome = 2
            show bg dinnerdatewithmom_71
            pov "Oh... um. I might have underestimated tonight's dinner..."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "5... 500..."
            show bg dinnerdatewithmom_74
            mum "5-00... Do you know how many ice cream sticks I can buy with that money?!"
            show bg dinnerdatewithmom_75
            mum "But you've got it covered right? Son?"
            show bg dinnerdatewithmom_76
            pov "Uhm... yeah..."
            pov "..."
            pov "No... I'm short..."
            show bg dinnerdatewithmom_72
            mum "How much do you have?"
            show bg dinnerdatewithmom_73
            pov "$[inventory.money]."
            show bg dinnerdatewithmom_77
            mum "Jesus, [povname]. Are you kidding me right now?"
            show bg dinnerdatewithmom_78
            pov "I'm really sorry, Mom..."
            show bg dinnerdatewithmom_75
            mum "I'm just- You're lucky I'm drunk, otherwise you'd be in a lot more trouble, mister."
            show bg dinnerdatewithmom_76
            pov "I'll pay you back every cent."
            show bg dinnerdatewithmom_75
            mum "You better, buddy-boy."
    elif inventory.money <= 499:
        if mum_points >= 7:
            $ dinnerdatewithmom_outcome = 3
            show bg dinnerdatewithmom_71
            pov "Oh... um. I might have underestimated tonight's dinner..."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "5... 500..."
            show bg dinnerdatewithmom_74
            mum "Oh... wow! That's... a whole heap of chicken nuggets."
            show bg dinnerdatewithmom_73
            pov "Y-yeah..."
            pov "I'm actually a little short..."
            show bg dinnerdatewithmom_72
            mum "Oh? Really? How much do you have?"
            show bg dinnerdatewithmom_73
            pov "$[inventory.money]."
            show bg dinnerdatewithmom_72
            mum "That's, actually a reasonable amount to think you'd need. I'll give you that one, sir."
            show bg dinnerdatewithmom_66
            mum "Don't worry about it, baby-sir. I'll cover the rest for ya."
            show bg dinnerdatewithmom_67
            pov "Really? Sorry about that, Mom."
            show bg dinnerdatewithmom_66
            mum "No, really. I enjoyed it a lot more than I imagined I would."
            show bg dinnerdatewithmom_67
            pov "Hehe, I'm glad you did. Rest assured, I'll pay you back eventually."
            show bg dinnerdatewithmom_66
            mum "You better, honey-bum."
        elif mum_points <= 6:
            $ dinnerdatewithmom_outcome = 4
            show bg dinnerdatewithmom_71
            pov "Oh... um. I might have underestimated tonight's dinner..."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "5... 500..."
            show bg dinnerdatewithmom_74
            mum "5-00... Do you know how many cookies I can buy with that money?!"
            show bg dinnerdatewithmom_75
            mum "But you've got it covered right? Son?"
            show bg dinnerdatewithmom_71
            pov "I'm actually a tad short..."
            show bg dinnerdatewithmom_72
            mum "How ‘tad' is a ‘tad short'? How much do you have?"
            show bg dinnerdatewithmom_71
            pov "$[inventory.money]."
            show bg dinnerdatewithmom_77
            mum "{i}*Sigh*{/i} [povname]. You said not to worry about it."
            show bg dinnerdatewithmom_79
            mum "I trusted youuuu-hu-hu-hoooo!"
            show bg dinnerdatewithmom_66
            mum "I'll cover the rest. ‘Momma [povname]' to the rescue!"
            show bg dinnerdatewithmom_67
            pov "I'm sorry, Mom. I promise I'll pay back every cent."
            show bg dinnerdatewithmom_77
            mum "I know you will. Well, I'd be lying if I said that it didn't ruin the mood a little."
            mum "Thought today was my chance to feel like a spoilt princess."
            show bg dinnerdatewithmom_78
            pov "I'm really sorry..."
            show bg dinnerdatewithmom_80
            mum "..."
            show bg dinnerdatewithmom_81
            mum "You better pay me back, my dear disappointmen-."
            show bg dinnerdatewithmom_82
            mum "I'M JOKING! I'm drunk as a football player in a Norwegian summer house full of elbow moisturizer."
    elif inventory.money >= 500:
        if mum_points >= 7:
            show bg dinnerdatewithmom_71
            pov "Oh... wow... that is a LOT more expensive that I would have imagined it to be."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "$500."
            show bg dinnerdatewithmom_74
            mum "Oh... wow! That's... a whole heap of waffles."
            show bg dinnerdatewithmom_73
            pov "Yeah, it is."
            show bg dinnerdatewithmom_72
            mum "You do have enough, right? Honeeeey?"
            show bg dinnerdatewithmom_67
            pov "Yeah, of course. You think I'd be ill-prepared tonight?"
            show bg dinnerdatewithmom_77
            mum "It still is a very expensive dinner..."
            show bg dinnerdatewithmom_72
            mum "I mean, those breadsticks must've cost $100 all by themselves."
            show bg dinnerdatewithmom_81
            mum "How about we split it?"
            show bg dinnerdatewithmom_80
            pov "Split it 50-50?"
            show bg dinnerdatewithmom_81
            mum "Yeah! I'm a grown woman. I have money."
            show bg dinnerdatewithmom_66
            mum "Technically it's your dad's money but you know. HAHAHA!"

            menu:
                "I'll pay the full amount.":
                    $ dinnerdatewithmom_outcome = 5
                    show bg dinnerdatewithmom_80
                    pov "It's okay, Mom. I promised you that I would pay for all of this."
                    show bg dinnerdatewithmom_81
                    mum "You sure, baby-girl?"
                    show bg dinnerdatewithmom_80
                    pov "No doubt about it."
                    show bg dinnerdatewithmom_81
                    mum "You're going to make me cry..."
                    show bg dinnerdatewithmom_80
                    mum "..."
                    show bg dinnerdatewithmom_77
                    mum "What did I do to deserve you?"
                    show bg dinnerdatewithmom_80
                    pov "You gave me all the love in the world, it's the least I can do for you."
                    show bg dinnerdatewithmom_81
                    mum "{i}*Sniff*{/i} You're unbelievably cheesy... I love you sooo much."
                    show bg dinnerdatewithmom_77
                    mum "I really do."
                    show bg dinnerdatewithmom_80
                    pov "I love you too, Mom."
                    show bg dinnerdatewithmom_77
                    mum "No, like- I really, REALLY fucking love you."
                    mum "Excuse my French..."
                    show bg dinnerdatewithmom_83
                    mum "But fuck."
                    show bg dinnerdatewithmom_84
                    mum "If only you can feel what love-adrenaline I'm feeling right now."
                    show bg dinnerdatewithmom_85
                    pov "Trust me, Mom. I can feel it too."
                    show bg dinnerdatewithmom_83
                    mum "Let's get out of here, shall we?"
                "Let's split the bill.":
                    $ dinnerdatewithmom_outcome = 6
                    show bg dinnerdatewithmom_80
                    pov "You know what, I really do appreciate your offer to split the bill."
                    pov "I mean, it is alright for you, right?"
                    show bg dinnerdatewithmom_66
                    mum "Of course, honey. I would do anything for you. Anything."
                    mum "You've proven to me that you're more than just a son."
                    show bg dinnerdatewithmom_67
                    pov "..."
                    pov "What do you mean?"
                    show bg dinnerdatewithmom_66
                    mum "You're one the greatest person I have in my life, you silly fuck."
                    show bg dinnerdatewithmom_81
                    mum "And I'm grateful that you're right there across the hall from me."
                    show bg dinnerdatewithmom_85
                    pov "Mom, you're getting too sappy."
                    show bg dinnerdatewithmom_84
                    mum "I don't care. You mean the world to me and I want you to know that."
                    show bg dinnerdatewithmom_85
                    pov "You mean just as much to me too, Mom."
                    show bg dinnerdatewithmom_84
                    mum "Good! Because I will never forgive myself if you don't."
                    show bg dinnerdatewithmom_83
                    mum "Let's get out of here, shall we?"
        elif mum_points <= 6:
            $ dinnerdatewithmom_outcome = 5
            show bg dinnerdatewithmom_71
            pov "Oh... wow... that is a LOT more expensive that I would have imagined it to be."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "$500."
            show bg dinnerdatewithmom_74
            mum "Oh... wow! That's... a whole heap of chocolate eggs."
            show bg dinnerdatewithmom_73
            pov "Yeah, it is."
            show bg dinnerdatewithmom_72
            mum "You do have enough, right?"
            show bg dinnerdatewithmom_67
            pov "Yeah, of course. You think I'd be ill-prepared tonight?"
            show bg dinnerdatewithmom_66
            mum "No, I know you wouldn't."
            show bg dinnerdatewithmom_72
            mum "Still though, even to me, that is a shocking number for two people."
            show bg dinnerdatewithmom_67
            pov "Yeah, but I'm sure tonight was worth it."
            show bg dinnerdatewithmom_66
            mum "Oh, it was definitely worth it. I'm never going to forget about tonight."
            mum "Never, ever, ever."
            show bg dinnerdatewithmom_79
            mum "Hopefully."
            show bg dinnerdatewithmom_66
            mum "I am quite a tip bitsy." ## Spelling is on purpose
            show bg dinnerdatewithmom_80
            pov "..."
            show bg dinnerdatewithmom_81
            mum "I-"
            mum "I really needed this, [povname]. You really did make me feel like a queen, tonight."
            show bg dinnerdatewithmom_80
            pov "It was my pleasure, Mom. You deserve every bit of it."
            show bg dinnerdatewithmom_83
            mum "Like, real talk, yo. You made me feel loved again; special. Like I actually mean something to someone."
            show bg dinnerdatewithmom_84
            mum "Marriage really sucks that feeling out of your life."
            show bg dinnerdatewithmom_85
            mum "..."
            show bg dinnerdatewithmom_83
            mum "But there's always a silver lining."
            mum "You're my silver lining, [povname]. Don't ever change who you are."
            show bg dinnerdatewithmom_85
            pov "I won't. I promise you that."
            show bg dinnerdatewithmom_83
            mum "And don't ever get married!"
            show bg dinnerdatewithmom_85
            pov "Uh..."
            show bg dinnerdatewithmom_83
            mum "I'm glad you agree. I love you."
            show bg dinnerdatewithmom_85
            pov "Heheh, I love you too."
            show bg dinnerdatewithmom_83
            mum "C'mon, let's get out of here."

    scene black
    with fade
    if inventory.money >= 500:
        "You paid for the meal and you both left the restaurant to go home."
        $ renpy.notify("You paid $500")
        $ inventory.money -= 500
    else:
        $ dinnerdatewithmom_owe = (500-inventory.money)
        "You and Mom paid for the meal and you both left the restaurant to go home."
        $ renpy.notify("You paid $[inventory.money]")
        $ renpy.pause(3,hard=True)
        $ renpy.notify("You owe Mom $[dinnerdatewithmom_owe]")
        $ renpy.pause(3,hard=True)
        $ inventory.money = 0
    $ mum_path = 27
    $ gtime = 3

    jump lbl_myhallway_night_setup

### NO WINC ###
label lbl_dinner_date_with_mom_winc0:

    scene bg dinnerdatewithmom_1
    with fade
    $ renpy.pause()
    show bg dinnerdatewithmom_2
    mum "Wow, honey. Are you sure you're okay to eat here? This place looks like it costs a fortune..."
    show bg dinnerdatewithmom_3
    mum "These teeny breadsticks must be at least $10 each..."
    show bg dinnerdatewithmom_4
    pov "[missus], please, don't worry about it. Let's just clear our minds of it and enjoy the moment. Together."
    show bg dinnerdatewithmom_5
    mum "Okay, sweetie. This is honestly the most romantic thing anyone has done for me in a really long time."
    mum "I can't remember the last time your [dadrole]..."
    show bg dinnerdatewithmom_6
    mum "Y'know, forget about your [dadrole]. This is about us, right?"
    show bg dinnerdatewithmom_7
    pov "A night for just us. No [dadname], no [sister], no interference."
    show bg dinnerdatewithmom_8
    mum "..."
    pov "What?"
    show bg dinnerdatewithmom_9
    mum "Hm? Nothing. I'm just admiring how good you look in that suit. You really do grow up so fast."
    mum "Like a real man now."
    show bg dinnerdatewithmom_10
    $ renpy.pause(1,hard=True)
    show bg dinnerdatewithmom_11
    pov "..."

    menu:
        "You think so?":
            pov "You really think so?"
            show bg dinnerdatewithmom_12
            mum "120 percent."
            show bg dinnerdatewithmom_11
            pov "Thanks, [missus]."
        "You don't look too bad yourself." if skill_cha >= 3:
            pov "You don't look too bad yourself."
            show bg dinnerdatewithmom_13
            mum "Oh, I just threw this on. It's not that impressive."
            show bg dinnerdatewithmom_7
            pov "It looks good on you."
        "You don't look a year over 20." if skill_cha >= 6:
            $ skill_cha -= 3
            $ mum_points += 1
            $ renpy.notify("Your relationship with [missus] has increased")
            show bg dinnerdatewithmom_4
            pov "You don't look a year over 20."
            show bg dinnerdatewithmom_5
            mum "Oh, stop, that's not true."
            show bg dinnerdatewithmom_4
            pov "I'm serious, [missus]."
            show bg dinnerdatewithmom_2
            mum "Hehe, really though? I'm starting to worry about wrinkles forming on my-"
            show bg dinnerdatewithmom_14
            pov "You look great, [missus]."
        "You are the most stunning woman." if skill_cha >= 9:
            $ skill_cha -= 5
            $ mum_points += 2
            $ renpy.notify("Your relationship with [missus] has increased by 2")
            show bg dinnerdatewithmom_14
            pov "You are the most stunning woman."
            show bg dinnerdatewithmom_12
            mum "...in this room?"
            show bg dinnerdatewithmom_7
            pov "No."
            show bg dinnerdatewithmom_15
            mum "...that you've ever seen?"
            show bg dinnerdatewithmom_16
            pov "No."
            show bg dinnerdatewithmom_17
            mum "...in the world?"
            show bg dinnerdatewithmom_11
            pov "No, just. Stunning. Period."
            show bg dinnerdatewithmom_12
            mum "You're too much, [povname]."
    show bg dinnerdatewithmom_11
    $ renpy.pause()
    pov "I don't know about you but I'm ready to order mains."
    show bg dinnerdatewithmom_12
    mum "That makes two of us."
    show bg dinnerdatewithmom_18
    with fade
    pov "What are you craving for?"
    show bg dinnerdatewithmom_19
    mum "It all looks so good! Oh, gosh- it's how much?"
    show bg dinnerdatewithmom_20
    pov "[missus]."
    show bg dinnerdatewithmom_21
    mum "Okay okay, I'll try not to cry."
    show bg dinnerdatewithmom_22
    mum "How about the Chef's Seafood Special?"
    show bg dinnerdatewithmom_23
    pov "Sounds good to me."
    show bg dinnerdatewithmom_24
    mum "How's about a bottle of chardonnay to go with that?"
    show bg dinnerdatewithmom_25
    pov "Whatever you want, [missus]."
    show bg dinnerdatewithmom_26
    mum "Hehehe~"

    scene black
    with fade
    $ renpy.pause(1,hard=True)

    scene bg dinnerdatewithmom_27
    with fade
    mum "And then your sister said, I don't know, [missus], we don't have a dog!"
    show bg dinnerdatewithmom_28
    pov "Oh my God, really? That's so bad."
    show bg dinnerdatewithmom_29
    mum "I love her to death but she can be so clueless sometimes."
    show bg dinnerdatewithmom_30
    pov "She's a weird one that is."
    pov "At least you raised one of us right."
    if mum_points >= 6:
        show bg dinnerdatewithmom_31
        mum "I raised the most beautiful boy in the world. I'm so happy to be here with you tonight."
        show bg dinnerdatewithmom_27
        mum "But don't get me wrong. Your [sisrole] is just as important to me as you are."
        show bg dinnerdatewithmom_33
        pov "You just love me a little more, right?"
        show bg dinnerdatewithmom_34
        mum "..." ##GRIN
        show bg dinnerdatewithmom_31
        mum "Your [sisrole] may be weird but you're definitely a smug one."
        show bg dinnerdatewithmom_32
        mum "At the end of the day, I consider myself lucky to have had [povsisrole]s."
    else:
        show bg dinnerdatewithmom_35
        mum "Hey! I raised two amazing [povsisrole]s, thank you very much, young man. And it hasn't been easy."
        show bg dinnerdatewithmom_36
        pov "I can't imagine how hard it was for you, raising us [povsisrole]."
        show bg dinnerdatewithmom_29
        mum "Tell me about it. But I've always considered myself lucky."
    show bg dinnerdatewithmom_27
    mum "I mean, how often can a [mumrole] say that they are a [mumrole] of [povsisrole]s?"
    mum "To be honest with you, it brings up a lot of interest and conversations."
    if sister_points <= 3:
        show bg dinnerdatewithmom_30
        pov "All in all, being a [povsisrole], at least for me, isn't that bad."
        pov "Sure, we fight, we bicker, and yell till your ears bleed."
        pov "But there isn't anyone I would rather argue with than her."
    elif sister_points <= 7:
        show bg dinnerdatewithmom_30
        pov "I'm glad I'm a [povsisrole], jokes aside."
        pov "I can't imagine growing up without [sister]. She really brought out the fun in my life."
        pov "Would I consider her my ‘best friend'? That's a little too sappy to confirm."
        pov "But would I turn my back on her? Hell no."
    else:
        show bg dinnerdatewithmom_30
        pov "Yeah, I actually am really glad that I'm a [povsisrole]."
        pov "[sister] is definitely a pain in my butt, but I can assure you that I'm a pain in hers too."
        pov "Maybe the term ‘best friend' may be pushing it but imagining a childhood without her just depresses me."
    show bg dinnerdatewithmom_29
    mum "You're a good [povsisrole]. Arguments and immaturity aside. I can tell you really care for her."
    mum "Protect her, okay, [povname]?"
    show bg dinnerdatewithmom_30
    pov "I will, [missus]. I don't hate her that much."
    show bg dinnerdatewithmom_37
    mum "I know, but I'm just telling you. If anything happens, it's her over me."
    mum "I can't continue living knowing my [povmumrole]s have suffered."
    show bg dinnerdatewithmom_38
    pov "Damn, [missus]. Why are you so dark all of a sudden?"
    mum "..."
    show bg dinnerdatewithmom_32
    mum "Sorry, a Korean Drama flashed in my mind."
    show bg dinnerdatewithmom_30
    pov "Hehehe, fair enough."
    show bg dinnerdatewithmom_39
    mum "Oh, no..."
    show bg dinnerdatewithmom_40
    pov "What's wrong?"
    show bg dinnerdatewithmom_37
    mum "I'm out of wine. How about another for your dear old [mumrole]?"
    show bg dinnerdatewithmom_30
    pov "Sure thing. I'll just flag someone down."

    scene black
    with fade
    $ renpy.pause(1,hard=True)

    scene bg dinnerdatewithmom_28
    with fade

    menu:
        "Nougat!":
            show bg dinnerdatewithmom_41
            pov "Nougat!"
            show bg dinnerdatewithmom_42
            mum "HAHAHAHAHA!"
            show bg dinnerdatewithmom_43
            mum "Oh my God! Nougat?"
        "A Lebanese midget!":
            show bg dinnerdatewithmom_41
            pov "A Lebanese midget!"
            show bg dinnerdatewithmom_42
            mum "HAHAHAHAHA!"
            show bg dinnerdatewithmom_43
            mum "Oh my God! A Lebanese midget?"
        "Nizzle fizzle, fo... hizzle drizzle!!":
            show bg dinnerdatewithmom_41
            pov "Nizzle fizzle, fo... hizzle drizzle!"
            show bg dinnerdatewithmom_42
            mum "HAHAHAHAHA!"
            show bg dinnerdatewithmom_43
            mum "Oh my God! Fizzle hizzle fo drizzle pizzle?!"
    show bg dinnerdatewithmom_42
    mum "That is frikkin hilarious."
    show bg dinnerdatewithmom_44
    pov "Yeah, Jacob told me that one."
    show bg dinnerdatewithmom_45
    mum "Jacob? Who's this Jacob? Your friend from university?"
    show bg dinnerdatewithmom_44
    pov "Yeah, he's a little... special."
    show bg dinnerdatewithmom_45
    mum "Nawww, my baby has a special wittle friend."
    show bg dinnerdatewithmom_44
    pov "Oh, c'mon, [missus]. He's alright. Just made a weird first impression."
    show bg dinnerdatewithmom_45
    mum "How IS university, by the way? If you do not mind me asking."

    menu:
        "It's great.":
            show bg dinnerdatewithmom_46
            pov "University's great so far."
            pov "I really like my teachers, made a nice set of friends."
            pov "The work's not too shabby."
            pov "Uni's... Uni's good."
            show bg dinnerdatewithmom_47
            mum "That's great to hear, honey. I'm glad you're liking it so far."
        "It's alright.":
            show bg dinnerdatewithmom_46
            pov "University's alright so far."
            pov "The teachers are fine, friends are pretty a'ight."
            pov "The work's pretty ‘meh', to be honest."
            pov "Uni's... just, y'know, fine."
            show bg dinnerdatewithmom_47
            mum "That's good to hear, honey. I'm sure it'll pick up later on."
        "It's not so good.":
            show bg dinnerdatewithmom_48
            pov "University's not so good so far."
            pov "The teachers are crap, my friends; pretty ‘eh'."
            pov "The work is mind-numbing, generously speaking."
            pov "Uni's... the worst."
            show bg dinnerdatewithmom_49
            mum "I'm sorry to hear, honey. Maybe the tides will turn, eventually."
    show bg dinnerdatewithmom_50
    mum "Not everyone has that great of an experience with university."
    show bg dinnerdatewithmom_49
    mum "I sure didn't."
    show bg dinnerdatewithmom_46
    pov "Your parents were strict about studies?"
    show bg dinnerdatewithmom_45
    mum "Strict doesn't even define it, boy. You have it lucky, y'know, being raised in a western culture and all."
    show bg dinnerdatewithmom_51
    mum "That does not mean you can get away with bad grades, mister!"
    show bg dinnerdatewithmom_52
    pov "C'mon, [missus]. I'm here to have a nice dinner, not be lectured by you."
    show bg dinnerdatewithmom_51
    mum "I'm still your [mumrole]... I can do what I want."
    show bg dinnerdatewithmom_47
    mum "I love you."
    show bg dinnerdatewithmom_46
    pov "I love you too, [missus]."
    show bg dinnerdatewithmom_52
    pov "But you're drunk."
    show bg dinnerdatewithmom_49
    mum "Not THAT drunk."
    show bg dinnerdatewithmom_45
    mum "Heh."
    show bg dinnerdatewithmom_43
    mum "Hehe."
    show bg dinnerdatewithmom_51
    mum "DRRRRRR-Unk."
    show bg dinnerdatewithmom_41
    pov "..."
    pov "Want desser-"
    show bg dinnerdatewithmom_42
    mum "YES!"
    show bg dinnerdatewithmom_53
    mum "‘F' yeah."

    scene black
    with fade
    $ renpy.pause(1,hard=True)
    show bg dinnerdatewithmom_54
    $ renpy.pause()
    show bg dinnerdatewithmom_55
    mum "You know, honey, I don't think you understand how much I really do cherish my moments with you."
    mum "You're quite the treasure."
    show bg dinnerdatewithmom_56
    mum "Who would have thought that my own [povmumrole] would bring me to such a luxurious restaurant."
    mum "For what reason? It's goddamn adorable."
    show bg dinnerdatewithmom_55
    mum "I must be the luckiest [mumrole] in the history of [mumrole]s."
    show bg dinnerdatewithmom_54
    pov "[missus], please."
    show bg dinnerdatewithmom_55
    mum "I love you, honeypuff."
    show bg dinnerdatewithmom_54
    pov "I love you too."
    show bg dinnerdatewithmom_55
    mum "Hehe, you're soooooo cute. I love you three."
    show bg dinnerdatewithmom_54
    pov "[missus], please, you've had too much to drink."
    show bg dinnerdatewithmom_56
    mum "Am I? Psssh No? Psssh... PSSSSSSHHHHHSHSHShhsuu!"
    mum "How could you even say that? I don't drink."
    show bg dinnerdatewithmom_58
    mum "Maybe on special ocassions..."
    show bg dinnerdatewithmom_57
    mum "..."
    show bg dinnerdatewithmom_55
    mum "Today."
    mum "Today is a special occasion."
    show bg dinnerdatewithmom_54
    mum "..."
    show bg dinnerdatewithmom_59
    mum "How about just one more glass for your dear, old [missus], poppins?"

    menu:
        "Fine.":
            $ mum_points += 1
            $ renpy.notify("Your relationship with [missus] has increased")
            $ dinnerdatewithmom_drink = 1
            show bg dinnerdatewithmom_57
            pov "{i}*Sigh*{/i}"
            show bg dinnerdatewithmom_54
            pov "Alright, but just one more glass, okay? We'll be getting a taxi home anyway."
        "No.":
            show bg dinnerdatewithmom_57
            pov "No, [missus], you've had too much. I love you too much to see you any worse than this."
            pov "No matter how funny and giddy you are now, at any moment, you can drop."
            show bg dinnerdatewithmom_58
            mum "Awh. Poo-poo head."
            show bg dinnerdatewithmom_60
            mum "You're so sweet. I lovvvee yoooou."
            show bg dinnerdatewithmom_61
            pov "Love y-"
            show bg dinnerdatewithmom_58
            mum "But screw you too. This is supposed to be my night."

    scene black
    with fade
    $ renpy.pause()
    show bg dinnerdatewithmom_62
    pov "Waiter, could we please have the check? I think we're done here."
    wai "How was your date, sir, madam?"
    show bg dinnerdatewithmom_63
    mum "HA! He called you ‘madam'. Hahaha!"
    show bg dinnerdatewithmom_64
    mum "Date. Oh, it was such a delight. This cutiepie right here is my favourite person in the world."
    show bg dinnerdatewithmom_63
    mum "You know how these nights end."
    show bg dinnerdatewithmom_65
    if skill_int <= 6:
        pov "[missus]! Don't... say that."
        show bg dinnerdatewithmom_62
        wai "..."
        wai "I'll go get you and your... date the bill."
        show bg dinnerdatewithmom_66
        with dissolve
        mum "You idiot. Hahaha, now he knows our secret."
        show bg dinnerdatewithmom_67
        pov "Oh... sh-"
        show bg dinnerdatewithmom_68
        mum "Language, mister."
    elif skill_int <= 13:
        pov "[missus]... {i}*Clears throat*{/i}"
        pov "Babe, maybe you should quiet down a little."
        show bg dinnerdatewithmom_63
        mum "Oh, did you hear that?! He called me ‘babe'!"
        show bg dinnerdatewithmom_62
        wai "Yes, enthralling."
        wai "I'll go get your bill, sir."
        show bg dinnerdatewithmom_68
        mum "Oh, he was referring ‘madam' to me. That's uncomfortable."
        show bg dinnerdatewithmom_69
        mum "Am I really that old?"
    elif skill_int >= 14:
        pov "{i}*Clears throat*{/i}"
        pov "Honey, have some class, will you please?"
        show bg dinnerdatewithmom_63
        mum "Oh! How adorable, he called me ‘honey'!"
        show bg dinnerdatewithmom_62
        wai "I'm absolutely ecstatic for you, madam."
        wai "I'll get that bill for you, sir. I won't be a moment."
        show bg dinnerdatewithmom_68
        mum "Hehe, I- will- get- that- bill- for- you- si-i-ir."
        show bg dinnerdatewithmom_66
        mum "That fellow sounds like a robot."
        show bg dinnerdatewithmom_67
        pov "Shhh."
    show bg dinnerdatewithmom_62
    with dissolve
    wai "Here's your bill, sir."
    show bg dinnerdatewithmom_70
    with dissolve
    $ renpy.pause()
    if inventory.money <= 299:
        if mum_points >= 7:
            $ dinnerdatewithmom_outcome = 1
            show bg dinnerdatewithmom_71
            pov "Oh... um. I might have underestimated tonight's dinner..."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "5... 500..."
            show bg dinnerdatewithmom_74
            mum "Oh... wow! That's... a whole heap of chicken nuggets."
            show bg dinnerdatewithmom_73
            pov "Y-yeah..."
            show bg dinnerdatewithmom_71
            pov "Um... I- don't have that much money..."
            show bg dinnerdatewithmom_72
            mum "Oh? Really? How much do you have?"
            show bg dinnerdatewithmom_73
            pov "$[inventory.money]."
            show bg dinnerdatewithmom_66
            mum "Y'know what. I'm the real adult here. I've enjoyed myself more than I imagined."
            mum "I'll pay the remaining."
            show bg dinnerdatewithmom_67
            pov "Sorry, [missus]..."
            show bg dinnerdatewithmom_66
            mum "Oh, don't worry about it, [povname]. It's just money."
            mum "Your [dadrole]'s money. HAHAHA!"
            mum "As you said, ‘don't let it ruin our night.'"
            show bg dinnerdatewithmom_67
            pov "I really am sorry, [missus]. I'll pay you back."
            show bg dinnerdatewithmom_66
            mum "You better, sweetie-poo."
        else:
            $ dinnerdatewithmom_outcome = 2
            show bg dinnerdatewithmom_71
            pov "Oh... um. I might have underestimated tonight's dinner..."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "5... 500..."
            show bg dinnerdatewithmom_74
            mum "5-00... Do you know how many ice cream sticks I can buy with that money?!"
            show bg dinnerdatewithmom_75
            mum "But you've got it covered right? [povname]?"
            show bg dinnerdatewithmom_76
            pov "Uhm... yeah..."
            pov "..."
            pov "No... I'm short..."
            show bg dinnerdatewithmom_72
            mum "How much do you have?"
            show bg dinnerdatewithmom_73
            pov "$[inventory.money]."
            show bg dinnerdatewithmom_77
            mum "Jesus, [povname]. Are you kidding me right now?"
            show bg dinnerdatewithmom_78
            pov "I'm really sorry, [missus]..."
            show bg dinnerdatewithmom_75
            mum "I'm just- You're lucky I'm drunk, otherwise you'd be in a lot more trouble, mister."
            show bg dinnerdatewithmom_76
            pov "I'll pay you back every cent."
            show bg dinnerdatewithmom_75
            mum "You better, buddy-boy."
    elif inventory.money <= 499:
        if mum_points >= 7:
            $ dinnerdatewithmom_outcome = 3
            show bg dinnerdatewithmom_71
            pov "Oh... um. I might have underestimated tonight's dinner..."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "5... 500..."
            show bg dinnerdatewithmom_74
            mum "Oh... wow! That's... a whole heap of chicken nuggets."
            show bg dinnerdatewithmom_73
            pov "Y-yeah..."
            pov "I'm actually a little short..."
            show bg dinnerdatewithmom_72
            mum "Oh? Really? How much do you have?"
            show bg dinnerdatewithmom_73
            pov "$[inventory.money]."
            show bg dinnerdatewithmom_72
            mum "That's, actually a reasonable amount to think you'd need. I'll give you that one, sir."
            show bg dinnerdatewithmom_66
            mum "Don't worry about it, baby-sir. I'll cover the rest for ya."
            show bg dinnerdatewithmom_67
            pov "Really? Sorry about that, [missus]."
            show bg dinnerdatewithmom_66
            mum "No, really. I enjoyed it a lot more than I imagined I would."
            show bg dinnerdatewithmom_67
            pov "Hehe, I'm glad you did. Rest assured, I'll pay you back eventually."
            show bg dinnerdatewithmom_66
            mum "You better, honey-bum."
        elif mum_points <= 6:
            $ dinnerdatewithmom_outcome = 4
            show bg dinnerdatewithmom_71
            pov "Oh... um. I might have underestimated tonight's dinner..."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "5... 500..."
            show bg dinnerdatewithmom_74
            mum "5-00... Do you know how many cookies I can buy with that money?!"
            show bg dinnerdatewithmom_75
            mum "But you've got it covered right? [povname]?"
            show bg dinnerdatewithmom_71
            pov "I'm actually a tad short..."
            show bg dinnerdatewithmom_72
            mum "How ‘tad' is a ‘tad short'? How much do you have?"
            show bg dinnerdatewithmom_71
            pov "$[inventory.money]."
            show bg dinnerdatewithmom_77
            mum "{i}*Sigh*{/i} [povname]. You said not to worry about it."
            show bg dinnerdatewithmom_79
            mum "I trusted youuuu-hu-hu-hoooo!"
            show bg dinnerdatewithmom_66
            mum "I'll cover the rest. ‘Mrs [povname]' to the rescue!"
            show bg dinnerdatewithmom_67
            pov "I'm sorry, [missus]. I promise I'll pay back every cent."
            show bg dinnerdatewithmom_77
            mum "I know you will. Well, I'd be lying if I said that it didn't ruin the mood a little."
            mum "Thought today was my chance to feel like a spoilt princess."
            show bg dinnerdatewithmom_78
            pov "I'm really sorry..."
            show bg dinnerdatewithmom_80
            mum "..."
            show bg dinnerdatewithmom_81
            mum "You better pay me back, my dear disappointmen-."
            show bg dinnerdatewithmom_82
            mum "I'M JOKING! I'm drunk as a football player in a Norwegian summer house full of elbow moisturizer."
    elif inventory.money >= 500:
        if mum_points >= 7:
            show bg dinnerdatewithmom_71
            pov "Oh... wow... that is a LOT more expensive that I would have imagined it to be."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "$500."
            show bg dinnerdatewithmom_74
            mum "Oh... wow! That's... a whole heap of waffles."
            show bg dinnerdatewithmom_73
            pov "Yeah, it is."
            show bg dinnerdatewithmom_72
            mum "You do have enough, right? Honeeeey?"
            show bg dinnerdatewithmom_67
            pov "Yeah, of course. You think I'd be ill-prepared tonight?"
            show bg dinnerdatewithmom_77
            mum "It still is a very expensive dinner..."
            show bg dinnerdatewithmom_72
            mum "I mean, those breadstick must've costed $100 itself."
            show bg dinnerdatewithmom_81
            mum "How about we split it?"
            show bg dinnerdatewithmom_80
            pov "Split it 50-50?"
            show bg dinnerdatewithmom_81
            mum "Yeah! I'm a grown woman. I have money."
            show bg dinnerdatewithmom_66
            mum "Technically it's your [dadrole]'s money but you know. HAHAHA!"

            menu:
                "I'll pay the full amount.":
                    $ dinnerdatewithmom_outcome = 5
                    show bg dinnerdatewithmom_80
                    pov "It's okay, [missus]. I promised you that I would pay for all of this."
                    show bg dinnerdatewithmom_81
                    mum "You sure, baby-girl?"
                    show bg dinnerdatewithmom_80
                    pov "No doubt about it."
                    show bg dinnerdatewithmom_81
                    mum "You're going to make me cry..."
                    show bg dinnerdatewithmom_80
                    mum "..."
                    show bg dinnerdatewithmom_77
                    mum "What did I do to deserve you?"
                    show bg dinnerdatewithmom_80
                    pov "You gave me all the love in the world, it's the least I can do for you."
                    show bg dinnerdatewithmom_81
                    mum "{i}*Sniff*{/i} You're unbelievably cheesy... I love you sooo much."
                    show bg dinnerdatewithmom_77
                    mum "I really do."
                    show bg dinnerdatewithmom_80
                    pov "I love you too, [missus]."
                    show bg dinnerdatewithmom_77
                    mum "No, like- I really, REALLY fucking love you."
                    mum "Excuse my French..."
                    show bg dinnerdatewithmom_83
                    mum "But fuck."
                    show bg dinnerdatewithmom_84
                    mum "If only you can feel what love-adrenaline I'm feeling right now."
                    show bg dinnerdatewithmom_85
                    pov "Trust me, [missus]. I can feel it too."
                    show bg dinnerdatewithmom_83
                    mum "Let's get out of here, shall we?"
                "Let's split the bill.":
                    $ dinnerdatewithmom_outcome = 6
                    show bg dinnerdatewithmom_80
                    pov "You know what, I really do appreciate your offer to split the bill."
                    pov "I mean, it is alright for you, right?"
                    show bg dinnerdatewithmom_66
                    mum "Of course, honey. I would do anything for you. Anything."
                    mum "You've proven to me that you're more than just a [povmumrole]."
                    show bg dinnerdatewithmom_67
                    pov "..."
                    pov "What do you mean?"
                    show bg dinnerdatewithmom_66
                    mum "You're one the greatest person I have in my life, you silly fuck."
                    show bg dinnerdatewithmom_81
                    mum "And I'm grateful that you're right there across the hall from me."
                    show bg dinnerdatewithmom_85
                    pov "[missus], you're getting too sappy."
                    show bg dinnerdatewithmom_84
                    mum "I don't care. You mean the world to me and I want you to know that."
                    show bg dinnerdatewithmom_85
                    pov "You mean just as much to me too, [missus]."
                    show bg dinnerdatewithmom_84
                    mum "Good! Because I will never forgive myself if you don't."
                    show bg dinnerdatewithmom_83
                    mum "Let's get out of here, shall we?"
        elif mum_points <= 6:
            $ dinnerdatewithmom_outcome = 5
            show bg dinnerdatewithmom_71
            pov "Oh... wow... that is a LOT more expensive that I would have imagined it to be."
            show bg dinnerdatewithmom_72
            mum "How much is it?"
            show bg dinnerdatewithmom_73
            pov "$500."
            show bg dinnerdatewithmom_74
            mum "Oh... wow! That's... a whole heap of chocolate eggs."
            show bg dinnerdatewithmom_73
            pov "Yeah, it is."
            show bg dinnerdatewithmom_72
            mum "You do have enough, right?"
            show bg dinnerdatewithmom_67
            pov "Yeah, of course. You think I'd be ill-prepared tonight?"
            show bg dinnerdatewithmom_66
            mum "No, I know you wouldn't."
            show bg dinnerdatewithmom_72
            mum "Still though, even to me, that is a shocking number for two people."
            show bg dinnerdatewithmom_67
            pov "Yeah, but I'm sure tonight was worth it."
            show bg dinnerdatewithmom_66
            mum "Oh, it was definitely worth it. I'm never going to forget about tonight."
            mum "Never, ever, ever."
            show bg dinnerdatewithmom_79
            mum "Hopefully."
            show bg dinnerdatewithmom_66
            mum "I am quite a tip bitsy." ## Spelling is on purpose
            show bg dinnerdatewithmom_80
            pov "..."
            show bg dinnerdatewithmom_81
            mum "I-"
            mum "I really needed this, [povname]. You really did make me feel like a queen, tonight."
            show bg dinnerdatewithmom_80
            pov "It was my pleasure, [missus]. You deserve every bit of it."
            show bg dinnerdatewithmom_83
            mum "Like, real talk, yo. You made me feel loved again; special. Like I actually mean something to someone."
            show bg dinnerdatewithmom_84
            mum "Marriage really sucks that feeling out of your life."
            show bg dinnerdatewithmom_85
            mum "..."
            show bg dinnerdatewithmom_83
            mum "But there's always a silver lining."
            mum "You're my silver lining, [povname]. Don't ever change who you are."
            show bg dinnerdatewithmom_85
            pov "I won't. I promise you that."
            show bg dinnerdatewithmom_83
            mum "And don't ever get married!"
            show bg dinnerdatewithmom_85
            pov "Uh..."
            show bg dinnerdatewithmom_83
            mum "I'm glad you agree. I love you."
            show bg dinnerdatewithmom_85
            pov "Heheh, I love you too."
            show bg dinnerdatewithmom_83
            mum "C'mon, let's get out of here."

    scene black
    with fade
    if inventory.money >= 500:
        "You paid for the meal and you both left the restaurant to go home."
        $ renpy.notify("You paid $500")
        $ inventory.money -= 500
    else:
        $ dinnerdatewithmom_owe = (500-inventory.money)
        "You and [missus] paid for the meal and you both left the restaurant to go home."
        $ renpy.notify("You paid $[inventory.money]")
        $ renpy.pause(3,hard=True)
        $ renpy.notify("You owe [missus] $[dinnerdatewithmom_owe]")
        $ renpy.pause(3,hard=True)
        $ inventory.money = 0
    $ mum_path = 27
    $ gtime = 3

    jump lbl_myhallway_night_setup
