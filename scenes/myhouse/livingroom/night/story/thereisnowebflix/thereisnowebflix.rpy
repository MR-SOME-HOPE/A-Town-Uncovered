## There is No Webflix

label lbl_there_is_no_webflix:
    #-Mc and Effie end up in his living room after the previous scene-
    # CG of them lounging, cuddling on the couch watching TV together...

    scene bg thereisnowebflix_1
    show effeyes neutral_thereisnowebflix
    show effmouth neutral_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    with dissolve
    pov "Effie, why were you so adamant we made a stop here?"

    show effeyes shocked_thereisnowebflix
    show povmouth boredtalk_thereisnowebflix
    pov "We are gonna miss the movie, at this rate."
    show effmouth neutraltalk_thereisnowebflix
    show poveyebrows shocked_thereisnowebflix
    show povmouth bored_thereisnowebflix

    eff "Don’t be silly, [povname]. We aren’t going to the movie theater."
    show effmouth neutral_thereisnowebflix
    show povmouth boredtalk_thereisnowebflix
    pov "We are not?"

    show effeyes confused_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show povmouth bored_thereisnowebflix
    eff "All I told my dad and what I heard you tell him, was that we were going to go watch a movie, right?"
    show effeyes neutral_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    eff "That means, he too likely believes we are going to the movie theater."
    show effeyes shocked_thereisnowebflix
    show effmouth boredtalk_thereisnowebflix
    show povmouth neutral_thereisnowebflix

    eff "But if the plan all along was to watch a movie at your house, then not only can he not spy on us, but he also can’t be mad he mistook the place~."
    show effeyes confused_thereisnowebflix
    show effmouth bored_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "Is that kind of logic really going to work on him?"
    show poveyebrows shocked_thereisnowebflix
    show povmouth boredtalk_thereisnowebflix
    pov "Wouldn’t he just be angrier if he learned you were at my house?"
    show effeyes neutral_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show povmouth bored_thereisnowebflix
    eff "It’ll be fine! It’s not really the first time that I try to outsmart him like this."

    show effeyes shocked_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    eff "Plus, he had you for a whole 10 minutes, interrogating you. If it didn’t occur to him to ask where we were going to watch the movie specifically, then that’s on him."
    show effeyes confused_thereisnowebflix
    show effmouth neutral_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix

    pov "I still don’t understand how the two of you can have a relationship like this..."
    show effeyes confused_thereisnowebflix
    show effmouth boredtalk_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    eff "Isn’t your old man also a massive a-hole?"

    show poveyebrows neutral_thereisnowebflix
    eff "Hell, I’d argue he is worse than mine sometimes, from what you and [sister] have told me!"
    show effeyes confused_thereisnowebflix
    show effmouth neutral_thereisnowebflix
    show povmouth boredtalk_thereisnowebflix

    pov "Alright, fair point."
    show poveyebrows confused_thereisnowebflix
    pov "But still, has he always been like this?"
    show effeyes shocked_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    eff "No, not at all!"

    show effeyes confused_thereisnowebflix
    eff "When I was a kid, he used to be very carefree, relaxed, and had this policy to not make unnecessary scandals."
    show effmouth neutral_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix

    pov "I genuinely can’t imagine that sort of vibe from him."
    show effeyes sad_thereisnowebflix
    show poveyebrows shocked_thereisnowebflix
    pov "What changed?"
    show effmouth boredtalk_thereisnowebflix
    show povmouth bored_thereisnowebflix
    eff "Well..."

    #-From this point forth, the scene splits itself into 2 variants depending on
    # whether or not the Player has reached the point in the main story where
    # Effie shares her Mom’s backstory. Chapter 110 in main_story-

    #-If the player hasn’t learned about Effie’s mom-

    if main_story < 110:
        show effeyes sad_thereisnowebflix
        show poveyebrows confused_thereisnowebflix
        eff "It’s a bit of a long story that it’s kind of a super sensitive topic for me."
        show effeyes shocked_thereisnowebflix
        eff "So while I don’t want to head into details, I’ll just say that something happened in my childhood that turned him from this super chill guy into what he is now."

        show effmouth bored_thereisnowebflix
        show poveyebrows shocked_thereisnowebflix
        show povmouth boredtalk_thereisnowebflix
        pov "Can you go, even the slightest bit, into more detail than that?"
        show effeyes sad_thereisnowebflix
        show effmouth boredtalk_thereisnowebflix
        show poveyebrows confused_thereisnowebflix
        show povmouth bored_thereisnowebflix
        eff "Like I said, SUPER sensitive topic for me."
        eff "I know we are dating now, and all, but this whole thing is like a major thing, and I’m just not ready to talk about it."
        show effeyes confused_thereisnowebflix
        eff "It’s something I’ve only ever told to like three or four people, ever."
        show effmouth bored_thereisnowebflix
        show poveyebrows sad_thereisnowebflix
        show povmouth boredtalk_thereisnowebflix

        pov "Dang, it’s that serious?"
        show effmouth boredtalk_thereisnowebflix
        show povmouth bored_thereisnowebflix
        eff "Big enough that it completely changed my dad."
        show effeyes confused_thereisnowebflix
        show effmouth neutraltalk_thereisnowebflix
        eff "I promise to tell you sometime in the future."

        show effeyes shocked_thereisnowebflix
        eff "Just not now, when I’m already stressed out as all hell, with him and all his rules."
        show effeyes sad_thereisnowebflix
        show effmouth neutral_thereisnowebflix
        show poveyebrows confused_thereisnowebflix
        show povmouth boredtalk_thereisnowebflix

        pov "Yeah, you said he put a lot on you recently?"

    #-If the player has learned about Effie’s mom-

    else:

        show effeyes sad_thereisnowebflix
        show effmouth bored_thereisnowebflix
        show poveyebrows confused_thereisnowebflix
        show povmouth boredtalk_thereisnowebflix
        pov "It’s your mom, isn’t it?"
        show effmouth boredtalk_thereisnowebflix
        show poveyebrows sad_thereisnowebflix
        show povmouth bored_thereisnowebflix
        eff "Y-Yeah..."
        show effeyes confused_thereisnowebflix
        eff "Glad to see you still remember it."
        show effmouth bored_thereisnowebflix
        show povmouth neutraltalk_thereisnowebflix
        pov "Not really something you forget, Effie."
        show effmouth boredtalk_thereisnowebflix
        show povmouth neutral_thereisnowebflix
        eff "Tell that to my dad and I..."
        show effeyes shocked_thereisnowebflix
        show effmouth neutraltalk_thereisnowebflix
        show poveyebrows confused_thereisnowebflix
        eff "But yes, after her disappearance, all the rumors, and the constant pressure we felt from the whole situation, kinda threw him down a spiral."
        show effeyes shocked_thereisnowebflix
        show poveyebrows sad_thereisnowebflix
        eff "That’s why, even after all he does, I can’t genuinely hate him."
        show effeyes confused_thereisnowebflix
        show effmouth bored_thereisnowebflix
        show povmouth boredtalk_thereisnowebflix

        pov "I can’t imagine what he must have gone through."
        show effeyes sad_thereisnowebflix
        show effmouth boredtalk_thereisnowebflix
        show poveyebrows shocked_thereisnowebflix
        show povmouth bored_thereisnowebflix
        eff "There weren’t many people on his side then."

        show effeyes neutral_thereisnowebflix
        eff "So he doesn’t trust, just anyone now."
        show effeyes confused_thereisnowebflix
        show poveyebrows confused_thereisnowebflix
        eff "I don’t want to see it this way, but it feels like he is taking it out on me sometimes, with all his rules and attitude, especially now that he’s added more."
        show effeyes neutral_thereisnowebflix
        show effmouth bored_thereisnowebflix
        show poveyebrows sad_thereisnowebflix
        show povmouth boredtalk_thereisnowebflix
        pov "Yeah, you said he put a lot on you recently?"

    show effeyes confused_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    show povmouth bored_thereisnowebflix
    eff "I basically had to get on my knees and agree to a bunch of stupid shit so he saw I was serious about you, in order to get his permission to keep seeing you."
    show effeyes shocked_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    eff "It’s like walking on eggshells, in my own freaking house!"
    show effmouth neutral_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix

    pov "And you are willingly putting up with it for me?"
    show effeyes confused_thereisnowebflix
    show poveyebrows sad_thereisnowebflix
    pov "Geez, I don’t know what to say..."

    pov "Though I do feel bad that I’m practically the cause you are under so much pressure now."
    show effmouth neutraltalk_thereisnowebflix
    show povmouth bored_thereisnowebflix
    eff "Please don’t be."
    show effeyes neutral_thereisnowebflix
    eff "I’m doing this because I want to be with you, so if you wanna pay it back, make sure you think of fun dates and pamper me a lot~"
    show effmouth neutral_thereisnowebflix
    show poveyebrows neutral_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "Heh. Can and will do."
    show effeyes confused_thereisnowebflix
    show poveyebrows shocked_thereisnowebflix
    pov "Though what I had planned for our first date kinda revolved around going to the actual movie theater..."
    show effeyes shocked_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    show povmouth bored_thereisnowebflix
    eff "Oh, shoot. I didn’t think about that. You are right!"
    show povmouth neutral_thereisnowebflix

    eff "Holy shit, did I just completely ruin our night?!"
    show effmouth bored_thereisnowebflix
    show poveyebrows neutral_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "Easy there! No one said it was ruined."
    show effeyes sad_thereisnowebflix
    pov "We can totally watch something here!"
    show effeyes confused_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    eff "Won’t we be making a lot of noise? I wouldn’t want to disturb people here..."

    show effmouth neutral_thereisnowebflix
    show poveyebrows shocked_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "Actually, we kind of lucked out. I think everyone’s out tonight."
    show effeyes neutral_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    show povmouth neutral_thereisnowebflix

    eff "Oh, really~?"
    show effmouth neutral_thereisnowebflix
    show poveyebrows neutral_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    pov "Yep, so we can just pick something to watch and-"
    show effmouth neutraltalk_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    eff "Actually, I think I have a better idea on what we should do tonight. If you catch my meaning~"
    show effmouth neutral_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "W-Won’t your dad find out though?"
    show effeyes shocked_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    eff "He thinks we went to the movies, so we got the average length of a movie plus the 30 minute trip to and from the theater."
    show effeyes confused_thereisnowebflix
    eff "It takes about 5 minutes to go from my house to yours."
    show effeyes neutral_thereisnowebflix
    show poveyebrows neutral_thereisnowebflix
    eff "Can you imagine anything fun we can do with 2 and a half spare hours before my dad expects me to be home~?"

    show effeyes shocked_thereisnowebflix
    eff "Especially when we have the house all to ourselves tonight?"
    show effmouth neutral_thereisnowebflix
    show poveyebrows shocked_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "Oh, I definitely like where your mind is at!"
    show effmouth neutraltalk_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    eff "Think of it as my way to make up for messing up your date night plans."
    show effmouth neutral_thereisnowebflix
    show poveyebrows shocked_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "Hell, if that’s the case, then you can mess up my plans as much as you like!"
    show effeyes confused_thereisnowebflix
    show effmouth boredtalk_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    eff "Heh, jerk."
    show effeyes confused_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    eff "Still, we totally, are going on a proper date next time. I actually already have something planned!"
    show effmouth neutral_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "You do?"
    show effeyes confused_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    eff "I was invited to a beach party, next Friday night actually."
    show effeyes neutral_thereisnowebflix
    show poveyebrows neutral_thereisnowebflix
    eff "Figured we could go and have some fun together!"
    show effmouth neutral_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "Sounds like fun!"
    show effeyes sad_thereisnowebflix
    show effmouth boredtalk_thereisnowebflix
    show poveyebrows confused_thereisnowebflix
    show povmouth bored_thereisnowebflix
    eff "Sadly, this is going to be one of the things we’ll need to ask permission from my dad later though."
    show effeyes confused_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show povmouth neutral_thereisnowebflix

    eff "And you’ll have to be with me when I do..."
    show effmouth neutral_thereisnowebflix
    show poveyebrows neutral_thereisnowebflix
    show povmouth neutraltalk_thereisnowebflix
    pov "You think we got a shot at him saying yes?"

    show effeyes neutral_thereisnowebflix
    show effmouth neutraltalk_thereisnowebflix
    show poveyebrows shocked_thereisnowebflix
    show povmouth neutral_thereisnowebflix
    eff "Just leave the talking to me, and let me do my magic."
    show poveyebrows neutral_thereisnowebflix

    eff "Now, enough about that, let’s have some fun~"

    ## HSCENE
    # MC kisses Effie
    #-Effie embraces the MC and the two have sex in the living room before a fade to black-

label lbl_there_is_no_webflix_sex:
    $ thereisnowebflix_sex = 1

    scene bg thereisnowebflix_sex_1
    with fade

label lbl_there_is_no_webflix_sex_0:
    jump lbl_there_is_no_webflix_sex_1


label lbl_there_is_no_webflix_sex_1:
    scene img_there_is_no_webflix_sex_1
    if skill_sta <= 7:
        $ renpy.pause(10,hard=True)
        jump lbl_there_is_no_webflix_sex_cum
    elif skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_there_is_no_webflix_sex_2

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_there_is_no_webflix_sex_2

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_there_is_no_webflix_sex_1

image img_there_is_no_webflix_sex_1:
    "bg thereisnowebflix_sex_1"
    pause 0.3
    "bg thereisnowebflix_sex_2"
    pause 0.1
    "bg thereisnowebflix_sex_3"
    pause 0.1
    "bg thereisnowebflix_sex_4"
    pause 0.2
    "bg thereisnowebflix_sex_2"
    pause 0.2
    repeat

label lbl_there_is_no_webflix_sex_2:
    scene img_there_is_no_webflix_sex_2
    if skill_sta <= 14:
        $ renpy.pause(15,hard=True)
        jump lbl_there_is_no_webflix_sex_cum

    elif skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_there_is_no_webflix_sex_3

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_there_is_no_webflix_sex_2

image img_there_is_no_webflix_sex_2:
    "bg thereisnowebflix_sex_1"
    pause 0.3
    "bg thereisnowebflix_sex_2"
    pause 0.1
    "bg thereisnowebflix_sex_4"
    pause 0.2
    "bg thereisnowebflix_sex_2"
    pause 0.2
    repeat

label lbl_there_is_no_webflix_sex_3:
    scene img_there_is_no_webflix_sex_3
    if skill_sta <= 20:
        $ renpy.pause(20,hard=True)
        jump lbl_there_is_no_webflix_sex_cum

    else:
        $ renpy.pause(10,hard=True)
        jump lbl_there_is_no_webflix_sex_3

image img_there_is_no_webflix_sex_3:
    "bg thereisnowebflix_sex_1"
    pause 0.2
    "bg thereisnowebflix_sex_4"
    pause 0.1
    "bg thereisnowebflix_sex_2"
    pause 0.2
    repeat

label lbl_there_is_no_webflix_sex_cum:
    call screen scr_there_is_no_webflix_sex_cum

screen scr_there_is_no_webflix_sex_cum():
    if skill_sta <= 20:
        imagebutton auto "btn hscene_continue_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_there_is_no_webflix_sex_0")
        imagebutton auto "btn hscene_cum_%s" xpos 0 ypos 0 focus_mask True action Jump("lbl_there_is_no_webflix_sex_cumming")
    else:
        pass

label lbl_there_is_no_webflix_sex_cumming:
    scene bg thereisnowebflix_sex_5_1
    $ renpy.pause(1.5,hard=True)
    show bg thereisnowebflix_sex_5_2
    $ renpy.pause(0.6,hard=True)
    show bg thereisnowebflix_sex_5_3
    $ renpy.pause(0.6,hard=True)
    $ renpy.pause()

    $ effie_path = 15

    scene black
    with fade
    $ renpy.pause()
    "After falling asleep in each other's arms..."

    call lbl_next_date
    call lbl_next_day
    $ gtime = 0

    scene bg mylivingroom_day
    with fade

    pov "{i}Effie must've left...{/i}"
    pov "{i}Quick- I need to get my clothes on before someone catches me...{/i}"

    jump lbl_mylivingroom_day_setup
