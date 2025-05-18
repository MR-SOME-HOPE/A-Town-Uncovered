## Indecent Arrest ##
label lbl_indecent_arrest:
    default indecentarrest_shutup = 0
    if winc == 0:
        jump lbl_indecent_arrest_winc0

    scene bg indecentarrest_1
    with fade
    pov "{i}Well... I can safely say this isn't how I was planning to spend my morning.{/i}"
    pau "Hey, Flash! You got a visitor."
    pov "{i}He is talking about me, isn't he?{/i}"

    scene bg jailhouse_1
    with fade
    show povn shocked_talk at left
    with dissolve
    show dad angry at right
    with dissolve
    pov "Dad!"
    show povn confused_talk at left
    pov "...Dad?"
    pov "Uhh-"
    show povn shocked at left
    show dad angry_talk at right
    dad "Shut up! You won't believe how much trouble you're in right now. Put some damn clothes on!"
    show povn sad_talk at left
    show dad angry at right
    pov "Dad, please, you need to get me out of here!"
    show povn sad at left
    show dad angry_talk at right
    dad "What I need to do is go back home and try to calm your mother down!"
    dad "Not only have you been missing for the entire day but when we started asking around for you, we find out you were found unconscious and naked at the lake!"
    dad "Not to mention arrested!"
    dad "Your mother almost had a heart attack when a police officer came knocking at our door, she thought something happened to you!"
    dad "What the hell you were even thinking?!"

    menu:
        "I'm sorry I let you guys down.":
            #if dad_points <= 9:
            #    $ dad_points += 1
            #else:
            #    $ dad_points = 10
            #if mum_points <= 9:
            #    $ mum_points += 1
            #else:
            #    $ mum_points = 10
            #$ renpy.notify("Your relationship with Dad has increased")
            #$ renpy.pause(3,hard=False)
            #$ renpy.notify("Your relationship with Mom has increased")
            show povn sad_talk at left
            show dad angry at right
            pov "I'm sorry I let you guys down. I promise it won't happen again."
            show povn sad at left
            show dad neutral_talk at right
            dad "{i}*Sigh*{/i}"
            show povn embarrassed at left
            show dad angry_talk at right
            dad "Just make sure this shit doesn't happen again and you'll make everyone's life easier, got that?"
            show povn embarrassed_talk at left
            show dad angry at right
            pov "Every single word."
            show povn sad at left
            show dad neutral_talk at right
            dad "I'll go back home and try to calm your mother down, she has been losing her mind all night"
        "I had a very crazy night.":
            show povn sad_talk at left
            show dad angry at right
            pov "I had a very crazy night. Things... got out of hand."
            show povn sad at left
            show dad angry_talk at right
            dad "I bet, we are going to have a VERY long talk about it when you're back home tomorrow."
            dad "Your mother is furious and worried sick so you better have a very good damn excuse for all of this!"
            dad "We even had to talk to your university, to figure out where you where and they had to ask your friends!"
            dad "You had us all looking for you while you were out having fun doing God knows what!"
        "Will you shut up and listen to what I have to say?!":
            $ indecentarrest_shutup = 1
            #if dad_points >= 2:
            #    $ dad_points -= 2
            #else:
            #    $ dad_points = 0
            #if mum_points >= 1:
            #    $ mum_points -= 1
            #else:
            #    $ mum_points = 0
            #$ renpy.notify("Your relationship with Dad has decreased by 2")
            #$ renpy.pause(3,hard=False)
            #$ renpy.notify("Your relationship with Mom has decreased")
            show povn angry_talk at left
            show dad angry at right
            pov "Will you shut up and listen to what I have to say?!"
            pov "Why are you even here?"
            show povn angry at left
            show dad angry_talk at right
            dad "Hey! Shut the fuck up."
            dad "I. Don't. Want. To hear ANYTHING you have to say right now!"
            dad "You're lucky your mother cares enough to make me come down here."
            show povn sad at left
            dad "She's distraught right now."
            dad "Your mother was crying the whole night thinking something horrible had happened to you!"
            dad "She made me and your sister go out looking for you while she calls what few people she knows around town to ask if they have seen you."
            dad "And now you have the balls to tell me to shut up?!"
            dad "How do you think she felt when the police showed up at our door telling us they found you naked by the side of the lake?"
            dad "They even told us that you may have been drugged or have been taking drugs."
            dad "She nearly fainted at our doorstep!"
            dad "When she sees you tomorrow I can guarantee she will have her own comments about all of this!"
    show povn shocked_talk at left
    show dad neutral at right
    pov "Wait, so I'm going to spend the whole day here?!"
    show povn sad_talk at left
    pov "Aren't you going to bail me out?"
    show povn sad at left
    show dad neutral_talk at right
    dad "Officer Mina informed me that the state law dictates that all first time offenders for Public Exposure spend the minimum time of 24 hours."
    dad "Be thankful she won't press any further charges and this should serve as the first part to your punishment."
    dad "Hopefully this will be enough to teach you the lesson."
    dad "I knew this would happen sooner or later. And yet, I'm very disappointed in you."
    if indecentarrest_shutup == 1:
        show dad angry_talk at right
        dad "And maybe fix that attitude of yours before your mother picks you up tomorrow morning or I swear to God..."
    hide dad neutral_talk
    hide dad angry_talk
    show povn bored at left
    show min neutral_talk at Position(xpos=1350)
    show dad neutral at right
    mina "Don't worry, sir, this isn't the first time I've had some dumb teen locked behind those bars for something like this."
    show min smirk_talk at Position(xpos=1350)
    mina "A day or two in there is usually enough for them to learn their lesson."
    show min neutral_talk at Position(xpos=1350)
    mina "His tests came negative regarding any kind of foreign substances in his bloodstream, but if he did take anything his body would have passed it down by now."
    if backtosafety_angel == 1:
        mina "But, to be honest, your son doesn't seem the type to get into any of that stuff, he seems like a good kid."
    show min neutral at Position(xpos=1350)
    show dad neutral_talk at right
    dad "I'll leave him in your more than capable hands then, Officer."
    dad "Your mother will be the one to come to pick you up tomorrow."
    dad "She'll want to hear your version of the story before she decides the punishment."
    dad "I've had enough of you for one lifetime."
    if indecentarrest_shutup == 1:
        show dad angry_talk at right
        dad "She will want an explanation of all this and I want this attitude of yours taken care of by the next time I see you, you got that?"
        show povn bored_talk at left
        show dad neutral at right
        pov "...Yes, sir..."
    else:
        show dad neutral_talk at right
        dad "You better come up with a tear jerking apology if you wanna live to see another day."
        show povn bored_talk at left
        show dad neutral at right
        pov "I will..."
        show povn bored at left
        show dad neutral_talk at right
        dad "Who knew you could let me down any further than you already have."
        show povn bored_talk at left
        show dad neutral at right
        pov "...Yeah. Who knew..?"
    show povn bored at left
    show min neutral at Position(xpos=1350)
    show dad neutral_talk at right
    dad "Well, with that I should take my leave, Officer."
    show min neutral_talk at Position(xpos=1350)
    show dad neutral at right
    mina "Careful on your way home, sir. We'll take care of your kid."
    show povn bored at left
    show min confused at Position(xpos=1350)
    show dad neutral_talk at right
    dad "Oh, and before I forget."
    show povn shocked at left
    show min smirk at Position(xpos=1350)
    show dad neutral_talk at right
    dad "I actually have a change of clothes with me for you."
    show dad neutral_talk at right
    dad "Courtesy of your mother."
    show povn angry_talk at left
    show min neutral at Position(xpos=1350)
    show dad neutral at right
    pov "What the hell, why didn't you give that to me earlier!"

    scene black
    with fade
    $ renpy.pause(0.5,hard=True)

    scene bg jailhouse_1
    with fade
    show pov sad at left
    with dissolve
    show min smirk_talk at right
    with dissolve
    mina "Try and get comfortable, it's going to be a long, boring 24 hours."
    show pov sad_talk at left
    show min neutral at right
    pov "Yeah, I can only imagine."

    scene black
    with fade
    if day <= 5:
        $ day += 1
    else:
        $ day = 0
    call lbl_next_date
    "The next morning."

    scene bg jailhouse_1
    show min bored_talk at right
    with hpunch
    mina "Wake up, Flash. Come on kid, you're free to go."
    show pov bored_talk at left
    with dissolve
    pov "T-that nickname catches on real quick, doesn't it?"
    show pov bored at left
    show min smirk_talk at right
    mina "If the boot fits."
    show pov shocked at left
    show min neutral_talk at right
    mina "Anyway, here you go ma'am, safe and sound."
    hide min neutral_talk
    show pov embarrassed at left
    show mumc embarrassed_talk at Position(xpos=1350)
    show min neutral at right
    mum "Thank you, Officer Mina, I'm sorry for all the trouble he's caused."
    show mumc embarrassed at Position(xpos=1350)
    show min neutral_talk at right
    mina "No need to worry about that, Ma'am."
    mina "Boys will be boys. Just plain stupid."
    mina "And he is at that age of making reaaally stupid decisions."
    show min confused_talk at right
    mina "Just make sure I don't see you back here anytime soon, [povname]. You got that?"
    show min bored_talk at right
    mina "Next time I won't go so easy on you."

    menu:
        "I'll try not to be a nuisance.":
            pass
        "I certainly wouldn't mind seeing you again.":
            pass
        "I hope there is a comfier cell next time.":
            pass
    show pov embarrassed_talk at left
    show min bored at right
    pov "I-"
    show pov bored at left
    show mumc angry_talk at Position(xpos=1350)
    show min neutral at right
    mum "I'll make sure he stays out of your hair, Officer. Now, if you'll excuse us."
    $ main_story = 38

    jump lbl_the_awkward_ride_home

###########
## NO WINC ##
## Indecent Arrest

label lbl_indecent_arrest_winc0:

    scene bg indecentarrest_1
    with fade
    pov "{i}Well... I can safely say this isn't how I was planning to spend my morning.{/i}"
    pau "Hey, Flash! You got a visitor."
    pov "{i}He is talking about me, isn't he?{/i}"

    scene bg jailhouse_1
    with fade
    show povn shocked_talk at left
    with dissolve
    show dad angry at right
    with dissolve
    pov "[dadname]!"
    show povn confused_talk at left
    pov "...[dadname]?"
    pov "Uhh-"
    show povn shocked at left
    show dad angry_talk at right
    dad "Shut up! You won't believe how much trouble you're in right now. Put some damn clothes on!"
    show povn sad_talk at left
    show dad angry at right
    pov "[dadname], please, you need to get me out of here!"
    show povn sad at left
    show dad angry_talk at right
    dad "What I need to do is go back home and try to calm your [mumrole] down!"
    dad "Not only have you been missing for the entire day but when we started asking around for you we find out you were found unconscious and naked at the lake!"
    dad "Not to mention arrested!"
    dad "Your [mumrole] almost had a heart attack when a police officer came knocking at our door, she thought something happened to you!"
    dad "What the hell you were even thinking?!"

    menu:
        "I'm sorry I let you guys down.":
            #if dad_points <= 9:
            #    $ dad_points += 1
            #else:
            #    $ dad_points = 10
            #if mum_points <= 9:
            #    $ mum_points += 1
            #else:
            #    $ mum_points = 10
            #$ renpy.notify("Your relationship with [dadname] has increased")
            #$ renpy.pause(3,hard=False)
            #$ renpy.notify("Your relationship with [missus] has increased")
            show povn sad_talk at left
            show dad angry at right
            pov "I'm sorry I let you guys down. I promise it won't happen again."
            show povn sad at left
            show dad neutral_talk at right
            dad "{i}*Sigh*{/i}"
            show povn embarrassed at left
            show dad angry_talk at right
            dad "Just make sure this shit doesn't happen again and you'll make everyone's life easier, got that?"
            show povn embarrassed_talk at left
            show dad angry at right
            pov "Every single word."
            show povn sad at left
            show dad neutral_talk at right
            dad "I'll go back home and try to calm your [mumrole] down, she has been losing her mind all night"
        "I had a very crazy night.":
            show povn sad_talk at left
            show dad angry at right
            pov "I had a very crazy night. Things... got out of hand."
            show povn sad at left
            show dad angry_talk at right
            dad "I bet, we are going to have a VERY long talk about it when you're back home tomorrow."
            dad "Your mother is furious and worried sick so you better have a very good damn excuse for all of this!"
            dad "We even had to talk to your university, to figure out where you where and they had to ask your friends!"
            dad "You had us all looking for you while you were out having fun doing God knows what!"
        "Will you shut up and listen to what I have to say?!":
            $ indecentarrest_shutup = 1
            #if dad_points >= 2:
            #    $ dad_points -= 2
            #else:
            #    $ dad_points = 0
            #if mum_points >= 1:
            #    $ mum_points -= 1
            #else:
            #    $ mum_points = 0
            $ renpy.notify("Your relationship with [dadname] has decreased by 2")
            $ renpy.pause(3,hard=False)
            $ renpy.notify("Your relationship with [missus] has decreased")
            show povn angry_talk at left
            show dad angry at right
            pov "Will you shut up and listen to what I have to say?!"
            pov "Why are you even here?"
            show povn angry at left
            show dad angry_talk at right
            dad "Hey! Shut the fuck up."
            dad "I. Don't. Want. To hear ANYTHING you have to say right now!"
            dad "You're lucky your [mumrole] cares enough to make me come down here."
            show povn sad at left
            dad "She's distraught right now."
            dad "Your [missus] was crying the whole night thinking something horrible had happened to you!"
            dad "She made me and your [sisrole] go out looking for you while she calls what few people she knows around town to ask if they have seen you."
            dad "And now you have the balls to tell me to shut up?!"
            dad "How do you think she felt when the police showed up at our door telling us they found you naked by the side of the lake?"
            dad "They even told us that you may have been drugged or have been taking drugs."
            dad "She nearly fainted at our doorstep!"
            dad "When she sees you tomorrow I can guarantee she will have her own comments about all of this!"
    show povn shocked_talk at left
    show dad neutral at right
    pov "Wait, so I'm going to spend the whole day here?!"
    show povn sad_talk at left
    pov "Aren't you going to bail me out?"
    show povn sad at left
    show dad neutral_talk at right
    dad "Officer Mina informed me that the state law dictates that all first time offenders for Public Exposure spend the minimum time of 24 hours."
    dad "Be thankful she won't press any further charges and this should serve as the first part to your punishment."
    dad "Hopefully this will be enough to teach you the lesson."
    dad "I knew this would happen sooner or later. And yet, I'm very disappointed in you."
    if indecentarrest_shutup == 1:
        show dad angry_talk at right
        dad "And maybe fix that attitude of yours before your [mumrole] picks you up tomorrow morning or I swear to God..."
    hide dad neutral_talk
    hide dad angry_talk
    show povn bored at left
    show min neutral_talk at Position(xpos=1350)
    show dad neutral at right
    mina "Don't worry, sir, this isn't the first time I've had some dumb teen locked behind those bars for something like this."
    show min smirk_talk at Position(xpos=1350)
    mina "A day or two in there is usually enough for them to learn their lesson."
    show min neutral_talk at Position(xpos=1350)
    mina "His tests came negative regarding any kind of foreign substances in his bloodstream, but if he did take anything his body would have passed it down by now."
    if backtosafety_angel == 1:
        mina "But, to be honest, your [povdadrole] doesn't seem the type to get into any of that stuff, he seems like a good kid."
    show min neutral at Position(xpos=1350)
    show dad neutral_talk at right
    dad "I'll leave him in your more than capable hands then, Officer."
    dad "Your [mumrole] will be the one to come to pick you up tomorrow, she'll want to hear your version of the story before she decides the punishment."
    dad "I've had enough of you for one lifetime."
    if indecentarrest_shutup == 1:
        show dad angry_talk at right
        dad "She will want an explanation of all this and I want this attitude of yours taken care of by the next time I see you, you got that?"
        show povn bored_talk at left
        show dad neutral at right
        pov "...Yes, sir..."
    else:
        show dad neutral_talk at right
        dad "You better come up with a tear jerking apology if you wanna live to see another day."
        show povn bored_talk at left
        show dad neutral at right
        pov "I will..."
        show povn bored at left
        show dad neutral_talk at right
        dad "Who knew you could let me down any further than you already have."
        show povn bored_talk at left
        show dad neutral at right
        pov "...Yeah. Who knew..?"
    show povn bored at left
    show min neutral at Position(xpos=1350)
    show dad neutral_talk at right
    dad "Well, with that I should take my leave, Officer."
    show min neutral_talk at Position(xpos=1350)
    show dad neutral at right
    mina "Careful on your way home, sir. We'll take care of your [povdadrole]."
    show povn bored at left
    show min confused at Position(xpos=1350)
    show dad neutral_talk at right
    dad "Oh, and before I forget."
    show povn shocked at left
    show min smirk at Position(xpos=1350)
    show dad neutral_talk at right
    dad "I actually have a change of clothes with me for you."
    show dad neutral_talk at right
    dad "Courtesy of your [mumrole]."
    show povn angry_talk at left
    show min neutral at Position(xpos=1350)
    show dad neutral at right
    pov "What the hell, why did you give that to me earlier!"

    scene black
    with fade
    $ renpy.pause(0.5,hard=True)

    scene bg jailhouse_1
    with fade
    show pov sad at left
    with dissolve
    show min smirk_talk at right
    with dissolve
    mina "Try and get comfortable, it's going to be a long, boring 24 hours."
    show pov sad_talk at left
    show min neutral at right
    pov "Yeah, I can only imagine."

    scene black
    with fade
    if day <= 5:
        $ day += 1
    else:
        $ day = 0
    call lbl_next_date
    "The next morning."

    scene bg jailhouse_1
    show min bored_talk at right
    with hpunch
    mina "Wake up, Flash. Come on, kid, you're free to go."
    show pov bored_talk at left
    with dissolve
    pov "T-that nickname catches on real quick, doesn't it?"
    show pov bored at left
    show min smirk_talk at right
    mina "If the boot fits."
    show pov shocked at left
    show min neutral_talk at right
    mina "Anyway, here you go ma'am, safe and sound."
    hide min neutral_talk
    show pov embarrassed at left
    show mumc embarrassed_talk at Position(xpos=1350)
    show min neutral at right
    mum "Thank you, Officer. I'm sorry for all the trouble he's caused."
    show mumc embarrassed at Position(xpos=1350)
    show min neutral_talk at right
    mina "No need to worry about that, Ma'am."
    mina "Boys will be boys and he is at that age of making stupid choices just to impress his peers or perhaps a special girl."
    show min confused_talk at right
    mina "Just make sure I don't see you back here anytime soon, [povname], you got that?"
    show min bored_talk at right
    mina "Next time I won't go so easy on you."

    menu:
        "I'll try not to be a nuisance.":
            pass
        "I certainly wouldn't mind seeing you again.":
            pass
        "I hope there is a comfier cell next time.":
            pass
    show pov embarrassed_talk at left
    show min bored at right
    pov "I-"
    show pov bored at left
    show mumc angry_talk at Position(xpos=1350)
    show min neutral at right
    mum "I'll make sure he stays out of your hair, Officer. Now, if you'll excuse us."
    $ main_story = 38

    jump lbl_the_awkward_ride_home
