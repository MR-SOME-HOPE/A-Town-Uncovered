#[Beach, afternoon - “Investigations_Jaiden”  - main_story =84-G]

#-The Mc approaches Jaiden as she is busy working out on the beach-
label lbl_investigations_jaiden:
    default investigations_jaiden = 0
    if investigations_jaiden != 0:
        show btn schoolgym_day_jaiden_idle
        pov "{i}I don't want to get into it with her right now.{/i}"
        if gtime == 0:
            jump lbl_schoolgym_day_setup
        else:
            jump lbl_schoolyard_day_setup

    #if gtime == 0:
    #    scene bg schoolgym_day
    #else:
    #    scene bg schoolyard_day
    show btn schoolgym_day_jaiden_idle
    $ renpy.pause(0.001)


    show pov embarrassed_talk at left
    with dissolve
    show jai smirk at right
    hide btn schoolgym_day_jaiden_idle
    with dissolve
    pov "Hey Jaiden?"
    show pov embarrassed at left
    show jai smirk_talk at right
    jai "Afternoon, Maggot!"
    jai "You came just in time."
    show pov confused_talk at left
    show jai smirk at right
    pov "I did?"
    show pov confused at left
    show jai neutral_talk at right
    jai "Certainly, do me a favour and take this stopwatch, I need someone to help me check on my time."
    show jai bored_talk at right
    jai "Violette usually gives me a hand with it but she is busy with lifeguard duties right now."
    jai "I’m working leg today and I start with a good laps on beach sand."
    show pov confused_talk at left
    show jai smirk at right
    pov "Training for something specific or do you just do this for fun?"
    show pov confused at left
    show jai smirk_talk at right
    jai "A girl has to be on top of her game in dangerous times."
    show pov embarrassed_talk at left
    jai "If some sneaky fuck is dumb and suicidal enough to try and enter my house in the middle of the night, I have to make sure I’m at my best to help them meet god faster."
    show pov embarrassed_talk at left
    show jai smirk at right
    pov "Makes sense you and your family would be more active about all this."
    show pov embarrassed at left
    show jai embarrassed_talk at right
    jai "It’s the sort of situation my father has us have drills for."
    show pov shocked at left
    show jai bored_talk at right
    jai "He is planning to form a neighborhood watch even."
    show jai smirk_talk at right
    jai "Meanwhile, I’ll be one of the instructors for the community funded self defense class."
    show pov confused_talk at left
    show jai bored at right
    pov "I did hear about it, but I wasn’t aware you were going to be an instructor."
    show pov confused at left
    show jai bored_talk at right
    jai "Well, more of an assistant instructor, black belt or not, I don’t have the proper permits to teach the class myself."
    show jai neutral_talk at right
    jai "Still, if you join in, I’ll give extra special attention to you."
    show pov embarrassed_talk at left
    show jai neutral at right
    pov "Uhhh… Not that I don’t appreciate it, but what’s the reason for it?"
    show pov confused at left
    show jai smirk_talk at right
    jai "You are kidding, right?"

    ##-The following IF statements vary depending on the Strength stat of the Mc-
    if skill_strmax <= 7:
    ##-If Strength 0 to 7-
        show pov shocked at left
        show jai smirk_talk at right
        jai "You look like I could bend you can’t even lift a full pickle jar, much less even attempt to open it!"
        show pov bored at left
        show jai bored_talk at right
        jai "I think foam cups have more muscle mass than you do."
        show jai smirk_talk at right
        jai "Do you even know what lift is, Maggot?"
        show pov bored_talk at left
        show jai smirk at right
        pov "Wow, exactly what I was hoping to hear today when I woke up."
        show pov bored at left
        show jai smirk_talk at right
        jai "Giving you the hard truth so you can start a change in your life, Maggot!"
        show jai shocked_talk at right
        jai "I feel like I could bench press 5 of you and still not have enough weight for a good workout."
        show jai neutral_talk at right
        jai "I know body positivity is all the rage and it's important and whatever."
        show jai smirk_talk at right
        jai "But you ain’t gonna last long in a kidnapping situation if it looks like I could break your spine from a pat on your back."
        show pov bored_talk at left
        show jai smirk at right
        pov "To be fair, you have quite the heavy hand."
        show pov confused at left
        show jai smirk_talk at right
        jai "Thanks! But I have more strength in my legs and thighs."
        show jai shocked_talk at right
        jai "Lot’s of kickboxing and squats, I can actually crush a watermelon with them."
        show jai neutral_talk at right
        jai "Tend to gather quite the crowd of guys when I do that."
        show pov bored_talk at left
        show jai neutral at right
        pov "Can definitely see why…"
        show pov shocked at left
        show jai shocked_talk at right
        jai "So!"
        show pov embarrassed at left
        show jai neutral_talk at right
        jai "I plan on whipping you into shape and giving you a good routine so even a little man like you can stand a chance and defend yourself if needed!"
        show pov confused_talk at left
        show jai smirk at right
        pov "Little man?!"
        show pov bored at left
        show jai smirk_talk at right
        jai "Willing to put it to the test? If you can pin me down, I won’t call you that~"
        show pov embarrassed_talk at left
        show jai confused at right
        pov "U-Umm… I’ll pass for now."
        show pov embarrassed at left
        show jai smirk_talk at right
        jai "Thought so, but you are lucky I prefer calling you Maggot for now."
        show pov bored_talk at left
        show jai smirk at right
        pov "Not sure if that’s much better…"
        show pov embarrassed at left
        show jai smirk_talk at right
        jai "So, what do you say?"
        show jai neutral_talk at right
        jai "Willing to give it a shot?"

        ##=RESULT END=

    elif 8 >= skill_strmax <= 15:
    ##-If Strength 8 to 15-
        show pov bored at left
        show jai bored_talk at right
        jai "You are a fit enough kinda guy, but I doubt you have much technique."
        show jai smirk_talk at right
        jai "I can fix that easily and get you in proper shape."
        show pov smirk_talk at left
        show jai smirk at right
        pov "Why the sudden interest?"
        show pov smirk at left
        show jai shocked_talk at right
        jai "Glad you asked, Maggot!"
        show pov shocked at left
        show jai bored_talk at right
        jai "You see, aside from Violette and Brock, I don’t have a lot of up to the task of being my training partner."
        show pov bored at left
        jai "Violette is always busy with lifeguard duty and Brock has his job at the coffee shop, both of them have close to no time to help me train."
        show jai smirk_talk at right
        jai "So, here comes the neighborhood Maggot getting into shape of his own and I have a gold mine!"
        show jai neutral_talk at right
        jai "Just have to whip you into proper shape some more and I’ll have my perfect sparring partner!"
        show pov bored_talk at left
        show jai neutral at right
        pov "Don’t you mean training partner?"
        show pov bored at left
        show jai neutral_talk at right
        jai "I know what I said."
        show pov bored_talk at left
        show jai neutral at right
        pov "Oh boy…"
        show pov confused at left
        show jai neutral_talk at right
        jai "Still, I really think I can shape you to be the all around gladiator our country’s military is proud for."
        show jai smirk_talk at right
        jai "Plus, I would owe you one and I can assure you that sort of thing can be quite helpful for a Maggot like you."
        show pov confused_talk at left
        show jai neutral at right
        pov "What do you mean?"
        show pov confused at left
        show jai smirk_talk at right
        jai "I’ll leave it up to your imagination. I’m a resourceful gal and you are the type of rookie to constantly get into trouble."
        show pov bored_talk at left
        show jai smirk at right
        pov "Alright, you got me there."
        show pov confused at left
        show jai neutral_talk at right
        jai "So, what do you say?"
        show pov embarrassed at left
        show jai smirk_talk at right
        jai "Willing to give it a shot?"

        ##=RESULT END=


    elif 16 >= skill_strmax <= 20:
    ##-If Strength 16 to 20-
        show pov shocked at left
        show jai smirk_talk at right
        jai "You are ripped!"
        show pov embarrassed at left
        show jai neutral_talk at right
        jai "Exactly what I was looking for!"
        show pov embarrassed_talk at left
        show jai neutral at right
        pov "Uhhh, thanks?"
        show pov embarrassed at left
        show jai neutral_talk at right
        jai "I’ve been dying to find someone around my same fitness level that could really match up with my routine."
        show pov neutral at left
        show jai embarrassed_talk at right
        jai "My usual picks are usually busy with work, so color me surprised when I find out the neighborhood Maggot is one suburban Hercules!"
        show pov embarrassed at left
        show jai smirk_talk at right
        jai "With that kind of attitude you may just advance from Maggot to Worm, you know?"
        show pov embarrassed_talk at left
        show jai smirk at right
        pov "What an honor…"
        show pov embarrassed at left
        show jai neutral_talk at right
        jai "Exactly!"
        show jai smirk_talk at right
        jai "I don’t just ask anyone to train with me you know?"
        show pov embarrassed_talk at left
        show jai smirk at right
        pov "I doubt just anyone can keep up with you, Jaiden."
        show pov embarrassed at left
        show jai embarrassed_talk at right
        jai "That too."
        show pov neutral at left
        show jai shocked_talk at right
        jai "Tell you what, we could also use a good sparring partner for the self defense class."
        show pov confused at left
        show jai neutral_talk at right
        jai "someone the girls could practice a few moves and such."
        show pov embarrassed at left
        show jai smirk_talk at right
        jai "Show them on a live target where to hold and strike proper."
        show pov smirk_talk at left
        show jai neutral at right
        pov "Do I look like a boxing dummy or something?"
        show pov bored at left
        show jai smirk_talk at right
        jai "Don’t be such a baby, Maggot."
        show jai confused_talk at right
        jai "You are not actually going to get hurt, doubt the girls and even some of the guys there could even really do much by themselves against you."
        show pov embarrassed at left
        show jai neutral_talk at right
        jai "It would be mostly quick getaway moves they can practice against actual human weight."
        show jai smirk_talk at right
        jai "It would be really helpful for them, plus you would get paid some cash for your troubles."
        show pov embarrassed_talk at left
        show jai confused at right
        pov "I don’t know, I kind of already have a full plate here and-"
        show pov shocked at left
        show jai shocked_talk at right
        jai "Are you really telling me here you don’t want to rub yourself against a bunch of ladies in yoga pants and sports wear?"
        show pov embarrassed at left
        show jai confused_talk at right
        jai "Having them all over you and on top of you as they practice keeping you down on the ground?"
        show pov bored_talk at left
        show jai smirk at right
        pov "Alright, that does spark my interest a bit."
        show pov embarrassed at left
        show jai smirk_talk at right
        jai "Knew it would, Maggot."
        show pov smirk at left
        show jai confused_talk at right
        jai "So, what do you say?"
        show jai smirk_talk at right
        jai "Willing to give it a shot?"

        ##=RESULT END=

        ##=END=

    ##continue

    show pov embarrassed_talk at left
    show jai smirk at right
    pov "I’ll think about it, thanks for the offer though."
    show pov shocked at left
    show jai smirk_talk at right
    jai "Don’t keep me waiting too long, Maggot."
    show pov embarrassed at left
    show jai bored_talk at right
    jai "Offer is for a limited time only."
    show pov embarrassed_talk at left
    show jai bored at right
    pov "I’ll keep it in mind, I promise."
    show pov embarrassed at left
    show jai smirk_talk at right
    jai "Good!"
    show jai bored_talk at right
    jai "Now keep an eye on the stopwatch, I spent too much time talking already, my muscles are cooling down."
    show pov embarrassed_talk at left
    show jai confused at right
    pov "Actually, before you go."
    show pov confused_talk at left
    show jai shocked at right
    pov "I was hoping that you could tell me if you have noticed anything weird going on at the beach lately?"
    show pov embarrassed at left
    show jai confused_talk at right
    jai "Only thing I have my complete focus on when I’m here is giving my 120%% on my exercise routine."
    show jai bored_talk at right
    jai "That and my power mix."
    show jai embarrassed_talk at right
    jai "You should ask Violette for that kind of stuff."
    show pov embarrassed_talk at left
    show jai confused at right
    pov "I see… Well, thanks anyway, but I really gotta go and-"
    show pov shocked at left
    show jai angry_talk at right
    jai "DID I GIVE YOU PERMISSION TO LEAVE, MAGGOT?!"
    show pov shocked_talk at left
    show jai angry at right
    pov "Gah!"
    show pov embarrassed_talk at left
    pov "N-No sir!"
    show pov embarrassed at left
    show jai angry_talk at right
    jai "JUST FOR THAT, YOU ARE RUNNING MY LAPS WITH ME WHILE KEEPING THE TIME!"
    show jai shocked_talk at right
    jai "AND YOU BETTER KEEP GOOD TRACK OF IT OR WE ARE STARTING RIGHT OVER, I’M FEELING GOOD TODAY AND NOW I ALSO GET TO SMACK A MAGGOT IN SHAPE."
    show pov shocked at left
    show jai angry_talk at right
    jai "DID I MAKE MYSELF CLEAR, YOU MAGGOT?!"
    show pov shocked_talk at left
    show jai smirk at right
    pov "Sir, yes Ma’am!"
    show pov embarrassed at left
    show jai smirk_talk at right
    jai "GOOD, NOW START RUNNING!"

    scene black with fade
    "You and Jaiden spend some quality time together running a few laps on the beach while she constantly calls you maggot and other related species of vermin-"

    ##=SCENE END=

    $ investigations_jaiden = 1

    if gtime == 0:
        jump lbl_schoolgym_day_setup
    else:
        jump lbl_schoolyard_day_setup
