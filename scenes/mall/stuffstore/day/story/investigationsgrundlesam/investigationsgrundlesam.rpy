label lbl_investigations_grundlesam:
    default investigations_grundlesam = 0
    default investigations_grundlesam_choice_chosen_history = False
    default investigations_grundlesam_choice_chosen_mystery = False
    ##-Mc enters Grundle Sam’s store where he is met with his usual brand of weirdness-
    if investigations_grundlesam != 0:
        pov "{i}I've learned all I can here for the moment.{/i}"
        jump lbl_stuffstore_day
    else:
        $ investigations_grundlesam = 1
        show pov shocked at left
        with dissolve
        show sam smirk_talk at right
        with dissolve
        call lbl_stuffstore_counter_check
        sam "Hello there, explorer of the unknown!"
        sam "The mystical totems informed me that I would be seeing you today."
        show pov embarrassed at left
        show sam neutral_talk at right
        sam "You are always welcome in my emporium of the unknown."
        show pov embarrassed_talk at left
        show sam neutral at right
        pov "Uh, thanks Sam."
        show pov confused_talk at left
        pov "Did the totems actually tell you I would be coming?"
        show pov shocked at left
        show sam smirk_talk at right
        sam "{i}*Snort*{/i} I wish!"
        sam "Sadly, the spirits within are not very talkative with me."
        show pov embarrassed at left
        show sam neutral_talk at right
        sam "No, that’s just a line I say when customers come in."
        show sam bored_talk at right
        sam "The whole act helps sell the mysticism."
        show pov confused_talk at left
        show sam smirk at right
        pov "It does?"
        show pov confused at left
        show sam bored_talk at right
        sam "Well, it does for the random kids that come in after getting separated from their parents."
        show sam smirk_talk at right
        sam "The whole occultist vibe of the place attracts them like moths to a flame."
        sam "Every kid believes in the occult to some degree and tends to orbit around places that may have plausible proof around it."
        show pov embarrassed at left
        show sam neutral_talk at right
        sam "I learned a ton of magic tricks and cardistry to keep em entertained until their parents come looking for them!"
        show pov neutral_talk at left
        show sam neutral at right
        pov "That’s quite nice of you!"
        show pov neutral at left
        show sam neutral_talk at right
        sam "Anything to keep the younglings faith in magic and the supernatural for as long as possible!"
        show pov embarrassed at left
        show sam embarrassed_talk at right
        sam "I just wish it also meant an increase in sales from time to time."
        show sam shocked_talk at right
        sam "The parents appreciate it though!"
        show pov neutral at left
        show sam embarrassed_talk at right
        sam "I have even been requested to perform at birthday parties and the like so at least my name is going around town in a positive manner!"
        show pov embarrassed_talk at left
        show sam embarrassed at right
        pov "Well that’s good, right?"
        show pov smirk_talk at left
        show sam smirk at right
        pov "Free advertising for your business and the like."
        show pov smirk at left
        show sam smirk_talk at right
        sam "I assumed so at first, but now I’m mostly just known for my magic tricks."
        show pov embarrassed at left
        show sam embarrassed_talk at right
        sam "It feels wrong how often I have to pay the rent from my profits from the magic act rather than any actual income coming directly from the register…"
        show pov confused at left
        show sam shocked_talk at right
        sam "But then I remember how much more I prefer it over telling my parents they were right and have to go back to using my degree in a soul crushing job."
        show pov shocked_talk at left
        show sam shocked at right
        pov "You went to college?"
        show pov shocked at left
        show sam embarrassed_talk at right
        sam "I made my masters in communications, was valedictorian for my generation and was even named “Most likely to succeed” in the year book."
        show pov confused_talk at left
        show sam embarrassed at right
        pov "What happened then?"
        show pov confused at left
        show sam embarrassed_talk at right
        sam "Found my own happiness and lived my life without regrets."
        show pov neutral at left
        show sam neutral_talk at right
        sam "Quirky, difficult and imperfect as it may be at times, I wouldn’t trade it for the world."
        show pov neutral_talk at left
        show sam neutral at right
        pov "I can respect that."
        show pov shocked at left
        show sam embarrassed_talk at right
        sam "But enough about me, how can I help you?"
        show pov embarrassed_talk at left
        show sam neutral at right
        pov "Well, I was hoping to ask you some questions actually."
        show pov embarrassed at left
        show sam smirk_talk at right
        sam "Ah, a fellow wanderer of life’s endless mysteries, eh?"
        show pov neutral at left
        show sam neutral_talk at right
        sam "I’ll do my very best to help you out!"
        show pov embarrassed at left
        show sam confused_talk at right
        sam "Are you perhaps on the hunt of the lost Aztec treasures following the events of “La Noche Triste”?"
        show sam smirk_talk at right
        sam "Or is it the whereabouts of Cleopatra and Alexander’s tomb that has awakened your inquisitive mind?"
        show pov embarrassed_talk at left
        show sam confused at right
        pov "Uh, no. Nothing in an archaeological sense, I think."
        show pov embarrassed at left
        show sam confused_talk at right
        sam "Then perhaps it is a new desire to awaken your senses and get to know more of the supernatural world around us?"
        show sam embarrassed_talk at right
        sam "There is a certain ritual to make you intune with the energy of the forest itself by consuming a concoction made from elements of the forest itself!"
        show pov confused at left
        show sam bored_talk at right
        sam "It is fabled to allow you to see a set of spirits that inhabit our planet and who will make your life generally easier if you go out of your way and present them with gifts or bundles containing items from the land."
        show pov embarrassed_talk at left
        show sam neutral at right
        pov "That seems more useful to a farmer or rancher than it does me."
        show pov bored_talk at left
        show sam embarrassed at right
        pov "Plus, there isn’t that much forest around the town I’m willing to venture into with everything that’s going on."
        show pov embarrassed_talk at left
        show sam smirk at right
        pov "So I’ll pass on that."
        show pov embarrassed at left
        show sam smirk_talk at right
        sam "That’s fair enough actually."
        sam "Plus, farming can be very expensive."
        show sam confused_talk at right
        sam "Are you then perhaps looking for evidence of the paranormal and mystical?"
        show pov shocked at left
        show sam angry_talk at right
        sam "I gotta warn you though, messing with the undead tends to open the gate for other less benign beings to access our realm."
        show pov embarrassed at left
        show sam shocked_talk at right
        sam "You never have a certain way to verify who it is you are contacting."
        show sam smirk_talk at right
        sam "So don’t be surprised when your occultism studies are suddenly shifted harshly into the domains of demonology."
        show pov embarrassed_talk at left
        show sam smirk at right
        pov "A-Again Sam, I don’t think that’s what I’m looking for entirely."
        show pov bored_talk at left
        pov "At least definitely not in the sense of communicating with stuff."
        show pov embarrassed_talk at left
        show sam neutral at right
        pov "I much prefer those to stay right where they came from and as far away from me as possible."
        show pov embarrassed at left
        show sam neutral_talk at right
        sam "Ok, I gave it my guesses, I suppose that’s what I get for missing the clairvoyance online class sign up."
        show sam bored_talk at right
        sam "It was either that or advance sleight of hand and cardistry."
        show pov neutral at left
        show sam embarrassed_talk at right
        sam "And the fact I have 4 shows booked for the end of the week around town and a very comfy rest of the month not having to worry about rent, tells me I made a good call."
        show pov embarrassed_talk at left
        show sam embarrassed at right
        pov "Congrats on that, but can I tell you now what I wanted to ask you?"
        show pov embarrassed at left
        show sam smirk at right
        sam "Certainly!"
        show pov embarrassed at left
        show sam embarrassed_talk at right
        sam "Sorry, I tend to go on tangents about this when I don’t notice."
        show pov embarrassed_talk at left
        show sam confused at right
        pov "Listen, do you know of anything… Weird… about the town?"
        show pov embarrassed at left
        show sam confused_talk at right
        sam "That's a bit of a vague word, isn’t it?"
        sam "I tend to get called that far too often so you are going to need to be a bit more specific here."
        show pov embarrassed_talk at left
        show sam neutral at right
        pov "I-I’m sorry, I didn’t mean to offend you."
        show pov embarrassed at left
        show sam neutral_talk at right
        sam "Nah, it’s cool!"
        show sam embarrassed_talk at right
        sam "When you decide to live your life the way I do, you tend to expect this sort of words."
        sam "If you run away from reality, it only makes sense for people to call you that."
        show sam bored_talk at right
        sam "Anyway, go on."
        show pov embarrassed_talk at left
        show sam neutral at right
        pov "Well, I was more focused on learning about the town itself."
        show pov confused_talk at left
        show sam smirk at right
        pov "Do you know of any… Well, any mysteries or unnatural phenomenons local to the area?"

        #-Grundle gives the mc a knowing smile at this-
        show pov confused at left
        show sam smirk_talk at right
        sam "You had a close encounter with something didn’t you?"
        show pov confused_talk at left
        show sam smirk at right
        pov "U-Um…"
        show pov embarrassed at left
        show sam confused_talk at right
        sam "Gonna guess it was not a good encounter at that."
        show pov embarrassed_talk at left
        show sam embarrassed at right
        pov "How did you-"
        show pov shocked at left
        show sam embarrassed_talk at right
        sam "I know my fair share of things, I can tell the face of someone who went through something supernatural and has trouble believing it even though they are 100%% sure it happened."
        show pov shocked_talk at left
        show sam shocked at right
        pov "So you have seen it before, then do you anything about-"
        show pov shocked at left
        show sam shocked_talk at right
        sam "Woah, hold your horses there, cowboy."
        show sam embarrassed_talk at right
        sam "I know well that look on your eyes, but I’ve mainly seen it in separate events outside of town."
        show pov embarrassed at left
        show sam bored_talk at right
        sam "Back in the days I traveled around the country that is."
        sam "I have quite the eye to spot charlatans and people who actually witness something strange."
        show pov embarrassed_talk at left
        show sam bored at right
        pov "I-Is that so?"
        show pov embarrassed at left
        show sam shocked_talk at right
        sam "Quite so!"
        show pov confused at left
        show sam confused_talk at right
        sam "Now, about the town itself however?"
        show sam smirk_talk at right
        sam "There are a couple of mysteries itself."
        show pov shocked at left
        show sam bored_talk at right
        sam "Primarily about it’s founding and other mysteries surrounding it."
        show sam shocked_talk at right
        sam "Plus the frequent disappearances of a few years ago and now all the recent mess."
        show pov embarrassed at left
        show sam embarrassed_talk at right
        sam "I have a few theories about it along with the legends themselves if you want to hear them."
        show pov embarrassed_talk at left
        show sam neutral at right
        pov "That would be of great help like you have no idea."
        show pov embarrassed at left
        show sam smirk_talk at right
        sam "Alright, I can tell you more about the town’s history or let you in some of the town's very own mysteries!"


        #-The following choices loop back to the choice menu after Grundle is done with the dialogue. Once its all read, the Mc will ask about his theories regarding everything-

        #=CHOICE=
        menu investigations_grundlesam_choices:
            "The town’s history"if not investigations_grundlesam_choice_chosen_history:
                jump investigations_grundlesam_history
            "Other mysteries"if not investigations_grundlesam_choice_chosen_mystery:
                jump investigations_grundlesam_mystery


        label investigations_grundlesam_history:
            #-If “The town’s history” was picked-
            $ investigations_grundlesam_choice_chosen_history = True
            show pov confused_talk at left
            with dissolve
            show sam neutral at right
            with dissolve
            pov "You mentioned something about the town's history and its founding?"
            show pov confused at left
            show sam shocked_talk at right
            sam "I did!"
            show pov neutral at left
            show sam neutral_talk at right
            sam "There is quite a bit of mystery regarding the founding families and the early generations of the town."
            show sam embarrassed_talk at right
            sam "Then again, the town was founded around 200 years ago and people back then didn’t really keep track of records."
            show pov embarrassed at left
            show sam bored_talk at right
            sam "At least not until the Great Fire of the “New Hope Library” which was renovated a few years later, only to be demolished and then turned into the school around the 1960’s."
            show pov embarrassed_talk at left
            show sam neutral at right
            pov "I had no idea the town was that old."
            show pov shocked at left
            show sam neutral_talk at right
            sam "It’s the usual for small towns like this."
            show sam smirk_talk at right
            sam "There are pieces of documents detailing the fact  witchcraft and dark magic were involved in the towns flourish even!"
            show pov confused_talk at left
            show sam smirk at right
            pov "For real?"
            show pov confused at left
            show sam smirk_talk at right
            sam "Not a trusted source, man."
            show sam bored_talk at right
            sam "It was the early years, back then any sort of innovation could be taken as demonic work or some kind of dark magic."
            show pov shocked at left
            show sam shocked_talk at right
            sam "Not to mention the fact being moody or just odd overall could get you accused of being a witch or warlock without much substantial evidence and be put on the stake by the end of the day."
            show pov shocked_talk at left
            show sam smirk at right
            pov "Wait, are you saying we have a history of witch trials and burnings?"
            show pov shocked at left
            show sam bored_talk at right
            sam "Actually no, believe it or not."
            show pov confused at left
            sam "From what the old records say, some of the founding families, one in particular at that, were suspected of some sort of dark magic by the townsfolk."
            show sam shocked_talk at right
            sam "But one day, a large chunk of members of said families, along with other members of town suspected to be in cahoots with them in some way, simply disappeared."
            show sam embarrassed_talk at right
            sam "There is not a lot information left regarding who they were or what happened afterwards, but the town took it as some sort of divine retribution and moved on with their lives."
            show pov shocked at left
            show sam shocked_talk at right
            sam "One family was almost completely wiped out with the disappearance, but since they were wealthy enough, they managed to keep their status."
            show pov confused at left
            show sam embarrassed_talk at right
            sam "Rich people always manage to land on their feet, you know?"
            show pov bored_talk at left
            show sam embarrassed at right
            pov "You don’t say."
            show pov bored at left
            show sam smirk_talk at right
            sam "Still, it’s quite the mystery!"
            show pov embarrassed at left
            show sam neutral_talk at right
            sam "Some believe they were spirited away to the underworld in the midst of a ritual, others think they were abducted in a large scale operation by extraterrestrial beings, There are some who think they were actually dragged to hell after a ritual went wrong even!"
            show pov neutral at left
            show sam smirk_talk at right
            sam "I have my own theories but I’ll tell you some other day since I do need to set up the slides and everything since it’s a bit out there."
            show pov neutral_talk at left
            show sam smirk at right
            pov "Alright then?"
            show pov embarrassed at left
            show sam embarrassed_talk at right
            sam "Okay, what do you want to know next?"

            jump investigations_grundlesam_check

        label investigations_grundlesam_mystery:
            ##-If “Other Mysteries” was picked-
            $ investigations_grundlesam_choice_chosen_mystery = True
            show pov smirk_talk at left
            with dissolve
            show sam neutral at right
            with dissolve
            pov "Well, since you mentioned it."
            show pov confused_talk at left
            pov "What other sort of mysteries are around the town?"
            show pov neutral at left
            show sam smirk_talk at right
            sam "Quite plenty, my friend!"
            show sam shocked_talk at right
            sam "This is what I love about small towns, big cities are just far too cluttered with stuff for a passionate paranormal investigator!"
            show sam embarrassed_talk at right
            sam "Our small town has its own good share of mysterious happenings to keep an enthusiast like me quite entertained without absolutely overwhelming them!"
            show pov embarrassed at left
            show sam smirk_talk at right
            sam "A manageable treasure trove of mystery, believe it or not!"
            show pov embarrassed_talk at left
            show sam smirk at right
            pov "I’m finding myself far more inclined to believe it nowadays…"
            show pov confused_talk at left
            pov "So, what sort of things does our little town offer?"
            show pov confused at left
            show sam neutral_talk at right
            sam "Well, the bigger one is about the recent disappearances as I’m sure you are aware by now, so I’ll just focus on the one that has affected me to the point I can’t even sleep sometimes!"
            show pov shocked_talk at left
            show sam neutral at right
            pov "Sounds good, I guess?"
            show pov shocked at left
            show sam neutral_talk at right
            sam "One of the town's most recent mysteries, the town’s Ghost Girl!"
            show pov embarrassed_talk at left
            show sam smirk at right
            pov "A ghost girl..."
            show pov embarrassed at left
            show sam smirk_talk at right
            sam "A haunting image of a girl that stalks you wherever you go and seems to disappear without a trace whatsoever once you try and give her a second look!"
            show pov embarrassed_talk at left
            show sam smirk at right
            pov "That sounds far too familiar…"
            show pov embarrassed at left
            show sam confused_talk at right
            sam "So you have seen her then?"
            show sam embarrassed_talk at right
            sam "I’m not surprised, there are a ton of people in town who have reported witnessing her. It’s a bit of a popular phenomenon."
            show pov shocked at left
            show sam smirk_talk at right
            sam "One I have been a bit obsessed over since my last encounter with her."
            show pov shocked_talk at left
            show sam embarrassed at right
            pov "You encountered her recently?"
            show pov confused at left
            show sam smirk_talk at right
            sam "A full on face to face encounter at that!"
            sam "I don’t think anyone has ever gotten as closed to her as I have!"
            show pov embarrassed at left
            show sam shocked_talk at right
            sam "I’m talking just a few feet of distance too!"
            show pov confused at left
            show sam smirk_talk at right
            sam "To the point she even noticed me and smiled before turning a corner and disappearing out of sight!"
            show pov smirk_talk at left
            show sam smirk at right
            pov "You are kidding…"
            show pov embarrassed_talk at left
            pov "C-Can you tell me more about her?"
            show pov shocked_talk at left
            show sam neutral at right
            pov "Any distinct features of her you might remember?"
            show pov shocked at left
            show sam shocked_talk at right
            sam "Oh, I have a very detailed mental image of her in my mind!"
            show pov smirk at left
            show sam neutral_talk at right
            sam "Witnessing something like that is something that doesn’t leave you easily, you know?"
            show pov neutral at left
            show sam embarrassed_talk at right
            sam "It’s embarrassing to admit it since I’m a researcher to the unknown and an enthusiast of such paranormal events, but I sometimes have nightmares about it."
            show pov embarrassed at left
            show sam shocked_talk at right
            sam "Plus I now get the feeling of being watched from time to time."
            show pov embarrassed_talk at left
            show sam embarrassed at right
            pov "I hear you…"
            show sam confused at right
            pov "She is quite the frightening sight with her whole white dress and all."
            show pov confused at left
            show sam confused_talk at right
            sam "White dress?"
            show sam angry_talk at right
            sam "What are you talking about, she wears something similar to a victorian or gothic style attire."
            show pov shocked_talk at left
            show sam confused at right
            pov "Wait, what?"
            show pov shocked at left
            show sam bored_talk at right
            sam "Yeah, I distinctly remember her black skirt and the little red tie she uses on her outfit and don’t even get me started on her little heart accessories on her hair…"
            show pov confused_talk at left
            show sam confused at right
            pov "Wait a minute, isn’t that-"
            show pov shocked at left
            show sam bored_talk at right
            sam "It’s unsettling how the supernatural world can turn even something cute and alluring into such a horrifying visage."
            show pov bored_talk at left
            show sam confused at right
            pov "Uhhh…"
            show pov embarrassed_talk at left
            pov "Sam, I don’t know how to tell you this, but-"
            show pov embarrassed at left
            show sam smirk_talk at right
            sam "No need to say anything, [povname]."
            show sam neutral_talk at right
            sam "This is a mystery I must get to the bottom of on my own."
            show sam smirk_talk at right
            sam "I am triangulating her usual haunting locations from other reported sightings of her and I feel like I'm getting ever closer to the truth!"
            show pov embarrassed_talk at left
            show sam smirk at right
            pov "T-That's great and all Sam, but I should really let you know that-"
            show pov shocked at left
            show sam bored_talk at right
            sam "Don't even attempt to dissuade me, [povname]!"
            show pov confused at left
            show sam smirk_talk at right
            sam "I know the dangers of approaching the origin location of a supernatural entity, but my desire for truth is far greater than my survival instincts. Nevertheless, I assure you that I am taking precautions!"
            show pov confused_talk at left
            show sam smirk at right
            pov "Are you actually?"
            show pov shocked at left
            show sam smirk_talk at right
            sam "This is not my first wrestling match with the extra dimensional spirits, my friend!"
            show pov embarrassed at left
            show sam neutral_talk at right
            sam "I have my fair share of talisman, banishment rites and dispel enchantments that will keep me free from any and all possessions until I can find the cause this spirit remains on this earth!"
            show pov embarrassed_talk at left
            show sam smirk at right
            pov "And then what?"
            show pov shocked at left
            show sam smirk_talk at right
            sam "I'll find her remains and set her free of course!"
            show sam neutral_talk at right
            sam "Get rid of what's keeping her haunting this earth and then banish her from this plane into either eternal rest or damnation, depending on the true nature of the spirit, of course."
            show pov bored_talk at left
            show sam neutral at right
            pov "Huh…"
            show pov smirk_talk at left
            show sam smirk at right
            pov "Well, good luck then Sam, just try not to get arrested…"
            show pov embarrassed_talk at left
            show sam neutral at right
            pov "Especially in these times…"
            show pov embarrassed at left
            show sam neutral_talk at right
            sam "I'll be careful! I know quite well that even if the place the entity resides in can be classified as an abandoned building as a whole, it is still breaking and entering in the eyes of the law."
            show pov embarrassed_talk at left
            show sam neutral at right
            pov "Yeah, I doubt the place she haunts is that abandoned to begin with…"

            jump investigations_grundlesam_check

        label investigations_grundlesam_check:
            if investigations_grundlesam_choice_chosen_history and investigations_grundlesam_choice_chosen_mystery:
                jump investigations_grundlesam_busy
            else:
                jump investigations_grundlesam_choices

        label investigations_grundlesam_busy:
            show pov embarrassed at left
            with dissolve
            show sam embarrassed_talk at right
            with dissolve
            sam "I would love to tell you some more, man, but sadly it is still business hours and gotta keep holding vigilant for clients."
            show pov embarrassed_talk at left
            show sam embarrassed at right
            pov "That’s alright, I think I’ve had my fill for now, thanks for your time."
            show pov confused_talk at left
            show sam neutral at right
            pov "You said you had your own theory as to what happened to the families that disappeared all those years ago?"
            show pov confused at left
            show sam embarrassed_talk at right
            sam "Well, it’s not much of a theory as it is speculation at this point."
            show pov embarrassed at left
            show sam neutral_talk at right
            sam "Mainly just strings of evidence that I managed to gather into a plausible outcome."
            show pov confused_talk at left
            show sam neutral at right
            pov "Isn’t that the definition of a theory?"
            show pov embarrassed at left
            show sam neutral_talk at right
            sam "Even someone in the world of investigation of the supernatural must know to differentiate a solid theory from just a bunch of sticky notes and red string tied to the wall."
            show pov neutral at left
            show sam bored_talk at right
            sam "Otherwise, you go cray-cray and start seeing martians everywhere you go or feel the paranoia make goop of your brain."
            show sam embarrassed_talk at right
            sam "You can’t go jumping at shadows thinking you struck the next big mystery."
            sam "I have friends who to this day think they are being targeted by a government hitman because he thinks an anagram on a newspaper from 1978 that contains the entire “Wasp Movie” script is the secret to find the entrance to the secret reptilian society."
            show pov confused_talk at left
            show sam embarrassed at right
            pov "Does it even count as an anagram when it has that many words?"
            show pov embarrassed at left
            show sam embarrassed_talk at right
            sam "You see my point?"
            show sam smirk_talk at right
            sam "You start accepting all pieces of information blindly and you’ll start thinking everything is a clue or hint to some ancestral mystery and you’ll start seeing every man or woman glaring at you as a hitman coming to kill you."
            sam "Ignoring the fact they are glaring at you in the first place because you keep digging in trash or accusing their children of being robot replicas."
            show pov smirk_talk at left
            show sam smirk at right
            pov "You have a weird group of friends, Sam."
            show pov embarrassed at left
            show sam neutral_talk at right
            sam "It’s a fine line between a mystery enthusiast and a conspiracy nut, my friend."
            show pov neutral at left
            show sam neutral_talk at right
            sam "So ask me about it later once I properly gather my thoughts about it and find some solid proof."
            show pov embarrassed at left
            show sam shocked_talk at right
            sam "Or at least make a kickass slideshow."
            show sam smirk_talk at right
            sam "If I’m gonna waste someone’s time with a crazy theory, I may as well make it fun for everyone involved, right?"
            show pov embarrassed_talk at left
            show sam neutral at right
            pov "Weirdly kind of you, but I’ll take it."
            pov "Still, I’m really not sure where to take it from here…"
            show pov embarrassed at left
            show sam smirk_talk at right
            sam "Well, fear not my fellow mystery enthusiast!"
            show sam neutral at right
            sam "So far from what you’ve told me I would recommend you either give a follow up to the beach story from Violette or maybe you could gather your thoughts with yet another enthusiast in your particular field!"
            show pov confused_talk at left
            show sam smirk at right
            pov "What do you mean?"
            show pov confused at left
            show sam smirk_talk at right
            sam "There are two guys, a girl and a dude, who used to ask me a lot regarding mysteries of the town. Sure it was a few years ago but I’m sure she can give you a different perspective about all of this."
            show sam shocked_talk at right
            sam "I’ve seen you with her in the mall actually!"
            show pov shocked at left
            show sam confused_talk at right
            sam "Effie and Jacob?"
            show pov shocked_talk at left
            show sam confused at right
            pov "So they’ve come to you about this?"
            show pov confused at left
            show sam neutral_talk at right
            sam "Yeah! I had just opened my store and they were quite the little detectives!"
            show sam smirk_talk at right
            sam "I used to act as a bit of their “Informant” back in the day and give them clues about whatever case they were on about."
            show pov embarrassed at left
            show sam neutral_talk at right
            sam "I have very fond memories of back then, so I’m sure they’ll help you out!"
            show pov neutral at left
            show sam smirk_talk at right
            sam "Jacob still comes by to talk from time to time and Effie does wave when she passes by, so it’s nice to see you getting along with them."
            show pov neutral_talk at left
            show sam smirk at right
            pov "I’ll keep it in mind, thanks for everything Sam."
            show pov neutral at left
            show sam neutral_talk at right
            sam "My pleasure!"
            show pov embarrassed at left
            sam "This has been the most entertaining part of the day so far so do come by to chat or if you need a new totem."
            show sam smirk_talk at right
            sam "You never know when a little boost can help you out!"
            show pov shocked at left
            show sam shocked_talk at right
            sam "Oh and if you do talk to Violet… Please tell her I’m sorry for what happened a few nights ago."
            show pov confused at left
            show sam embarrassed_talk at right
            sam "She’ll know what I mean."
            show pov confused_talk at left
            show sam embarrassed at right
            pov "Okay?"
            show pov neutral_talk at left
            show sam smirk at right
            pov "See you later, Sam!"
            show pov embarrassed at left
            show sam smirk_talk at right
            sam "Farewell, fellow man of mystery!"
            $ gtime = 1

            jump lbl_stuffstore_day

        ##=SCENE END=

        ##-From this point on, the Player can decide which location to investigate next-
