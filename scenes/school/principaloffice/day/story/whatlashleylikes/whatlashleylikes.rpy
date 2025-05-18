label lbl_what_lashley_likes:
    ##-This scene takes place a few days after the previous one, once entering Lashley's office after school-
    #scene bg whatlashleylikes_temp1
    #with fade
    ##-You enter Lashley's office to see her looking upset at several objects on her desk, varying from magazines, pictures and even small toys-
    ##"Developer Note: The art assets are a WIP, faces, actions, and lipsyncing are yet to be added."
    scene bg whatlashleylikes_look_down_sad with fade
    pov "Uhh… Sorry, is this a bad time?"
    scene bg whatlashleylikes_confused_talk
    pri "Oh?"
    scene bg whatlashleylikes_shocked_talk
    pri "Ah, hello, [povname]!"
    scene bg whatlashleylikes_embarrassed_talk
    pri "Not at all! Come in, sit!"

    ##-The Mc sits on the chairs in front of her desk-
    scene bg whatlashleylikes_embarrassed with fade
    pov "I… should really knock when I visit, huh?"
    scene bg whatlashleylikes_sad_talk
    pri "I have a policy of open doors when in class hours."
    scene bg whatlashleylikes_embarrassed_talk
    pri "If a student needs me, then my door is always open; knock or not. It's not like I have anything to hide."
    scene bg whatlashleylikes_sad_talk
    pri "… But that being said, I do advise you to knock on other people's door before you enter. It shows good manners."
    scene bg whatlashleylikes_sad
    pov "Noted."
    scene bg whatlashleylikes_neutral_talk
    pri "Good! So, how are you doing this fine day? Did you have a good day in your classes?"
    scene bg whatlashleylikes_neutral
    pov "Yeah, I did. Um…"
    pov "I caught you at a bad time or…?"
    scene bg whatlashleylikes_confused_talk
    pri "Oh, you mean because of all of this?"
    scene bg whatlashleylikes_neutral_talk
    pri "Not at all! In fact, I made quite an advancement towards one of my bigger offenders."
    scene bg whatlashleylikes_smirk_talk
    pri "I almost feel like celebrating!"
    scene bg whatlashleylikes_smirk
    pov "Director Lashley's on the case, huh?"
    scene bg whatlashleylikes_neutral_talk
    pri "Quite so! And I'm so close to catching them."
    scene bg whatlashleylikes_shocked
    pov "You haven’t?"
    pov "I mean, one would assume you have; with all of this stuff laying around."
    scene bg whatlashleylikes_angry_talk
    pri "Oh no, this is only the tip of the iceberg."
    pri "A student has made quite a profit from selling smut within the university walls."
    pri "It started small with the odd magazine here and there, but now it's evolved through the years, into… Well, all of this."
    scene bg whatlashleylikes_shocked_talk
    pri "Toys, novels, starter kits into BDSM, fetish specific magazines and videos, different kinds of textured lubricant, edible underwear."
    pri "Even different types of flavored condoms!"
    scene bg whatlashleylikes_neutral_talk
    pri "Although, I’ll have to admit that I’m relieved to know those and regular condoms seem to be the items that get passed around and sold more often."
    pri "It’s a relief to know the students are aware of the dangers of unprotected sex and are taking the precautions seriously."
    scene bg whatlashleylikes_embarrassed
    pov "'Red Ball-Gag Diaries', 'Tales from the Gloryhole Stall Part IV: A New Hope', 'CBT for Beginners', 'The Sex Toys that Made Us'..."
    pov "…"
    pov "The whole saga of “The Cock-Ring” horror porn movies… I didn't even know horror porn was a thing…"
    scene bg whatlashleylikes_embarrassed_talk
    pri "The things I have seen some of you kids are into nowadays has likely scarred me for life."
    scene bg whatlashleylikes_sad
    pov "I'm so sorry."
    scene bg whatlashleylikes_sad_talk
    pri "I don't blame you, I don't even blame the students. It's a slippery slope of temptations and once you slip, it's really hard to go anywhere but down."
    scene bg whatlashleylikes_neutral_talk
    pri "So any advancement to catch this student and end his market is a success I celebrate."
    scene bg whatlashleylikes_neutral
    pov "How long has this been going on?"
    scene bg whatlashleylikes_sad_talk
    pri "Pretty much since I took position as the administrator."
    pri "Just when I think I got rid of the problem when my suspect graduates; a new generation comes in, and it starts all over again."
    scene bg whatlashleylikes_sad
    pov "At least it keeps you occupied."
    scene bg whatlashleylikes_neutral_talk
    pri "That it does."
    scene bg whatlashleylikes_neutral
    pov "Still, this is a lot of stuff! How did you find all of this?"
    scene bg whatlashleylikes_smirk_talk
    pri "For all that talk some of you kids have about not snitching, you would be surprised how easy it is to make you kids talk sometimes."
    pri "I just had to threaten with calling some parents and I ended up with enough information to find this stash."
    scene bg whatlashleylikes_neutral_talk
    pri "The student was using one of the unused lockers to hide away all this merchandise, to then sell it later."
    scene bg whatlashleylikes_neutral
    pov "Sounds like a lot of work just to sell porn."
    scene bg whatlashleylikes_confused_talk
    pri "I am at least 35%% sure that this volume of sales, are in part just to upset me."
    pri "Some weird way to get back at me or the rules I have in place."
    scene bg whatlashleylikes_confused
    pov "Smells like teen spirit, I guess."
    scene bg whatlashleylikes_sad_talk
    pri "Better than drugs, I suppose."
    pri "I mean, just look at all this stuff!"
    pri "It's concerning, all the varieties of smut you find nowadays!"
    pri "I don’t know what is the problem with your generation but I find myself more and more concerned with the future of humanity, every day."

    ##-If Intelligence is 12 or higher-
    if skill_int >= 5:
        $ renpy.notify("You used 5 Intelligence Points")
        $ skill_int -= 5
        scene bg whatlashleylikes_shocked
        pov "Internet makes it easy for all kind of freaks to share their particular kinks."
        pov "Gather enough, and it becomes a trend - and from that trend you have a market."
        pov "Then you have a bunch of hungry businessmen preying on that market of perverts and because their kink is so niche, they’ll be willing to pay even large amounts of money in order to consume it."
        pov "The vicious cycle of Capitalism."

        $ add_points("principallashley_points",1)
        scene bg whatlashleylikes_neutral_talk
        pri "Well, someone has been paying attention during their business class!"
        scene bg whatlashleylikes_neutral
        pov "You did tell me to focus on my grades, after all."
        scene bg whatlashleylikes_neutral_talk
        pri "I’m happy to see you followed my advice. I’m impressed!"

    scene bg whatlashleylikes_neutral
    pov "So, I assume you found something concerning on this bust of yours?"
    scene bg whatlashleylikes_shocked_talk
    pri "Too many things related to having sex with Dragons and Dinosaurs, as of late."
    pri "To the point, it almost makes me miss the times the trend was to just have sex with their moms, sisters or videogame girls."
    scene bg whatlashleylikes_confused
    pov "Ehhh… I wouldn’t say the times have changed that much."
    scene bg whatlashleylikes_confused_talk
    pri "I haven’t even finished sorting through all this stuff…"
    pri "A single movie is already around an hour long - not to mention all the articles in the magazines!"
    pri "I don’t understand why they make this content so long. From what I know, the majority of people only see this stuff for around 5 minutes before tossing it away anyway."
    scene bg whatlashleylikes_confused
    pov "Not going to deny the truth in that…"
    scene bg whatlashleylikes_shocked
    pov "Wait?? When you sort this stuff, you actually sit and watch all of it?"
    scene bg whatlashleylikes_embarrassed_talk
    pri "I make sure to do my research and then work out the misconceptions of the porn they consume with them, during detention."
    scene bg whatlashleylikes_embarrassed
    pov "And it doesn’t ever… um…"
    scene bg whatlashleylikes_confused_talk
    pri "What?"
    scene bg whatlashleylikes_confused
    pov "Y-You know, all that porn - something surely has to resonate and…"
    scene bg whatlashleylikes_smirk_talk
    pri "You’re asking if it ever “Heats up my engine” as you kids say?"
    scene bg whatlashleylikes_smirk
    pov "I-I’m sorry, I shouldn’t have, I-"
    scene bg whatlashleylikes_smirk_talk
    pri "It’s okay, [povname]."
    pri "While it is a very personal question - and I advise you not to ask it so easily to people - I guess I cannot fault you for being curious after the way I presented it."
    scene bg whatlashleylikes_sad_talk
    pri "Sex without any love or feeling isn’t something I find appealing."
    scene bg whatlashleylikes_sad
    pov "Is that so?"
    scene bg whatlashleylikes_sad_talk
    pri "It’s just the way I was raised, I suppose."
    pri "Not only due to my religious background, but my father made it very clear to me that sex without purpose is just a waste of time."
    pri "I already get too many looks and disgusting comments on the street because of my figure. So seeing strangers humping away for an hour really does nothing for me."
    scene bg whatlashleylikes_neutral_talk
    pri "If I have sex, then I want it to be with someone I care about and they care for me in return."
    pri "Plus, an opportunity for marriage later on, would help make things even better for me."
    scene bg whatlashleylikes_neutral
    pov "Didn’t see you as the type to still think about wedding and so."
    scene bg whatlashleylikes_neutral_talk
    pri "I’ll admit, I gave a bit too much time to my career on my younger days, but it’s every little girl’s dream to one day wear a white dress, you know?"
    scene bg whatlashleylikes_neutral
    pov "That’s fair enough."
    pov "Thanks for sharing with me, I’m honestly shocked I didn’t offend you with the question."
    scene bg whatlashleylikes_smirk_talk
    pri "I was the one who opened up the topic, it’s only natural for you to be curious when I have a pile of pornography on my desk."
    scene bg whatlashleylikes_neutral_talk
    pri "But still, I’ve told you before [povname]."
    pri "I really like talking with you."
    pri "I don’t know why but I’ve got this… This feeling around you."
    pri "A warm feeling and I just find myself talking and talking here."
    pri "I enjoy your company."
    scene bg whatlashleylikes_neutral

    menu:
        "The feeling is mutual.":
            pov "The feeling is very much Mutual, Director Lashley."
            pov "You are just a joy to be around."

            $ add_points("principallashley_points",2)
            scene bg whatlashleylikes_smirk_talk
            pri "You are so sweet as always, [povname]."
            scene bg whatlashleylikes_smirk
            pov "You give me a good reason to be."

            if skill_cha >= 5:
                $ renpy.notify("You used 5 Charisma Points")
                $ skill_cha -= 5
                scene bg whatlashleylikes_embarrassed
                pov "It's easy to be sweet when you are in the presence of a beautiful woman."
                scene bg whatlashleylikes_embarrassed_talk
                pri "I-I, Um…!"
                pri "G-Goodness, quite the silver tongued devil, aren't you?"
                scene bg whatlashleylikes_embarrassed
                pov "Really?"
                pov "Here I was afraid, it was too cheesy of a line."
                scene bg whatlashleylikes_smirk_talk
                pri "W-Well, sometimes “cheesy” is good too."
                $ add_points("principallashley_points",2)

        "Why is that?":
            scene bg whatlashleylikes_shocked
            pov "Pardon the question, but I'm curious. Why do you find it so enjoyable?"
            pov "I mean, I don't really do that much to gain your favor, do I?"
            scene bg whatlashleylikes_neutral_talk
            pri "It's the fact you take the time to come talk to me that makes all the difference."
            pri "It makes me feel appreciated."
            pri "Any woman likes a kind man to give them attention."
            scene bg whatlashleylikes_neutral
            pov "I know a lot of people stuck in the friendzone who would disagree with you."

    scene bg whatlashleylikes_bored_talk
    pri "Nevertheless."
    pri "As much as I enjoy our time together, I really should be going back to work."
    pri "Far too much smut to look through."
    scene bg whatlashleylikes_bored
    pov "I better not take any more of your time, then."
    scene bg whatlashleylikes_neutral_talk
    pri "Thanks for understanding, [povname]."
    pri "You are welcome to come back some other time."
    pri "My door is always open, so don’t be a stranger!"
    scene bg whatlashleylikes_neutral
    pov "I’ll keep that in mind."
    pov "See you later, Director Lashley."

    ##-The Mc Leaves-
    scene bg whatlashleylikes_neutral_talk with fade
    pri "He is such a nice young man…"
    scene bg whatlashleylikes_confused_talk
    pri "Alright, lets see…"
    scene bg whatlashleylikes_look_mag_confused




    pri "{i}Let’s start with the magazines.{/i}"
    scene bg whatlashleylikes_look_mag_angry
    pri "{i}I swear, if I find one of those upside down books with pictures of girls with dicks, I'm going to-{/i}"

    ##-She stops when she spots an erotic magazine for women-
    #show bg whatlashleylikes_temp2
    scene bg whatlashleylikes_look_mag_embarrassed
    pri "{i}Huh, don’t see a lot of this often…{/i}"
    pri "{i}The guy in the cover… He seems… Familiar?{/i}"

    ##-Scene shows Lashley admiring the magazine-
    scene bg whatlashleylikes_look_mag_horny
    pri "{i}W-Well… I guess I shall start with this one, then…{/i}"

    ##-She opens the magazine and starts blushing like crazy-

    ##-Scene ends with the close up of the magazine’s cover where a character that looks like the MC is posing, the magazine’s called something like “Sinful Girl”, “Earthly Desires”, “Delectable Smut” or something else ironic. In the cover there could also be easter eggs or something in the articles."-

    $ principallashley_path = 4

    jump lbl_schoolhallway2_day_setup
