## Night Club Hookups
default nightclub_hookups_bachelorette = 0
default nightclub_hookups_dancefloor = 0
default nightclub_hookups_djbooth = 0

label lbl_nightclub_hookups:
    #-Scene takes place on the next available friday night after the previous scene-

    #-Mc and Jacob arrive on the night club and sit by the bar while going over
    # their battle plan-

    show pov shocked_talk at left
    show jac smirk at right
    with dissolve
    pov "Alright, we are here."
    pov "How are you feeling, man?"
    show pov confused at left
    show jac bored_talk at right
    jac "Honestly?"
    show pov neutral at left
    show jac embarrassed_talk at right
    jac "I feel surprisingly okay."
    show jac smirk_talk at right
    jac "Especially when you consider that all the time leading up to here I’ve been either nervous as all hell or nearly throwing up from the anxiety."
    show pov neutral_talk at left
    show jac embarrassed at right
    pov "Ok, that’s good!"
    show pov embarrassed_talk at left
    show jac smirk at right
    pov "Uh… The fact that you are feeling okay now, not the other stuff."
    pov "You are looking good, you are smelling good and we arrived at a time this place has a good amount of people."
    show pov smirk_talk at left
    show jac bored at right
    pov "Let’s go down our options and see what we can do."
    show pov confused_talk at left
    pov "How do you wanna tackle this?"
    show pov confused at left
    show jac bored_talk at right
    jac "Well, I’m not really sure to be honest, I doubt my usual tactics are gonna work with the wingman set up."
    show pov neutral_talk at left
    show jac bored at right
    pov "Alright, that doesn’t help me out much but I’m sure we can figure something out."
    show pov neutral at left
    show jac confused_talk at right
    jac "Let’s go with the classic, try chatting them up and send them my way?"
    show pov  at left
    show jac embarrassed_talk at right
    jac "I don’t want them to think we are looking for a three way if we both approach at the same time."
    show pov confused at left
    show jac shocked_talk at right
    jac "I mean- Unless you’d be down for one?"
    show pov confused_talk at left
    show jac shocked at right
    pov "Uhh- I’ll pass on this one. The point of this whole thing is to show you that you can get girls and bring back your confidence and having me around for the whole thing isn’t gonna help."
    show pov neutral_talk at left
    pov "Other than that, I think it’s a good plan!"
    show pov smirk_talk at left
    show jac bored at right
    pov "Have you seen any girls you’d like to try your luck with?"
    show pov confused at left
    show jac embarrassed_talk at right
    jac "Definitely a few."
    show jac shocked_talk at right
    jac "Actually, doesn’t it seem like there’s more women here than usual?"

    #-Steven appears on scene from the bar-
    show jac shocked at Position(xpos=1400)
    show ste smirk_talk at Position(xpos=1600)
    with dissolve
    ste "That’s because it’s ladies night, you two."
    show pov neutral at left
    show jac smirk_talk at Position(xpos=1400)
    show ste smirk at Position(xpos=1600)
    jac "Steven, my man!"
    show pov neutral_talk at left
    show jac smirk at Position(xpos=1400)
    pov "Hey, Steven."
    show pov confused_talk at left
    show ste neutral at Position(xpos=1600)
    pov "I didn’t know you guys did ladies night. You don’t really advertise it?"
    show pov confused at left
    show ste smirk_talk at Position(xpos=1600)
    ste "Well, normally we do, but we got a reservation for some booths by some people of the TRC."
    show ste embarrassed_talk at Position(xpos=1600)
    ste "Apparently they are having a bachelorette party for one of their managers, so seeing as we would get an influx of ladies, I decided to just call it a Ladies night."
    show pov embarrassed at left
    show jac neutral at Position(xpos=1400)
    show ste neutral_talk at Position(xpos=1600)
    ste "Figured that by doing so I can attract dudes that will try to flirt and hookup with said ladies who would take advantage of the situation and order extra drinks."
    show pov embarrassed_talk at left
    show jac confused at Position(xpos=1400)
    show ste embarrassed at Position(xpos=1600)
    pov "How’s that coming along so far?"
    show pov embarrassed at left
    show ste smirk_talk at Position(xpos=1600)
    ste "I certainly ain’t complaining, what are you two guys here for?"
    show jac confused_talk at Position(xpos=1400)
    show ste confused at Position(xpos=1600)
    jac "Pretty much try exactly what you said, yeah…"
    show jac embarrassed at Position(xpos=1400)
    show ste smirk_talk at Position(xpos=1600)
    ste "Well, good luck you two."
    ste "Despite being a bachelorette and having a higher influx of girls tonight, I’ve been seeing a lot of guys get rejected or stood up."
    show pov bored at left
    show ste embarrassed_talk at Position(xpos=1600)
    ste "Seems like most ladies are sticking tightly with their groups so you might find it harder."
    show jac shocked_talk at Position(xpos=1400)
    show ste embarrassed at Position(xpos=1600)
    jac "Well, what’s life without a little challenge, right?"
    show ste smirk_talk at Position(xpos=1600)
    jac "Especially when the opportunity of experiencing some office worker older woman taste is at hand?"
    show pov smirk_talk at left
    show jac confused at Position(xpos=1400)
    show ste smirk at Position(xpos=1600)
    pov "Oh, so you’ve decided on who you wanna try making a move on?"
    show pov smirk at left
    show jac smirk_talk at Position(xpos=1400)
    show ste confused at Position(xpos=1600)
    jac "I think I have though best to have options. You ready, dude?"
    show pov neutral_talk at left
    show jac embarrassed at Position(xpos=1400)
    pov "Certainly!"
    pov "Just sit back and I’ll try sending them your way for you to work the charms"
    show pov bored at left
    show jac embarrassed_talk at Position(xpos=1400)
    show ste embarrassed at Position(xpos=1600)
    jac "God, I wish I had a mint or something."
    show jac smirk at Position(xpos=1400)
    show ste smirk_talk at Position(xpos=1600)
    ste "Here you go, mate. On the house."
    show pov embarrassed at left
    show jac neutral at Position(xpos=1400)
    show ste confused_talk at Position(xpos=1600)
    ste "Now, are you and [povname] going to buy something to drink or…?"
    show pov neutral_talk at left
    show ste smirk at Position(xpos=1600)
    pov "I’m off to speak to ladies then!"

    #-transition back to full view of the club-

    #-A menu shows up listing out all the girls in the bar Jacob is interested in-

label lbl_nightclub_hookups_menu:
    if nightclub_hookups_bachelorette == 0:
        pass
    elif nightclub_hookups_dancefloor == 0:
        pass
    elif nightclub_hookups_djbooth == 0:
        pass
    else:
        jump lbl_nightclub_hookups_2

    menu:
        "Approach the bachelorette party" if nightclub_hookups_bachelorette == 0:
            jump lbl_nightclub_hookups_bachelorette
        "Head for the dance floor" if nightclub_hookups_dancefloor == 0:
            jump lbl_nightclub_hookups_dancefloor
        "Reach for the DJ booth" if nightclub_hookups_djbooth == 0:
            jump lbl_nightclub_hookups_djbooth

    #-Regardless of choice this all end in failure after a short scene with them-

label lbl_nightclub_hookups_bachelorette:

    #-Mc approaches the bachelorette party and amongst the multitude of ladies,
    # he is able to reach out to Gloria who has clearly been drinking-

    #-Mc appears into the scene alongside Gloria-

    show pov smirk at left
    show glo smirk_talk at right
    with dissolve
    glo "Woooo! More tequila shots for the ladies!"
    show glo smirk_talk at right
    glo "Geez, where are the hunky guys ready to flirt with us ladies?!"
    show pov smirk_talk at left
    show glo confused at right
    pov "Uhh…"
    show pov smirk at left
    show glo neutral_talk at right
    glo "Well, about time!"
    show glo smirk_talk at right
    glo "How are you doing there, hot stuff~?"
    show pov shocked at left
    show glo shocked_talk at right
    glo "Wait, do I know you?"
    show pov embarrassed at left
    show glo smirk_talk at right
    glo "Honestly, I may be a little bit too tipsy to tell so if I do know you, please keep this between us, alright~?"
    show pov smirk_talk at left
    show glo smirk at right
    pov "Heh, alright then?"
    pov "Seems you are having quite a lot of fun tonight, huh?"
    show pov neutral_talk at left
    show glo shocked_talk at right
    glo "Oh, you bet!"
    show pov neutral at left
    show glo neutral_talk at right
    glo "Our little Jeannie from the accounting division is finally getting hitched so we had to come out and celebrate it!"
    glo "We already went to a restaurant and raided their red wine catalog and we just had to come over here and get her nice and loose for her wedding night!"
    show pov smirk_talk at left
    show glo neutral at right
    pov "So you are having red wine and tequila shots?"
    show pov shocked_talk at left
    show glo smirk at right
    pov "You ladies don’t mess around."
    show pov shocked at left
    show glo smirk_talk at right
    glo "What’s wrong with living a little? Besides, she has all the time in the world to be a boring housewife, right now she is having her fun with drinking body shots from the abs of a hunky stripper!"
    show pov neutral at left
    show glo shocked_talk at right
    glo "She’s usually so shy and introverted, but a few drinks in and she is borderline sucking on his cock!"
    show pov smirk_talk at left
    show glo confused at right
    pov "You sure it’s smart to take it so far?"
    show pov smirk at left
    show glo shocked_talk at right
    glo "Oh, for sure! It’s not like her husband is gonna find out or anything!"
    show pov confused at left
    show glo neutral_talk at right
    glo "Besides, it’s not cheating if they aren’t actually having sex."
    show pov shocked at left
    show glo smirk_talk at right
    glo "I’m sure he is doing the same thing with a stripper off with his pals!"
    show glo confused_talk at right
    glo "So while we are having fun, I’m just taking pictures to remember the night when we are out during brunch."
    show pov embarrassed_talk at left
    show pov confused at left
    pov "Taking pictures while you are doing all of this doesn’t seem like the best idea…"
    show pov embarrassed at left
    show glo angry_talk at right
    glo "Gosh, you are such a worrywart!"
    show pov confused at left
    show glo smirk_talk at right
    glo "But that is cute too in it’s own way~"
    show pov confused at left
    show glo smirk_talk at right
    glo "What about you, honey? You are looking for some fun~?"
    show pov smirk_talk at left
    show glo confused at right
    pov "Well now that you mention it, I have this friend over by the bar who is more than interested to-"
    show pov smirk at left
    show glo shocked_talk at right
    glo "Oh my gosh, you are playing wingman for your friend?!"
    show pov shocked at left
    show glo embarrassed_talk at right
    glo "That is so nice of you!"
    show glo shocked_talk at right
    glo "You know? Nowadays there just aren’t enough people who would be willing to do something like that for their friend!"
    show glo smirk_talk at right
    glo "I mean, look at these girls for example!"
    show pov confused at left
    show glo bored_talk at right
    glo "Do you know how much convincing it took me to get them to follow through with my bachelorette plans?"
    show pov embarrassed at left
    show glo smirk_talk at right
    glo "All they wanted to do was have a little quiet get together and miss out on all the fun!"
    show pov embarrassed_talk at left
    show glo bored at right
    pov "Oh… So you convinced them to do this?"
    show pov embarrassed at left
    show glo embarrassed_talk at right
    glo "Yeah and it wasn’t easy let me tell you that much!"
    show glo shocked_talk at right
    glo "Had to make sure the boring ones had enough wine glasses in the restaurant to convince them to come here and properly have a party!"
    show glo bored_talk at right
    glo "Not to mention the strippers were my idea and now they can’t get their hands off them!"
    show pov confused at left
    show glo confused_talk at right
    glo "Oh, I can’t wait for their reactions once i show them the pictures tomorrow, they are gonna have such a big laugh!"
    show pov embarrassed_talk at left
    show glo smirk at right
    pov "Uhh… you sure that is what's going to happen?"
    show pov confused at left
    show glo smirk_talk at right
    glo "They need to loosen up a little bit!"
    show pov embarrassed at left
    show glo neutral_talk at right
    glo "Now, were you telling me about your friend and-"
    show pov confused at left
    show glo shocked_talk at right
    glo "OH MY GOD, OUR BRIDE IS LICKING OUR STRIPPERS CHEST!"
    show pov shocked at left
    show glo smirk_talk at right
    glo "I’m sorry sugar but I need to have this filmed."
    show pov confused at left
    show glo shocked_talk at right
    glo "Good luck with hooking your friend up! In other circumstances, I would have drained you and your friend dried~"
    show pov bored at left
    glo "Bye, now!"

    #-Gloria disappears from the scene-
    show pov shocked_talk at left
    hide glo
    with dissolve
    pov "Wait, you really shouldn’t-!"
    show pov confused_talk at left
    pov "And she’s gone…"
    show pov embarrassed_talk at left
    pov "Alright, let’s not get Jacob involved with the upcoming mess this is gonna be…"
    show pov smirk_talk at left
    pov "Next option."

    $ nightclub_hookups_bachelorette = 1

    jump lbl_nightclub_hookups_menu

label lbl_nightclub_hookups_dancefloor:

    #-Mc goes out into the dancefloor where he spots Janae in the middle of it all-

    #-Mc appears into the scene alongside Janae-

    show pov smirk_talk at left
    show jan confused at right
    with dissolve
    pov "Hey, how you doing tonight?"
    show pov smirk at left
    show jan confused_talk at right
    jan "Oh, hey!"
    show pov shocked at left
    show jan smirk_talk at right
    jan "Haven’t I seen you around the mall sometimes?"
    show pov embarrassed_talk at left
    show jan shocked at right
    pov "Yeah, I believe you have. How’s it going?"
    show pov embarrassed at left
    show jan smirk_talk at right
    jan "Pretty alright!"
    jan "Having a fun night out with my gals, How about you?"
    show pov neutral at left
    show jan neutral_talk at right
    jan "I thought I saw you hanging out with someone by the bar, right?"
    show pov neutral_talk at left
    show jan neutral at right
    pov "Right, I’m trying to help my friend out a bit with his game actually!"
    show pov confused_talk at left
    show jan confused at right
    pov "Speaking off, I think you’d love to meet him!"
    show pov embarrassed at left
    show jan smirk_talk at right
    jan "Sorry hotshot, not happening."
    show pov neutral at left
    show jan neutral_talk at right
    jan "Not that I don’t think your friend isn’t ok or that I don’t find cute how you are trying to help him, but I’m not interested, sorry."
    show pov neutral_talk at left
    show jan embarrassed at right
    pov "Hey, that’s alright!"
    show pov confused_talk at left
    show jan bored at right
    pov "I ain’t gonna be a jerk about it either, but can I at least know why?"
    show pov smirk_talk at left
    show jan neutral at right
    pov "Did I come on too strong or…?"
    show pov smirk at left
    show jan neutral_talk at right
    jan "It’s nothing that you did, honest."
    show pov confused at left
    show jan embarrassed_talk at right
    jan "I’m afraid to say, I would have had to say no regardless of your approach here."
    show pov shocked_talk at left
    show jan embarrassed at right
    pov "How come? If it’s alright for me to ask?"
    show pov shocked at left
    show jan smirk_talk at right
    jan "Because I doubt my boyfriend would have approved or been much of a fan of it, to be honest with you."
    show pov smirk at left
    show jan neutral_talk at right
    jan "Oh look, here he comes now!"

    #-Mc’s sprite turns around as if seeing where Janae was pointing him-
    show pov smirk_talk at left
    show jan neutral at right
    pov "You mean that Din Petrol looking guy who is looking at me like I just knocked down his bike and is now heading this way like he wants to kick my teeth down my throat?"
    show pov bored at left
    show jan neutral_talk at right
    jan "Yep! That’s my boo right there~"
    show pov smirk at left
    show jan smirk_talk at right
    jan "Don’t worry though, I have no hard feelings but you really should get moving."
    show pov bored at left
    show jan bored_talk at right
    jan "He has his temper."
    show pov smirk_talk at left
    show jan bored at right
    pov "Yeah, I’m out."
    show pov neutral_talk at left
    show jan neutral at right
    pov "Enjoy your night!"
    show pov smirk at left
    show jan neutral_talk at right
    jan "You too! Good luck with helping out your friend!"

    #-Mc leaves the scene-
    hide pov
    hide jan
    with dissolve

    $ nightclub_hookups_dancefloor = 1

    jump lbl_nightclub_hookups_menu

label lbl_nightclub_hookups_djbooth:

    #-Mc approaches the Dj booth where he sees Zariah vibing out-

    show pov smirk_talk at left
    with dissolve
    pov "Yo, Zariah!"
    show pov confused at left
    zar "{i}*Continues vibing*{/i}"
    show pov embarrassed_talk at left
    pov "Zariah, over here!"
    show pov embarrassed at left
    zar "{i}*Continues vibing*{/i}"
    show pov bored_talk at left
    show zar confused at right
    with dissolve
    pov "…"
    show zar shocked at right
    pov "Yo, Karma!"
    show pov bored at left
    show zar shocked_talk at right
    zar "Hey, man!"
    show zar smirk_talk at right
    zar "Sorry, can’t talk right now, Busy working!"
    zar "Talk to ya later!"
    show pov shocked_talk at left
    hide zar
    with dissolve
    pov "Yeah, but I-"
    show pov bored at left
    zar "{i}*Goes back to vibing*{/i}"
    show pov bored_talk at left
    pov "Well, that was pointless."
    show pov smirk_talk at left
    pov "Not sure what I expected to happen by approaching a DJ booth mid show…"

    #-Mc leaves the scene-
    hide pov
    with dissolve
    $ nightclub_hookups_djbooth = 1

    jump lbl_nightclub_hookups_menu

label lbl_nightclub_hookups_2:

    #=ONCE ALL OPTIONS ARE EXHAUSTED THE MC RETURNS TO THE BAR WITH JACOB=

    #-Scene shifts back to the bar with Jacob and Steven are at-

    #-Mc appears on scene after Jacob and Steven appear-

    show pov embarrassed_talk at left
    show jac neutral at right
    with dissolve
    pov "Hey, I’m back…"
    show pov smirk at left
    show jac confused_talk at right
    jac "Sup man, how did it go?"
    show pov embarrassed_talk at left
    show jac shocked at right
    pov "Not great, I’m gonna be honest with you…"
    show pov embarrassed at left
    show jac smirk_talk at right
    ste "What, a lot of rejections, mate?"
    show pov confused_talk at left
    show jac smirk at right
    pov "Not really but way too many strings attached."
    show pov embarrassed_talk at left
    show jac confused at right
    pov "Actually, you may want to keep an eye on that bachelorette party because they are about to either start sucking the strippers off or they are about to pass out from how much they’ve been drinking."
    pov "And the lady taking pictures all of it certainly isn’t helping with things…"
    show pov embarrassed at left
    show jac shocked_talk at Position(xpos=1400)
    show ste confused at Position(xpos=1600)
    with dissolve
    jac "Wait, she is documenting what’s happening at the bachelorette party?"
    show pov shocked_talk at left
    show jac shocked at Position(xpos=1400)
    pov "Like a journalist taking pictures of a crime scene dude, it’s kind of wild."
    show pov shocked at left
    show jac smirk at Position(xpos=1400)
    show ste smirk_talk at Position(xpos=1600)
    ste "Oh come on, mate. It’s common sense not to do that."
    show pov embarrassed at left
    show jac shocked_talk at Position(xpos=1400)
    show ste smirk at Position(xpos=1600)
    jac "That has to be the worst thing you can do to a person about to get married!"
    jac "One of those pictures could ruin the whole thing!"
    show pov embarrassed_talk at left
    show jac bored at Position(xpos=1400)
    pov "Yeah, I didn’t want to get us caught up in that whole mess."
    pov "Though to be fair, she was certainly willing to give you a shot until the bride started licking tequila off the stripper’s chest."
    show pov smirk_talk at left
    pov "Seriously, Steven, you should send someone there because there ain’t no way half of them are gonna remember what happened when they wake up."
    show pov embarrassed at left
    show jac neutral at Position(xpos=1400)
    show ste bored_talk at Position(xpos=1600)
    ste "I’ll at least keep an eye out to make sure they don’t puke on the floors."
    show ste shocked_talk at Position(xpos=1600)
    ste "Guess I should have left them in the VIP area after all."
    show jac confused_talk at Position(xpos=1400)
    show ste bored at Position(xpos=1600)
    jac "Well, there go my chances of seducing an older woman tonight."
    show pov confused at left
    show jac embarrassed_talk at Position(xpos=1400)
    jac "And probably my chances of scoring tonight in general."
    show pov confused_talk at left
    show jac embarrassed at Position(xpos=1400)
    show ste smirk at Position(xpos=1600)
    pov "Come on, dude. There’s still time!"
    pov "We’ve just arrived and I’m sure we still have a shot!"
    show pov neutral at left
    show jac embarrassed at Position(xpos=1400)
    show ste smirk_talk at Position(xpos=1600)
    ste "You miss all the shots you don’t take, champ. Chin up a little."
    show jac confused at Position(xpos=1400)
    show ste neutral_talk at Position(xpos=1600)
    ste "Actually, there is a girls on one of the booths that’s just drinking by herself."
    show pov smirk at left
    show ste confused_talk at Position(xpos=1600)
    ste "She’s already rejected a few guys coming to talk to her but you two might have better luck?"
    show jac embarrassed_talk at Position(xpos=1400)
    show ste smirk at Position(xpos=1600)
    jac "Well, I guess it’s worth a try…"
    show pov neutral_talk at left
    show jac shocked at Position(xpos=1400)
    show ste neutral at Position(xpos=1600)
    pov "That’s the spirit!"
    pov "Which booth is she in, Steven?"
    show pov neutral at left
    show jac confused at Position(xpos=1400)
    show ste neutral_talk at Position(xpos=1600)
    ste "Right by the door, you can see her from here actually."
    show pov confused_talk at left
    show ste neutral at Position(xpos=1600)
    pov "Wait a minute, that’s…"
    show pov smirk at left
    show jac shocked_talk at Position(xpos=1400)
    jac "That’s Hitomi!"
    jac "Dang, you weren’t kidding when you said she was in bad shape…"
    show jac shocked at Position(xpos=1400)
    show ste smirk_talk at Position(xpos=1600)
    ste "Yeah, she’s been coming here for a bit and just drinks until satisfied, I’ve tried asking her what’s on her mind but I never get too far."
    show pov smirk_talk at left
    show ste smirk at Position(xpos=1600)
    pov "I think a project of hers or something fell under and she feels awful about the whole thing."
    show pov smirk at left
    show jac embarrassed at Position(xpos=1400)
    show ste neutral_talk at Position(xpos=1600)
    ste "You guys know her?"
    show pov neutral_talk at left
    show ste confused at Position(xpos=1600)
    pov "Yeah, she is a friend of ours. It’s a bit of a long story."
    show pov neutral at left
    show jac embarrassed_talk at Position(xpos=1400)
    jac "And part of the reason why we are out here getting me a hot date as well."
    show jac confused_talk at Position(xpos=1400)
    show ste bored at Position(xpos=1600)
    jac "…"
    jac "I’ll go talk to her now, [povname]."
    show pov confused_talk at left
    show jac shocked at Position(xpos=1400)
    show ste confused at Position(xpos=1600)
    pov "What? But we haven’t gotten you a girl yet?"
    show pov confused at left
    show jac shocked_talk at Position(xpos=1400)
    jac "I know, but…"
    show jac embarrassed_talk at Position(xpos=1400)
    jac "Well you are out here trying to help me out even when you are clearly still very much concerned about her and I’d feel like an ass if I don’t do something to help out."
    jac "especially when she is right there and looking miserable."
    show pov bored at left
    show jac neutral_talk at Position(xpos=1400)
    jac "Let me work my magic and you can go talk to her once I’m done."
    show pov shocked_talk at left
    show jac neutral at right
    pov "I’m not gonna just ditch you, especially when I haven’t fulfilled my part of the bargain, dude."
    show pov smirk_talk at left
    show jac embarrassed at Position(xpos=1400)
    show ste smirk at Position(xpos=1600)
    pov "I’m your wingman!"
    show pov confused at left
    show jac neutral_talk at Position(xpos=1400)
    jac "I know, I know. But it’s alright, man."
    show jac smirk_talk at Position(xpos=1400)
    show ste confused at Position(xpos=1600)
    jac "Honestly, I feel better just knowing I got a good friend always watching my back."
    show pov embarrassed at left
    show jac neutral_talk at Position(xpos=1400)
    jac "Now let me properly apologize for the way I acted and patch things over with her as well."
    show pov confused_talk at left
    show jac neutral at Position(xpos=1400)
    pov "And you sure you can do this in just a chat just like that?"
    show pov confused at left
    show jac smirk_talk at Position(xpos=1400)
    jac "Hey, have a little trust in your bro."
    show jac neutral_talk at Position(xpos=1400)
    show ste neutral at Position(xpos=1600)
    jac "This is B.J. We are talking about dudes! I got this!"
    show pov smirk at left
    show jac bored_talk at Position(xpos=1400)
    show ste smirk at Position(xpos=1600)
    jac "Just watch and learn."
    show pov embarrassed_talk at left
    show jac smirk at Position(xpos=1400)
    pov "Alright- If you are sure, man. Thank yo..."
    show pov embarrassed at left
    show jac smirk_talk at Position(xpos=1400)
    jac "Don’t worry about it, I always got you covered."

    #-Jacob leaves the scene-

    show pov confused at left
    hide jac
    with dissolve
    show ste smirk_talk at Position(xpos=1600)
    ste "You got a good friend there, mate."
    show pov confused_talk at left
    show ste smirk at Position(xpos=1600)
    pov "Yeah… I know I do…"
    show pov smirk at left
    show ste confused_talk at Position(xpos=1600)
    ste "Also, does he actually call himself 'B.J.' or did I imagine that?"
    show pov smirk_talk at left
    show ste confused at Position(xpos=1600)
    pov "Again, bit of a long story, dude."
    show pov bored_talk at left
    pov "Still, I’m still upset I couldn’t manage to get him any dates…"
    show pov bored at left
    show ste shocked_talk at Position(xpos=1600)
    ste "Well, in my experience seeing guys try to wingman each other out and either succeeding or crash and burning, I can only say this…"
    show pov embarrassed at left
    show ste neutral_talk at Position(xpos=1600)
    ste "Sometimes there’s good night, sometimes there’s bad nights."
    ste "It’s really up to the girls whether or not they are down to do anything with you and you can’t force that."
    show pov neutral_talk at left
    ste "No matter how many drinks you buy her, if she is not into you, there’s not much you can do."
    show ste smirk_talk at Position(xpos=1600)
    ste "At least if you don’t want to be labeled as a creepy loser or go straight to jail."
    show pov smirk_talk at left
    show ste smirk at Position(xpos=1600)
    pov "I have enough problems with the law as it is, so I guess this night’s a bust."
    show pov confused at left
    show ste bored_talk at Position(xpos=1600)
    ste "Don’t call it in just yet, man."
    show ste neutral_talk at Position(xpos=1600)
    ste "You never know with these sorts of things."
    show pov smirk_talk at left
    show ste neutral at Position(xpos=1600)
    pov "I suppose you are right, though I don’t think a girl is just gonna come out of nowhere."

    #-Suddenly, the drunk girl from the beach appears wearing a really skimpy outfit-
    show pov confused at left
    show ste confused at Position(xpos=1400)
    show drug smirk_talk at Position(xpos=1600)
    with dissolve
    drug "Hey, barman. Cun ah get anothar drink here?"
    show ste bored_talk at Position(xpos=1400)
    show drug smirk at Position(xpos=1600)
    ste "I think you’ve had enough for tonight sweet heart."
    show ste bored at Position(xpos=1400)
    show drug smirk_talk at Position(xpos=1600)
    drug "Awww come on! I’m nhot done partying yet!"
    show pov  at left
    show ste bored_talk at Position(xpos=1400)
    show drug angry at Position(xpos=1600)
    ste "Sorry, my mind is made up here."
    show pov embarrassed at left
    show ste bored at Position(xpos=1400)
    show drug smirk_talk at Position(xpos=1600)
    drug "Awwwww! You are no fun!"

    #-She turns to look at the MC and immediately smiles-
    show pov embarrassed at left
    show drug neutral_talk at Position(xpos=1600)
    drug "Hey, youuuu~"
    show pov embarrassed_talk at left
    show drug neutral at Position(xpos=1600)
    pov "Uhh, hey…"
    show pov confused at left
    show drug smirk_talk at Position(xpos=1600)
    drug "Aren’t you the guy who wuz like, talking to that blonde dude just a second ago?"
    show pov confused_talk at left
    show drug smirk at Position(xpos=1600)
    pov "What, you mean Jacob?"
    show pov confused at left
    show ste smirk at Position(xpos=1400)
    show drug shocked_talk at Position(xpos=1600)
    drug "Nho, no, no… Ah mean the blonde guy who starz in that one movie bout the guy…"
    show pov embarrassed_talk at left
    show drug shocked at Position(xpos=1600)
    pov "Uhhh, I think you got it wrong here, I was just talking to my friend and-"
    show pov embarrassed at left
    show drug confused_talk at Position(xpos=1600)
    drug "Nuh-uh, you can’t fool meh!"
    show ste smirk at Position(xpos=1400)
    show drug smirk_talk at Position(xpos=1600)
    drug "He ish totally the guy isn’t he?!"
    show ste smirk_talk at Position(xpos=1400)
    show drug confused at Position(xpos=1600)
    ste "Listen, neither I or this guy genuinely know what you are talking about and-"
    show pov confused at left
    show ste smirk at Position(xpos=1400)
    show drug shocked_talk at Position(xpos=1600)
    drug "Cahn yew two introduce meh to him?!"
    show drug smirk_talk at Position(xpos=1600)
    drug "I’ve always whanted to suck on some famous cock~!"
    show pov smirk at left
    show ste shocked_talk at Position(xpos=1400)
    show drug smirk at Position(xpos=1600)
    ste "Wait, what?"
    show ste smirk at Position(xpos=1400)
    show drug neutral_talk at Position(xpos=1600)
    drug "Oh my gosh, here he comes! Play it cool!"

    #-Jacob reappears on scene with a smile-
    show pov confused at left
    show ste bored at Position(xpos=1000)
    show drug neutral at Position(xpos=1400)
    show jac embarrassed_talk at Position(xpos=1800)
    with dissolve
    jac "It’s done, dude!"
    jac "He is willing to talk and is going to be waiting for you in one of the VIP booths!"
    show pov embarrassed at left
    show jac smirk_talk at Position(xpos=1800)
    jac "She is a bit tipsy but it should be fine!"
    show pov confused_talk at left
    show jac smirk at Position(xpos=1800)
    pov "Wait, you actually managed to talk to her and convince her to meet up with me?"
    show pov confused at left
    show jac smirk_talk at Position(xpos=1800)
    jac "I told you, man. Have faith in your bro!"
    jac "I happen to have my tricks, you know?"
    show ste smirk_talk at Position(xpos=1000)
    show jac smirk at Position(xpos=1800)
    ste "Huh, cheers to that then."
    show ste embarrassed at Position(xpos=1000)
    show drug smirk at Position(xpos=1400)
    show jac confused_talk at Position(xpos=1800)
    jac "Who’s your friend?"
    show pov embarrassed_talk at left
    show jac confused at Position(xpos=1800)
    pov "Uhh, she is…"
    show pov embarrassed at left
    show drug smirk_talk at Position(xpos=1400)
    drug "Oh my gosh, hiiii!"
    show drug smirk at Position(xpos=1400)
    show jac smirk_talk at Position(xpos=1800)
    jac "Well, hi there! You certainly look friendly."
    show drug smirk_talk at Position(xpos=1400)
    show jac neutral at Position(xpos=1800)
    drug "Oh gosh, I can’t believe I’m meeting up with you!"
    show drug neutral at Position(xpos=1400)
    show jac confused_talk at Position(xpos=1800)
    jac "You are excited about meeting me?"
    show drug neutral_talk at Position(xpos=1400)
    show jac confused at Position(xpos=1800)
    drug "How could I nhot be?!"
    show drug confused_talk at Position(xpos=1400)
    show jac embarrassed at Position(xpos=1800)
    drug "I was ashking your friend here to introduce meh!"
    show pov confused at left
    show drug smirk_talk at Position(xpos=1400)
    drug "Do yah wanna get out of here?"
    show drug neutral at Position(xpos=1400)
    show jac smirk_talk at Position(xpos=1800)
    jac "By get out of here you mean…?"
    show drug neutral_talk at Position(xpos=1400)
    show jac confused at Position(xpos=1800)
    drug "I whanna get ya away from here and have ya wreck me on the fist flat surface we find!"
    show drug smirk at Position(xpos=1400)
    show jac smirk_talk at Position(xpos=1800)
    jac "A-Are you serious?"
    show pov bored at left
    show drug neutral_talk at Position(xpos=1400)
    show jac confused at Position(xpos=1800)
    drug "Totally!"
    show pov shocked at left
    show ste smirk at Position(xpos=1000)
    show drug smirk_talk at Position(xpos=1400)
    show jac neutral at Position(xpos=1800)
    drug "Come ooooon, I wanna choke on your cock!"
    show drug neutral at Position(xpos=1400)
    show jac smirk_talk at Position(xpos=1800)
    jac "I… S-Sure! Let’s get out here, can you let me say goodbye to my friends?"
    show drug neutral_talk at Position(xpos=1400)
    show jac smirk at Position(xpos=1800)
    drug "I’ll beh outside, don’t take too long~"
    show pov smirk at left
    show ste neutral at Position(xpos=1000)
    show drug smirk at Position(xpos=1400)
    show jac neutral_talk at Position(xpos=1800)
    jac "I’ll be right there, I promise!"

    #-Drunk girl leaves the scene-
    show ste bored at Position(xpos=1200)
    hide drug
    with dissolve
    show jac smirk_talk at Position(xpos=1600)
    jac "[povname], I genuinely don’t know how you do it but I’m certainly impressed, dude!"
    jac "Did you see what she was wearing, dude she’s crazy hot!"
    show pov bored_talk at left
    show jac shocked at Position(xpos=1600)
    pov "Uhhh…"
    show pov bored at left
    show jac smirk_talk at Position(xpos=1600)
    jac "Seriously dude, thank you so much for this and good luck with Hitomi!"
    show ste smirk at Position(xpos=1200)
    jac "God, I could kiss you right now!"
    show pov smirk_talk at left
    show jac neutral at Position(xpos=1600)
    pov "Please, don’t."
    pov "Just get out of here and go get her man."
    show pov smirk at left
    show ste neutral at Position(xpos=1200)
    show jac neutral_talk at Position(xpos=1600)
    jac "I sure will! Thanks again, dude!"
    show pov neutral_talk at left
    show jac smirk at Position(xpos=1600)
    pov "Yeah, yeah…"

    #-Jacob leaves the scene-
    show pov embarrassed_talk at left
    show ste confused at Position(xpos=1200)
    hide jac
    with dissolve
    pov "..."
    show pov embarrassed at left
    show ste confused_talk at Position(xpos=1200)
    ste "..."
    show pov smirk_talk at left
    show ste smirk at Position(xpos=1200)
    pov "Steven, what just happened?"
    show pov confused at left
    show ste smirk_talk at Position(xpos=1200)
    ste "I- I genuinely don’t know what to tell ya, mate… I guess you were a good wingman?"
    show pov smirk_talk at left
    show ste neutral at Position(xpos=1200)
    pov "Should I be worried considering how drunk she seemed?"
    pov "I don’t want to see my bro being stabbed after taking a psycho home."
    show pov smirk at left
    show ste neutral_talk at Position(xpos=1200)
    ste "Nah, no need to worry about it."
    show ste smirk_talk at Position(xpos=1200)
    ste "She is a regular here and has the reputation as a bit of a man eater, especially when she’s drunk."
    ste "Seems like your boy is about to have the soul sucked out of him so I’d say it’s a win-win for everybody."
    show pov smirk_talk at left
    show ste neutral at Position(xpos=1200)
    pov "You cool with me and Hitomi using one of the VIP booths?"
    show pov smirk at left
    show ste neutral_talk at Position(xpos=1200)
    ste "Sure, I mean… It’s not like anyone came over and asked me but I’m not gonna deny it now that it’s happening."
    show ste confused_talk at Position(xpos=1200)
    ste "But if she orders more drinks there I hope you have cash on you."
    show pov embarrassed_talk at left
    show ste smirk at Position(xpos=1200)
    pov "I do but hopefully we wont be drinking and won’t be there for long."
    pov "Thanks, man!"
    show pov neutral at left
    show ste neutral_talk at Position(xpos=1200)
    ste "Don’t mention it, now get going and stop hoggin your place in the bar!"

    #-MC leaves the scene-
    hide pov
    with dissolve
    show ste confused_talk at Position(xpos=1200)
    ste "..."
    show ste smirk_talk at Position(xpos=1200)
    ste "..."
    show ste bored_talk at Position(xpos=1200)
    ste "I suppose you are right, though I don’t think a million bucks is just gonna come out of nowhere!"
    show ste confused at Position(xpos=1200)
    ste "..."
    ste "..."
    show ste smirk_talk at Position(xpos=1200)
    ste "{i}*Sigh*{/i} Of course it doesn’t work when I do it…"
    show ste smirk at Position(xpos=1200)
    "Girl in crowd" "OH MY GOD, THE BRIDE IN THE BACHELORETTE JUST PUKED ALL OVER THE STRIPPER!"
    show ste bored_talk at Position(xpos=1200)
    ste "And that has to be a punishment for my greed."
    show ste smirk_talk at Position(xpos=1200)
    ste "This night’s just getting better and better..."

    scene black
    with fade

    $ hitomi_path = 28

    scene bg street_night
    with fade

    jump lbl_vip_heart_to_heart
