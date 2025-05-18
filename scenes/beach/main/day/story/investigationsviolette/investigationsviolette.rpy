##[Beach, afternoon - “Investigations_Violette”  - main_story =84-H]

##-The Mc approaches Violette who is looking at a clipboard-
label lbl_investigations_violette:
    default investigations_violette = 0
    show btn beachmain_day_chair_idle
    $ renpy.pause(0.001)

    if beach_naked == 0:
        pov "{i}I'll need to get naked first, otherwise she'll scold me.{/i}"
        jump lbl_beachmain_day_setup

    elif investigations_violette != 0:
        pov "{i}I'll leave her to her work just now.{/i}"
        jump lbl_beachmain_day_setup

    show povn neutral_talk at left
    with dissolve
    show vio confused at right
    hide btn beachmain_day_chair_idle
    with dissolve
    pov "Hi, Violette!"
    show vio embarrassed at right
    vio "Hey, [povname], nice to see ya!"
    show povn embarrassed_talk at left
    pov "Sorry, did I catch you in the middle of work?"
    show povn embarrassed at left
    show vio embarrassed_talk at right
    vio "Nah, I’m just in the middle of some mild paperwork."
    show vio bored_talk at right
    vio "Gotta do it once in a while, keep inventory of all my equipment and report any incidents worth noting."
    show povn neutral at left
    show vio neutral_talk at right
    vio "It’s nothing too difficult but it can get tedious at times."
    show povn neutral_talk at left
    show vio neutral at right
    pov "I can imagine."
    show povn embarrassed_talk at left
    pov "Say, I actually wanted to ask you about a certain incident."
    show povn embarrassed at left
    show vio neutral_talk at right
    vio "You got something to report?"
    show vio smirk_talk at right
    vio "Great, that’s just 3 more pages of paperwork for me then..."
    vio "Are kids painting obscene graffiti on the rocks again?"
    show povn neutral at left
    show vio bored_talk at right
    vio "I told those little scamps I would have their parents force them to clean the paint out of the rocks with their toothbrushes if they did so again!"
    show povn embarrassed_talk at left
    show vio bored at right
    pov "No, I’m not reporting anything."
    show povn smirk_talk at left
    show vio smirk at right
    pov "And last time I checked, the rocks were just fine."
    show povn neutral_talk at left
    pov "I just wanted to ask you something about the beach."
    show povn neutral at left
    show vio smirk_talk at right
    vio "Oh, good."
    show povn smirk at left
    vio "You just saved me a morning migraine, then."
    show povn neutral at left
    show vio bored_talk at right
    vio "Sure dude, what can I help you with?"
    show povn embarrassed_talk at left
    show vio bored at right
    pov "Well, I’ve heard a rumor circling around town about something weird going on at the beach that you’ve come to take notice of."
    pov "I was hoping to find out what it was from the source rather than trust random rumors."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "Well, aren’t you a nosy little man?"
    show vio bored_talk at right
    vio "What’s got you so interested about it?"
    show povn smirk_talk at left
    show vio shocked at right
    pov "Don’t mean to be nosy. I just decided to do a paper about weird stuff happening around town for school so I figured I would ask the locals, you know?"
    show povn embarrassed_talk at left
    show vio smirk at right
    pov "Get to also know the town a little more that way as well."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "Huh, is that so?"
    vio "Not a bad idea for a class project."
    show vio shocked_talk at right
    vio "I mainly used to talk about whatever the internet thought interesting at the moment."
    show vio bored_talk at right
    vio "The copy-n-paste technique saved me many summers of boredom and let me in the waves and sand that I love."
    show povn neutral at left
    show vio smirk_talk at right
    vio "Alright, I’ll help ya out."
    show povn neutral_talk at left
    show vio neutral at right
    pov "You will?"
    show povn neutral at left
    show vio neutral_talk at right
    vio "Yeah! Plus, talking with you beats the paperwork any day now."
    show povn embarrassed at left
    show vio smirk at right
    vio "And it’s not like I’m doing anything else right now, the beach is mostly empty anyway."
    show povn embarrassed_talk at left
    show vio smirk at right
    pov "I really appreciate it, thanks a ton."
    show povn embarrassed at left
    show vio bored_talk at right
    vio "Eh, don’t think too much about it, I will call you in for a favour later though."
    show povn embarrassed_talk at left
    show vio smirk at right
    pov "Sounds fair, I suppose."
    show povn embarrassed at left
    show vio bored_talk at right
    vio "Well, to make a long story short, I have been noticing people sort of appear out of nowhere lately."
    show povn confused_talk at left
    show vio bored at right
    pov "What do you mean?"
    show povn confused at left
    show vio bored_talk at right
    vio "Well, think of it this way."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "My whole job is lifeguard duties, right?"
    show vio bored_talk at right
    vio "A lot of the time I stay on my tower observing the crowd as I make sure nothing is wrong."
    vio "I take my job quite seriously and I’d even say I am damn good at what I do."
    show povn confused at left
    show vio smirk_talk at right
    vio "I can spot people trying to sneak around and try to bother girls or take pics of them without their consent better than a shark can smell blood in the ocean."
    show povn shocked at left
    show vio confused_talk at right
    vio "Hell, I can even spot you forgetting to take off your clothes when you enter the beach area even when I have my back turned to the changing rooms!"
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "I’m damn good at what I do and taking care of the people on my beach."
    show vio shocked_talk at right
    vio "So when people I didn’t even see come into the beach start just suddenly appearing out of nowhere, I know something is wrong."
    show povn embarrassed_talk at left
    show vio smirk at right
    pov "Sounds like you have been dealing with it for a while."
    show povn embarrassed at left
    show vio bored_talk at right
    vio "It happened from time to time that I didn’t pay too much attention to it."
    show vio confused_talk at right
    vio "Figured I was just distracted or let my mind wander too much out of boredom."
    show povn confused at left
    show vio shocked_talk at right
    vio "But lately I seem to turn around for a second or two and when I look back there are three more people in the water out of nowhere when I counted just six before."
    show povn smirk_talk at left
    show vio smirk at right
    pov "Dang, that does sound freaky."
    show povn confused at left
    show vio smirk_talk at right
    vio "Not to mention a huge potential risk as a lifeguard."
    show povn embarrassed at left
    show vio bored_talk at right
    vio "I mean, what good is a lifeguard who doesn't even keep track on how many people are in the water or isn’t paying full attention to it?"
    show povn shocked at left
    show vio embarrassed_talk at right
    vio "My biggest fear is someone drowning or getting injured because of it."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "Maybe I need to get glasses or something, perhaps hire some extra help to keep me focused?"
    show povn embarrassed_talk at left
    show vio smirk at right
    pov "I’m sure you’ll think of something. I know you are a damn good lifeguard so I doubt anyone is going to be in danger with you around."
    pov "Even if they appeared out of nowhere."
    show povn embarrassed at left
    show vio smirk_talk at right
    vio "That’s sweet of you to say, thank you for believing in me, [povname]."
    show povn embarrassed_talk at left
    show vio smirk at right
    pov "That’s easy to do."
    show povn shocked at left
    show vio smirk_talk at right
    vio "Awww!"
    show povn embarrassed_talk at left
    show vio bored_talk at right
    vio "Well, mushy stuff aside, I hoped that helped you out with your report thingy."
    show povn neutral_talk at left
    show vio smirk at right
    pov "It definitely did!"
    show povn embarrassed_talk at left
    vio "I tried talking to Sam at the mall about it but he went on raving about Doppelgangers and I kind of walked away quietly."
    show povn smirk at left
    show vio bored_talk at right
    vio "He is a nice guy and all, but he kinda creeps me out."
    show povn embarrassed at left
    show vio smirk_talk at right
    pov "No one can blame you for that."
    show povn confused_talk at left
    show vio smirk at right
    pov "Still, Doppelgangers?"
    show povn bored at left
    show vio bored_talk at right
    vio "Those monsters that look exactly like you?"
    show vio smirk_talk at right
    vio "Apparently if you meet your copy it would try to kill you to take your place or something, I kinda zoned out once he bombarded me with the whole explanation."
    show povn embarrassed at left
    vio "Still, I don’t want to imagine a copy of myself coming out of the water and coming to kill me. I have enough to worry about as it is!"
    show povn smirk_talk at left
    show vio smirk at right
    pov "Coming out of the water?"
    show povn smirk at left
    show vio smirk_talk at right
    vio "Yeah, that’s why I’m concerned about it."
    show povn embarrassed at left
    show vio shocked_talk at right
    vio "People just show up in the water out of nowhere."
    show povn confused_talk at left
    show vio smirk at right
    pov "Is that so…"
    show povn embarrassed_talk at left
    show vio neutral at right
    pov "Well, thanks again Violette, it was a big help."
    show povn embarrassed at left
    show vio neutral_talk at right
    vio "Glad I could help. Keep in mind you owe me a favour though!"
    show povn neutral at left
    show vio bored_talk at right
    vio "Now, if you’ll excuse me, I have to get back to paperwork."
    show vio smirk_talk at right
    vio "Talk to ya later, man. Do remember to keep your cute nudist ass on beach perimeters, okay?"
    show povn smirk_talk at left
    show vio smirk at right
    pov "You had to bring that up again, didn’t you?"
    show povn neutral at left
    show vio neutral_talk at right
    vio "Hehehe, just making sure you follow the rules~"

    $ investigations_violette = 1

    jump lbl_beachmain_day_setup
    ##=SCENE END=
