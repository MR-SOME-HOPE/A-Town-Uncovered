label lbl_investigations_allaway:
    default investigations_allaway = 0
    scene bg cafeoutside_day
    with fade
    ##$ townmap_enabled = 0
    $ investigations_allaway = 1
    ##-If Allaway was picked and is romanced-
    if missallaway_path >= 24:
        show pov embarrassed_talk at left
        with dissolve
        pov "Hey, Alla-"
        show pov shocked at left
        show misc neutral_talk at right
        with dissolve
        mis "[povname]!"
        show pov embarrassed at left
        show misc smirk_talk at right
        mis "Gosh, I swear I could jump into your arms and kiss you right now, but…"
        show pov shocked at left
        mis "You know, public space and all."
        show pov embarrassed_talk at left
        show misc smirk at right
        pov "Don’t worry, I understand."
        show pov smirk_talk at left
        show misc neutral at right
        pov "If it’s any help, the feeling is mutual."
        show pov neutral at left
        show misc neutral_talk at right
        mis "Please, sit down!"
        mis "It’s been a while since we’ve last managed to find some time to each other and I really want some company right now."
        show pov embarrassed_talk at left
        show misc neutral at right
        pov "You had but to ask."

        ##-Allaway and Mc sit down facing one another, the only variant here is that they are holding hands over the table-
        show pov smirk_talk at left
        show misc smirk at right
        pov "You are quite clingy today."
        show pov neutral at left
        show misc neutral_talk at right
        mis "Can you blame me?"
        show pov embarrassed at left
        show misc embarrassed_talk at right
        mis "Last time we talked you were thinking it would have been better if you had disappeared instead."
        show misc shocked_talk at right
        mis "I’m worried about your mental health."
        show pov embarrassed_talk at left
        show misc sad at right
        pov "Normally you call me when you are that worried."
        show pov embarrassed at left
        show misc sad_talk at right
        mis "I figured you needed a night to collect your thoughts."
        show pov neutral at left
        show misc embarrassed_talk at right
        mis "As much as I worry, I don’t want to be the type of girlfriend who constantly spams your inbox and demands to know where you are 24/7."
        show misc neutral_talk at right
        mis "I respect your privacy and know you’ll come to me if there is an issue."
        show pov embarrassed_talk at left
        show misc embarrassed at right
        pov "You really are my dream girl, you know that?"
        show pov smirk at left
        show misc embarrassed_talk at right
        mis "There you go saying stuff like that again!"
        show misc smirk_talk at right
        mis "Don’t get me all blushing in public!"
        show pov embarrassed_talk at left
        show misc smirk at right
        pov "I can’t help myself sometimes."
        show pov neutral_talk at left
        pov "So, you having a coffee?"
        show pov neutral at left
        show misc neutral_talk at right
        mis "Yeah, as much as things are weird nowadays, I still want to be able to enjoy myself from time to time."
        show pov neutral_talk at left
        show misc confused at right
        pov "That’s fair enough, how are you handling the news of the new security system?"
        show pov confused at left
        show misc embarrassed_talk at right
        mis "I’m not at all comfortable knowing some strangers want to install a full security system I didn’t ask for."
        show misc confused_talk at right
        mis "But then again, I guess i’ll have to see how it performs in school."
        show pov confused_talk at left
        show misc bored at right
        pov "They are installing one at school?"
        show pov confused at left
        show misc confused_talk at right
        mis "Yeah, Lashley was quite adamant about it when she informed us."
        show pov shocked at left
        show misc bored_talk at right
        mis "She seems to be quite trustful of the company so I’ll take her word for it."
        show pov embarrassed at left
        show misc shocked_talk at right
        mis "But for now I’ll stick to locking doors and windows until i’ve read some reviews."
        show pov embarrassed_talk at left
        show misc embarrassed at right
        pov "Probably a smart choice, still, I can’t help but worry about you."
        show pov neutral at left
        show misc embarrassed_talk at right
        mis "You know I have your number on speed dial in case anything happens."
        show misc smirk_talk at right
        mis "Plus, my apartment has a gate with a buzzer to enter the complex so I feel more secure with that."
        show misc neutral_talk at right
        mis "Not to mention I live on the fourth floor so I can at least rest easy knowing no one is gonna go climbing the windows anytime soon."
        show pov smirk_talk at left
        show misc smirk at right
        pov "If you wanted me to, I could-"
        show pov neutral at left
        show misc smirk_talk at right
        mis "If you are going that far, just ask me for a key, you goober!"
        show pov neutral_talk at left
        show misc smirk at right
        pov "Can’t blame me for being romantic."
        show pov shocked at left
        show misc smirk_talk at right
        mis "More like reckless and idiotic."
        show pov embarrassed at left
        show misc shocked_talk at right
        mis "You already worry me enough for me to also worry about you falling off my window or getting caught and arrested if the landlord spots you!"
        show pov smirk at left
        show misc neutral_talk at right
        mis "Don’t worry about me, I’ll be fine!"
        show pov smirk_talk at left
        show misc neutral at right
        pov "Is it me, or are we telling each other that far too often lately?"
        show pov smirk at left
        show misc smirk_talk at right
        mis "I’m hoping the repetition will keep you from going out of your way and doing something stupid."
        show pov embarrassed_talk at left
        show misc smirk at right
        pov "Me going out of my way and doing something stupid is what lead us to this point you know?"
        show pov smirk at left
        show misc smirk_talk at right
        mis "You saying that gets me both incredibly flustered and upset at the same time, you know?"
        show pov embarrassed_talk at left
        show misc smirk at right
        pov "Well, I do like seeing you blush and you are quite cute when you are upset."
        show pov neutral at left
        show misc embarrassed_talk at right
        mis "Alright, Casanova, cool it with the lines, we are in public and I’ll get real upset if you get us caught because of me blushing like a schoolgirl again."
        show pov embarrassed_talk at left
        show misc neutral at right
        pov "Sorry."
        show pov neutral at left
        show misc neutral_talk at right
        mis "So, what are you up to today?"
        show pov embarrassed at left
        show misc bored_talk at right
        mis "I doubt you came to the cafe specifically to see me."
        show pov embarrassed_talk at left
        show misc bored at right
        pov "It is a nice surprise I do plan to enjoy for as much as I can."
        show pov embarrassed at left
        show misc shocked_talk at right
        mis "W-What did I say about the lines?!"
        mis "I’m seriously gonna smack you!"
        show pov smirk_talk at left
        show misc angry at right
        pov "Hehehehe."
        show pov smirk at left
        show misc angry_talk at right
        mis "Ugh, you are lucky that I love you…"
        show pov neutral_talk at left
        show misc angry at right
        pov "You can say that again."

        ##-An embarrassed Allaway proceeds to pinch the Mc’s hand she is holding-
        show pov shocked_talk at left
        show misc angry at right
        pov "Yeowch!"
        show pov embarrassed at left
        show misc angry_talk at right
        mis "I warned you!"
        show pov neutral_talk at left
        show misc smirk at right
        pov "Alright, alright, I’ll stop!"
        show pov embarrassed_talk at left
        show misc neutral at right
        pov "I’m just going around town and figured I may stop by the cafe."
        show pov embarrassed at left
        show misc confused_talk at right
        mis "And just what are you up to around town?"
        show pov bored_talk at left
        show misc confused at right
        pov "So far just getting accustomed to it."
        show pov embarrassed_talk at left
        pov "Taking a nice stroll around town."
        show pov confused_talk at left
        show misc bored at right
        pov "Say, do you happen to know of anything strange going on in the town?"
        show pov embarrassed at left
        show misc bored_talk at right
        mis "Is that a trick question or something?"
        show misc shocked_talk at right
        mis "Have you not noticed everything going on around town lately?"
        show pov embarrassed_talk at left
        show misc bored at right
        pov "Okay, that’s fair enough, but I meant something older and hopefully less traumatic."
        show pov embarrassed at left
        show misc smirk_talk at right
        mis "Well, my boyfriend does happen to be a nudist and-"
        show pov shocked_talk at left
        show misc confused at right
        pov "I-I meant something like a town legend or interesting rumor?"
        show pov embarrassed at left
        show misc confused_talk at right
        mis "Why so curious about it?"
        show pov embarrassed_talk at left
        show misc bored at right
        pov "W-Well, I-"
        show pov embarrassed at left
        show misc bored_talk at right
        mis "Oh, could you have chosen a topic for your end of semester essay?"
        show pov shocked_talk at left
        show misc bored at right
        pov "Uh… Y-Yeah, actually!"
        show pov embarrassed_talk at left
        show misc confused at right
        pov "I kind of figured it would be a nice topic to also get myself to know about the town and its history."
        show pov smirk_talk at left
        show misc neutral at right
        pov "Kill two birds with one stone and all."
        show pov embarrassed at left
        show misc neutral_talk at right
        mis "That’s a wonderful idea!"
        mis "I’m happy to see you are taking your assignments seriously even with everything going on!"
        show pov embarrassed_talk at left
        show misc bored at right
        pov "Well, as fun as summer school may be with you, I wouldn’t want to disappoint you."
        show pov embarrassed at left
        show misc smirk_talk at right
        mis "Very funny. I’ve warned you before what going to summer school would get you and it isn’t a quicker way under my pants."
        show pov shocked at left
        show misc bored_talk at right
        mis "A well educated man is the biggest turn on for me, you know?"
        show pov shocked_talk at left
        show misc bored at right
        pov "Oh?"
        show pov smirk_talk at left
        show misc smirk at right
        pov "Then how would you feel if I told you my plans to go to university?"
        show pov smirk at left
        show misc smirk_talk at right
        mis "Oooh baby, now you are talking~"
        show pov smirk_talk at left
        show misc neutral at right
        pov "Work hard and graduate with honours, perhaps aim for valedictorian and top of my class?"
        show pov smirk at left
        show misc smirk_talk at right
        mis "Boy did it just get hot in here? I swear I wasn’t this moist between my legs just a second ago."
        show pov shocked_talk at left
        show misc smirk at right
        pov "Go a semester abroad, join the dean’s list, work on a thesis or an academic paper…"
        show pov smirk_talk at left
        pov "Perhaps even start a Masters in the way for a Doctorate?"
        show pov smirk at left
        show misc smirk_talk at right
        mis "STOP!"
        show misc embarrassed_talk at right
        mis "A woman can only get so horny before she pounces on you and you get ravaged."
        show misc smirk_talk at right
        mis "Really not up to get us caught doing it just yet."
        show pov smirk_talk at left
        show misc smirk at right
        pov "Nothing of what you just said makes me want to stop whatsoever."

        ##-An even more embarrassed Allaway pinches the Mc’s hand again-
        show pov shocked_talk at left
        show misc smirk at right
        pov "Ow ow ow ow ow! Ok, ok, that’s gonna do it!"
        show pov smirk at left
        show misc angry_talk at right
        mis "Ugh, you are so annoying sometimes…"
        show pov smirk_talk at left
        show misc smirk at right
        pov "But you still love me, right?"
        show pov smirk at left
        show misc embarrassed_talk at right
        mis "Sadly, I do."
        mis "Very much."
        show pov neutral at left
        show misc shocked_talk at right
        mis "Now, as for your question."
        show misc confused_talk at right
        mis "I think you should ask some of your classmates."
        mis "Local legends and stuff elude me, but if it’s something worth gossiping about, I’m sure they are going to be the first to know."
        show pov embarrassed at left
        show misc bored_talk at right
        mis "Plus, this way you get to hold more conversations with them and get even closer to the townsfolk!"
        show pov confused at left
        show misc smirk_talk at right
        mis "What kind of girlfriend, or teacher for that matter, would I be if I prevented you from growing and getting close to people?"
        show pov smirk_talk at left
        show misc smirk at right
        pov "I dunno, a possessive one?"
        show pov smirk at left
        show misc smirk_talk at right
        mis "Oh, I think I’m already quite possessive of you, considering everything we get to do behind closed doors."
        show pov embarrassed_talk at left
        show misc neutral at right
        pov "Okay, that’s fair enough."
        show pov embarrassed at left
        show misc neutral_talk at right
        mis "I recommend you start with Cole or Jacob!"
        mis "They are both quite sociable and seem to like you, so hopefully you’ll get something out of them."
        show pov neutral at left
        show misc confused_talk at right
        mis "You can find Cole at the school at this hour and Jacob usually hangs around the comic book store I believe."
        show pov neutral_talk at left
        show misc embarrassed at right
        pov "Thanks, Allaway, I guess it’s a better start than nothing."
        show pov neutral at left
        show misc neutral_talk at right
        mis "Don’t mention it, I’m happy to help if it means you are taking your studies seriously."
        show pov smirk at left
        show misc smirk_talk at right
        mis "I may know just how to reward you if you do well in your exams, actually~"
        show pov smirk_talk at left
        show misc neutral at right
        pov "Really?"
        show pov neutral_talk at left
        show misc smirk at right
        pov "Now you got me interested."
        show pov shocked at left
        show misc smirk_talk at right
        mis "What would you say to having a bit of a role reversal?"
        show pov smirk at left
        mis "I happened to find online a cute school girl outfit, but it seems to be a few sizes too small on me, but still quite functional for what I have in mind~"
        show pov smirk_talk at left
        show misc smirk at right
        pov "Oh, I love you."
        show pov neutral at left
        show misc smirk_talk at right
        mis "I know~"
        show pov smirk at left
        show misc neutral_talk at right
        mis "Now hit the books and be sure to call me soon, I could use a night out with my man."
        show pov neutral_talk at left
        show misc neutral at right
        pov "Duly noted, I’ll get everything sorted and take you out, I promise."
        show pov neutral at left
        show misc smirk_talk at right
        mis "Good boy!"
        show pov smirk at left
        show misc smirk_talk at right
        mis "See you soon~"

        ##=RESULT END=



    ##-If Allaway was picked and has not been romanced-
    else:
        show pov neutral_talk at left
        with dissolve
        show misc neutral at right
        with dissolve
        pov "Hello, Miss Allaway."
        show pov embarrassed at left
        show misc neutral_talk at right
        mis "Oh hey, [povname]. Fancy meeting you here!"
        mis "Coming over for a cup of coffee?"
        show pov embarrassed_talk at left
        show misc neutral at right
        pov "Mainly just roaming around town."
        show pov shocked at left
        show misc embarrassed_talk at right
        mis "Staying out of trouble too, I hope."
        show pov embarrassed_talk at left
        show misc smirk at right
        pov "To the best of my ability, but you never know with my kind of luck."
        show pov shocked at left
        show misc embarrassed_talk at right
        mis "That doesn't comfort me at all. Must I remind you that you are already under supervision because of what happened recently?"
        show pov embarrassed at left
        mis "Please do your best to stay out of trouble..."
        show pov embarrassed_talk at left
        show misc neutral at right
        pov "I know, I know."
        pov "It was just a joke, believe me when I say I'm not looking to wake up besides a lake naked again."
        show pov bored_talk at left
        show misc smirk at right
        pov "Really not my definition of a good time."
        show pov shocked at left
        show misc smirk_talk at right
        mis "You should know you aren’t in the exact position to make those sort of jokes."
        show pov bored_talk at left
        show misc embarrassed at right
        pov "I know, I know."
        show pov embarrassed_talk at left
        show misc neutral at right
        pov "Still, better to look at it with a bit of humour than to wallow in self-pity and embarrassment."
        show pov neutral at left
        show misc embarrassed_talk at right
        mis "I guess you got a point in there."
        show misc neutral_talk at right
        mis "Glad to see you are putting the effort to move past this."
        show pov embarrassed_talk at left
        show misc neutral at right
        pov "Pretty sure it's gonna be forgotten soon enough if things keep escalating in town like this."
        show pov embarrassed at left
        show misc embarrassed_talk at right
        mis "Let’s hope that doesn’t become entirely the case."
        show misc shocked_talk at right
        mis "Changing the subject though, I hope you are putting as much effort in your final essay as you are moving past all of this."
        show pov embarrassed_talk at left
        show misc confused at right
        pov "Well, you know-"
        show pov shocked at left
        show misc bored_talk at right
        mis "It is important [povname]."
        show pov bored at left
        show misc confused_talk at right
        mis "Besides, with everything going on around town, I’m certain there's plenty enough things to write and draw inspiration from."
        show pov bored_talk at left
        show misc embarrassed at right
        pov "Well, since you opened the subject."
        show pov confused_talk at left
        show misc confused at right
        pov "Do you happen to know of anything strange going on in the town?"
        show pov confused at left
        show misc confused_talk at right
        mis "Is that a trick question or something?"
        show pov bored at left
        show misc angry_talk at right
        mis "Have you not noticed everything going on around town lately?"
        show pov bored_talk at left
        show misc angry at right
        pov "Okay, that’s fair enough, but I meant something older and hopefully less traumatic."
        show pov confused_talk at left
        show misc embarrassed at right
        pov "Something like a town legend or interesting rumor?"
        show pov embarrassed at left
        show misc embarrassed_talk at right
        mis "Is this related to your essay?"
        show pov shocked_talk at left
        show misc confused at right
        pov "U-Uh, yeah!"
        show pov confused_talk at left
        show misc shocked at right
        pov "Figured it would be a nice topic to also get myself to know more about the town."
        show pov smirk_talk at left
        show misc neutral at right
        pov "Kill two birds with one stone and all."
        show pov embarrassed at left
        show misc smirk_talk at right
        mis "That’s a wonderful idea!"
        show misc neutral_talk at right
        mis "I’m happy to see you are taking your assignments seriously even with everything going on!"
        show pov embarrassed_talk at left
        show misc shocked at right
        pov "Well, as fun as summer school may be with you, I wouldn’t want to disappoint you."
        show pov embarrassed at left
        show misc smirk_talk at right
        mis "Oh, you really don’t want to find out how bad summer courses with me can be."
        show pov smirk at left
        show misc bored_talk at right
        mis "It is my summer too and I don’t plan on spending it babysitting."
        show misc smirk_talk at right
        mis "So do your best not to fail now."
        show pov smirk_talk at left
        show misc embarrassed at right
        pov "Duly noted."
        show pov confused at left
        show misc embarrassed_talk at right
        mis "Now, as for your question."
        mis "I think you should ask some of your classmates."
        show pov bored at left
        show misc bored_talk at right
        mis "Local legends and stuff elude me, but if it’s something worth gossiping about, I’m sure they are going to be the first to know."
        show pov neutral at left
        show misc smirk_talk at right
        mis "Plus, this way you get to hold more conversations with them and get even closer to the townsfolk!"
        show pov neutral_talk at left
        show misc confused at right
        pov "Okay, that's as good of a place to start as any."
        show pov neutral at left
        show misc shocked_talk at right
        mis "I recommend you start with Cole or Jacob!"
        show misc smirk at right
        mis "They are both quite sociable and seem to like you, so hopefully you’ll get something out of them."
        show misc bored at right
        mis "You can find Cole at the school at this hour and Jacob usually hangs around the comic book store I believe."
        show pov embarrassed at left
        show misc smirk_talk at right
        mis "I found him skipping class in there one day, scared the crap out of him and landed him on detention for two weeks."
        show pov embarrassed_talk at left
        show misc embarrassed at right
        pov "How did you catch him if you were giving class that day?"
        show pov confused at left
        show misc embarrassed_talk  at right
        mis "It was my day off and I was out on a run when I caught him."
        show pov embarrassed at left
        show misc smirk_talk at right
        mis "It was mainly the fact he tried to bullshit his way out of it what made me give him detention."
        mis "Just tell it like it is! One day off isn’t gonna ruin your academic year, but don’t just lie straight to my face, I hate that!"
        show pov embarrassed_talk at left
        show misc smirk at right
        pov "That’s fair enough, I suppose."
        show pov neutral_talk at left
        show misc neutral at right
        pov "Well, thank you Allaway, I guess I know where to head to next."
        show pov neutral at left
        show misc neutral_talk at right
        mis "No problem, [povname]."
        show pov shocked at left
        show misc smirk_talk at right
        mis "Your topic for your essay sounds really interesting so I can’t wait to read it!"
        show pov embarrassed at left
        show misc shocked_talk at right
        mis "Now, if you excuse me, I’ll continue my drink and reading."
        show pov embarrassed_talk at left
        show misc smirk at right
        pov "I’ll leave you quite surprised if things go my way."
        show pov neutral_talk at left
        show misc embarrassed at right
        pov "And of course! Sorry for bothering you."
        show pov smirk_talk at left
        show misc neutral at right
        pov "I’ll see you in class!"
        show pov neutral at left
        show misc neutral_talk at right
        mis "See you there!"

    jump lbl_cafeoutside_day_setup
    ##=SCENE END=
