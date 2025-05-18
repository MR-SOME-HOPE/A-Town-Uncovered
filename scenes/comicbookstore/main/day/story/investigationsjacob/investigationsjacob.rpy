##[Comic Book Shop, afternoon - “Investigations_Jacob”  - main_story =84-N]

##-Jacob only becomes available to be talked to once the player has interacted with Effie first-

##-The Mc approaches Jacob who is busy looking at a magazine upside down. It is upside down because he is hiding the hentai doujin he is actually reading inside it and he hasn’t noticed it’s upside down-
label lbl_investigations_jacob:
    default investigations_jacob = 0
    show btn_comicbookstore_day_hitomi_idle2
    show btn_comicbookstore_day_jacob_idle2
    $ renpy.pause(0.001)

    if investigations_effie == 0:
        pov "I'll leave Jacob alone for now."
    elif investigations_jacob == 1:
        pov "I already spoke to Jacob. That's enough for now"
    else:
        show pov confused_talk at left
        with dissolve
        show jac neutral at right
        hide btn_comicbookstore_day_jacob_idle2
        with dissolve
        pov "Uhhh… Jacob?"
        show pov confused at left
        show jac confused_talk at right
        jac "Hmm?"
        show pov neutral at left
        show jac neutral_talk at right
        jac "Oh, hey dude. What’s up?"
        show pov neutral_talk at left
        show jac neutral at right
        pov "What are you doing?"
        show pov shocked at left
        show jac embarrassed_talk at right
        jac "Catching up with the latest issue of Group Leveling, this really cool korean comic book I’m into, something really interesting."
        show pov confused_talk at left
        show jac embarrassed at right
        pov "And do you tend to read them upside down?"
        show pov confused at left
        show jac confused_talk at right
        jac "What are you talking abou-"
        show jac shocked_talk at right
        jac "Oh, God dangit!"
        show jac angry_talk at right
        jac "How long have I had it upside down?!"
        show pov confused_talk at left
        show jac shocked at right
        pov "You just noticed?!"
        show pov confused at left
        show jac smirk_talk at right
        jac "Oh, don’t be so surprised, you know I’m just using it as cover."
        show pov confused_talk at left
        show jac smirk at right
        pov "Then what are you actually reading?"
        show pov confused at left
        show jac smirk_talk at right
        jac "What do you think I could be reading that would require me to hide it with another thing?"
        show pov embarrassed_talk at left
        show jac smirk at right
        pov "I’m afraid to ask to be honest with you."
        show pov embarrassed at left
        show jac smirk_talk at right
        jac "I’ll tell ya anyway."
        show jac neutral_talk at right
        jac "It’s the newest edition of the Anti-Devil Samurai Women!"
        show pov shocked at left
        show jac shocked_talk at right
        jac "Has a buttload of backstory and version but basically, a group of hot samurai women who specialize on demon killing get roped into an arena match and lots of bad, yet hot, stuff happens to them."
        show pov neutral at left
        show jac embarrassed_talk at right
        jac "Definitely recommend it, has a ton of versions out there, even a mobile card game!"
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "And you find it prudent to be reading that kind of thing in public?"
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Dad’s a “good christian” and monitors my search history religiously, ok?"
        show jac embarrassed_talk at right
        jac "If he found me reading this, it would be a one way trip to christian camp for the summer."
        show pov neutral at left
        show jac smirk_talk at right
        jac "I am NOT going back there dude."
        show pov neutral_talk at left
        show jac smirk at right
        pov "Alright fair enough."
        show pov neutral at left
        show jac smirk_talk at right
        jac "You could do me a solid and hide them in your house for me to get, if you feel charitable, you know?"
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "We can discuss that later, I sort of need your help right now."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "You know you can always count on good ol’ Jacob."
        show jac confused_talk at right
        jac "What’s wrong?"
        show pov embarrassed_talk at left
        show jac confused at right
        pov "Well, it’s about Effie."
        show pov embarrassed at left
        show jac confused_talk at right
        jac "What about her? Is she on her time of the month again?"
        show pov shocked at left
        show jac smirk_talk at right
        jac "If it’s so bad she is lashing out at you, then I better start running for the hills before she sees me!"
        show pov shocked_talk at left
        show jac smirk at right
        pov "No! At least I don’t think so."
        show pov embarrassed_talk at left
        show jac confused at right
        pov "We just sort of had a fight earlier and now she refuses to talk or even see me."
        show pov sad_talk at left
        show jac embarrassed at right
        pov "I’m at a loss of what to do."
        show pov sad at left
        show jac embarrassed_talk at right
        jac "Oh damn dude, what did you do?"
        show pov confused_talk at left
        show jac embarrassed at right
        pov "Wh-Why do you immediately assume I was the one who did anything?"
        show pov sad at left
        show jac embarrassed_talk at right
        jac "Because we are talking about Effie, here dude."
        show pov embarrassed at left
        show jac confused_talk at right
        jac "I speak from experience here, there is a very small list of things in the world that upsets her."
        show pov shocked at left
        show jac shocked_talk at right
        jac "I broke her arm on accident one summer when we were climbing a tree and she didn’t even yell at me or complained once even though she had to wear the cast the whole summer!"
        show pov confused_talk at left
        show jac embarrassed at right
        pov "How do you break someone's arm by accident?"
        show pov confused at left
        show jac bored_talk at right
        jac "I got stuck on a tree, she offered to catch me and I didn’t exactly fall the way we planned, ok?"
        show pov embarrassed at left
        show jac embarrassed_talk at right
        jac "We are missing the point, anyway."
        show jac confused_talk at right
        jac "What did you do to get her so upset she won’t even talk to you?"
        show pov embarrassed_talk at left
        show jac embarrassed at right
        pov "I…"
        show pov embarrassed_talk at left
        show jac shocked at right
        pov "I kind of pushed her a bit too far regarding some questions that she didn’t want to answer…"
        show pov embarrassed at left
        show jac embarrassed_talk at right
        jac "Oh boy, I see the problem."
        show pov confused_talk at left
        show jac embarrassed at right
        pov "You do?"
        show pov confused at left
        show jac confused_talk at right
        jac "Effie is a pretty open person dude, I have literally asked her what periods are like and she goes into horrifying detail no problem."
        show jac embarrassed_talk at right
        jac "There aren’t a lot of things she is serious to keep quiet about, but the few there are, It’s best to not even touch them with a ten foot pole at a safe distance."
        show pov confused_talk at left
        show jac embarrassed at right
        pov "Things like what?"
        show pov confused at left
        show jac bored_talk at right
        jac "Really not comfortable being a blabbermouth about them dude."
        show pov embarrassed at left
        show jac embarrassed_talk at right
        jac "She’s my oldest friend so I’m not about to talk behind her back like that. I’m sorry."
        show pov shocked_talk at left
        show jac embarrassed at right
        pov "No, it’s okay."
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "Not gonna push it and risk getting you upset too."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Thanks, dude."
        show jac embarrassed_talk at right
        jac "Just give her some time, it’s not easy to get her mad but even if you do, it’s not easy for her to stay mad at you."
        show pov neutral at left
        show jac neutral_talk at right
        jac "She is not one to hold grudges, so she’ll eventually calm down and that’ll be your chance to get things right."
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "If you say so…"
        show pov sad_talk at left
        show jac bored at right
        pov "Still, without her answers I’m sort of put in a bad situation."
        show pov sad at left
        show jac embarrassed_talk at right
        jac "Alright, I’ll bite. What is it you tried asking her?"
        show pov embarrassed_talk at left
        show jac confused at right
        pov "Just please promise you won’t get mad as well."
        show pov embarrassed at left
        show jac smirk_talk at right
        jac "I give you my Boy Scout word of honor."
        show jac neutral_talk at right
        jac "I won’t get mad no matter what it is."
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "Thanks, man."
        show pov confused_talk at left
        show jac embarrassed at right
        pov "Well…"
        show pov embarrassed_talk at left
        show jac confused at right
        pov "You know how I’ve been a bit… Twitchy, lately?"
        show pov embarrassed at left
        show jac confused_talk at right
        jac "Dude, you look like you are about to have a heart attack at the sight of your own shadows sometimes."
        show pov embarrassed_talk at left
        show jac confused at right
        pov "Yeah, that."
        show pov shocked_talk at left
        pov "Well, I decided enough was enough and I started doing some research about it."
        show pov shocked at left
        show jac smirk_talk at right
        jac "Facing your problems head on, like a man, good to hear!"
        show pov embarrassed_talk at left
        show jac shocked at right
        pov "Long story short, a lot of the people I talked to eventually just led me to Effie and when I tried asking her about it, she just shut me off completely."
        show pov embarrassed at left
        show jac shocked_talk at right
        jac "It led you to Effie?"
        show pov embarrassed_talk at left
        show jac shocked at right
        pov "I was asking about mysteries and stuff about the town and some people told me Effie used to be all about that sort of stuff in the past."
        show pov confused_talk at left
        show jac embarrassed at right
        pov "People like Grundle Sam and Meghan told me how you two used to be quite the junior detectives and knew all about weird happenings in the town and such."
        show pov confused at left
        show jac embarrassed_talk at right
        jac "Oh…"
        jac "So you asked her about Those days…"
        show pov embarrassed_talk at left
        show jac embarrassed at right
        pov "Yeah, but she immediately turned hostile on me and kicked me out of the cafe."
        show pov embarrassed at left
        show jac embarrassed_talk at right
        jac "Yeah, I’m not surprised."
        show pov shocked at left
        show jac bored_talk at right
        jac "Effie doesn’t have many fond memories about the latter half of our detective agency days."
        show pov shocked_talk at left
        show jac bored at right
        pov "She got mad how I kept quiet with you two about what was going on with me and after that she just put a wall between us and kicked me out."
        show pov embarrassed_talk at left
        show jac sad at right
        pov "Don’t suppose there is a chance of you helping me out here?"
        show pov embarrassed at left
        show jac sad_talk at right
        jac "Sorry man, I really wish I could."
        show pov sad at left
        jac "But she does have a point there."
        show pov embarrassed at left
        show jac embarrassed_talk at right
        jac "We did try to reach out for you but you kept pushing us away and saying you were fine."
        show pov shocked_talk at left
        show jac shocked at right
        pov "It wasn’t my intention to push you away or anything!"
        show pov confused_talk at left
        pov "I just had no idea how to even tell you about it without sounding crazy."
        show pov angry_talk at left
        show jac embarrassed at right
        pov "Hell, I still don’t even know what going on entirely myself, so I had no clue how to tell other people."
        show pov angry at left
        show jac embarrassed_talk at right
        jac "I get that dude, whatever happened must not be exactly easy to talk about."
        show pov confused at left
        show jac sad_talk at right
        jac "But she may have taken more of an insult seeing how worried she got about you only for you to shut her off to then start asking her personal questions and expect an answer."
        show pov confused_talk at left
        show jac sad at right
        pov "She got worried about me?"
        show pov shocked at left
        show jac embarrassed_talk at right
        jac "We both did, dude."
        jac "You are our friend and the fact you didn’t feel comfortable enough to fully tell us what has us so scared, stings a little."
        show jac sad_talk at right
        jac "Made her think like you didn’t trust her or that you didn’t really see us as friends."
        show pov shocked_talk at left
        show jac sad at right
        pov "You know that's not the case!"
        show pov angry at left
        show jac bored_talk at right
        jac "Yeah, I do and that’s what I told her."
        show pov sad at left
        show jac embarrassed_talk at right
        jac "I convinced her that you are still the new kid so she shouldn’t expect you to just tell us all our problems right away."
        show jac confused_talk at right
        jac "Whatever is wrong clearly has you so disturbed you haven’t even told your folks so there was a slim chance you would tell us right away."
        show pov embarrassed at left
        show jac embarrassed_talk at right
        jac "But as you kept being weird and the whole situation going around you with the school monitoring and then the kidnapping, she got more and more worried about you."
        show pov confused_talk at left
        show jac embarrassed at right
        pov "She didn’t really show she was that worried about me…"
        show pov confused at left
        show jac embarrassed_talk at right
        jac "{i}*sigh*{/i}"
        show pov sad at left
        show jac sad_talk at right
        jac "Effie… Is complicated dude…"
        jac "She has issues with people disappearing or distancing themselves from her."
        show jac embarrassed_talk at right
        jac "So when you started showing signs of doing so, well…"
        show jac sad_talk at right
        jac "She got rather scared."
        show jac embarrassed_talk at right
        jac "She just doesn’t show it cuz she puts this front of being confident and laid back at all times."
        show pov confused at left
        show jac shocked_talk at right
        jac "Don’t ever tell her I told you this, but when she found out from your mom that you were missing, she came running to my house to get me to help, but I had to take nearly 20 minutes calming her down from how bad she was panicking."
        show pov shocked_talk at left
        show jac embarrassed at right
        pov "Wow…"
        show pov shocked at left
        show jac embarrassed_talk at right
        jac "I got scared too, dude, don’t get me wrong."
        show pov sad at left
        show jac neutral_talk at right
        jac "But Ephs has a very soft spot for you, that much is obvious."
        jac "Even if she never shows it, at least not in public or when we are hanging out."
        show pov sad_talk at left
        show jac embarrassed at right
        pov "Damn… I feel awful now…"
        show pov sad at left
        show jac sad_talk at right
        jac "I’ll try to ease the beast a little, man. But keep it in mind when you ask her questions like that."
        show jac bored_talk at right
        jac "Especially about those times."
        show pov embarrassed_talk at left
        show jac bored at right
        pov "What’s so bad about those days?"
        show pov embarrassed at left
        show jac bored_talk at right
        jac "It’s a long story, dude."
        show pov confused at left
        show jac embarrassed_talk at right
        jac "I think it would be better if you heard it from her though."
        jac "But she needs to know you are willing to share stuff of that caliber as well before she opens up to you."
        show pov embarrassed at left
        show jac confused_talk at right
        jac "You know what I mean?"
        show jac embarrassed_talk at right
        jac "Don’t ask for an inch and then take a mile if you are not willing for us to do the same."
        show pov smirk at left
        show jac smirk_talk at right
        jac "Equivalent exchange and all that mumbo jumbo."
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "Alright…"
        show pov neutral_talk at left
        pov "So what are you proposing?"
        show pov neutral at left
        show jac neutral_talk at right
        jac "I’ll calm Effie down, then once she is open to talk, I’ll call you and we can all come clean."
        show pov embarrassed at left
        show jac embarrassed_talk at right
        jac "It’s gonna be hard to get her to open up here man, so I expect you to come and speak the god’s honest truth with us."
        show jac confused_talk at right
        jac "I know it sounds like a tough sell as I have no idea what you are going through."
        show pov sad at left
        show jac embarrassed_talk at right
        jac "But at least that way you may get some of the answers you seek out of her and that won’t make me a blabbermouth."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Plus, it will make my two best friends stop fighting, so I think everyone wins this way, huh?"
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "Well…"
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Come on, man!"
        show jac embarrassed_talk at right
        jac "I’m risking my neck out here too for your ass, least you could do is make some compromises!"
        show jac bored_talk at right
        jac "If Effie gets mad at you she’ll at least have the courtesy of keeping it civil."
        show pov sad at left
        show jac shocked_talk at right
        jac "If she gets mad at me, I am at risk of death here!"
        show jac smirk_talk at right
        jac "It’s a give and take kind of deal."
        jac "You have something to gain but you have to give something back."
        show pov embarrassed at left
        show jac embarrassed_talk at right
        jac "That’s as fair as I can make it."
        show pov embarrassed_talk at left
        show jac embarrassed at right
        pov "It’s not that simple."
        show pov confused_talk at left
        show jac bored at right
        pov "What if you don’t believe me even when I’m telling you the truth?"
        show pov confused at left
        show jac bored_talk at right
        jac "That front, I’ll leave to Effie."
        show pov embarrassed at left
        show jac smirk_talk at right
        jac "She can spot a liar from a mile away. As long as you don’t try to hide something or give her half truths, you should be in the clear."
        show jac bored_talk at right
        jac "Even if you tell her something as ridiculous as you being abducted by aliens or being a secret superhero, or being able to cross to another dimension or something."
        show pov embarrassed_talk at left
        show jac bored at right
        pov "That’s…"
        show pov embarrassed at left
        show jac smirk_talk at right
        jac "Just have a bit of faith and trust me ok?"
        show jac embarrassed_talk at right
        jac "When have I steered you wrong?"
        show pov embarrassed_talk at left
        show jac embarrassed at right
        pov "Well… OK…"
        show jac neutral at right
        pov "Alright, I’ll give it a shot and trust you on this…"
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Awesome!"
        show jac embarrassed_talk at right
        jac "For the record though, if you are indeed a superhero and have cool powers and shit, I’m going to be super hurt that you didn’t tell me sooner."
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "I promise I’m not a superhero."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "That’s what a superhero would say to protect their secret identity."
        show pov embarrassed_talk at left
        show jac embarrassed at right
        pov "Ease it on the comics, dude."
        show pov neutral at left
        show jac smirk_talk at right
        jac "Technically reading a Doujinshi inspired by a novelization, inspired by a visual novel, not a comic book."
        show pov smirk_talk at left
        show jac smirk at right
        pov "You know what I mean."
        show pov embarrassed_talk at left
        pov "Still dude, color me surprised: I didn’t think you had this much insight in you."
        show pov embarrassed at left
        show jac smirk_talk at right
        jac "Well, I know you guys call me a goober and I have my silly moments and all, but I still care about you guys like family."
        show pov neutral at left
        show jac neutral_talk at right
        jac "Hell, Effie pretty much is family seeing as how we grew up together and all."
        show jac bored_talk at right
        jac "So I’m not about to sit with a thumb up my own ass while you two have a fight."
        show pov neutral_talk at left
        show jac smirk at right
        pov "I appreciate it, dude."
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "I really do."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Don’t mention it man, besides I already have to deal with the split between my dad and my actual mom."
        show jac angry_talk at right
        jac "No way in hell am I also gonna be experiencing that with you guys."
        show jac bored at right
        jac "It’s better if we remain a trio of pals than me splitting myself to be each of your dynamic duos."
        show pov embarrassed_talk at left
        show jac bored at right
        pov "Fair enough."
        show pov confused_talk at left
        show jac shocked at right
        pov "Whatever happened to your actual Mom, Jacob?"
        show pov shocked at left
        show jac angry_talk at right
        jac "Touchy subject dude, what did we just finish talking about?!"
        show pov embarrassed_talk at left
        show jac confused at right
        pov "Sorry, sorry!"
        show jac neutral at right
        pov "My bad..."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Nah, just messing with you."
        jac "She is happily married to some rich black neurosurgeon and living in his penthouse in Miami."
        show pov neutral at left
        show jac bored_talk at right
        jac "I spend spring break and alternate between christmas and new years with them each year. It’s a bitch to have to fly in the holidays..."
        show jac embarrassed_talk at right
        jac "He’s a nice dude and all but he is trying way too hard for me to call him dad."
        show jac shocked_talk at right
        jac "Something about him not being able to have kids or something."
        show pov shocked_talk at left
        show jac bored at right
        pov "Huh, not what I expected to hear."
        show pov confused at left
        show jac bored_talk at right
        jac "I’ll introduce them to you sometime, they love meeting new friends of mine."
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "I’ll keep my schedule open then."
        show pov neutral_talk at left
        pov "Again, thanks a lot for all of this Jacob, I really owe you one."
        show pov neutral at left
        show jac neutral_talk at right
        jac "No biggie, dude. That's what bros are for, right?"
        show pov smirk_talk at left
        show jac smirk at right
        pov "Damn straight."
        show pov neutral_talk at left
        pov "Well, I still have to go investigate some more around town, may as well keep getting more clues that will help make a bigger picture to explain to you guys."
        show pov neutral at left
        show jac neutral_talk at right
        jac "That sounds smart, the least you have to ask Effie at the end of the day, the better."
        show pov confused_talk at left
        show jac confused at right
        pov "Don’t suppose you have any idea where I should go next?"
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "Well, not really, but whenever I have a question or need some answers I usually ask Effie, but if she is not available or is in her “Time of the Month”, I usually ask Edward."
        show jac bored_talk at right
        jac "Dude is like a super computer or something, though most of the time he usually asks me why I’m not asking the question to an actual computer and browser."
        show pov confused_talk at left
        show jac neutral at right
        pov "Why don’t you?"
        show pov confused at left
        show jac smirk_talk at right
        jac "I crave human interaction."
        jac "You never know when it could be the last time you see another person or when you are going to be forced to stay inside for an indefinite amount of time."
        show pov embarrassed at left
        show jac neutral_talk at right
        jac "So best enjoy it even if its as little as buying something in a store with a few regulars to make conversation with."
        show pov embarrassed_talk at left
        show jac neutral at right
        pov "Noted."
        show pov embarrassed at left
        show jac bored_talk at right
        jac "But seriously, if anything, he can help you gather some evidence if needed for example."
        show pov confused_talk at left
        show jac neutral at right
        pov "You don’t say…"
        show pov embarrassed_talk at left
        pov "Thanks again, Jacob."
        show pov neutral_talk at left
        pov "You really help a ton, man."
        show pov neutral at left
        show jac neutral_talk at right
        jac "Here to serve!"
        show jac shocked_talk at right
        jac "And remember, I’ll call you once I sort everything with Effie."
        show jac smirk_talk at right
        jac "So keep your schedule open cuz she is not going to want to wait for you to show up this time."
        show pov embarrassed at left
        show jac embarrassed_talk at right
        jac "Slim window of success here."
        show pov neutral_talk at left
        show jac neutral at right
        pov "Understood, I’ll be waiting for your call."
        pov "See you later, man."
        show pov neutral at left
        show jac smirk_talk at right
        jac "Later, bro!"

        #=SCENE END=

        #=END=
        $ investigations_jacob = 1

jump lbl_comicbookstore_day_setup
