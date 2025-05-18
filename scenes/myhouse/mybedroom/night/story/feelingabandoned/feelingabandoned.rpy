## Feeling Abandoned ##
label lbl_feeling_abandoned:
    if winc == 0:
        jump lbl_feeling_abandoned_winc0

    scene bg mybedroom_night_lightson
    with fade
    show pov angry at left
    with dissolve
    show mum angry_talk at right
    with dissolve
    mum "Hey, mister! We need to talk."

    menu:
        "What's there to talk about?":
            show pov angry_talk at left
            show mum angry at right
            pov "What's there to talk about?"
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with Mom has decreased by 3")
        "I don't want to talk to you.":
            show pov angry_talk at left
            show mum angry at right
            pov "I don't want to talk to you."
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with Mom has decreased by 3")
        "Why don't you just go finish what YOU started.":
            show pov angry_talk at left
            show mum angry at right
            pov "Why don't you just go finish what YOU started."
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with Mom has decreased by 3")
        "Fine, let's talk." if skill_cha >= 3:
            show pov angry_talk at left
            show mum angry at right
            pov "Fine, let's talk."
            if mum_points >= 1:
                $ mum_points -= 1
            else:
                $ mum_points = 0
            if skill_cha >= 3:
                $ skill_cha -= 3
            else:
                $ skill_cha = 0
            $ renpy.notify("You used 3 Charisma Points\nYour relationship with Mom has decreased")
    show pov angry at left
    show mum angry_talk at right
    mum "What is your problem? Why'd you storm off like that?"

    menu:
        "Because you and Dad were 'busy'.":
            show pov angry_talk at left
            show mum angry at right
            pov "Because you and Dad were 'busy'."
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with Mom has decreased by 3")
        "Because I thought you and I had a thing.":
            show pov angry_talk at left
            show mum angry at right
            pov "Because I thought you and I had a thing for each other."
            if mum_points >= 6 and skill_cha >= 4:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                if skill_cha >= 4:
                    $ skill_cha -= 4
                else:
                    $ skill_cha = 0
                $ renpy.notify("You used 4 Charisma Points\nYour relationship with Mom has decreased")
            else:
                if mum_points >= 3:
                    $ mum_points -= 3
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with Mom has decreased by 3")
        "Because I was mad at Dad.":
            show pov angry_talk at left
            show mum angry at right
            pov "Because I was mad. I was mad at.. Dad."
            if mum_points <= 5 and skill_cha >= 3:
                if mum_points >= 2:
                    $ mum_points -= 2
                else:
                    $ mum_points = 0
                if skill_cha >= 3:
                    $ skill_cha -= 3
                else:
                    $ skill_cha = 0
                $ renpy.notify("You used 3 Charisma Points\nYour relationship with Mom has decreased")
            else:
                if mum_points >= 4:
                    $ mum_points -= 4
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with Mom has decreased by 3")
    show pov angry at left
    show mum angry_talk at right
    mum "You do realise that your father and I are married right?"
    show mum confused_talk at right
    mum "You do understand that your father and I conceived you, right?"
    mum "Your Dad is a real man. He could please me like you never could."
    mum "You want to be treated like a man, [povname]? Start acting like one."
    show mum angry_talk at right
    mum "I only did what I did because I thought you would stand up and be the man you were supposed to be."
    mum "You know how he is nowadays."

    menu:
        "Nowadays?":
            show pov confused_talk at left
            show mum angry at right
            pov "Nowadays?"
            show pov confused at left
            show mum angry_talk at right
            mum "It's the stress! This move, th-this new job, this whole change in our life."
            mum "It's stressing the hell out of your father and it's my duty-"
            show pov angry_talk at left
            show mum sad at right
            pov "Your duty? What? As a wife to relieve him of his stress by fuc-"
            show pov sad at left
            show mum angry_talk at right
            mum "Yes, [povname]! Yes it is."
            mum "This isn't always about you. You're not the man of the house."
            mum "You don't understand what it's like having your own family."
            mum "You don't know how soul sucking it is for him to make sure he's putting bread on the table."
            mum "Every. Single. Night."
            mum "The very least I can do is be the wife he deserves."
            mum "This is what we both deserve!"
            mum "Now stop being so ungrateful. Your father has done wonders for this family. More than you ever could."
            show pov sad_talk at left
            show mum sad at right
            pov "..."
            pov "He doesn't treat you right."
            show pov sad at left
            show mum sad_talk at right
            mum "He treats me fine, [povname]."
            show pov angry_talk at left
            show mum sad at right
            pov "No he doesn't and you know it."
            mum "What about that time he took me to Monet's? That was one of the best nights of my life."
            if main_story >= 35:
                show pov shocked_talk at left
                show mum angry at right
                pov "He's not even the same Dad! The real Dad that we know wouldn't act like tha-"
                show pov angry at left
                show mum angry_talk at right
                mum "Don't."
                show pov angry_talk at left
                show mum angry at right
                pov "I'm telling you! He's someone else from a diff-"
                show pov angry at left
                show mum angry_talk at right
                mum "[povname]!"
                show pov sad_talk at left
                show mum angry at right
                pov "Mom! I know I sound crazy but please lis-"
            else:
                pass
            show pov sad at left
            show mum angry_talk at right
            mum "Don't start with that, [povname]. I'm your mother not your lover."
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with Mom has decreased by 3")
        "Be a man?":
            show pov confused_talk at left
            show mum angry at right
            pov "Be a man?"
            show pov angry at left
            show mum angry_talk at right
            mum "Yeah, it means take responsibility for your actions!"
            show pov angry_talk at left
            show mum angry at right
            pov "I know what it means, Mom!"
            show pov angry at left
            show mum angry_talk at right
            mum "Then why are you acting like a little baby?"
            show pov angry_talk at left
            show mum angry at right
            pov "I'm not acting like it!"
            show pov angry at left
            show mum angry_talk at right
            mum "Well, you sure like being treated like one."
            if mum_points >= 6:
                show pov angry at left
                show mum angry_talk at right
                mum "You know how embarrassing that is, for a person your age to still want to cuddle in their mother's arms?"
                show pov angry_talk at left
                show mum angry at right
                pov "You were the one who wanted it!"
                show pov angry at left
                show mum angry_talk at right
                mum "So? You could have said no!"
                if mum_points >= 3:
                    $ mum_points -= 3
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with Mom has decreased by 3")
            else:
                if mum_points >= 2:
                    $ mum_points -= 2
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with Mom has decreased by 2")
        "Supposed to be?":
            show pov confused_talk at left
            show mum angry at right
            pov "Supposed to be?"
            show pov confused at left
            show mum angry_talk at right
            mum "Yeah, supposed to be. I expected you to step up and be the man of the house when your father wasn't around but obviously you're still a kid."
            show pov shocked_talk at left
            show mum bored at right
            pov "I am a man!"
            show pov angry at left
            show mum bored_talk at right
            mum "You're joking, [povname]. You're nowhere near what your father is."
            mum "He's an amazing man. And you? Well..."
            show pov angry_talk at left
            show mum confused at right
            pov "If anything I would want to be the total opposite of what Dad is."
            show pov angry at left
            show mum confused_talk at right
            mum "So... a weak person who can't support his family?"
            show pov angry_talk at left
            show mum bored at right
            pov "What the hell, Mom?!"
            show pov angry at left
            show mum angry_talk at right
            mum "Oh, just grow up for once, [povname]. This isn't your fantasy where everything is perfect and you have everything you ever want."
            show pov angry_talk at left
            show mum angry at right
            pov "I'm not trying to!"
            show pov angry at left
            show mum angry_talk at right
            mum "Did I mother you too much? Is this my fault? Did I raise two girls?"
            show pov angry_talk at left
            show mum angry at right
            pov "Shut the hell up, Mom!"
            show pov angry at left
            show mum angry_talk at right
            mum "Don't speak to your mother like that, [povname]. I can call your father up hear any second now!"
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with Mom has decreased by 3")
    show pov angry at left
    show mum angry at right
    mum "..."
    show mum angry_talk at right
    mum "Your Dad may be a prick and an asshole but at least he can make me feel like a woman."
    show pov sad at left
    show mum bored_talk at right
    mum "The only thing I feel when I'm with you is emptiness, like I want more from you."
    show pov angry at left
    mum "You don't even have time for me. You want me to die all alone."
    mum "At least your father is here sometimes."
    mum "At least he's there for me."

    menu:
        "I was there for you.":
            show pov sad_talk at left
            show mum sad at right
            pov "I was there for you, wasn't I?"
            show pov sad at left
            show mum sad_talk at right
            mum "No, [povname]. No you weren't."
        "I'm still a teenager. Give me a break.":
            show pov angry_talk at left
            show mum bored at right
            pov "I'm still a teenager, Mom. Give me a break."
            show pov angry at left
            show mum angry_talk at right
            mum "Don't make excuses, [povname]. Life doesn't give you a free pass because you're a teenager."
        "Why are you being such a bitch?":
            show pov angry_talk at left
            show mum shocked at right
            pov "Why are you being such a bitch?"
            show pov angry at left
            show mum sad_talk at right
            mum "Wow. The truth finally comes out. Is that how you really think that of me, [povname]?"
    if mum_points >= 1:
        $ mum_points -= 1
    else:
        $ mum_points = 0
    $ renpy.notify("Your relationship with Mom has decreased")
    show pov sad at left
    show mum sad_talk at right
    mum "I'm very disappointed with you."

    menu:
        "Why are you disappointed?":
            show pov sad_talk at left
            show mum sad at right
            pov "Why are you disappointed?"
            show pov sad at left
            show mum sad at right
            mum "..."
            show mum bored_talk at right
            mum "Wow. You are dense."
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
        "I'm sorry.":
            show pov sad_talk at left
            show mum sad at right
            pov "I'm sorry."
            show pov sad at left
            show mum sad at right
            mum "..."
            if skill_cha >= 3:
                show mum sad_talk at right
                mum "I hope so, [povname]."
                if skill_cha >= 3:
                    $ skill_cha -= 3
                else:
                    $ skill_cha = 0
                $ renpy.notify("You used 3 Charisma Points")
            else:
                show mum sad_talk at right
                mum "You throw that phrase around so much, I don't think you know what it really means."
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with Mom has decreased")
        "Stay silent":
            show pov sad at left
            show mum sad at right
            pov "..."
            mum "...."
            if skill_cha >= 3:
                show mum sad_talk at right
                mum "Don't leave me again."
                if skill_cha >= 3:
                    $ skill_cha -= 3
                else:
                    $ skill_cha = 0
                $ renpy.notify("You lost 3 Charisma Points")
            else:
                show pov bored at left
                show mum bored_talk at right
                mum "Nothing? Good, it's best you don't say anything else to break my heart."
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with Mom has decreased")
    show pov sad at left
    show mum sad at right
    mum "..."
    show mum sad_talk at right
    mum "We were supposed to spend every night together. That was the plan."
    show mum sad at right
    mum "..."
    show mum sad_talk at right
    mum "I didn't ask very much of you, [povname]."
    mum "All I wanted was for some mother and son time before the term year ended."
    mum "I- I don't know how long we have with each other before you leave us."
    mum "Before you leave me."
    show mum sad at right
    mum "..."
    show mum sad_talk at right
    mum "I feel abandoned..."
    mum "Every single day."
    mum "It's not a feeling I had, but a constant emotion that's lurking with me."
    mum "That's why spending time with you was so important, but I guess you don't want to."
    show pov sad_talk at left
    show mum sad at right
    pov "We can still have our mother-son time if you want, Mom but..."
    show pov embarrassed_talk at left
    pov "I'm just suggesting, hear me out before you put your foot down."
    pov "How about not every night?"
    show pov sad at left
    show mum sad_talk at right
    mum "[povname]... I'm in too of a lonely mess to just have SOME nights with you."
    show pov sad_talk at left
    show mum sad at right
    pov "I can't possibly be there all the time, Mom. I'm being realistic here. We can only compromise..."
    pov "Can't you have some nights with [sister]? She's your child too."
    show pov embarrassed_talk at left
    show mum confused at right
    pov "Have some girl on girl time? I'm sure she'd be down for that."
    show pov embarrassed at left
    mum "..."
    show mum confused_talk at right
    mum "[povname]... that's a little innapropriate."
    if sister_points >= 4:
        show pov shocked_talk at left
        show mum embarrassed at right
        pov "What?! No. I'm not saying that you two... I mean- if you- what?! No. Mom!"
    elif sister_points <= 3:
        show pov shocked_talk at left
        show mum embarrassed at right
        pov "Mom?! That isn't what I meant."
    if momfallenasleep_lovewithsister == 1:
        show pov shocked at left
        show mum confused_talk at right
        mum "You're just one perverted boy aren't you? Thinking of [sister] and I like that?"
        mum "It's not just me that you want but your sister involved too, hmm?"
        show mum smirk_talk at right
        mum "Tsk tsk tsk, naughty naughty naughty."
        mum "You two are already having fun without me, aren't you?"

        menu:
            "No! That's crazy!":
                show pov sad_talk at left
                show mum smirk at right
                pov "N-No!? That's crazy!"
                show pov sad at left
                show mum smirk_talk at right
                mum "Sounding a little flustered there, are we, [povname]?"
                if mum_points <= 8:
                    $ mum_points += 2
                    $ renpy.notify("Your relationship with Mom has increased by 2")
                else:
                    $ mum_points = 10
            "You're okay with it?":
                show pov sad_talk at left
                show mum embarrassed at right
                pov "Y-you're okay with it?"
                show pov embarrassed at left
                show mum embarrassed_talk at right
                mum "You two are young and free. You have to look out for each other, don't you?"
                if mum_points <= 9:
                    $ mum_points += 1
                    $ renpy.notify("Your relationship with Mom has increased")
                else:
                    $ mum_points = 10
                if sister_points <= 9:
                    $ sister_points += 1
                    $ renpy.notify("Your relationship with [sister] has increased")
                else:
                    $ sister_points = 10
                $ renpy.pause(3,hard=True)
    else:
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "I'm just joking, [povname]. Calm down."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "Heh..heh... yeah..."
    show pov embarrassed at left
    show mum sad at right
    mum "..."
    show pov sad at left
    show mum sad_talk at right
    mum "{i}*Sigh*{/i}"
    mum "I'm sorry for what I said earlier. I'm just- y'know... well..."
    mum "The situation we're in isn't really the best to be in."
    mum "O-on top of that. I'm just naturally an emotional mess..."
    mum "Don't get me wrong... I'm still upset that you weren't there when I was counting on you."
    mum "But.. um... I hope you can forgive me for yelling at you."

    menu:
        "It's alright, Mom.":
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "It's alright, Mom."
            show pov sad_talk at left
            pov "And I'm sorry too, for not being there for you."
            pov "I understand your anger towards me."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Thanks..."
            show mum sad_talk at right
            mum "I'm not crazy or messed up in the head..."
            show pov sad at left
            mum "I just can't get over the reality of losing you."
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "I'll be there for you as much as I can. You're my number one priority."
        "I forgive you.":
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "I forgive you."
            show pov sad_talk at left
            pov "And I'm sorry too, for not being there for you."
            pov "I understand your anger towards me."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Thanks, [povname]."
            mum "I do hope you do..."
            show mum sad_talk at right
            mum "I wish I could take back all the terrible things I said to you."
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "Water under the bridge, Mom."
            pov "I can move on if you can."
        "Just give me some space.":
            show pov sad_talk at left
            show mum sad at right
            pov "Just give me some space first."
            pov "You can't just treat me like that and look down at me for not being the perfect son."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "I understand, [povname]."
            mum "Space."
            show mum sad_talk at right
            mum "I'll give you some space..."
    show pov sad at left
    show mum sad_talk at right
    mum "I guess I should head back to... um.. your dad..."
    show pov sad at left
    show mum sad at right
    pov "..."
    show pov sad_talk at left
    pov "Do you have to?"
    show pov sad at left
    show mum sad_talk at right
    mum "He's expecting me, [povname]. I don't want to upset him anymore than he already is when you showed up."

    menu:
        "Lock the door and stay with me.":
            show pov sad_talk at left
            show mum embarrassed at right
            pov "Stay with me, Mom. Lock the door and stay with me."
            show pov sad at left
            show mum embarrassed_talk at right
            mum "Heheh.. I don't think that's a good idea, [povname]."
            mum "Your Dad is more than capable of kicking that door down."
            if mum_points >= 5:
                mum "Besides, he'll get really suspicious if we're locked together in your room."
                mum "The last thing we need is suspicion."
            else:
                mum "Besides, he's already full of hormones and adrenaline from... well.. y'know."
                mum "Who know what he'd do to you... I wouldn't want anything to happen to you, honey."
        "How about I go down there and handle it?":
            show pov sad_talk at left
            show mum embarrassed at right
            pov "How about I go down there and handle it?"
            show pov bored at left
            show mum embarrassed_talk at right
            mum "Hehehe.. yeah, I don't think you should take on your dad. No offence, honey."
            show pov confused_talk at left
            show mum sad at right
            pov "What? Just because he's bigger than me?"
            show pov embarrassed at left
            show mum sad_talk at right
            mum "[povname]. I don't want you fighting your father for me, that isn't right."
            mum "That actually says a lot about our family and I don't want to be known as ‘that messed up family'."
            if mum_points >= 5:
                show pov embarrassed_talk at left
                show mum embarrassed at right
                pov "Mom... between you and me, it's already messed up."
                show pov smirk at left
                show mum embarrassed_talk at right
                mum "Shhh... you don't have to point that out."
            else:
                show pov embarrassed_talk at left
                show mum embarrassed at right
                pov "Right.. right. Yeah, what was I thinking?"
                show pov embarrassed at left
                show mum embarrassed_talk at right
                mum "Even if you go down there, I'm going to have to clean up the mess, and I'm not in a cleaning mood..."
        "Alright.":
            show pov sad_talk at left
            show mum sad at right
            pov "Alright, Mom..."
            show pov embarrassed_talk at left
            pov "Just.. yell out my name if you need me."
            show pov sad at left
            show mum embarrassed_talk at right
            mum "I'm not going to yell out your name."
            if mum_points >= 6:
                show pov bored at left
                mum "Yelling out some other guy's name is one thing but to scream my own son's name?"
                mum "He's going to want answers..."
                show pov bored_talk at left
                show mum embarrassed at right
                pov "Mom. It's a cry of help not a moan of pleasure."
            else:
                pass
    show pov sad at left
    show mum embarrassed_talk at right
    mum "I'll be fine, sweetie. Just, whatever you do. Don't come downstairs... Promise?"

    menu:
        "I promise.":
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "I promise..."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Thank you, [povname]. I love you?"
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "I love you too."
            $ momfeelingabandoned_promise = 1
        "I can't promise that.":
            show pov sad_talk at left
            show mum sad at right
            pov "I can't promise that..."
            show pov sad at left
            show mum sad_talk at right
            mum "Just please...? Don't do anything stupid."
            show pov sad_talk at left
            show mum embarrassed at right
            pov "Alright, Mom."
            $ momfeelingabandoned_promise = 0
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with Mom has decreased")
            else:
                $ mum_points = 0
    if mum_points >= 6:
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "And... [povname]."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "Yeah?"
        scene bg mommakeupkiss_1
        $ renpy.pause(1.2, hard=True)
        show bg mommakeupkiss_2
        $ renpy.pause(1.2, hard=True)
        show bg mommakeupkiss_1
        $ renpy.pause()
        scene black
        with fade
    else:
        scene black
        with fade
    pov "{i}The fight really left a big tear in our relationship.{/i}"
    pov "{i}She may have acted like it was all okay, but I know she's still broken inside.{/i}"
    pov "{i}Who is at fault? Am I at fault for not being there for her?{/i}"
    pov "{i}Or is it her fault for forcing onto me such demanding expectations.{/i}"
    pov "{i}I love her and I know she loves me, but I am merely an animal with a lust for many different women.{/i}"
    pov "{i}I honestly can't expect myself to be loyal to her, and only her forever.{/i}"
    pov "{i}If I want this to work between us, I need to suck it up and mend the tear.{/i}"
    pov "{i}She is my mom, and I love her all too much. I'll need to build the trust between us again.{/i}"
    pov "..."
    pov "{i}Who ever said wincest was a walk in the park?{/i}"
    $ gtime = 3
    $ mum_path = 9

    jump lbl_mybedroom_night_setup

### NO WINC ###
label lbl_feeling_abandoned_winc0:

    scene bg mybedroom_night_lightson
    with fade
    show pov angry at left
    with dissolve
    show mum angry_talk at right
    with dissolve
    mum "Hey, mister! We need to talk."

    menu:
        "What's there to talk about?":
            show pov angry_talk at left
            show mum angry at right
            pov "What's there to talk about?"
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with [missus] has decreased by 3")
        "I don't want to talk to you.":
            show pov angry_talk at left
            show mum angry at right
            pov "I don't want to talk to you."
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with [missus] has decreased by 3")
        "Why don't you just go finish what YOU started.":
            show pov angry_talk at left
            show mum angry at right
            pov "Why don't you just go finish what YOU started."
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with [missus] has decreased by 3")
        "Fine, let's talk." if skill_cha >= 3:
            show pov angry_talk at left
            show mum angry at right
            pov "Fine, let's talk."
            if mum_points >= 1:
                $ mum_points -= 1
            else:
                $ mum_points = 0
            if skill_cha >= 3:
                $ skill_cha -= 3
            else:
                $ skill_cha = 0
            $ renpy.notify("You used 3 Charisma Points\nYour relationship with [missus] has decreased")
    show pov angry at left
    show mum angry_talk at right
    mum "What is your problem? Why'd you storm off like that?"

    menu:
        "Because you and [dadname] were 'busy'.":
            show pov angry_talk at left
            show mum angry at right
            pov "Because you and [dadname] were 'busy'."
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with [missus] has decreased by 3")
        "Because I thought you and I had a thing.":
            show pov angry_talk at left
            show mum angry at right
            pov "Because I thought you and I had a thing for each other."
            if mum_points >= 6 and skill_cha >= 4:
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                if skill_cha >= 4:
                    $ skill_cha -= 4
                else:
                    $ skill_cha = 0
                $ renpy.notify("You lost 4 Charisma Points\nYour relationship with [missus] has decreased")
            else:
                if mum_points >= 3:
                    $ mum_points -= 3
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with [missus] has decreased by 3")
        "Because I was mad at [dadname].":
            show pov angry_talk at left
            show mum angry at right
            pov "Because I was mad. I was mad at.. [dadname]."
            if mum_points <= 5 and skill_cha >= 3:
                if mum_points >= 2:
                    $ mum_points -= 2
                else:
                    $ mum_points = 0
                if skill_cha >= 3:
                    $ skill_cha -= 3
                else:
                    $ skill_cha = 0
                $ renpy.notify("You lost 3 Charisma Points\nYour relationship with [missus] has decreased")
            else:
                if mum_points >= 4:
                    $ mum_points -= 4
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with [missus] has decreased by 3")
    show pov angry at left
    show mum angry_talk at right
    mum "You do realise that your [dadrole] and I are married right?"
    show mum confused_talk at right
    mum "You do understand that your [dadrole] and I took you in, right?"
    mum "Your [dadrole] is a real man. He could please me like you never could."
    mum "You want to be treated like a man, [povname]? Start acting like one."
    show mum angry_talk at right
    mum "I only did what I did because I thought you would stand up and be the man you were supposed to be."
    mum "You know how he is nowadays."

    menu:
        "Nowadays?":
            show pov confused_talk at left
            show mum angry at right
            pov "Nowadays?"
            show pov confused at left
            show mum angry_talk at right
            mum "It's the stress! This move, th-this new job, this whole change in our life."
            mum "It's stressing the hell out of your [dadrole] and it's my duty-"
            show pov angry_talk at left
            show mum sad at right
            pov "Your duty? What? As a wife to relieve him of his stress by fuc-"
            show pov sad at left
            show mum angry_talk at right
            mum "Yes, [povname]! Yes it is."
            mum "This isn't always about you. You are not the man of the house."
            mum "You don't understand what it's like having your own family."
            mum "You don't know how soul sucking it is for him to make sure he's putting bread on the table."
            mum "Every. Single. Night."
            mum "The very least I can do is be the wife he deserves."
            mum "This is what we both deserve!"
            mum "Now stop being so ungrateful. Your [dadrole] has done wonders for this family. More than you ever could."
            show pov sad_talk at left
            show mum sad at right
            pov "..."
            pov "He doesn't treat you right."
            show pov sad at left
            show mum sad_talk at right
            mum "He treats me fine, [povname]."
            show pov angry_talk at left
            show mum sad at right
            pov "No he doesn't and you know it."
            mum "What about that time he took me to Monet's? That was one of the best nights of my life."
            if main_story >= 35:
                show pov shocked_talk at left
                show mum angry at right
                pov "He's not even the same [dadrole]! The real [dadname] that we know wouldn't act like tha-"
                show pov angry at left
                show mum angry_talk at right
                mum "Don't."
                show pov angry_talk at left
                show mum angry at right
                pov "I'm telling you! He's someone else from a diff-"
                show pov angry at left
                show mum angry_talk at right
                mum "[povname]!"
                show pov sad_talk at left
                show mum angry at right
                pov "Mom! I know I sound crazy but please lis-"
            else:
                pass
            show pov sad at left
            show mum angry_talk at right
            mum "Don't start with that, [povname]. I'm your [mumrole] not your lover."
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with [missus] has decreased by 3")
        "Be a man?":
            show pov confused_talk at left
            show mum angry at right
            pov "Be a man?"
            show pov angry at left
            show mum angry_talk at right
            mum "Yeah, it means take responsibility for your actions!"
            show pov angry_talk at left
            show mum angry at right
            pov "I know what it means, [missus]!"
            show pov angry at left
            show mum angry_talk at right
            mum "Then why are you acting like a little baby?"
            show pov angry_talk at left
            show mum angry at right
            pov "I'm not acting like it!"
            show pov angry at left
            show mum angry_talk at right
            mum "Well, you sure like being treated like one."
            if mum_points >= 6:
                show pov angry at left
                show mum angry_talk at right
                mum "You know how embarrassing that is, for a person your age to still want to cuddle in their [mumrole]'s arms?"
                show pov angry_talk at left
                show mum angry at right
                pov "You were the one who wanted it!"
                show pov angry at left
                show mum angry_talk at right
                mum "So? You could have said no!"
                if mum_points >= 3:
                    $ mum_points -= 3
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with [missus] has decreased by 3")
            else:
                if mum_points >= 2:
                    $ mum_points -= 2
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with [missus] has decreased by 2")
        "Supposed to be?":
            show pov confused_talk at left
            show mum angry at right
            pov "Supposed to be?"
            show pov confused at left
            show mum angry_talk at right
            mum "Yeah, supposed to be. I expected you to step up and be the man of the house when your [dadrole] wasn't around but obviously you're still a kid."
            show pov shocked_talk at left
            show mum bored at right
            pov "I am a man!"
            show pov angry at left
            show mum bored_talk at right
            mum "You're joking, [povname]. You're nowhere near what your [dadrole] is."
            mum "He's an amazing man. And you? Well..."
            show pov angry_talk at left
            show mum confused at right
            pov "If anything I would want to be the total opposite of what [dadname] is."
            show pov angry at left
            show mum confused_talk at right
            mum "So... a weak person?"
            show pov angry_talk at left
            show mum bored at right
            pov "What the hell, [missus]?!"
            show pov angry at left
            show mum angry_talk at right
            mum "Oh, just grow up for once, [povname]. This isn't your fantasy where everything is perfect and you have everything you ever want."
            show pov angry_talk at left
            show mum angry at right
            pov "I'm not trying to!"
            show pov angry at left
            show mum angry_talk at right
            mum "Did I coddle you too much? Is this my fault? Did I raise two girls?"
            show pov angry_talk at left
            show mum angry at right
            pov "Shut the hell up, [missus]!"
            show pov angry at left
            show mum angry_talk at right
            mum "Don't speak to your [mumrole] like that, [povname]. I can call your [dadrole] up hear any second now!"
            if mum_points >= 3:
                $ mum_points -= 3
            else:
                $ mum_points = 0
            $ renpy.notify("Your relationship with [missus] has decreased by 3")
    show pov angry at left
    show mum angry at right
    mum "..."
    show mum angry_talk at right
    mum "Your [dadrole] may be a prick and an asshole but at least he can make me feel like a woman."
    show pov sad at left
    show mum bored_talk at right
    mum "The only thing I feel when I'm with you is emptiness, like I want more from you."
    show pov angry at left
    mum "You don't even have time for me. You want me to die all alone."
    mum "At least your [dadrole] is here sometimes."
    mum "At least he's there for me."

    menu:
        "I was there for you.":
            show pov sad_talk at left
            show mum sad at right
            pov "I was there for you, wasn't I?"
            show pov sad at left
            show mum sad_talk at right
            mum "No, [povname]. No you weren't."
        "I'm still a teenager. Give me a break.":
            show pov angry_talk at left
            show mum bored at right
            pov "I'm still a teenager, Mom. Give me a break."
            show pov angry at left
            show mum angry_talk at right
            mum "Don't make excuses, [povname]. Life doesn't give you a free pass because you're a teenager."
        "Why are you being such a bitch?":
            show pov angry_talk at left
            show mum shocked at right
            pov "Why are you being such a bitch?"
            show pov angry at left
            show mum sad_talk at right
            mum "Wow. The truth finally comes out. Is that how you really think that of me, [povname]?"
    if mum_points >= 1:
        $ mum_points -= 1
    else:
        $ mum_points = 0
    $ renpy.notify("Your relationship with [missus] has decreased")
    show pov sad at left
    show mum sad_talk at right
    mum "I'm very disappointed with you."

    menu:
        "Why are you disappointed?":
            show pov sad_talk at left
            show mum sad at right
            pov "Why are you disappointed?"
            show pov sad at left
            show mum sad at right
            mum "..."
            show mum bored_talk at right
            mum "Wow. You are dense."
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
        "I'm sorry.":
            show pov sad_talk at left
            show mum sad at right
            pov "I'm sorry."
            show pov sad at left
            show mum sad at right
            mum "..."
            if skill_cha >= 3:
                show mum sad_talk at right
                mum "I hope so, [povname]."
                if skill_cha >= 3:
                    $ skill_cha -= 3
                else:
                    $ skill_cha = 0
                $ renpy.notify("You used 3 Charisma Points")
            else:
                show mum sad_talk at right
                mum "You throw that phrase around so much, I don't think you know what it really means."
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with [missus] has decreased")
        "Stay silent":
            show pov sad at left
            show mum sad at right
            pov "..."
            mum "...."
            if skill_cha >= 3:
                show mum sad_talk at right
                mum "Don't leave me again."
                if skill_cha >= 3:
                    $ skill_cha -= 3
                else:
                    $ skill_cha = 0
                $ renpy.notify("You lost 3 Charisma Points")
            else:
                show pov bored at left
                show mum bored_talk at right
                mum "Nothing? Good, it's best you don't say anything else to break my heart."
                if mum_points >= 1:
                    $ mum_points -= 1
                else:
                    $ mum_points = 0
                $ renpy.notify("Your relationship with [missus] has decreased")
    show pov sad at left
    show mum sad at right
    mum "..."
    show mum sad_talk at right
    mum "We were supposed to spend every night together. That was the plan."
    show mum sad at right
    mum "..."
    show mum sad_talk at right
    mum "I didn't ask very much of you, [povname]."
    mum "All I wanted was for some [mumrole] and [povmumrole] time before the term year ended."
    mum "I- I don't know how long we have with each other before you leave us."
    mum "Before you leave me."
    show mum sad at right
    mum "..."
    show mum sad_talk at right
    mum "I feel abandoned..."
    mum "Every single day."
    mum "It's not a feeling I had, but a constant emotion that's lurking with me."
    mum "That's why spending time with you was so important, but I guess you don't want to."
    show pov sad_talk at left
    show mum sad at right
    pov "We can still have our [mumrole]-[povmumrole] time if you want, [missus] but..."
    show pov embarrassed_talk at left
    pov "I'm just suggesting, hear me out before you put your foot down."
    pov "How about not every night?"
    show pov sad at left
    show mum sad_talk at right
    mum "[povname]... I'm in too of a lonely mess to just have SOME nights with you."
    show pov sad_talk at left
    show mum sad at right
    pov "I can't possibly be there all the time, [missus]. I'm being realistic here. We can only compromise..."
    pov "Can't you have some nights with [sister]? She's your [povmumrole] too."
    show pov embarrassed_talk at left
    show mum confused at right
    pov "Have some girl on girl time? I'm sure she'd be down for that."
    show pov embarrassed at left
    mum "..."
    show mum confused_talk at right
    mum "[povname]... that's a little innapropriate."
    if sister_points >= 4:
        show pov shocked_talk at left
        show mum embarrassed at right
        pov "What?! No. I'm not saying that you two... I mean- if you- what?! No. [missus]!"
    elif sister_points <= 3:
        show pov shocked_talk at left
        show mum embarrassed at right
        pov "[missus]?! That isn't what I meant."
    if momfallenasleep_lovewithsister == 1:
        show pov shocked at left
        show mum confused_talk at right
        mum "You're just one perverted boy aren't you? Thinking of your [sisrole] and me like that?"
        mum "It's not just me that you want but your [sisrole] involved too, hmm?"
        show mum smirk_talk at right
        mum "Tsk tsk tsk, naughty naughty naughty."
        mum "You two are already having fun without me, aren't you?"

        menu:
            "No! That's crazy!":
                show pov sad_talk at left
                show mum smirk at right
                pov "N-No!? That's crazy!"
                show pov sad at left
                show mum smirk_talk at right
                mum "Sounding a little flustered there, are we, [povname]?"
                if mum_points <= 8:
                    $ mum_points += 2
                else:
                    $ mum_points = 10
                $ renpy.notify("Your relationship with [missus] has increased by 2")
            "You're okay with it?":
                show pov sad_talk at left
                show mum embarrassed at right
                pov "Y-you're okay with it?"
                show pov embarrassed at left
                show mum embarrassed_talk at right
                mum "You two are young and free. You have to look out for each other, don't you?"
                if mum_points <= 9:
                    $ mum_points += 1
                    $ renpy.notify("Your relationship with [missus] has increased")
                else:
                    $ mum_points = 10
                if sister_points <= 9:
                    $ sister_points += 1
                    $ renpy.notify("Your relationship with [sister] has increased")
                else:
                    $ sister_points = 10
                $ renpy.pause(3,hard=True)
    else:
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "I'm just joking, [povname]. Calm down."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "Heh..heh... yeah..."
    show pov embarrassed at left
    show mum sad at right
    mum "..."
    show pov sad at left
    show mum sad_talk at right
    mum "{i}*Sigh*{/i}"
    mum "I'm sorry for what I said earlier. I'm just- y'know... well..."
    mum "The situation we're in isn't really the best to be in."
    mum "O-on top of that. I'm just naturally an emotional mess..."
    mum "Don't get me wrong... I'm still upset that you weren't there when I was counting on you."
    mum "But.. um... I hope you can forgive me for yelling at you."

    menu:
        "It's alright, [missus].":
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "It's alright, [missus]."
            show pov sad_talk at left
            pov "And I'm sorry too, for not being there for you."
            pov "I understand your anger towards me."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Thanks..."
            show mum sad_talk at right
            mum "I'm not crazy or messed up in the head..."
            show pov sad at left
            mum "I just can't get over the reality of losing you."
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "I'll be there for you as much as I can. You are my number one priority."
        "I forgive you.":
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "I forgive you."
            show pov sad_talk at left
            pov "And I'm sorry too, for not being there for you."
            pov "I understand your anger towards me."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Thanks, [povname]."
            mum "I do hope you do..."
            show mum sad_talk at right
            mum "I wish I could take back all the terrible things I said to you."
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "Water under the bridge, [missus]."
            pov "I can move on if you can."
        "Just give me some space.":
            show pov sad_talk at left
            show mum sad at right
            pov "Just give me some space first."
            pov "You can't just treat me like that and look down at me for not being the perfect [povmumrole]."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "I understand, [povname]."
            mum "Space."
            show mum sad_talk at right
            mum "I'll give you some space..."
    show pov sad at left
    show mum sad_talk at right
    mum "I guess I should head back to... um.. your [dadrole]..."
    show pov sad at left
    show mum sad at right
    pov "..."
    show pov sad_talk at left
    pov "Do you have to?"
    show pov sad at left
    show mum sad_talk at right
    mum "He's expecting me, [povname]. I don't want to upset him anymore than he already is when you showed up."

    menu:
        "Lock the door and stay with me.":
            show pov sad_talk at left
            show mum embarrassed at right
            pov "Stay with me, [missus]. Lock the door and stay with me."
            show pov sad at left
            show mum embarrassed_talk at right
            mum "Heheh.. I don't think that's a good idea, [povname]."
            mum "Your [dadrole] is more than capable of kicking that door down."
            if mum_points >= 5:
                mum "Besides, he'll get really suspicious if we're locked together in your room."
                mum "The last thing we need is suspicion."
            else:
                mum "Besides, he's already full of hormones and adrenaline from... well.. y'know."
                mum "Who know what he'd do to you... I wouldn't want anything to happen to you, honey."
        "How about I go down there and handle it?":
            show pov sad_talk at left
            show mum embarrassed at right
            pov "How about I go down there and handle it?"
            show pov bored at left
            show mum embarrassed_talk at right
            mum "Hehehe.. yeah, I don't think you should take on your [dadrole]. No offence, honey."
            show pov confused_talk at left
            show mum sad at right
            pov "What? Just because he's bigger than me?"
            show pov embarrassed at left
            show mum sad_talk at right
            mum "[povname]. I don't want you fighting your [dadrole] for me, that is not right."
            mum "That actually says a lot about our household and I don't want to be known as ‘that messed up household'."
            if mum_points >= 5:
                show pov embarrassed_talk at left
                show mum embarrassed at right
                pov "[missus]... between you and me, it's already messed up."
                show pov smirk at left
                show mum embarrassed_talk at right
                mum "Shhh... you don't have to point that out."
            else:
                show pov embarrassed_talk at left
                show mum embarrassed at right
                pov "Right.. right. Yeah, what was I thinking?"
                show pov embarrassed at left
                show mum embarrassed_talk at right
                mum "Even if you go down there, I'm going to have to clean up the mess, and I'm not in a cleaning mood..."
        "Alright.":
            show pov sad_talk at left
            show mum sad at right
            pov "Alright, [missus]..."
            show pov embarrassed_talk at left
            pov "Just.. yell out my name if you need me."
            show pov sad at left
            show mum embarrassed_talk at right
            mum "I'm not going to yell out your name."
            if mum_points >= 6:
                show pov bored at left
                mum "Yelling out some other guy's name is one thing but to scream my own [povmumrole]'s name?"
                mum "He's going to want answers..."
                show pov bored_talk at left
                show mum embarrassed at right
                pov "[missus]. It's a cry of help not a moan of pleasure."
            else:
                pass
    show pov sad at left
    show mum embarrassed_talk at right
    mum "I'll be fine, sweetie. Just, whatever you do. Don't come downstairs... Promise?"

    menu:
        "I promise.":
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "I promise..."
            show pov embarrassed at left
            show mum embarrassed_talk at right
            mum "Thank you, [povname]. I love you?"
            show pov embarrassed_talk at left
            show mum embarrassed at right
            pov "I love you too."
            $ momfeelingabandoned_promise = 1
        "I can't promise that.":
            show pov sad_talk at left
            show mum sad at right
            pov "I can't promise that..."
            show pov sad at left
            show mum sad_talk at right
            mum "Just please...? Don't do anything stupid."
            show pov sad_talk at left
            show mum embarrassed at right
            pov "Alright, [missus]."
            $ momfeelingabandoned_promise = 0
            if mum_points >= 1:
                $ mum_points -= 1
                $ renpy.notify("Your relationship with [missus] has decreased")
            else:
                $ mum_points = 0
    if mum_points >= 6:
        show pov embarrassed at left
        show mum embarrassed_talk at right
        mum "And... [povname]."
        show pov embarrassed_talk at left
        show mum embarrassed at right
        pov "Yeah?"
        scene bg mommakeupkiss_1
        $ renpy.pause(1.2, hard=True)
        show bg mommakeupkiss_2
        $ renpy.pause(1.2, hard=True)
        show bg mommakeupkiss_1
        $ renpy.pause()
        scene black
        with fade
    else:
        scene black
        with fade
    pov "{i}The fight really left a big tear in our relationship.{/i}"
    pov "{i}She may have acted like it was all okay, but I know she's still broken inside.{/i}"
    pov "{i}Who is at fault? Am I at fault for not being there for her?{/i}"
    pov "{i}Or is it her fault for forcing onto me such demanding expectations.{/i}"
    pov "{i}I love her and I know she loves me, but I am merely an animal with a lust for many different women.{/i}"
    pov "{i}I honestly can't expect myself to be loyal to her, and only her forever.{/i}"
    pov "{i}If I want this to work between us, I need to suck it up and mend the tear.{/i}"
    pov "{i}She is my [mumrole], and I love her all too much. I'll need to build the trust between us again.{/i}"
    pov "..."
    pov "{i}Who ever said trust was a walk in the park?{/i}"
    $ gtime = 3
    $ mum_path = 9

    jump lbl_mybedroom_night_setup
