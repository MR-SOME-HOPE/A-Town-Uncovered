## Store Rendezvous
label lbl_store_rendezvous:
    #-Scene takes place 3 days after the previous scene-

    #-Mc enters the scene upon talking to Hitomi who is working the counter again-

    #-Scene dialogue varies depending on whether or not Hitomi has been romanced-

    if more_than_friends_with_hitomi_chosen:
        show pov embarrassed_talk at left
        show hit confused at right
        show pov embarrassed_talk at left
        show hit confused at right
        with dissolve
        pov "Heyo."
        show pov confused at left
        show hit smirk_talk at right
        hit "*Giggle* Seriously, babe?"
        show hit confused_talk at right
        hit "You show up at your girlfriend’s store and the first thing you say is just 'Heyo'?"
        show pov smirk_talk at left
        show hit smirk at right
        pov "I can do it in a sing-songy kind of tone if you prefer."
        show pov neutral_talk at left
        show hit neutral at right
        pov "Heyoooo~"
        show pov neutral at left
        show hit smirk_talk at right
        hit "God you are a dork, you know that?"
        show pov smirk_talk at left
        show hit smirk at right
        pov "The dork you chose, so who is really the dork here, hmm?"
        show pov confused at left
        show hit confused_talk at right
        hit "Heh, Smart ass, you are lucky I like you."
        show pov smirk_talk at left
        show hit shocked at right
        pov "I tell myself that everyday."
        show pov neutral at left
        show hit smirk_talk at right
        hit "..."

        #-Hitomi suddenly blushes and appears really embarrassed-
        show pov smirk at left
        show hit bored_talk at right
        hit "Ok, god, you win. I give up!"
        show pov smirk_talk at left
        show hit smirk at right
        pov "Hehehe, still the king of the flirting game!"
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "You get flustered way too easily."
        show pov neutral at left
        show hit smirk_talk at right
        hit "How could I not?!"
        show pov embarrassed at left
        show hit confused_talk at right
        hit "I’ve never been in a real relationship before and we are suddenly talking like this and joking around!"
        show pov neutral at left
        show hit embarrassed_talk at right
        hit "It’s embarrassing and I’m still not used to it!"
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "Hey, you are the one who begged me to start trying it so you could get used to it faster!"
        show hit confused at right
        pov "Though to be fair, I wasn’t expecting you to be Ko’d so easily."
        show pov smirk_talk at left
        pov "You really have like, zero defenses."
        show pov smirk at left
        show hit embarrassed_talk at right
        hit "I’m just new at it, ok?!"
        hit "Give me some time, I’ll be sure to get my revenge on you soon and have you be the one all flustered!"
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "As long as you don’t borderline pass out on me like you did after what we did in the VIP room."
        show pov neutral at left
        show hit embarrassed_talk at right
        hit "T-That’s because I was tipsy from what I was drinking!"
        show pov smirk_talk at left
        show hit shocked at right
        pov "Steven was still mad once he saw the crowd of people watching us."
        show pov confused at left
        show hit smirk_talk at right
        hit "Gah! Don’t remind me!"
        show hit shocked_talk at right
        hit "I work right next door, what if someone from there comes in and recognizes me?!"
        show pov smirk_talk at left
        show hit shocked at right
        pov "You were facing back and I covered your face once I noticed the stares."
        show pov confused_talk at left
        pov "but maybe, next time we decide to drink, let’s do it at your place instead huh?"
        show pov neutral at left
        show hit embarrassed_talk at right
        hit "Agreed…"
    else:
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "Hi, Hitomi!"
        show pov neutral at left
        show hit smirk_talk at right
        hit "There’s my favorite client!"
        hit "I was wondering if you were gonna show up today!"
        show pov smirk_talk at left
        show hit neutral at right
        pov "Well, I was in the neighborhood and figured I should pop in to say hi."
        show pov smirk at left
        show hit smirk_talk at right
        hit "Well, I’m happy you did."
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "Likewise!"
        pov "You looking to be in a good mood."
        show pov neutral at left
        show hit neutral_talk at right
        hit "Definitely!"
        hit "Have my new page set to start posting again and so farm it seems like things are looking up to be better than on the last site."
        show pov shocked at left
        show hit embarrassed at right
        hit "At the very least they had a very clear note that they wouldn’t be randomly deleting people’s work on the site as a recent addition to their rules when I signed up."
        show pov neutral at left
        show hit smirk_talk at right
        hit "So I have very high hopes things will be different for the better this time."
        show pov smirk at left
        show hit embarrassed_talk at right
        hit "Some people even recognize my username from the other site and are excited at the prospect of seeing new work from me!"
        show pov smirk_talk at left
        show hit embarrassed at right
        pov "That’s genuinely great!"
        pov "You’ll be in the front page in no time!"
        show pov confused at left
        show hit embarrassed_talk at right
        hit "Hehehe, thanks but I’ve learn my lesson and that’s not the goal this time."
        show hit neutral_talk at right
        hit "This time’s for me and for my art to be seen and enjoyed properly."
        show pov confused_talk at left
        show hit embarrassed at right
        pov "Sounds like you got it all figured out then."
        show pov confused at left
        show hit embarrassed_talk at right
        hit "I do… I think I really do and I owe it all to you."
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "Ok, ok, let’s not get overly sentimental here."
        show pov smirk_talk at left
        pov "We’ll get in more trouble if we aren’t careful here than the slap on the wrist we got from Steven for the whole VIP room thing."
        show pov smirk at left
        show hit embarrassed_talk at right
        hit "T-That’s because I was tipsy from what I was drinking and I got carried away!"
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "Steven was still mad at us once he saw the crowd of people watching us though."
        show pov confused at left
        show hit shocked_talk at right
        hit "Gah! Don’t remind me!"
        hit "I work right next door, what if someone from there comes in and recognizes me?!"
        show pov confused_talk at left
        show hit shocked at right
        pov "You were facing back and I covered your face once I noticed the stares."
        pov "but maybe, next time we decide to drink, let’s do it at your place instead huh?"
        show pov smirk at left
        show hit neutral_talk at right
        hit "Agreed…"

    #-Jacob appears into scene-

    show pov confused at left
    show hit neutral at Position(xpos=1400)
    show jac smirk_talk at Position(xpos=1600)
    with dissolve
    jac "Hey, hey, hey!"
    jac "What’s up my guy and my guyette?"
    show pov embarrassed_talk at left
    show jac smirk at Position(xpos=1600)
    pov "Hey, dude!"
    show pov embarrassed at left
    show hit smirk_talk at Position(xpos=1400)
    hit "Jacob, what does guyette even mean?"
    show hit smirk at Position(xpos=1400)
    show jac smirk_talk at Position(xpos=1600)
    jac "A girl who is also my guy!"
    show pov embarrassed at left
    show hit bored at Position(xpos=1400)
    show jac neutral_talk at Position(xpos=1600)
    jac "I like to keep you guys guessing with my greetings and nicknames."
    show pov neutral_talk at left
    show jac confused at Position(xpos=1600)
    pov "Well, it’s just nice to see you back in a nicer mood."
    show pov confused_talk at left
    pov "By the way, how did it go with that one girl from the bar? I haven’t gotten the chance to ask you about it."
    show pov neutral at left
    show hit neutral_talk at Position(xpos=1400)
    show jac embarrassed at Position(xpos=1600)
    hit "Look at that! Little Jacob getting himself girls!"
    hit "Come on, spill!"
    show hit neutral at Position(xpos=1400)
    show jac embarrassed_talk at Position(xpos=1600)
    jac "Hehehe, well…"
    jac "Honestly speaking, it was hella weird, dudes…"
    show pov smirk_talk at left
    show jac embarrassed at Position(xpos=1600)
    pov "Weird in what way? Was she into freaky stuff or something?"
    show pov smirk at left
    show hit confused at Position(xpos=1400)
    show jac smirk_talk at Position(xpos=1600)
    jac "Well… Kind of?"
    jac "She pretty much just dragged me to the beach in the middle of the night and had me take my clothes off and we banged on the water."
    show hit neutral_talk at Position(xpos=1400)
    show jac embarrassed at Position(xpos=1600)
    hit "T.M.I. but I’m happy for you!"
    show pov neutral at left
    show jac smirk_talk at Position(xpos=1600)
    jac "Thanks!"
    show pov neutral at left
    show jac embarrassed_talk at Position(xpos=1600)
    jac "It was awesome and we ended up on the sand for the rest, but after we were done and the sun was starting to come out, she pretty much disappeared."
    show pov confused at left
    show jac shocked_talk at Position(xpos=1600)
    jac "I just turn away for a second to get my bearings and my clothes and by the timeI turn back, POOF!"
    show pov  at left
    show hit confused at Position(xpos=1400)
    show jac bored_talk at Position(xpos=1600)
    jac "She is gone like the summer's breeze comes autumn."
    show hit embarrassed at Position(xpos=1400)
    show jac embarrassed_talk at Position(xpos=1600)
    jac "Hell, I tried asking her multiple times for her name but all she did was giggle and make out with me until I forgot the question."
    show pov embarrassed_talk at left
    show hit smirk at Position(xpos=1400)
    show jac embarrassed at Position(xpos=1600)
    pov "Alright, that’s definitely weird…"
    show pov shocked at left
    show hit confused at Position(xpos=1400)
    show jac smirk_talk at Position(xpos=1600)
    jac "Don’t get me wrong, I kinda prefer it that way!"
    show jac neutral_talk at Position(xpos=1600)
    jac "She is gonna be my one night mystery lady who swept me off my feet and ravaged me like no other."
    show pov confused at left
    show jac neutral_talk at Position(xpos=1600)
    jac "Guys, as my bros and friends, I expect you two to back me up with the story when I tell it to people and they don’t believe me."
    show jac confused_talk at Position(xpos=1600)
    jac "hell, I wouldn’t believe it if somebody told it to me!"
    show hit embarrassed_talk at Position(xpos=1400)
    show jac confused at Position(xpos=1600)
    hit "Just don’t try to over embellish it to make it seem like you slept with a supermodel or something again, alright?"
    show jac embarrassed_talk at Position(xpos=1600)
    jac "I make no promises."
    show pov embarrassed at left
    show jac confused_talk at Position(xpos=1600)
    jac "Anyway, just checking in on you guys since I saw ya together!"
    show hit neutral at Position(xpos=1400)
    show jac neutral_talk at Position(xpos=1600)
    jac "By the way Hitomi, did the new volume of Samurai Office Ladies arrive?"
    show pov neutral at left
    show hit neutral_talk at Position(xpos=1400)
    show jac confused at Position(xpos=1600)
    hit "I saved you your copy and added it to your tab, Jacob. Knock yourself out."
    show hit embarrassed at Position(xpos=1400)
    show jac neutral_talk at Position(xpos=1600)
    jac "You are the best!"
    show jac smirk_talk at Position(xpos=1600)
    jac "Alright, I'm heading back home, I gotta go get my samurai girls in suits fix."
    show pov smirk at left
    show hit neutral at Position(xpos=1400)
    jac "See you later, guys!"

    #-Jacob leaves the scene-
    show hit smirk_talk at right
    hide jac
    with dissolve
    hit "Later!"
    show pov neutral_talk at left
    show hit smirk at right
    pov "Laters!"
    show pov smirk at left
    show hit confused_talk at right
    hit "It’s nice to see him in such a high mood, I’m glad he managed to score."
    show pov smirk_talk at left
    show hit confused at right
    pov "Yeah, me too. I was trying to be his wingman and things weren’t looking good."
    show pov smirk at left
    show hit smirk_talk at right
    hit "I do wonder who that girl was for her to just leave him naked on the beach like that."
    show pov embarrassed at left
    show hit neutral_talk at right
    hit "I’d like to give her a piece of my mind!"
    show pov embarrassed_talk at left
    show hit neutral at right
    pov "Let’s just be happy he scored, he really needed a W."
    show pov embarrassed at left
    show hit smirk_talk at right
    hit "No kidding. I was worried since I noticed he was on a foul mood lately, do you know why?"
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "Long story, best to just move on from it."

    if more_than_friends_with_hitomi_chosen:
        show pov confused at left
        show hit smirk_talk at right
        hit "If you say so…"
        show pov neutral at left
        show hit shocked_talk at right
        hit "Oh, I just remembered!"
        show pov shocked at left
        show hit neutral_talk at right
        hit "Do you wanna come over to my place and have a movie night?"
        show pov embarrassed at left
        show hit smirk_talk at right
        hit "I really wanna watch Koko’s Fast Food Delivery Service again and I’d love to watch it together!"
        show pov neutral_talk at left
        show hit neutral at right
        pov "I wouldn’t miss it for the world."
        show pov neutral at left
        show hit smirk_talk at right
        hit "God, I love finally having a boyfriend to watch my anime with!"
        show hit shocked_talk at right
        hit "We need to get you caught up with all my favorites, not to mention my catalog of pure BL goodness!"
        show pov confused_talk at left
        show hit shocked at right
        pov "What’s BL again?"
        show pov embarrassed at left
        show hit smirk_talk at right
        hit "Oh, you’ll find out~"
        show pov smirk_talk at left
        show hit neutral at right
        pov "Alright then!"
        show pov neutral at left
        show hit embarrassed_talk at right
        hit "Actually…"
        show pov confused at left
        show hit confused_talk at right
        hit "How about we close the store a little bit early?"
        show hit neutral_talk at right
        hit "Now that we are going out for real, there’s this one thing I’ve always wanted to try~"
        show pov smirk_talk at left
        show hit neutral at right
        pov "Won’t you get in trouble for closing up early?"
        show pov confused at left
        show hit embarrassed_talk at right
        hit "Well, technically I do need to close up shop to do inventory checks due to security reasons in order for my dad to not have a problem with it."
        show pov embarrassed_talk at left
        show hit neutral_talk at right
        hit "But I also know how he never checks the cameras and I’ve already made inventory before my shift started but he doesn’t need to know that~"
        show pov smirk_talk at left
        show hit neutral at right
        pov "You go from embarrassed to seductress real quick, babe."
        show pov confused_talk at left
        pov "how do you plan to get rid of the guys though?"
        show pov shocked at left
        show hit angry_talk at right
        hit "HEY GUYS, I HAVE TO CLOSE UP SHOP FOR NEW INVENTORY!"
        hit "FIRST 5 TO LEAVE GET FIRST PICK OF NEW BOOSTER PACKS TOMORROW MORNING!"

        #-Proceed to vibrate the screen up and down to indicate the nerd stampede-
        show pov embarrassed_talk at left
        show hit smirk at right
        pov "Woah… I don’t think I’ve ever seen Lord Kev run that fast… Or at all… He and the guys were the first out the door and they were all the way in the back!"
        show pov shocked at left
        show hit neutral_talk at right
        hit "I want to think that if nothing else, this whole experience got me better at wrangling the guys."
        show pov smirk at left
        show hit smirk_talk at right
        hit "Now help me lower the blinds and lock the door and lose those clothes~"
        show pov smirk_talk at left
        show hit neutral at right
        pov "Ma’am, yes ma’am!"

    else:
        show pov confused at left
        show hit neutral_talk at right
        hit "Alright, if you say so?"
        show hit smirk_talk at right
        hit "Changing topics, by the way."
        show pov neutral at left
        show hit embarrassed_talk at right
        hit "Do you think I could ask you to model for me some more?"
        hit "I need to capture more action poses and I have a few things I want you to hold while posing so I can reference them better."
        show pov embarrassed at left
        show hit smirk_talk at right
        hit "I need basic swords and gun stances."
        show pov embarrassed_talk at left
        show hit smirk at right
        pov "Hey, any art project that has me holding a sword is an instant yes from me!"
        show pov embarrassed at left
        show hit confused_talk at right
        hit "Well, you’ll be holding a broom handle rather than a sword but it’s the same concept."
        show pov smirk_talk at left
        show hit confused at right
        pov "The broom handle is every little boy’s first sword, you know?"
        show pov neutral_talk at left
        show hit embarrassed at right
        pov "We are leaving after your shift is done then?"
        show pov neutral at left
        show hit embarrassed_talk at right
        hit "Actually…"
        show pov confused at left
        hit "How about we close the store a little bit early?"
        show pov smirk at left
        show hit smirk_talk at right
        hit "Since we have… our understanding about intimacy… There’s something I’ve always wanted to do~"
        show pov smirk_talk at left
        show hit neutral at right
        pov "Won’t you get in trouble for closing up early?"
        show pov smirk at left
        show hit embarrassed_talk at right
        hit "Well, technically I do need to close up shop to do inventory checks due to security reasons in order for my dad to not have a problem with it."
        show hit bored_talk at right
        hit "But I also know how he never checks the cameras and I’ve already made inventory before my shift started but he doesn’t need to know that~"
        show pov smirk_talk at left
        show hit embarrassed at right
        pov "you have quite the pervy mind for schemes, you know?"
        show pov smirk at left
        show hit smirk_talk at right
        hit "I’ve written porn stories, [povname]. This is nothing new for me~"
        show pov neutral_talk at left
        show hit smirk at right
        pov "Heh, fair enough."
        show pov confused_talk at left
        show hit neutral at right
        pov "But how do you plan to get rid of the guys though?"
        show pov shocked at left
        show hit angry_talk at right
        hit "HEY GUYS, I HAVE TO CLOSE UP SHOP FOR NEW INVENTORY!"
        hit "FIRST 5 TO LEAVE GET FIRST PICK OF NEW BOOSTER PACKS TOMORROW MORNING!"

        #-Proceed to vibrate the screen up and down to indicate the nerd stampede-
        show pov embarrassed_talk at left
        show hit neutral at right
        pov "Woah… I don’t think I’ve ever seen Lord Kev run that fast… Or at all… He and the guys were the first out the door and they were all the way in the back!"
        show pov embarrassed at left
        show hit neutral_talk at right
        hit "I want to think that if nothing else, this whole experience got me better at wrangling the guys."
        show pov shocked at left
        show hit smirk_talk at right
        hit "Now help me lower the blinds and lock the door and lose those clothes~"
        show pov neutral_talk at left
        show hit smirk at right
        pov "Ma’am, yes ma’am!"


    scene black
    with fade

    $ hitomi_path = 30

    jump lbl_geek_sex
