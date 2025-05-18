## Allaway Private Talk ##
label lbl_allaway_private_talk:
    default allawayprivatetalk_telltruth = 0

    scene bg park_night
    with fade
    show pov confused at left
    with dissolve
    pov "..."
    pov "{i}Where is she?{/i}"
    pov "{i}... Should I be worried?{/i}"
    pov "..."
    pov "{i}I should probably be worried...{/i}"
    pov "{i}God, how did it come to this?!{/i}"
    pov "..."
    pov "{i}It's all ending soon... just a few days more...{/i}"
    show pov shocked at left
    show miso confused_talk at right
    with hpunch
    mis "What's ending soon?"
    show pov shocked_talk at left
    show miso shocked at right
    pov "Jesus! Fuck!"
    show pov bored at left
    show miso smirk_talk at right
    mis "Hehehe."
    mis "Didn't know you were so much of a scaredy cat."
    show pov embarrassed_talk at left
    show miso smirk at right
    pov "I-I wasn't scared!"
    show pov bored_talk at left
    pov "You just surprised me! That's all..."
    show pov bored at left
    show miso smirk_talk at right
    mis "Yeah, whatever you say, tough guy."
    show pov embarrassed at left
    show miso embarrassed_talk at right
    mis "Shall we sit?"

    scene bg allawayprivatetalk_2
    with fade
    pov "..."
    pov "Are you okay?"
    show bg allawayprivatetalk_4
    mis "Yes, [povname], I'm fine."
    show bg allawayprivatetalk_2
    mis "As fine as whatever 'fine' means nowadays."
    mis "Just had to do some laundry afterwards, so that's why I'm late."
    mis "And by laundry, I mean some errands for Jack."
    show bg allawayprivatetalk_1
    pov "I-I see..."
    show bg allawayprivatetalk_3
    mis "It's sweet how much you worry about me."
    mis "I really appreciate it you know?"
    show bg allawayprivatetalk_2
    mis "I know about your fight with Jack..."
    pov "O-Oh, you do?"
    pov "..."
    pov "Are you angry with me?"
    mis "Angry?"
    mis "Are you kidding me?"
    show bg allawayprivatetalk_4
    mis "What girl doesn't like it when her man fights for her?"
    mis "I heard you wiped the floor with him too!"
    mis "I actually find it a huge turn on."
    show bg allawayprivatetalk_2
    mis "Just imaganing Jack getting all that he deserves."
    pov "Oh, you bet!"
    show bg allawayprivatetalk_4
    pov "They had to hold me back from beating his skull in, once he was on the ground."
    pov "Coach almost suspended me because of it."
    mis "Almost? Isn't he really strict about club rules?"
    pov "Seems like I put up enough of a good show, for him to show me mercy."
    show bg allawayprivatetalk_2
    mis "Well, damn."
    mis "Color me impressed!"
    mis "And very very turned on."
    show bg allawayprivatetalk_4
    mis "Like to an 11."
    pov "Always trying to do my best to surprise you."
    show bg allawayprivatetalk_2
    mis "No kidding."
    show bg allawayprivatetalk_1
    pov "How did you find out about it anyway?"
    mis "..."
    mis "From Jack actually."
    pov "Oh, I assumed he'd be too embarrassed to bring it up to you."
    pov "..."
    show bg allawayprivatetalk_3
    pov "H-He didn't... hurt you because of it, right?"
    show bg allawayprivatetalk_4
    mis "No, [povname]. I'm fine really. Just... really... really... tired."
    mis "I barely have enough time in the night to sleep, as much of the work {i}is{/i} at night."
    mis "So, I do apoligize if I come off as cranky; busy; and just out of it."
    mis "Because I really am. I really have no choice but to go through with it."
    mis "And for how long? I don't know."
    mis "I'm just hoping for an end to all this."
    if parkingwithallaway_action == 0:
        show bg allawayprivatetalk_1
        pov "..."
        pov "Y'know? I shouldn't have accepted your offer to drive me home."
    elif parkingwithallaway_action == 1:
        show bg allawayprivatetalk_1
        pov "..."
        pov "Y'know? I shouldn't have.. made a move in that car. I was being reckless..."
    else:
        show bg allawayprivatetalk_1
        pov "..."
        pov "Y'know? I should've.. stopped you- from... y'know. I was being selfish..."
    show bg allawayprivatetalk_6
    with dissolve
    mis "Don't blame yourself, [povname]. I'm just as much a part of this mess as you are."
    mis "But being the responsible one, I am the one taking charge to fix the problem."
    mis "I'd hate to see you get involved in what I'm doing. There's nothing glamorous about it."
    mis "My senses are heightened. I feel like everyone is watching my every move."
    mis "You think I'm paranoid when nervous? I'm paranoid all the time now.."
    mis "I just- have to be careful of what I do and say..."
    mis "Don't worry, okay?"
    if missallaway_points <= 6:
        mis "I'm telling this not as your teacher; but as a friend."
    else:
        mis "I'm telling this not as your teacher; but as a lover."
    mis "Stay away from Jack."
    mis "You owe me that much."
    mis "I wouldn't have imagined myself in this very situation; but here I am."
    mis "I was an innocent teacher-"
    pov "Innocent on the outside."
    mis "..."
    mis "I was innocent on the outside- but now I've found myself falling for my own student."
    mis "And I'm literally - in a metaphorical sense - falling head-over-heels for him."
    show bg allawayprivatetalk_5
    pov "This student sounds like a great guy. I bet he's hung like a horse."
    mis "He is amazing-"
    mis "Well, I was going to say amazing in bed but we've done it in most places except in bed."
    mis "That's not abnormal.. is it?"
    show bg allawayprivatetalk_6
    pov "We're an abnormal pair, so I think it fits the bill."
    mis "In any case..."
    mis "I don't want there to be secrets between us, [povname]."
    mis "Right now, you're the only one I can count on."
    pov "..."
    pov "Y-Yeah. I know that, Miss..."
    mis "With that being said..."
    show bg allawayprivatetalk_6
    $ renpy.pause(1,hard=True)
    show bg allawayprivatetalk_7
    with hpunch
    $ renpy.pause()
    show bg allawayprivatetalk_6
    with dissolve
    mis "I really appreciate what you do for me."
    mis "Out of everything that is happening to me- to us."
    mis "You're the only thing I have absolutely no regrets about."
    mis "And..."
    mis "A-And if I had the chance to start this all over again..."
    show bg allawayprivatetalk_5
    mis "..."
    mis "Well... I don't think I would choose a single thing differently, if it meant that I can enjoy your company."
    mis "To be this close to you..."
    mis "A-And..."
    mis "And to have our after-class sexcapades-"
    show bg allawayprivatetalk_5
    mis "..."
    mis "Maybe this is just all the emotions and exhaustion making me say crazy things..."
    mis "But I really feel that you complete me..."
    mis "Is that weird? It's weird isn't it?"
    show bg allawayprivatetalk_6
    mis "It's definitely cliche."

    menu:
        "Yes, but...":
            pov "Well, yes, but not in a bad way."
            mis "Elaborate."
            pov "Well..."
            show bg allawayprivatetalk_5
            pov "After everything we have been through, I definitely feel like you're an important part of my life, you know?"
            pov "It's hard to explain..."
            pov "I feel like I know you better than I know anyone, but at the same time there are so many more things I want to know about you."
            pov "I want to know everything in fact."
            pov "Maybe it's the whole 'people who share a tragedy tend to be closer' thing."
            pov "But there is no way in hell I could be experiencing anything near, as half of the shit that's been thrown your way."
            show bg allawayprivatetalk_6
            pov "You're quite the warrior, Allaway."
            pov "To still be able to get up in the morning and go to class, despite everything that's happened to you..."
            pov "And you have no idea how glad I am that you still find it in your heart to talk to me, after everything..."
            pov "To still feel the way you feel about me, despite what I have pretty much put you through..."
            pov "I guess what I'm trying to say..."
            pov "Is that I'm proud of you."
            pov "Proud of who you are and proud to consider myself, someone you hold so close to your heart."
            show bg allawayprivatetalk_5
            pov "You also complete me in ways you cannot imagine."
            pov "And I swear I'll do everything in my power to make sure that we get ourselves out."
            pov "I want to consider myself the only one allowed to do that..."
            pov "That is... If you'll have me?"
        "Not at all.":
            pov "No... No, I don't think so."
            show bg allawayprivatetalk_5
            pov "We have shared a lot with each other and it's no secret that I have been trying to charm you since day one."
            mis "You have been surprisingly effective."
            pov "I mean, aside from the physical attraction I have towards you."
            pov "Well, I really do care about you."
            pov "I wasn't about to half-ass my intentions with you."
            mis "Hope you have that same drive with your grades."
            pov "Well, I do have the odds against me, with the beautiful sexy woman teaching me being too hot for her own good."
            pov "Hard to concentrate with her occupying my mind, y'know?"
            mis "Kiss-ass."
            mis "We'll see how flirty you'll be when you end up catching up with your coursework over summer."
            show bg allawayprivatetalk_6
            pov "A whole summer with you? Make all of the tests oral and that sounds like a paradise."
            mis "..."
            pov "..."
            mis "..."
            mis "Pfft-!"
            mis "Hahahaha!"
            mis "Y-You smooth mothertrucker."
            pov "Just the best corny lines for you."
            mis "Gee, I feel {i}so{/i} honored!"
            pov "You know you love my lines!"
            mis "Sadly, I do."
            mis "I really, really do."
            mis "What does that say about me?"
            pov "That you're either a woman of the most refined of tastes in comedy and flirting."
            pov "Or just have such a level of extreme poor taste that you ended up with dorky little me."
            pov "I know which one sounds better of the two."
            mis "And I think I know which one I actually am."
            pov "It's not the first option is it?"
            mis "No, not in the slightest."
            mis "Hehehe~"
            mis "Even for my standards, you really are a dork."
            show bg allawayprivatetalk_5
            pov "..."
            pov "You're really important to me..."
            pov "I cherish every moment we share together."
            pov "I want you to know you're one of the bravest women I have ever had the pleasure of knowing."
            pov "You are smart, funny, adorably quirky and one of the best teachers to have ever existed."
            pov "And if you'll allow me..."
            show bg allawayprivatetalk_6
            pov "I want to stay by your side for a very, very long time."
            pov "Because I honestly think my life would be unbelievably grey, without you in it."
            pov "You just have this day to brighten my day in such a way, that if I got to see you everyday of my life I'm certain I would become the happiest man in the world."
            pov "... So as a student, a friend or maybe even something more..."
            pov "I hope you let me stay next to you, even if it is just for a little while longer."
    show bg allawayprivatetalk_5
    mis "{i}*Sniff*{/i}"
    mis "{i}*Sniff*{/i} That was really, really, really corny, [povname]. {i}*Sniff*{/i}"
    mis "Like {i}*sniff*{/i} I wanna cringe into a ball so bad."
    mis "But I'd be lying to myself if I didn't say that this is everything I've ever wanted..."
    mis "My fairytale romance..."
    mis "{i}*Sniff*{/i}"
    show bg allawayprivatetalk_6
    mis "And that's saying something, since I really don't like romantic fairytales."
    mis "Not enough guns and explosions. {i}*sniff*{/i}"
    pov "You really like your dick-flicks, don't you?"
    mis "The vibrations coming from my subwoofer makes my body tingle..."
    pov "... That explains a lot."
    mis "{i}*Sniff*{/i}"
    mis "Oh, look at me, a grown woman making an embarrassing cry-baby of herself."
    mis "I-I..."
    mis "I don't know why you would want, a mess like me, but..."
    mis "P-Please... Please, never let me go..."
    show bg allawayprivatetalk_8
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg allawayprivatetalk_6
    with dissolve
    pov "I'm not planning to anytime soon..."
    show bg allawayprivatetalk_5
    pov "And besides."
    pov "When it comes to being weird, you are; but in a good way."
    mis "Pfft. Jerk."
    mis "Making me blush, cry and even laugh, all at the same time..."
    show bg allawayprivatetalk_6
    mis "You are an even weirder weirdo than me - I hope you're aware, right?"
    mis "Here I was expecting you to tell all of your friends, you managed to get into my pants; and you go and end up getting all of me."
    pov "Again, weird, but in a good way!"
    pov "Right?"
    mis "That's us, alright."
    mis "A very weird couple of oddballs..."
    show bg allawayprivatetalk_8
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg allawayprivatetalk_5
    with dissolve
    mis "So, with all of that finally off my chest."
    mis "What did you want to talk about?"
    mis "I assume you didn't just bring me here to look at my pretty face."
    pov "Nope, I wanted to kiss you."
    mis "Really, that's all?"
    show bg allawayprivatetalk_6
    pov "No, but it won't hurt to give me another one."
    show bg allawayprivatetalk_8
    with dissolve
    $ renpy.pause(1.2,hard=True)
    show bg allawayprivatetalk_6
    with dissolve
    mis "Okay, enough stalling."
    mis "What did you want to tell me?"
    show bg allawayprivatetalk_5
    pov "..."
    pov "...."
    pov "{i}I have to tell her about the deal I have with Jack.{/i}"
    pov "{i}After all of that, how can I not tell her?{/i}"
    pov "{i}We opened up ourselves to each other, for fuck's sake!{/i}"
    pov "{i}I know I have to tell her. I owe her that much, but...{/i}"
    pov "{i}But at the same time, what good will that do?{/i}"
    pov "{i}All I'm going to end up doing is worrying her - not to mention, likely get her angry at me.{/i}"
    pov "{i}She has been through so much already...{/i}"
    pov "{i}God, the last few days have been exhausting for her!{/i}"
    pov "{i}I know she is strong-as-hell, for even having to deal with all of this - but is giving her more to worry about, a good idea?{/i}"
    pov "{i}It's not like anyone is going to know I'm doing this, in the first place.{/i}"
    pov "{i}At least they won't if I don't screw this up...{/i}"
    pov "{i}Otherwise our relationship will consist of conjugal visits in prison...{/i}"
    pov "{i}I-{/i}"
    pov "{i}I owe her the truth but is that worth worrying her more?{/i}"
    pov "{i}Will she even be able to handle the stress, after everything that has happened?{/i}"
    show bg allawayprivatetalk_6
    with hpunch
    mis "[povname]!?"
    mis "Are you okay?"
    mis "You just stopped talking and stared out at the horizon."
    mis "For like... an uncomfortably long time."
    mis "I said your name at least four times."
    pov "..."
    mis "Do you feel ill?"
    pov "..."
    mis "You're scaring me..."
    pov "O-Oh, I..."
    show bg allawayprivatetalk_5
    pov "Y-Yeah, I'm fine."
    pov "It's just that-"

    menu:
        "Don't reveal your plans with Jack":
            pov "It's just that I'm trying to enjoy our time together, you know?"
            pov "It's been a while since we've had alone time together and I was really missing that."
            pov "Missing you..."
            mis "I'm sorry..."
            show bg allawayprivatetalk_6
            mis "I really should try and make some more time for you but-"
            pov "You don't need to explain yourself."
            pov "I don't hold it against you. It's not like you deliberately don't want to spend time with me."
            pov "I know you're exhausted - and Jack doesn't make things easier on you."
            mis "Y-Yeah..."
            mis "Sometimes I don't even want to get out of bed in the morning..."
            mis "At the beginning, I used to cry myself to sleep..."
            mis "I was so, so scared..."
            mis "I felt terrible. And ashamed with myself."
            mis "And I was scared that I would eventually lose you too..."
            pov "What?"
            pov "That's crazy talk."
            pov "Why did you think you would lose me?"
            mis "Well, for starters, I was deliberately avoiding you."
            mis "I tried so hard to make all this go away; and I figured, staying away from you would make it better-"
            mis "But it didn't. It was difficult."
            mis "It still is difficult but even just being with you now; it drives me forward."
            mis "I'm only doing it because he has dirt on us."
            show bg allawayprivatetalk_5
            mis "If only you knew what Jack's got me doing for him."
            mis "You'd hate me for it. I hate myself. I told myself to never get into this in my whole life."
            mis "It's funny how the world treats us. Like it hates us for trying to be good."
            mis "..."
            mis "We were in the wrong place at the wrong time."
            mis "And because of that, everything's- just going down hill."
            mis "If he ever releases those videos-"
            mis "I would never be able to step outside again!"
            mis "More than likely, I would have to move out of the country - and somewhere no one knows who I am."
            mis "Change my name, dye my hair, maybe get a tan or colored contact lenses."
            mis "Almost makes it sound like an adventure."
            mis "Although I don't like the reasons why I would have to do it..."
            mis "Neither the fact that I would have to leave everything I know... And you..."
            show bg allawayprivatetalk_6
            pov "..."
            pov "It won't come to that..."
            pov "I swear to you, I'll find a way to get you out of this mess."
            pov "No matter the cost."
            mis "I hope you're right, [povname]..."
            mis "But you should know better than to make a girl promises you can't keep..."
            pov "I mean it, Miss Allaway!"
            pov "No matter what I have to do, no matter how dangerous it is."
            pov "I'll get you out of this."
            pov "I promise!"
            if missallaway_points <= 8:
                $ missallaway_points += 2
            else:
                $ missallaway_points = 10
            $ renpy.notify("Your relationship with Miss Allaway has increased by 2")
            show bg allawayprivatetalk_8
            with dissolve
            $ renpy.pause(0.8,hard=True)
            show bg allawayprivatetalk_6
            with dissolve
            mis "..."
            mis "Thank you, [povname]."
            mis "Alright..."
            mis "I'll trust you."
            mis "Just please..."
            mis "Please don't do anything too crazy..."
            pov "I- I'll try..."
            mis "{i}*Yawn*{/i}"
            mis "Oof, excuse me."
            pov "You tired, Miss?"
            mis "It has been a long week."
            show bg allawayprivatetalk_5
            pov "You can say that again. I haven't even heard one of your spontaneous outbursts in a while now!"
            mis "I don't think risque outbursts happens when I'm with someone I'm comfortable with."
            mis "Plus, we've fooled around; so I think that helped manage the intensity of them."
            show bg allawayprivatetalk_6
            pov "You think we should be snuggling closely together like this?"
            pov "What if someone else from uni sees us?"
            mis "Don't worry about that."
            mis "I wasn't in the mood to be interrupted, so I dropped in an extra long cousework assignment at the last minute. Due for tomorrow."
            mis "One that I'm {i}sure{/i} you have completed by now, right?"
            show bg allawayprivatetalk_5
            pov "Um..."
            mis "Ugh, forget it. I'm too comfortable to let you go and be responsible."
            mis "Enjoy it while it lasts, this is your one and {i}only{/i} pass I'm giving you in our relationship!"
            show bg allawayprivatetalk_6
            pov "I had a pass?!"
            pov "I wish I've known that before and had used it on something bigger!"
            mis "Well, too bad. Now, be a good boy and put your hand down my pants."
            mis "Mama wants a... de-stressing massage."
            pov "I'm totally whipped in our relationship, aren't I?"
            mis "Ever heard the phrase 'teacher's pet'?"
            show bg allawayprivatetalk_5
            pov "That bad, huh?"
            mis "Just shows how much I care~"
            mis "Now, you better get comfortable, cause you're {i}not{/i} going home early tonight!"
            pov "I like this possessive side of you."
            mis "Damn straight, you do!"
            mis "Now work those hands!"
            show bg allawayprivatetalk_6
            pov "That's what she said!"
            show bg allawayprivatetalk_5
            mis "That is what she definitely said."

            jump lbl_allway_private_talk_end
        "Tell her everything about your plans with Jack":
            $ allawayprivatetalk_telltruth = 1
            pov "It's just that, well..."
            pov "There is something I need to tell you."
            show bg allawayprivatetalk_6
            pov "Something big."
            mis "Is it a bad thing?"
            pov "Sort of..."
            mis "Did you copy someone's assignent?"
            pov "No!"
            mis "Are you smoking crack?"
            pov "Hell no!"
            mis "Did you cheat on me?"
            pov "What? No!"
            mis "Because if you are, I totally, totally get why..."
            pov "No no no no no! I'm definitely not cheating on you, Miss."
            show bg allawayprivatetalk_5
            pov "Not in this universe, and not in any universe."
            pov "..."
            mis "Are you pregnant?"
            show bg allawayprivatetalk_6
            pov "What the hell?! Allaway, stop guessing!"
            mis "I-I'm sorry, [povname]."
            mis "I'm just not really good with bad news and I get nervous..."
            show bg allawayprivatetalk_5
            pov "I guess I can't blame you - with everything that's going on..."
            mis "{i}*Inhale*{/i}"
            mis "{i}*Exhale*{/i}"
            mis "I think I'm ready for it..."
            mis "Hit me."
            show bg allawayprivatetalk_6
            pov "B-"
            mis "Just do it."
            pov "Bef-"
            mis "Like a bandage."
            pov "Before I tell you!"
            pov "You need to promise me that you won't get mad at me..."
            mis "That just tells me that I'm not going to like what I'm about to hear."
            pov "Please... You have to promise."
            pov "I'm being honest and transparent with you right now."
            mis "I thought it was implied that we have to be that, regardless..?"
            pov "Allaway, please!"
            mis "..."
            pov "..."
            mis "{i}*Sigh*{/i} Alright, fine!"
            mis "I promise I won't get mad..."
            pov "Do you mean it?"
            mis "Yes..."
            pov "Really mean it?"
            mis "Yes!"
            pov "Really really mean it-"
            mis "[povname], if you don't tell me right now, I'll get mad, for real!"
            pov "Alright, just... don't freak out when I tell you, okay?"
            mis "[povname], what could you possibly say to make me upset right now?"
            pov "So... that night, after the fight with Jack..."
            scene black
            with fade
            $ renpy.pause(1.5)
            "An explanation later..."
            show bg allawayprivatetalk_4
            with hpunch
            mis "WHAT?!"
            if missallaway_points >= 2:
                $ missallaway_points -= 2
            else:
                $ missallaway_points = 0
            $ renpy.notify("Your relationship with Miss Allaway has decreased by 2")
            mis "ARE YOU CRAZY?!"
            mis "What the hell were you thinking?"
            show bg allawayprivatetalk_3
            mis "Were you even thinking at all? "
            mis "I didn't want you getting involved with Jack - and now you drop this on me?!"
            mis "You're playing russian roulette with a bullet in five chambers!"
            show bg allawayprivatetalk_2
            pov "Miss-!"
            pov "Look, I understand you're angry-"
            show bg allawayprivatetalk_4
            mis "Angry?!"
            mis "Why would I be angry?!"
            mis "I'm not going through all this shit for myself. I'm doing it for us."
            mis "So that your stupid-ass doesn't get involved!"
            pov "So {i}this{/i} is what Jack has {i}you{/i} doing?"
            mis "Yes, [povname]. I'm the designated getaway driver for him and his 'friends'."
            mis "Now you know!"
            show bg allawayprivatetalk_3
            pov "Well, I didn't have a choice!"
            mis "You could have said no!"
            show bg allawayprivatetalk_4
            pov "That would have only made things worse!"
            mis "How could they possibly be any worse?!"
            pov "I could be forced to do this without the chance at setting you free of all of this mess!"
            pov "I wanted you free from his shackles!"
            show bg allawayprivatetalk_2
            mis "..."
            show bg allawayprivatetalk_1
            pov "..."
            pov "{i}*Sigh*{/i}"
            pov "After I beat Jack, he..."
            pov "He came to my house. He ghosted me home."
            pov "I was sure it would end with one of us on the ground, but..."
            pov "After reminding me how much in control he is, of our- situation..."
            pov "He offered me a way out for you..."
            show bg allawayprivatetalk_2
            pov "A single job; no ties or contracts."
            pov "And if I do this, then..."
            show bg allawayprivatetalk_1
            pov "Then he promised to destroy every piece of evidence he has against us and to never speak to you again..."
            mis "And you believe him?"
            pov "Again, I didn't have a choice..."
            show bg allawayprivatetalk_3
            mis "Haven't you seen ‘Be Quiet and Boogie'?"
            show bg allawayprivatetalk_4
            pov "What the hell is that?"
            mis "It's an episode from White Reflection."
            show bg allawayprivatetalk_3
            pov "Look, if I refused to do it, he would have spread the pictures, and have the job done anyway."
            pov "He won't delete the evidence unless he gets something out of it; along with the feeling that he has all the power over me..."
            mis "It's still way too risky, [povname]!"
            show bg allawayprivatetalk_4
            pov "I-I know that!"
            show bg allawayprivatetalk_3
            pov "But..."
            pov "If there was still a chance to free you from this, then... Then I'm willing to take it..."
            mis "What about your future?!"
            show bg allawayprivatetalk_4
            pov "What about {i}your{/i} future?!"
            show bg allawayprivatetalk_2
            mis "..."
            show bg allawayprivatetalk_1
            pov "You wouldn't be able to show your face in this town or any other town, without people pointing fingers at you!"
            pov "You would eventually have to come to a decision to leave town; perhaps even the country!"
            pov "Change your hair, change your name..."
            pov "Change all of those things I love about you - so you wouldn't be recognized - and live, day by day, regretting that mistake..."
            pov "And that's assuming on the off-chance that you don't get locked behind bars."
            pov "Which may I remind you, will be the most likely scenario."
            pov "..."
            show bg allawayprivatetalk_1
            with hpunch
            pov "I'm not going to let that happen!"
            show bg allawayprivatetalk_2
            pov "I'm not willing to take that gamble."
            pov "I'm not losing you that way!"
            pov "..."
            pov "I got you in this problem, so I am going to get you out of it!"
            show bg allawayprivatetalk_1
            pov "..."
            mis "..."
            mis "...."
            mis "....."
            mis "{i}*Sniff*{/i}"
            show bg allawayprivatetalk_3
            mis "Why?"
            mis "Why would you do this... And for me?"
            mis "I don't get it."
            show bg allawayprivatetalk_1
            mis "I'm not worth all of this trouble..."
            mis "I-I'm just a crummy university lecturer, stuck in a small town, with a tendency to talk to myself and babble..."
            mis "I'm awkward and much older than you."
            mis "Have no good experience in relationships."
            mis "And will likely end up shriveled, grey and lonely - with only cats to keep me company..."
            show bg allawayprivatetalk_3
            mis "So why?"
            pov "..."
            show bg allawayprivatetalk_4
            pov "I'm doing it for the same reason you've been doing it for me."
            pov "Because I care about you."
            pov "Because there's no one better than you."
            mis "{i}*Sniff*{/i}"
            pov "I chose the crummy, small-town university lecturer."
            pov "One with a tendency to talk to herself and has the dirtiest mind there is out there..."
            mis "{i}*Sniff*{/i}"
            show bg allawayprivatetalk_6
            with dissolve
            pov "I chose you despite all your perfect imperfections."
            pov "And if you do end up shriveled, grey and lonely with a ton of cats."
            pov "Then we can be shriveled, grey and lonely together, waiting for them to eat us when we die."
            mis "{i}*Sniff*{/i}"
            show bg allawayprivatetalk_7
            $ renpy.pause(0.8,hard=True)
            show bg allawayprivatetalk_8
            with hpunch
            $ renpy.pause(1.5,hard=True)
            show bg allawayprivatetalk_6
            with dissolve
            pov "I love you, Allaway."
            pov "I have no regrets about it."
            pov "I'll set you free and whether you like it or not, I'm going to stay by your side to the best of my ability, for as long as humanly possible."
            pov "Because you're worth all of this."
            mis "..."
            mis "{i}*Sniff*{/i}"
            mis "I love you too, [povname]."

            jump lbl_allway_private_talk_end

label lbl_allway_private_talk_end:

    scene black
    with fade
    $ renpy.pause()
    "After a few more moments together..."
    "Back home..."

    scene bg myhousefront_night
    with fade
    $ missallaway_path = 22
    $ gtime = 3
    $ renpy.pause(1.5)
    jump lbl_myhousefront_night_setup
