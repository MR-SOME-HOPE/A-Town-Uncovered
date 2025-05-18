label lbl_the_effie_charm:
    $ map_blocking = False
    #[Comic Book Store Backroom, Afternoon - “The Effie Charm”  - hitomi_path = 17]#15

    #-Scene takes place in the backroom of the comic book store where Mc, Effie
    # and Hitomi convince the nerds to get out of the cave once again before
    # starting their couple’s modeling session-

    #-Mc and Effie enter the scene as Hitomi is chatting with Lord Kevlamin-

    scene bg comicbookbackroom_day
    with fade

            ## SPRITEWORK ##
    show hit angry_talk at Position(xpos=1000)
    show lor confused at right
    with dissolve
    hit "I'm just asking for some time using the back room. I don't understand why it's such a big issue with you guys!"
    show hit angry at Position(xpos=1000)
    show lor bored_talk at right
    lor "It is our sanctuary! Our fortress of solitude, while keeping companionship! It is our holy temple! You can't just take it away from us like that, all of a sudden!"
    show hit shocked at Position(xpos=1000)
    show lor angry_talk at right
    lor "At least last time it wasn't such a sudden invasion of our domain!"
    show hit angry_talk at Position(xpos=1000)
    show lor bored at right
    hit "I still don’t understand how you guys don’t seem to get that you are just occupying a space that belongs to my family in the first place, but I’m just asking to use it for a while!"
    show hit confused at Position(xpos=1000)
    show lor bored_talk at right
    lor "We have gone through the higher channels and approached the emperor himself regarding the occupation of these lands and properly presented our tribute to him to keep our right of ownership over the land!"
    show hit smirk_talk at Position(xpos=1000)
    show lor bored at right
    hit "Yeah, to run a supposed tournament of yours, that stopped taking place a week ago!"
    show hit shocked_talk at Position(xpos=1000)
    show lor smirk at right
    hit "You guys are back to just you three huddling up in the dark. And I'm pretty certain you haven't fully cleaned the place after said tournament!"
    show hit shocked at Position(xpos=1000)
    show lor smirk_talk at right
    lor "Our uncontested rule over the holy lands shall remain untouched until the next moon cycle, as agreed on our tribute to the emperor of this territory!"
    show hit confused at Position(xpos=1000)
    show lor shocked_talk at right
    lor "And I shall inform thee that we indeed have a law within our guild that ensures the lands are taken care of to avoid this very same argument during any future debates!"
    show hit angry at Position(xpos=1000)
    show lor bored_talk at right
    lor "And seeing as you have no further points to try and use against my order, I say good day to you, madam!"


    #-Lord Kev leaves the scene-
    hide lor
    show pov shocked at left
    show hit angry_talk at right
    with dissolve
    hit "UGH, I can't believe this!"
    show pov embarrassed_talk at left
    show hit angry at right
    pov "Uhhh… Hitomi?"
    show pov confused at left
    show hit shocked_talk at right
    hit "[povname], thank God you are here!"
    show pov shocked at left
    show hit bored_talk at right
    hit "I'm having no luck convincing the Nerd Supreme to let me use the back room!"
    show pov embarrassed at left
    show hit embarrassed_talk at right
    hit "But nevermind that. Please tell me you at least found another model!"
    show pov neutral at left
    show hit confused at Position(xpos=1400)
    show eff smirk_talk at Position(xpos=1600)
    with dissolve
    eff "Heyo!"
    show pov embarrassed at left
    show hit confused_talk at Position(xpos=1400)
    show eff smirk at Position(xpos=1600)
    hit "Effie?"
    show hit smirk_talk at Position(xpos=1400)
    show eff embarrassed at Position(xpos=1600)
    hit "Wow, I'm genuinely surprised you managed to find someone up for it, [povname]."



    #-+2 Hitomi RP-
    $ add_points("hitomi_points",2)

    show pov embarrassed_talk at left
    show hit smirk at Position(xpos=1400)
    pov "Yeah, I am too."
    show pov shocked at left
    show hit smirk_talk at Position(xpos=1400)
    show eff smirk at Position(xpos=1600)
    hit "He did explain to you what kind of job this is? Right, Effie?"
    show pov embarrassed at left
    show hit smirk at Position(xpos=1400)
    show eff shocked_talk at Position(xpos=1600)
    eff "Oh, he totally did. And I can definitely see why you were expecting him to come back empty handed."
    show hit neutral at Position(xpos=1400)
    show eff smirk_talk at Position(xpos=1600)
    eff "So you need references for your webcomic, then?"
    show hit embarrassed_talk at Position(xpos=1400)
    show eff bored at Position(xpos=1600)
    hit "Y-Yeah, that's the basic gist of it…"
    hit "[povname] has been helping me a ton with it, but the female figure isn't really something he can really help out with, you know?"
    show pov confused at left
    show hit embarrassed at Position(xpos=1400)
    show eff smirk_talk at Position(xpos=1600)
    eff "Gee, I wonder why?"
    show pov smirk_talk at left
    show hit shocked at Position(xpos=1400)
    show eff bored at Position(xpos=1600)
    pov "Mocking my lack of boobs, now?"
    show pov confused at left
    show eff bored_talk at Position(xpos=1600)
    eff "Oh, you would look great with a rack but I much prefer you as you are now!"
    show hit embarrassed_talk at Position(xpos=1400)
    show eff smirk at Position(xpos=1600)
    hit "A-Anyway, I really appreciate you doing for me. Like, you have no idea, Effie."
    hit "I don't have much cash, but I can further reimburse you for your time later."
    show pov embarrassed at left
    show hit embarrassed at Position(xpos=1400)
    show eff neutral_talk at Position(xpos=1600)
    eff "Oh come on, Hitomi, there's no need for that! We are all friends here."
    show hit neutral at Position(xpos=1400)
    show eff smirk_talk at Position(xpos=1600)
    eff "I'm just happy to help out [povname] and you with all of this."
    eff "Plus, it's not like you two haven't seen me naked on the beach and so, before, so it's not that big of a deal for me."
    show hit neutral_talk at Position(xpos=1400)
    show eff neutral at Position(xpos=1600)
    hit "I admire how casually you take all of this."
    hit "I could never…"
    show pov confused at left
    show hit embarrassed at Position(xpos=1400)
    show eff neutral_talk at Position(xpos=1600)
    eff "I'm comfortable about my own body. And this is all for the sake of art, right?"
    show pov shocked at left
    show hit neutral at Position(xpos=1400)
    show eff bored_talk at Position(xpos=1600)
    eff "If nothing else, I have that as a defense."
    show pov embarrassed_talk at left
    show hit confused at Position(xpos=1400)
    show eff smirk at Position(xpos=1600)
    pov "You are still the best, Effie."
    show pov embarrassed at left
    show hit shocked at Position(xpos=1400)
    show eff smirk_talk at Position(xpos=1600)
    eff "I know, I know~"
    show pov smirk at left
    show hit shocked at Position(xpos=1400)
    show eff shocked_talk at Position(xpos=1600)
    eff "So, where do you want me to stand and where should I put my clothes?"
    show hit neutral at Position(xpos=1400)
    show eff confused_talk at Position(xpos=1600)
    eff "Also, are the nerds gonna watch? Because if so, I may need to actually consider charging you all."
    show pov bored at left
    show hit embarrassed_talk at Position(xpos=1400)
    show eff smirk at Position(xpos=1600)
    hit "Ugh, I'm at my wits end with them!"
    hit "No matter what I do, they just don't want to leave. And I can't just kick them out!"
    show hit neutral_talk at Position(xpos=1400)
    show eff confused at Position(xpos=1600)
    hit "Whether I like it or not, they still paid in full for renting the space beforehand. And I would get in trouble with my dad for kicking out paying customers."
    show pov confused at left
    show hit bored_talk at Position(xpos=1400)
    hit "Even when I'm the one who orders them pizza because they are all too socially awkward to talk on the phone with strangers…"
    show pov smirk_talk at left
    show hit bored at Position(xpos=1400)
    show eff shocked at Position(xpos=1600)
    pov "Now that's just sad…"
    show pov confused at left
    show hit shocked at Position(xpos=1400)
    show eff confused_talk at Position(xpos=1600)
    eff "Hmmm, so we are trying to get rid of them, then?"
    eff "You mind if I try something?"
    show hit neutral_talk at Position(xpos=1400)
    show eff confused at Position(xpos=1600)
    hit "Be my guest, but I've tried everything I can - and they are adamant that they won't be moving…"
    show pov shocked at left
    show hit embarrassed at Position(xpos=1400)
    show eff neutral_talk at Position(xpos=1600)
    eff "Oh, you definitely haven't tried things my way, then!"


    #-Effie leaves the scene-

    show pov embarrassed at left
    show hit confused_talk at Position(xpos=1400)
    hide eff
    with dissolve
    hit "What does she mean by that?"
    hit "What could she possibly try?"
    show pov embarrassed_talk at left
    show hit embarrassed at Position(xpos=1400)
    pov "Just let her work her magic."
    show pov neutral at left
    show hit embarrassed_talk at Position(xpos=1400)
    hit "I still can't believe you managed to convince her to help us out…"
    show pov embarrassed at left
    show hit shocked_talk at Position(xpos=1400)
    hit "I mean, I'm surprised you didn't get slapped for that!"
    show pov embarrassed_talk at left
    show hit confused at Position(xpos=1400)
    pov "Well, there may be some rumors spreading around about me now, but nothing I am not used to by now."
    show pov embarrassed at left
    show hit neutral_talk at Position(xpos=1400)
    hit "I know I keep going into these praise and thankful rants, but I genuinely couldn't do any of this without you, [povname]."
    show pov smirk_talk at left
    show hit confused at Position(xpos=1400)
    pov "I'm happy to help. I just hope you manage to make the most out of this session."
    show pov smirk at left
    show hit embarrassed_talk at Position(xpos=1400)
    hit "I'll be absolutely sure to."
    show pov smirk at left
    show hit smirk_talk at Position(xpos=1400)
    hit "At least, if Effie actually manages to kick the nerds out, which I find very unlikely to actually hap-"

    #-Lord Kev enters the scene once more-
    show pov shocked at left
    show hit bored at Position(xpos=1400)
    show lor smirk_talk at Position(xpos=1600)
    with dissolve
    lor "Upon further consideration and farther negotiations that have been approved by the Galactic Federation Council. We, the members of the Fathership, have decided to submit to your demands and provide our domains for the pursuit of knowledge and further skill enhancement of the artistic tree!"
    show pov confused at left
    show hit shocked_talk at Position(xpos=1400)
    show lor smirk at Position(xpos=1600)
    hit "Wait? What?"
    show pov shocked at left
    show hit confused at Position(xpos=1300)
    show lor embarrassed at Position(xpos=1400)
    show eff smirk_talk at Position(xpos=1800)
    with dissolve
    eff "Thanks again, man! You are doing us a real solid here."
    show hit shocked at Position(xpos=1300)
    show lor neutral_talk at Position(xpos=1400)
    show eff smirk at Position(xpos=1800)
    lor "Y-Yeah, D-Don't mention it, Effie."
    show pov smirk at left
    show hit confused at Position(xpos=1300)
    show lor embarrassed_talk at Position(xpos=1400)
    lor "A-Anything for you…"
    show pov confused at left
    show hit confused at Position(xpos=1300)
    show lor shocked at Position(xpos=1400)
    show eff smirk_talk at Position(xpos=1800)
    eff "D'aww, see? You can be quite the softy with proper motivation, can't you, Kevin?"
    show lor embarrassed_talk at Position(xpos=1400)
    show eff smirk at Position(xpos=1800)
    lor "Ehehe… Well, you know me."
    lor "Nice and helpful, Kevin, that's me!"
    show lor neutral at Position(xpos=1400)
    show eff shocked_talk at Position(xpos=1800)
    eff "Alright, I'll let you know when you guys can come back in. And will keep my end of the bargain."
    show hit shocked at Position(xpos=1300)
    show lor neutral at Position(xpos=1400)
    show eff neutral_talk at Position(xpos=1800)
    eff "Could you be a dear and put out the do not disturb sign on the way out?"
    show lor shocked_talk at Position(xpos=1400)
    show eff smirk at Position(xpos=1800)
    lor "S-Sure!"
    show pov shocked at left
    show hit bored at Position(xpos=1300)
    show lor embarrassed_talk at Position(xpos=1400)
    show eff smirk at Position(xpos=1800)
    lor "C-Come on, guys. Let's give Effie some space!"


    #-Lord Kev and the nerds leave the room-

    show pov smirk at left
    show hit confused at Position(xpos=1300)
    hide lor
    show eff neutral_talk at Position(xpos=1400)
    with dissolve
    eff "Alright, that's one thing dealt with! What's next?"
    show hit confused_talk at Position(xpos=1300)
    show eff smirk at Position(xpos=1400)
    hit "I… What just happened?"
    show pov smirk_talk at left
    show hit confused at Position(xpos=1300)
    show eff shocked at Position(xpos=1400)
    pov "First time I heard him being called Kevin without him going on a rant about his title."
    show pov bored at left
    show hit confused at Position(xpos=1300)
    show eff embarrassed_talk at Position(xpos=1400)
    eff "Oh, Kevin and I go way back. And I know he has a bit of a crush on me."
    show hit shocked at Position(xpos=1300)
    show eff smirk_talk at Position(xpos=1400)
    eff "Add that, plus the thing we bargained for, and I managed not just to send them out of the back room, but for them to close down the store entirely!"
    eff "We should avoid being interrupted that way."
    show hit embarrassed_talk at Position(xpos=1300)
    show eff confused at Position(xpos=1400)
    hit "I… He is never this nice to me…"
    show pov shocked at left
    show hit bored_talk at Position(xpos=1300)
    show eff neutral at Position(xpos=1400)
    hit "Wait, did you say you managed to leave the store entirely?!"
    show pov confused at left
    show hit smirk_talk at Position(xpos=1300)
    show eff bored at Position(xpos=1400)
    hit "What did you offer to make him willingly want to go outside - let alone bring the guys with him?!"
    show pov bored at left
    show hit shocked at Position(xpos=1300)
    show eff neutral_talk at Position(xpos=1400)
    eff "I promised I would send him some feet pics later."
    show hit shocked_talk at Position(xpos=1300)
    show eff neutral at Position(xpos=1400)
    hit "WHAT?!"
    hit "Oh my gosh! Why would you do that?!"
    show pov shocked at left
    show hit shocked at Position(xpos=1300)
    show eff embarrassed_talk at Position(xpos=1400)
    eff "Relax, I'm not gonna actually send him some of mine. I'll just look online for pictures of some random girl's feet and send him that."
    show pov smirk at left
    show hit bored at Position(xpos=1300)
    show eff smirk_talk at Position(xpos=1400)
    eff "He would never be able to tell the difference."
    show pov smirk_talk at left
    show hit confused at Position(xpos=1300)
    show eff  at Position(xpos=1400)
    pov "That's the crafty Effie I know…"
    show pov confused at left
    show eff smirk_talk at Position(xpos=1400)
    eff "Just a heads-up for you, [povname]. If a girl you've never seen naked sends you nudes or pictures of any kind that don't show her face, there is an 80\% chance they are fake and you would never know about it."
    show pov embarrassed at left
    show hit embarrassed at Position(xpos=1300)
    show eff neutral_talk at Position(xpos=1400)
    eff "After all, it's not like you would be able to tell, right?"
    show pov bored_talk at left
    show hit confused at Position(xpos=1300)
    show eff neutral at Position(xpos=1400)
    pov "I… Thanks for the info, I guess?"
    show pov bored at left
    show eff neutral_talk at Position(xpos=1400)
    eff "Alright, we doing this or what?"
    show hit embarrassed at Position(xpos=1300)
    show eff smirk_talk at Position(xpos=1400)
    eff "I'm ready to have my body captured by the master!"
    show hit confused_talk at Position(xpos=1300)
    show eff confused at Position(xpos=1400)
    hit "I…"
    hit "I should be calling you, Master…"
    show hit smirk_talk at Position(xpos=1300)
    show eff neutral at Position(xpos=1400)
    hit "And seriously, should I take it personally that those guys don't treat me anywhere as nicely as they do you, Effie?"
    show pov confused at left
    show hit smirk at Position(xpos=1300)
    show eff neutral_talk at Position(xpos=1400)
    eff "They probably just see you as one of the guys, and as such, they are comfortable enough around you and don't care about showing you their usual selves."
    show hit embarrassed at Position(xpos=1300)
    show eff confused_talk at Position(xpos=1400)
    eff "I wouldn't think too much about it."
    show pov bored at left
    show hit embarrassed_talk at Position(xpos=1300)
    show eff neutral at Position(xpos=1400)
    hit "Well, I'm pretty, right? Why am I excluded from their simping?"
    show pov bored_talk at left
    show hit embarrassed at Position(xpos=1300)
    show eff confused at Position(xpos=1400)
    pov "L-Let's just focus on the job at hand, alright?"
    pov "You were pressed for time and needed the reference poses as soon as possible, right?"
    show pov embarrassed at left
    show hit embarrassed_talk at Position(xpos=1300)
    hit "R-Right!"
    show pov neutral at left
    show hit neutral_talk at Position(xpos=1300)
    show eff smirk at Position(xpos=1400)
    hit "Right, I don't have time to think about this!"
    show pov shocked at left
    show hit confused_talk at Position(xpos=1300)
    hit "[povname], Could you set up the room like you did for your session, while I set up my workstation?"
    show pov neutral at left
    show hit smirk_talk at Position(xpos=1300)
    show eff neutral at Position(xpos=1400)
    hit "You and Effie can then get naked and I'll guide you through the process!"
    show pov neutral_talk at left
    show hit smirk at Position(xpos=1300)
    pov "Sure thing!"
    show pov smirk at left
    show hit neutral at Position(xpos=1300)
    show eff smirk_talk at Position(xpos=1400)
    eff "Alright, this is when I get the girls out, right?"
    show pov embarrassed at left
    show hit smirk at Position(xpos=1300)
    show eff neutral_talk at Position(xpos=1400)
    eff "This is gonna be fun!"

    $ hitomi_path = 16

    #jump lbl_comicbookbackroom_day
    jump lbl_intense_modeling
