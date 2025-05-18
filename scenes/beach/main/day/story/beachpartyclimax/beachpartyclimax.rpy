## Beach Party Climax
label lbl_beach_party_climax:
    #-Scene takes place at another area of the beach where people are dancing
    # all around Effie and Mc as they too dance happily-

    #-Fade in from black to indicate the passage of time-

    scene black
    with fade
    $ renpy.pause()
    "After spending a few hours dancing and drinking with Effie..."

    #-Graphic of Mc and Effie Dancing together to some upbeat dance music-
    ## CG

    scene bg beachmain_nightparty
    show pov neutral at left
    show eff neutral_talk at right
    with dissolve
    eff "God, this is what I needed!"
    eff "Just some good music and a chill vibe, to get out of my funk!"

    show pov smirk_talk
    show eff neutral
    pov "Tell me about it! Feels nice to just let loose after a while!"
    pov "Gotta say, I’ve never seen you dance like this!"
    
    show pov smirk
    show eff smirk_talk
    eff "Really? Because I’ve certainly seen YOU dance like that before~"

    show pov smirk_talk
    show eff smirk
    pov "Oh really? Where?"

    show pov shocked
    show eff smirk_talk
    eff "In the night club! Sometimes when you get out on your own and decide you wanna try and bust a move~"
    eff "Been fun to see you go for wilder and wilder dances!"

    show pov embarrassed_talk
    show eff smirk
    pov "Please tell me you didn’t see the times I made a fool of myself..."

    show pov embarrassed
    show eff smirk_talk
    eff "And the times you totally rocked it too!"
    eff "Though it’s always more fun when you screw up and leave the dance club all awkwardly~"

    show pov embarrassed_talk
    show eff smirk
    pov "God, please don’t remind me about it..."

    show pov shocked
    show eff confused_talk
    eff "Hey, I’ve always wanted to ask, but who’s the one who kisses your cheek afterwards?"

    show pov neutral_talk
    show eff smirk
    pov "Depends on the night!"
    pov "Sometimes it’s one of our friends who happened to be there, or even Zariah on the booth."
    pov "Other times, it's some stranger, and even a few times it’s a grandma who was just partying out of nowhere!"

    show pov smirk
    show eff smirk_talk
    eff "No way! You are out on the dance floor getting kissed by grandma!"

    show pov smirk_talk
    show eff smirk
    pov "Pretty sure one night, I got kissed by a guy in drag."

    show pov smirk
    show eff smirk_talk
    eff "You know what? Good for him, for going for it - and better for you for not being weird about it!"

    show pov embarrassed_talk
    show eff confused
    pov "So hey, when you wanna head back?"
    show eff neutral
    pov "I know we have a curfew and all, but maybe if we return a bit earlier than planned, your dad won’t be as big of an A-Hole later on?"

    show pov embarrassed
    show eff embarrassed_talk
    eff "That’s not a bad idea actually! You’d really be okay with taking me home early? The party’s just getting good!"
    
    show pov smirk_talk
    show eff smirk
    pov "Heh, I think about it as a long term investment."
    pov "Maybe if we get your dad to like me; by following his rules, he’ll be more lenient about them and give us a bit of a break?"

    show pov shocked
    show eff smirk_talk
    eff "Oh~ are you saying that you see us as something long term?"

    show pov embarrassed_talk
    show eff smirk
    pov "W-Well, I’d certainly like to think so."
    pov "I really like you, after all."

    show pov embarrassed
    show eff smirk_talk
    eff "Hehehe, I’m glad you see it that way."
    show eff embarrassed_talk
    eff "Honestly, I’m open for that too."
    eff "But it makes me really happy to know that, not only you do too, but you are willing to put in the work for it."
    eff "How about one more drink and song - and we head out of here?"

    show pov smirk_talk
    show eff neutral
    pov "I’m down!"

    show pov neutral
    show eff neutral_talk
    eff "This one's on me, you want the same?"

    show pov neutral_talk
    show eff neutral
    pov "I'll have what you have if you're shouting."

    show pov neutral
    show eff smirk_talk
    eff "Gotcha! I'll be right back before you can say 'jiffy'."

    hide eff
    with dissolve


    #-Suddenly a drunk guy collides with Effie, spilling his drink all over her-
    show pov shocked
    with hpunch
    eff "HEY!"
    eff "WHAT THE FUCK?!"
    eff "WATCH WHERE YOU'RE GOING, ASSHOLE!"

    "Drunk Guy" "Ayo, sorry girl-brah! I didn't see you there."

    show pov shocked_talk
    pov "Effie?! What happened?!"

    hide pov
    with dissolve

    eff "THIS ASSHOLE RAN INTO ME AND SPILT HIS DRINK ALL OVER ME!"

    "Drunk Guy" "Ayo, shit! Sorry, girl-bruv. I swear, you're like really short and I'm really- fuckin' high right now..."

    eff "UGH, I'M FUCKING DRENCHED! WHAT EVEN IS THIS?!"

    "Drunk Guy" "It’s just beer, girl-dude. I’m sorry and shit."

    eff "Great, just fucking fantastic! Now I need to dry this off and change. Thanks a lot!"

    pov "Get the fuck outta here, dude. Before I break that same bottle over your head."

    "Drunk Guy" "Yo, yo. Alright. I'm outtie. Not cool, bro. Sorry, girl-bro. Seriously, my B."

    pov "You okay, Effie?"

    eff "Ugh, yeah. Just soaking wet - and not in a fun way..."
    eff "[povname], come with me to the changing rooms."

    pov "Yeah, of course..."

    "Guy" "Girl-gude, again, I’m super sorry!"

    eff "Yeah, yeah, whatever... Just fuck off already."

    scene black 
    with fade
    $ renpy.pause()
    #-Fade to black and back into changing area to indicate transition-

    

    eff "..."

    pov "Here you go."

    scene bg beachchangeroom_blue_night
    show pov embarrassed
    show effto sad_talk
    with fade
    eff "Thanks for the napkins- they don't have a towel or something?"

    show pov embarrassed_talk
    show effto sad
    pov "Not at the bar, a clean one at least."

    show pov embarrassed
    show effto angry_talk
    eff "Ugh, I still can’t believe some drunk idiot spilled his beer all over me!"
    eff "And it’s not even good beer! It’s that piss-tasting cheap one, you buy in bulk!"

    show pov embarrassed_talk
    show effto sad
    pov "Need me to get more napkins? I already texted Violette, and she’s on her way with a towel."

    show pov embarrassed
    show effto sad_talk
    eff "God, even now, she’s a saint to the rescue..."

    show pov sad_talk
    show effto sad
    pov "You okay?"

    show pov embarrassed
    show effto embarrassed_talk
    eff "Yeah... Funnily enough, this ain't the first time I have stinked of cheap beer, after a moron poured it on me."
    eff "And knowing the parties I go to, it definitely won’t be the last."
    eff "Thanks for standing up for me, [povname]."

    show pov neutral_talk
    show effto embarrassed
    pov "Don’t mention it."
    pov "I was ready to throw hands."
    show pov confused_talk
    pov "Anyway, you all dried up?"

    show pov sad
    show effto sad_talk
    eff "Mostly, but my top is ruined..."
    eff "Sorry, [povname]. I was hoping we could fool around before heading home, but I’d prefer to just head home and have a shower now..."
    eff "I'm not feeling that sexy right now."

    show pov embarrassed_talk
    show effto embarrassed
    pov "Totally understandable. Don’t worry about it."
    pov "I still had fun with you today - and that’s all that matters."

    show pov confused
    show effto embarrassed_talk
    eff "You are so sweet. Other guys would have already planned to bail on me, and hook up with someone else at the party."

    show pov smirk_talk
    show effto embarrassed
    pov "Hey, you know I wouldn’t do that."

    show pov embarrassed
    show effto embarrassed_talk
    eff "I do... That’s one of the reasons why I like you as much as I do."
    eff "Care to help me wipe off my back? I don't know how it got there but it's there and I feel it."

    show pov neutral_talk
    show effto embarrassed
    pov "Yeah, sure thing! Let me just get closer and-"

    show pov shocked
    show effto shocked
    with hpunch
    idk "KEEP YOUR HANDS OFF MY DAUGHTER YOU GODDAMNED HOOLIGAN!!!"

    show pov confused_talk
    show effto sad
    pov "What the-?!"

    show pov confused
    show effto sad_talk
    eff "Oh god, please no..."


    #-Scene moves back to outside the changing booths with Effie, her Dad and
    # our MC appearing into it as well-

label lbl_test111111:

    scene bg beachmain_nightparty
    show pov shocked at left
    show effto angry flip at Position(xpos=600)
    show effdad angry_talk at right
    with dissolve
    effdad "EFFIE, COVER YOURSELF, FOR GOD’S SAKE! WE ARE LEAVING!"

    show pov shocked
    show effto angry_talk flip
    show effdad angry
    eff "Dad! What the actual hell are you doing here?!"

    show pov shocked
    show effto angry flip
    show effdad angry_talk
    effdad "I CAME OVER TO CHECK ON YOU, TO MAKE SURE YOU ARE KEEPING YOUR PROMISES - AND WHAT DO I FIND?!"
    effdad "YOU, HALF-NAKED, WITH THIS DUMBASS, INSIDE OF A PRIVATE BOOTH AND REEKING OF NICE BOOZE?!"

    show pov shocked
    show effto sad_talk flip
    show effdad angry
    eff "Dad, calm the fuck down! I swear that all of this is not what you think!"

    show pov embarrassed_talk
    show effto angry flip
    show effdad angry
    pov "R-Right, sir! I promise you I wasn’t trying anything!"
    pov "Some guy accidentally poured beer all over Effie and-"

    show pov sad
    show effto angry flip
    show effdad angry_talk
    effdad "DON’T YOU COME OVER TO ME WITH YOUR LAME EXCUSES, BOY! YOU THINK I DON’T KNOW WHAT HAPPENS IN THOSE BOOTHS, HERE ON THE BEACH?!"

    show pov sad
    show effto angry flip
    show effdad angry
    "Party Guy 1" " Ayo, what's with grandpa blowing a gasket?"

    show pov sad
    show effto angry flip
    show effdad angry_talk
    effdad "EFFIE, WHATEVER THE HELL YOU WERE THINKING OF DOING WITH THIS BOY, YOU BETTER FORGET ABOUT, FOR THE REST OF YOUR LIFE!"

    show pov sad
    show effto angry flip
    show effdad angry
    "Party Guy 2" " I think he caught his daughter offering free BJ’s in the booth or something."

    "Party Guy 1" " Yo, for real?! Dude, why didn’t anyone tell me sooner?!"

    show pov sad
    show effto angry flip
    show effdad angry_talk
    effdad "I FORBID YOU FROM EVER SEEING HIM AGAIN!"

    show pov sad
    show effto angry flip
    show effdad angry
    "Party Girl 1" " Oh my gawd, is that Effie?"

    "Party Girl 2" " Was she really offering free rides in the booth?!"

    show pov sad
    show effto embarrassed_talk flip
    show effdad angry
    eff "D-Dad! You are making a huge scene! Will you calm down before you make weird rumors come out?!"

    show pov sad
    show effto angry flip
    show effdad angry
    "Party Girl 3" " That’s not all, I heard she was even letting dudes pay to double or triple team her, what a skank!"

    show pov sad
    show effto angry flip
    show effdad angry_talk
    effdad "I CANNOT BELIEVE THIS, EFFIE! THE ONE TIME I DECIDE NOT TO DO A PROPER BACKGROUND CHECK, AND THIS IS IMMEDIATELY WHAT YOU DO?!"
    show pov shocked
    effdad "OPENING YOUR LEGS TO THE FIRST JACKASS THAT SPEAKS NICE TO YOU?!"
    effdad "I DIDN’T RAISE YOU TO BECOME LIKE THIS!"
    effdad "I DIDN’T RAISE YOU TO BECOME A WHORE!"

    show pov shocked
    show effto angry_talk flip
    show effdad angry
    eff "WHAT DID YOU JUST CALL ME?!"

    show pov embarrassed_talk
    show effto angry flip
    show effdad angry
    pov "A-Alright, let’s not try and say anymore of what we might regret here and-"


    #-Violette arrives on scene-
    # "Violette shows up to see what is going on." #############


    show pov sad
    show effto angry flip
    show effdad angry
    show vioc confused_talk
    with dissolve
    vio "Guys, I’m back with the towel! What did I-"

    show pov shocked
    show effto angry flip
    show effdad angry_talk
    show vioc angry
    effdad "DO YOU THINK THIS IS WHAT YOUR MOTHER WOULD WANT TO SEE?!"
    effdad "YOU ARE SPITTING ON HER NAME, EFFIE! YOU HAVE NO IDEA JUST HOW DISAPPOINTED SHE MUST BE IN YOU!"

    show pov shocked
    show effto angry_talk flip
    show effdad angry
    show vioc angry
    eff "HOW DARE YOU BRING MOM INTO THIS?!"

    show effto angry flip
    show effdad angry_talk
    effdad "WHAT ELSE DO I HAVE LEFT TO TRY, EFFIE?!"
    effdad "EVERY TIME I GIVE YOU THE SLIGHTEST BIT OF FREEDOM, YOU STAB ME IN THE BACK LIKE THIS!"

    show effto angry_talk flip
    show effdad angry
    eff "FREEDOM?! YOU CALL FOLLOWING ME EVERYWHERE I GO FREEDOM?!"
    eff "YOU CALL PUTTING A GPS IN MY PHONE AND MONITORING MY EVERY MOOD, FREEDOM?!"
    eff "YOU ARE WAITING AT HOME WITH AN ACTUAL BREATHALYZER TO USE ON ME, FOR FUCK’S SAKE!"
    eff "DO YOU THINK SHE WOULD BE HAPPY KNOWING YOU ARE DOING ALL OF THIS BULLSHIT?!"
    eff "YOU ARE MAKING MY LIFE MISERABLE, WITH EVERYTHING YOU DO. AND YOU DON’T EVEN HAVE THE DECENCY TO ACKNOWLEDGE IT!"

    show effto angry flip
    show effdad angry_talk
    effdad "I DO ALL OF THIS, BECAUSE I’M TRYING TO PROTECT YOU!"

    show pov shocked
    show effto angry flip
    show effdad angry_talk
    show vioc angry
    eff "YOU ARE DOING THIS BECAUSE YOU ARE A CONTROL FREAK, WHO I HAVE TO CONSTANTLY WRESTLE THE CONTROL OF MY LIFE WITH!"

    show pov shocked
    show effto angry flip
    show effdad angry
    show vioc angry_talk
    vio "OK, OK. Let’s just stop this, take this family matter off my beach!"
    vio "This is a party for God's sake, not a freaking TV therapist show!"
    
    show pov embarrassed_talk
    show effto angry flip
    show effdad angry
    show vioc angry
    pov "R-Right, no need to escalate things. Let’s all just go home and-"

    show pov shocked
    show effto angry flip
    show effdad angry
    show vioc angry_talk
    vio "I want you both out of here!"

    show effto angry flip
    show effdad angry_talk
    effdad "YOU KNOW AS WELL AS I DO, THAT YOUR MOTHER WOULD BACK ME UP ON THIS!"

    show pov shocked
    show effto angry_talk flip
    show effdad angry
    show vioc angry
    eff "OH, DO YOU REALLY THINK SO?!"
    eff "SHE’S GONE, DAD! SOMETIMES I FEEL LIKE YOU KEEP TRYING TO LOCK ME UP SO I DON’T DO THE SAME!"

    show pov shocked
    show effto angry flip
    show effdad angry_talk
    show vioc angry
    effdad "AND SOMETIMES YOU MAKE ME WISH SHE TOOK YOU WITH HER!"

    show effdad angry
    "Everyone" "*{i}GASP!{/i}*"

    "Party Girl 2" "Oh no, he didn’t!"

    show effdad bored
    effdad "..."
    show effdad sad_talk
    effdad "E-Effie, I am so sorry, that came out, in the heat of the moment, and-"

    show effto angry_talk flip
    show effdad sad
    eff "No, it’s okay..."
    eff "Cause I always wish she actually did..."

    #-Effie leaves the scene
    hide effto
    with dissolve
    $ renpy.pause()

    show effdad sad_talk
    effdad "W-Wait, no. Effie, I-!"

    show effdad sad
    show vioc bored_talk
    vio "Alright, I think you dug yourself a deep enough hole this time."
    vio "I think it’s time you go home."
    show pov embarrassed
    show vioc embarrassed_talk
    vio "[povname], can you go check up on her?"

    show pov embarrassed_talk
    show vioc embarrassed
    show effdad shocked
    pov "Yeah, of course."

    show pov embarrassed
    show vioc embarrassed_talk
    vio "Good. Go quick."

    show vioc embarrassed
    pov "{i}I think Effie headed towards the park...{/i}"


    scene black
    with fade
    $ renpy.pause()
    "At the park..."

    $ effie_path = 19
    $ gtime = 2

    jump lbl_effie_breaks_down
