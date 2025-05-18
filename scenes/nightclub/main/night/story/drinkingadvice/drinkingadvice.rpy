label lbl_drinking_advice:
    #[Night club, Evening– “Drinking Advice” – misslashley_path = 14]

    #-With not a lot of options when it comes to alcohol acquisition, The Mc decides to ask the resident bartender on what exactly he should look for#-Mc approaches the bar and Steven looks at him with a small smile

    if steve_path == 0:
        show pov embarrassed at left
        with dissolve
        show ste neutral_talk at right
        with dissolve
        ste "Hey man, what can I get ya?"
        show pov embarrassed_talk at left
        show ste neutral at right
        pov "Uh, nothing for me, I was actually hoping to ask you a question."
        show pov neutral at left
        show ste embarrassed_talk at right
        ste "Sure dude, what’s up?"
        show pov embarrassed at left
        show ste confused_talk at right
        ste "Hey, have I met you before? You seem really familiar."
        show pov embarrassed_talk at left
        show ste confused at right
        pov "I don't think so."
        show pov confused_talk at left
        show ste bored at right
        pov "Look, I'm in a bit of a rush right now, think you can help me?"
        show pov confused at left
        show ste bored_talk at right
        ste "Well, unless you are asking me to help bring ya a bunch of shots to your booth, I don't know if I can't help ya out, man."
        show pov bored at left
        show ste angry_talk at right
        ste "And for that, I'm gonna need to see an ID first, you don't look around the age to be asking for shots."
        show pov bored_talk at left
        show ste confused at right
        pov "Yeah, not that either."
        show pov embarrassed_talk at left
        show ste smirk at right
        pov "It's actually an honest question."

        #=RESULT END steven_path == 0 (have not met yet)=


    elif steve_path == 1:# (have met him before)

        #-Mc approaches the bar while Steven works-
        show pov smirk_talk at left
        with dissolve
        show ste shocked at right
        with dissolve
        pov "Hey, Steven!"
        show pov embarrassed_talk at left
        show ste confused at right
        pov "Listen man, think you can hel-"
        show pov shocked at left
        show ste shocked_talk at right
        ste "Woah there, dude."
        show pov confused at left
        show ste smirk_talk at right
        ste "Pretty sure I've told you this before."
        show pov embarrassed at left
        show ste bored_talk at right
        ste "I'm cool with you coming here and dancing or hanging out with our gal Karma and all-"
        show pov smirk at left
        show ste bored_talk at right
        ste "But keep out of the bar area, alright?"
        show pov embarrassed at left
        show ste neutral_talk at right
        ste "No I.D, No Drinks."
        show pov embarrassed_talk at left
        show ste smirk at right
        pov "Yeah, I know that."
        show ste smirk at right
        pov "Actually, I was hoping you could help me out with something."
        show pov shocked at left
        show ste smirk_talk at right
        ste "I ain't letting you into the V.I.P. for you to impress your lady friend."
        show pov shocked_talk at left
        show ste confused at right
        pov "It's not that either!"
        show pov bored_talk at left
        show ste smirk at right
        pov "Look, I just need to ask you something."

        #=RESULT END steven_path == 1 (have met him before)=

    #=Common Route=

    show pov embarrassed at left
    show ste bored_talk at right
    ste "Alright, shoot."
    show pov confused_talk at left
    show ste confused at right
    pov "You happen to know a lot about wines?"
    show pov confused at left
    show ste confused_talk at right
    ste "Well, not really my specialty but I think I know enough."
    show pov embarrassed at left
    show ste smirk_talk at right
    ste "Why ya ask?"
    show pov embarrassed_talk at left
    show ste bored at right
    pov "Well…"
    pov "It's a long story, but basically I got this friend who really needs some wine."
    show pov embarrassed at left
    show ste bored_talk at right
    ste "You are out of luck dude. We don't really sell wine here."
    show pov smirk_talk at left
    show ste bored at right
    pov "Yeah, I figured. So I was hoping you could point me in the right direction of what to get them."
    show pov embarrassed at left
    show ste smirk_talk at right
    ste "Why don't you just take their favorite bottle to a liquor store?"
    show pov confused_talk at left
    show ste bored at right
    pov "Think any liquor store in the area is gonna be willing to sell me or have Pen Island Blend 'Prestige Rouge' in their inventory?"
    show pov bored at left
    show ste smirk_talk at right
    ste "Maybe, at least after they are done laughing in your face for buying an overpriced bottle of water and pretend wine."
    show pov shocked at left
    ste "Good news is that you will likely be able to buy it I.D. free!"
    show pov bored at left
    show ste shocked_talk at right
    ste "If you sell a kidney to pay for it…"
    show pov bored_talk at left
    show ste smirk at right
    pov "Yeah, you see. That's my problem."
    show pov smirk_talk at left
    show ste confused at right
    pov "My friend has a very \"picky\" palate and she can't have any other alcohol free wine."
    show pov smirk at left
    show ste confused_talk at right
    ste "Why?"
    show pov embarrassed at left
    show ste smirk_talk at right
    ste "They are basically just juice without the alcohol."
    show pov smirk_talk at left
    show ste smirk at right
    pov "Beats me."
    show pov bored_talk at left
    show ste embarrassed at right
    pov "Nothing in my life is ever easy to get."
    show pov confused at left
    show ste smirk_talk at right
    ste "Dude, you could literally just mix water with food colorant and get the same result as 'Prestige Rouge'..."
    show pov shocked at left
    show ste neutral_talk at right
    ste "Alright, I can help ya out."
    show pov confused_talk at left
    show ste neutral at right
    pov "You can?"
    show pov shocked at left
    show ste neutral_talk at right
    ste "Yeah, man."
    ste "At first I thought you were making all of this up to get some free booze or something out of me."
    ste "But I have to deal with my own lightweight on the daily basis so I know what you are going through."
    show pov confused_talk at left
    show ste smirk at right
    pov "You do?"
    show pov shocked at left
    show ste embarrassed at right
    show zar smirk_talk at Position(xpos=1200)
    with dissolve
    zar "Wooo! Yo, Steven!" ## (from the stage):
    show pov confused at left
    show ste smirk at right
    zar "How about some Jagerbombs for the DJ, huh?!"
    show pov embarrassed at left
    show ste bored_talk at right
    hide zar
    with dissolve
    ste "Poor thing still thinks I actually give her alcohol."
    show pov shocked at left
    show ste smirk_talk at right
    ste "I actually make the Jagerbombs for the customers but I just add food coloring to her energy drink."
    show pov smirk at left
    show ste embarrassed_talk at right
    ste "She can’t tell the difference."
    show pov embarrassed at left
    show ste smirk at right
    ste "Gets drunk out of Placebo and now believes she has resistance to hangovers or something."
    show pov smirk at left
    show ste neutral at right
    ste "It’s actually pretty funny."
    show pov smirk_talk at left
    show ste neutral at right
    pov "Huh, well I’ll be damned."
    show pov shocked at left
    show ste neutral_talk at right
    ste "Actually mistook her glass with an actual Jagerbomb once and she passed out in less than an hour and had to close early."
    show pov embarrassed at left
    show ste smirk_talk at right
    ste "It was adorable."
    show ste neutral_talk at right
    ste "So yeah, I’ll help you out."
    show pov confused_talk at left
    show ste neutral at right
    pov "How?"
    show pov confused at left
    show ste neutral_talk at right
    ste "Well, for as much shit I give “Prestige Rouge” it does have its own particular taste and connoisseurs will give you shit for it if they are familiar enough with it."
    show ste bored_talk at right
    ste "Though in my opinion wine snobs are just a bunch of hacks…"
    show pov confused_talk at left
    show ste bored at right
    pov "My friend has been drinking the thing since she was really young."
    show pov shocked_talk at left
    pov "More of a religious thing for her than anything else."
    show pov embarrassed at left
    show ste bored_talk at right
    ste "Then you have a bigger problem."
    show ste smirk_talk at right
    ste "Nothing more annoying to please than a religious wine snob."
    show pov embarrassed_talk at left
    show ste confused at right
    pov "So what can I do?"
    show pov confused at left
    show ste smirk_talk at right
    ste "Well, you are really out of options unless you sell your kidney or get a loan."
    show pov smirk at left
    show ste neutral_talk at right
    ste "The only thing that comes close to the taste and softness of 'Prestige Rouge' is a brand called 'Nom de Vin Prétentieux'."
    show pov confused_talk at left
    show ste smirk at right
    pov "Nom de what?"
    show pov shocked at left
    show ste smirk_talk at right
    ste "“Nom de Vin Prétentieux”."
    show pov smirk at left
    show ste smirk_talk at right
    ste "It’s a french cooking wine so light that it's primarily used for cooking."
    show pov neutral at left
    show ste bored_talk at right
    ste "Just to provide the wine smell to dishes along with the lightest of hints of taste to it."
    show ste neutral_talk at right
    ste "It’s rather cheap and most households tend to have a bottle or so since it goes great with some dishes."
    show pov neutral_talk at left
    show ste embarrassed at right
    pov "Alright, sounds exactly like what I need!"
    show pov confused at left
    show ste embarrassed_talk at right
    ste "There is a problem though."
    show pov embarrassed_talk at left
    show ste embarrassed at right
    pov "There always is…"
    show pov confused at left
    show ste neutral_talk at right
    ste "It has just the slightest hint of alcohol to it."
    show pov shocked at left
    show ste smirk_talk at right
    ste "I mean, the amount of alcohol in it is so small that even I would turn a blind eye and serve you some if I had a bottle at hand."
    show pov confused at left
    show ste bored_talk at right
    ste "No worries getting you over the limit if you know what you are doing."
    show pov bored at left
    show ste embarrassed_talk at right
    ste "But it’s always a gamble with lightweights."
    show pov confused at left
    show ste smirk_talk at right
    ste "Some people can get drunk with just the smell of strong drinks after all."
    show pov confused_talk at left
    show ste bored at right
    pov "You really think it's going to be a problem?"
    show pov embarrassed_talk at left
    show ste embarrassed at right
    pov "I mean, you said it’s primarily cooking wine right?"
    show pov confused at left
    show ste smirk_talk at right
    ste "Yeah, you are not really supposed to drink cooking wine like regular wine."
    show pov shocked at left
    show ste embarrassed_talk at right
    ste "It’s main purpose for it is to save your reserves while giving the dish the wine taste and smell."
    show pov embarrassed at left
    show ste bored_talk at right
    ste "Most cooking wines either taste wrong or it’s flavor just isn't as potent or fine when you drink it like regular wine."
    show pov bored_talk at left
    show ste bored at right
    pov "So, what's the problem?"
    show pov bored at left
    show ste bored_talk at right
    ste "It still has alcohol and you may need an I.D to buy it."
    show pov shocked_talk at left
    show ste bored at right
    pov "Seriously?!"
    show pov smirk_talk at left
    show ste smirk at right
    pov "Even if it’s just for cooking?"
    show pov shocked at left
    show ste smirk_talk at right
    ste "You really think dumb teens wouldn’t drink cooking wine in bulk if such a loophole existed?"
    show pov embarrassed_talk at left
    show ste smirk at right
    pov "Touche, Steven. Touche…"
    show pov embarrassed at left
    show ste smirk_talk at right
    ste "I thought as much."
    show pov confused at left
    show ste bored_talk at right
    ste "Again, can’t really help you getting it, but I do remind you that most households tend to have some around for cooking purposes."
    show pov bored at left
    show ste smirk_talk at right
    ste "That’s all I’m going to say."
    show pov bored_talk at left
    show ste neutral at right
    pov "Well, I guess I’m not in the room to complain since I was completely out of leads when I got here."
    show pov neutral_talk at left
    show ste smirk at right
    pov "Thanks Steven, you’ve been a huge help."
    show pov neutral at left
    show ste smirk_talk at right
    ste "No problem, man."
    show pov shocked at left
    show ste bored_talk at right
    ste "Now keep distance from the drink area before you get us in trouble."
    show pov embarrassed_talk at left
    show ste smirk at right
    pov "Yeah, right. Sorry."

    $ principallashley_path = 11

    jump lbl_nightclub_night

    #=SCENE END=
