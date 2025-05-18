label lbl_daily_grind_part2:
    $ officejobs_complete = 0
    $ officejobs_copymachine = 0
    $ officejobs_coffeerun = 0
    $ officejobs_emailproofread = 0
    default have_spoken_to_corrine_about_fistem = 0

    scene bg officefloor_day
    with fade
    #[Office, afternoon - “Daily Grind Part 2”  - main_story =103]

    #-Mc enters the office and is greeted by Corrine this time-

    show pov shocked at left
    show cor smirk_talk at right
    with dissolve
    cor "Hey there, kiddo!"
    cor "Looking forward to another day of intern work?"
    show pov embarrassed_talk at left
    show cor smirk at right
    pov "Just hoping to get through the day, at this point."
    show pov embarrassed at left
    show cor smirk_talk at right
    cor "Don’t we all?"
    show pov neutral at left
    show cor neutral_talk at right
    cor "Just try not to focus on the clock and keep your head deep in your work, and you’ll do just fine."
    show cor smirk_talk at right
    cor "Even if the colors of the world have faded away and the everlasting spark that carried us through the day-to-day grind has been extinguished and all hope for the future is forever lost."
    show pov smirk_talk at left
    show cor smirk at right
    pov "Woah, where the hell did that come from?"
    show pov neutral at left
    show cor neutral_talk at right
    cor "It’s the scheduled Manager Meeting Wednesday."
    show pov confused at left
    show cor bored_talk at right
    cor "My Schnookums Honey Bunny was taken away from me and will be assisting a “Basics of Team Leadership” seminar out of the office with the other managers."
    show pov embarrassed at left
    cor "It’s an entire day without me breathing in, the same air he is breathing. Or him showing me his grumpity grump-grump face whenever I try to spoil him!"
    cor "So every reason for me to smile or even live has pretty much been taken away from my grasp."
    show pov embarrassed_talk at left
    show cor smirk at right
    pov "Wow, you really like him that much, huh?"
    show pov embarrassed at left
    show cor smirk_talk at right
    cor "Oh, [povname]. When you find that one special person who gives meaning to your life and completes you, you’ll understand just how much it hurts when they are away, even when you know it’s only temporary."
    show pov confused_talk at left
    show cor smirk at right
    pov "Isn’t he like twice your age?"
    show pov confused at left
    show cor smirk_talk at right
    cor "We are both consenting adults, so age is just a number, for our situation."
    show pov shocked at left
    show cor bored_talk at right
    cor "And before you make assumptions I’ll strangle you for, I assure you: his family isn’t loaded and even his paycheck isn’t that much different than mine."
    show pov embarrassed at left
    show cor smirk_talk at right
    cor "I could easily be the secretary of one of the higher ranking members of the company; and earn three times as much as what he and I make combined right now."
    show pov embarrassed_talk at left
    show cor smirk at right
    pov "Yeah, he did mention something about him being the envy of the other departments and higher-ups, over having you with him."
    pov "He sounded quite proud of himself about it too."
    show pov shocked at left
    show cor confused_talk at right
    cor "He did?!"
    show pov confused at left
    show cor smirk_talk at right
    cor "Oh, honey you just brought back the spark to my life and earned my schnookums a special favor once he comes back."
    show pov confused_talk at left
    show cor smirk at right
    pov "Uhhh, glad I could help?"
    show pov embarrassed_talk at left
    show cor shocked at right
    pov "If you don’t mind me asking though, why do you like him so much?"
    show pov embarrassed at left
    show cor smirk_talk at right
    cor "Oh, now that is a very personal question there, kiddo."
    show pov confused at left
    show cor bored_talk at right
    cor "One that is accompanied by quite the story to it too, so maybe I’ll tell you once I feel you are trustworthy enough of the answer to it."
    show pov confused_talk at left
    show cor neutral at right
    pov "Sorry, didn’t mean to overstep boundaries."
    show pov embarrassed at left
    show cor neutral_talk at right
    cor "Oh, it’s quite alright, kiddo."
    show pov confused at left
    show cor embarrassed_talk at right
    cor "To be honest, it’s not a question I haven’t been asked before, at this point."
    show pov embarrassed at left
    show cor neutral_talk at right
    cor "But I have to make sure you are not a blabbermouth; and end up telling other people about it by accident. It’s something that could affect how my Honey Buns looks at me as a whole, after all."
    show pov smirk_talk at left
    show cor smirk at right
    pov "Dang, that heavy of a story, huh?"
    show pov smirk at left
    show cor smirk at right
    cor "Quite. But enough about that now."
    cor "You have managed to return the spark to my everlasting flame of love for my Schnookums, so that means we gotta work hard to show him everything is under control - even in his absence!"
    show pov neutral at left
    show cor neutral_talk at right
    cor "Be ready to give me your best and double that down, Hun!"
    show pov neutral at left
    show cor neutral at right
    pov "Well, at least you are in better spirits."

    $ have_spoken_to_corrine_about_fistem = 1

label lbl_daily_grind_part2_jobs_menu:
    scene bg officefloor_day
    with fade
    menu:
        "Copy Machine" if not officejobs_copymachine:
            jump lbl_officejobs_copymachine

        "Coffee Run" if not officejobs_coffeerun:
            jump lbl_officejobs_coffeerun

        #"Email Proofreading" if not officejobs_emailproofread:
        #    jump lbl_officejobs_emailproofread


label lbl_daily_grind_part2_jobs_midscene:
    #     #-Screen fades to black and minigame selection comes up-
    #
    #         #-MID MINIGAME SCENE- #TEMPORARY
    #
    # #-In this mid minigame scene, the MC will stumble into his first sex scene in the office along with an explanation that this is a common occurance in the TRC-
    #
    # #-Scene takes place in the Men’s restroom as Mc is on the stall just messing around with his phone-
    # show pov neutral_talk at left
    # show cor smirk at right
    # pov "At least I can check my phone for a while here without anyone looking over my shoulder."
    # pov "I should wrap up soon before people start asking where I am though."
    #
    # #-Mc’s monolog is interrupted as the sound of a door opening and someone stepping towards the sinks plays out-
    # show pov embarrassed_talk at left
    # show cor confused at right
    # pov "Aw man, I hope it isn’t anyone from the department wondering where I went…"
    #
    # #-The door to the bathroom opens and closes again but this time the sound of the door being locked plays as well-
    # show pov shocked_talk at left
    # show cor shocked at right
    # pov "Wait."
    # pov "Did someone just lock the door?!"
    #
    # "{color=b15c5c}Man{/color}" "Punctual as always, Charlotte…"
    #
    # show pov confused at left
    # show cor shocked at Position(xpos=1600)
    # show chr neutral_talk at right
    # with dissolve
    # chrltt "So are you, Raul…"
    # chrltt "I thought you told me you wouldn’t come by here anymore at this hour."
    # chrltt "What are you doing here?"
    # show pov  at left
    # show cor  at right
    # pov "{i}(Him?! What are you doing in here, lady?!){/i}"
    #
    # raul "Well, this IS the men’s restroom, after all. I just felt the need to go."
    #
    # chrltt "Oh, and you so happen to come into this particular restroom, so far away from your department, at this particular hour?"
    #
    # raul "I… had some errands to run, over this side of the company, and the need just arose."
    #
    # chrltt "Oh, don’t you try and play me for a fool, Raul de la Garza Esteban Josias de las Rosas de su Santísima Trinidad y Navarro!"
    # chrltt "You know damn well why you came into this bathroom at this specific hour!"
    #
    # raul "I… I don’t know what you are talking about."
    #
    # pov "{i}(Ditto…){/i}"
    #
    # chrltt "Oh, I think you do…"
    # chrltt "You still wanted to see me, didn’t you?"
    # chrltt "You still long for me, even after everything that happened at the dinner rehearsal of your niece’s quinceañera…"
    #
    # raul "How dare you bring what happened at the quinceañera up, Charlotte Dixon Parker?!"
    #
    # chrltt "Ah, so you don’t deny you were hoping to see me, then?!"
    #
    # pov "{i}(What is happening?){/i}"
    #
    # raul "A better question would be: what exactly are YOU doing here in the first place!"
    # raul "Weren’t you the one who said -- as clear as day -- that you wished I was the one who fell down the elevator shaft instead of my cousin Ernesto after his face reconstruction in order to avoid the Vatos Locos Cartel?!"
    #
    # pov "{i}(Did he just say a Cartel?!){/i}"
    #
    # chrltt "I… I admit I may have been unnecessarily visceral in the argument, with my words at that moment."
    # chrltt "I was just too overwhelmed when after everything that we’ve been through. You still just introduced me to your Great-Abuela as your “Friend from Work”..."
    #
    # raul "What were you expecting me to say, Charlotte?!"
    # raul "Half of my family believes we are an item, while the others just see you as that girl from business accounting I keep getting dragged around on a leash for!"
    #
    # pov "{i}(Could you guys not do this in a public restroom?!){/i}"
    #
    # chrltt "Well, it would help me to know what it is, in the first place, that YOU want for US to be, Raul!"
    #
    # raul "How can you not know?!"
    # raul "After I flew to Europe to stop your wedding with that abusive golf cart manufacturer and entrepreneur?!"
    # raul "Or after I had a Duel to the Death with Knives with your second cousin, to prevent him seizing control over your grandparents’ tiny horse and pony farm in the Scottish Highlands, and force him to surrender it, so he couldn’t sell it to a glue factory and rob you of your inheritance!"
    # raul "If after all of that you still don’t understand what I want us to be, then I’m just wasting more and more of my time!"
    # raul "Especially when you haven’t done anything to show me you feel the same, but keep leading me on!"
    #
    # pov "{i}(Did he just say a Duel to the Death with Knives?!){/i}"
    #
    # chrltt "Oh, and you think I haven’t made my intentions clear to you?!"
    #
    # pov "{i}(Seriously, did he say Duel to the Death with Knives?!){/i}"
    #
    # chrltt "What about the time I sat by your side in the hospital for days, without even so much as a break to eat, while you were in a coma from when you tripped on that toy car your nephew left on the floor?!"
    # chrltt "Or when I sold half of the jewels my ancestor Lady Charlotte left in my family for generations, just so I could support you and your dream of starting a Progressive Electronic Metal band with a focus in the Scottish Bagpipes?!"
    #
    # raul "YOU LOVED “BAGPIPES OF ELECTRIC MEGA-DESTRUCTION” JUST AS MUCH AS I DID!"
    #
    # chrltt "I LOVED THEM BECAUSE YOU WERE IN IT, RAUL!"
    #
    # raul "AND I KEEP COMING TO THIS RESTROOM BECAUSE I CAN’T BARE NOT TO SEE YOU!"
    #
    # pov "{i}(WHAT THE HELL IS GOING ON?!){/i}"
    #
    # raul "GODDAMNIT I LOVE YOU, CHARLOTTE DIXON PARKER!"
    #
    # chrltt "AND I LOVE YOU, RAUL DE LA GARZA ESTEBAN JOSIAS DE LAS ROSAS DE SU SANTÍSIMA TRINIDAD Y NAVARRO!"
    #
    #
    # #=SEX SCENE STARTS=
    # #-For this sex scene keep the peeping tom perpective in a pov shot through the Mc as he watches through the stall door this two fucking ontop of the sink-
    #
    #     #=SEX SCENE ENDS=
    #
    # #-Once sex scene ends dress the two back up and have them close to eachother-
    #
    # raul "Charlotte…"
    # raul "Is this truly what you want?"
    # raul "Our pasts aside, you are from the Operational Finances Department, while I’m from the Import-Export Department."
    # raul "Our worlds couldn’t be farther apart…"
    #
    # chrltt "As long as there is love, My Raul, we can overcome all obstacles…"
    # chrltt "But we must tread carefully; for God knows what would happen if your evil twin, Ricardo, in the Manufacturing Department were to find out about us!"
    #
    # raul "He will never find out, my love. But we must return to our respective departments before someone finds us."
    #
    # chrltt "When will I see you again?"
    #
    # raul "As soon as the stars will allow us, my love…"
    # raul "Also, my lunch break is the same as yours today."
    #
    # chrltt "Oh, right. It’s Wednesday, isn’t it?"
    # chrltt "I have to file in some reports for one, the bi-weekly review."
    #
    # raul "Yeah, and I have to check in some information on the Taiwaneese suppliers."
    #
    # chrltt "See you at lunch?"
    #
    # raul "You know it, love."
    #
    # #-The two unlock the door to the restroom and leave the room and after a few seconds, the Mc come out of the stall and to the sinks looking shocked-
    #
    # pov "…"
    # pov "{i}(WHAT THE HELL JUST HAPPENED?!){/i}"
    #
    # #-as the Mc asks this another man comes out from one of the other stalls.
    # $ rcrdo.name = "Man"
    # rcrdo "Heh. From your reaction, I assume you're new here, kid?"
    #
    # pov "JESUS!"
    # pov "Dude, don’t sneak up on people like that!"
    #
    # rcrdo "Sorry, I didn’t mean to scare you."
    #
    # pov "It-It’s fine…"
    # pov "You got trapped in here too?"
    #
    # rcrdo "More or less."
    # rcrdo "First time you stumbled onto someone fucking in the office?"
    #
    # pov "You ask that like it’s a common occurrence."
    #
    # rcrdo "Well… not so much common, but it is kind of an open secret that people like to mess around in the office."
    # rcrdo "Hours are long, stress builds up and shit just happens, you know?"
    # rcrdo "And sometimes you get to witness something spicy or be part of it yourself."
    #
    # pov "Shouldn’t HR be all over that?"
    #
    # rcrdo "They should, but what they don’t know won’t hurt ’em, you know?"
    # rcrdo "Just keep quiet when you stumble onto something, and you’ll get quite the show. I mean, you saw those two. They have their whole little novella going on!"
    #
    # pov "Y-Yeah, no kidding…"
    #
    # rcrdo "Just enjoy it for what it is. And who knows? Maybe one day you’ll be the one getting it on in office space."
    #
    # pov "Well, hopefully when it happens it will be where there aren’t as many people watching."
    #
    # rcrdo "Hah! Let’s hope that’s the case."
    # rcrdo "Well, we’ve been here for long enough, we better get back to our shift."
    # rcrdo "I think we all had our fun for the day."
    #
    # pov "You can say that again…"
    # pov "Oh, I’m [povname] by the way. Thanks for the heads-up on this sort of thing."
    #
    # $ rcrdo.name = "Ricardo"
    # rcrdo "Welcome to working in “TRC”, kid. The name’s Ricardo."
    # rcrdo "Now, if you’ll excuse me, I have to get back to Manufacturing before lunch break starts."
    #
    # #-The Man leaves the restroom-
    #
    # pov "What a nice guy!"
    # pov "Or, well… he would be if he had at least washed his hands before going back to work in Manufacturing…"
    # pov "Wait, did he say his name was Ricardo?"
    # pov "…"
    # pov "Oooooh shit…"
    jump lbl_daily_grind_part2_jobs_menu

label lbl_daily_grind_part2_jobs_end:
    #     #-MID MINIGAME SCENE END-
    #
    # #-Once the player has done the second minigame his shift is over and he has a few closing words with Corrine-
    scene bg officefloor_day with fade
    show pov neutral at left
    show cor smirk_talk at right
    with dissolve
    cor "Hey, Kiddo!"
    cor "You did a great job today."
    show pov embarrassed at left
    show cor neutral_talk at right
    cor "Keep it up like that, and you may just be heading places!"
    show pov neutral_talk at left
    show cor neutral at right
    pov "Thanks, Corrine."
    show pov confused at left
    pov "How did you handle being without Mr. Fistem all day?"
    show pov confused at left
    show cor smirk_talk at right
    cor "There was a very noticeable hole in both my heart and in my purpose in life, but you did at least bring back the spark to get me through the day."
    show pov embarrassed at left
    show cor neutral_talk at right
    cor "God, I can’t wait to see him tomorrow."
    show pov embarrassed_talk at left
    show cor confused at right
    pov "So you are always like this when he has to go to these type of meetings?"
    show pov embarrassed at left
    show cor smirk_talk at right
    cor "Plants need the Sun to grow; I need my Schnookums in order to have the motivation to exist."
    show pov neutral at left
    show cor neutral_talk at right
    cor "Plain and simple."
    show pov embarrassed_talk at left
    show cor smirk at right
    pov "Dang…"
    show pov neutral_talk at left
    pov "Well, as long as you are happy I guess that’s alright."
    show pov neutral at left
    show cor smirk_talk at right
    cor "Awww, thanks, Kiddo!"
    cor "Say, think I could have you asking his little brother if he has said anything about me to him?"
    show pov embarrassed at left
    show cor neutral_talk at right
    cor "He is a coach at your college, right?"
    show pov embarrassed_talk at left
    show cor smirk at right
    pov "That’s a bit of a tall order, Corrine."
    show pov embarrassed at left
    show cor confused_talk at right
    cor "Yeah, you are probably right."
    show pov smirk at left
    show cor smirk_talk at right
    cor "Still had to try asking, you know?"
    show pov embarrassed_talk at left
    show cor smirk at right
    pov "R-Right, well if that’s all, I should head home."
    show pov neutral at left
    show cor neutral_talk at right
    cor "See you tomorrow, Kiddo!"
    show pov embarrassed at left
    cor "Just two more days of this, and we won’t need you as often anymore."
    show pov neutral at left
    show cor embarrassed_talk at right
    cor "But seriously speaking, I think you are being a huge help, honest."
    show pov neutral_talk at left
    show cor embarrassed at right
    pov "Thanks, Corrine. I appreciate that."
    pov "Well, see you tomorrow."
    show pov neutral at left
    show cor neutral_talk at right
    cor "If you by chance see my Schnookums, tell him I love him!"

    #-Corrine’s smile turns scary-
    show pov embarrassed at left
    show cor bored_talk at right
    cor "And if you see him with another woman, tell him I’ll KILL him!"
    show pov embarrassed_talk at left
    show cor smirk at right
    pov "R-Right, yes, OK, bye!"
    show pov embarrassed at right with ease
    with hpunch
    hide pov with dissolve

    #-MC dashes out of there before Corrine can say anything else-

    #=SCENE ENDS=

    $ officejobs_complete = 0
    $ officejobs_copymachine = 0
    $ officejobs_coffeerun = 0
    $ officejobs_emailproofread = 0

    $ gtime = 2
    $ main_story = 102.9

    scene black with fade
    jump lbl_elevator_night

    #=SCENE ENDS=
