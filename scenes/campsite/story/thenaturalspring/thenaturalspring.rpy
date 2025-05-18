## The Natural Spring
label lbl_the_natural_spring:
    ## Time skip to after the tent has been built
    scene black
    with fade
    $ renpy.pause()
    "After a lot of pain and struggle getting the camp set up..."

    scene bg campsite_3
    with fade

    show pov embarrassed_talk
    with dissolve
    pov "{i}*Phew*{/i}"
    pov "I- should’ve asked them to stay to help."
    pov "Pitching a tent definitely requires more than one pair of hands…"
    pov "Ah well, I did say I could do it."
    pov "I didn’t wanna disappoint them and have them get their hands dirty too."
    show pov confused_talk
    pov "Anyway, I guess I’m done here and I can go meet them at the-"
    pov "Wherever they are…"
    pov "What did she say? Follow this path?"
    show pov bored_talk
    pov "I hope this isn’t an hour long walk to the next state over."
    pov "My back hurts."

    ## Time skip to the spring
    scene black
    with fade
    "After a few minutes of walking down the path..."

    if winc == 0:
        pov "[missus]? [sister]?!"
    else:
        pov "Mom? [sister]?!"
    pov "You guys here? I’m done with with tent-"
    pov "Oh- "

    mum "[povname]! Finally, we thought you’d never show up."

    ## CG of them in the hot spring.
    scene bg thenaturalspring_1
    with fade

    pov "What the fuck? This is so cool!"

    sis "{i}*Sigh*{/i} Yeah, this place is literally heaven."

    mum "Tsk! [povname]! Was that language really necessary?"
    mum "Come on, join us in here and relax."

    if winc == 0:
        sis "You’re right, [missus]. I am really enjoying this trip."
    else:
        sis "You’re right, mom. I am really enjoying this trip."

    mum "And it hasn’t even started, hon."
    mum "{i}*Sigh*{/i}"
    mum "I really needed this."
    mum "All that’s missing is a monkey to massage my back and feed me a platter of fruits."

    sis "I’m okay without the monkey but a massage would definitely hit the spot."

    pov "You guys sure it’s okay for me to join."

    mum "Oh c’mon, [povname]."
    mum "Don’t be so shy, just hop in."
    mum "We have the whole place to ourselves this weekend."
    mum "Thank God for that."

    sis "Yeah, you really did pick a great weekend."

    mum "Not to ruin the magic but I did just reserve it for us."
    mum "There’s an actual booking process for this camp area."

    sis "Aye, doesn’t make this any less nice."
    sis "Anyway, hurry up, [povname]."
    sis "Don’t stand there oogling at us like a perv."

    mum "He’s not a perv, don’t call [povname] that."
    mum "Don’t make me count to 10, sweetie."

    pov "I’m coming! Don’t rush me."


    ## You’re now in the spring with them, close to each other.
    scene black
    with fade
    $ renpy.pause(2,hard=True)

    scene thenaturalspring_hscene1
    with fade

    mum "Did you have a hard time with the tent?"

    pov "Not really. It was as easy as I expected it to be."

    sis "Then why’d you take forever?"

    pov "I was enjoying being outside. What’s the rush, it’s not like the sun is setting."

    sis "Psssh, sure."

    mum "I haven’t seen it yet but I know you did a tremendous job, honey."
    mum "Thank you for doing that."

    pov "Did you guys get some girl-on-girl bonding?"

    mum "Yeah, you could say that~"

    if winc == 0:
        sis "[missus] lectured me about being grateful and being part of the household means doing things I don’t exactly want to do."
    else:
        sis "Mom lectured me about being grateful and being part of the family means doing things I don’t exactly want to do."

    pov "You needed the lecture to be honest."

    sis "I’m gonna shut my ears and enjoy being here."
    sis "I expect not to be nagged at starting now."

    mum "Fine fine."
    mum "Last thing I want is for you to hop-skip-skidaddle back home before our camping trip is over."

    if winc == 0:
        pov "Yeah, if a bear attacks us, I’ll need someone to trip and I’m not tripping [missus]."
    else:
        pov "Yeah, if a bear attacks us, I’ll need someone to trip and I’m not tripping mom."

    sis "I can run faster than you and I’m way more nimble."

    mum "There’s no bears here. Don’t say that kind of stuff."

    if winc == 0:
        pov "You know I’m kidding right, [missus]?"
    else:
        pov "You know I’m kidding right, mom?"

    mum "Of course, honey."
    mum "Har har har."

    sis "What are we doing after this?"

    mum "I was thinking we would go for a hike."
    mum "There’s a popular trail that should take us to a nice picnic spot."

    sis "A hike…?"

    mum "C’mon. What did I say about the attitude?"

    sis "Right right…"

    pov "I could definitely use the exercise! What’s a camping trip without a little hike anyway?"

    if winc == 0:
        mum "See, this is why you’re my favourite person."

        sis "[missus]!"
    else:
        mum "See, this is why you’re my favourite kid."

        sis "MOM!"

    mum "I can joke too! I love you both equally."
    mum "I just do not like your attitude right now, [sister]."

    sis "You know what, that’s so fair."

    mum "Let’s finish each other off and we’ll head back in half an hour? I don’t wanna be too shribbly."

    pov "Sounds good."

label lbl_the_natural_spring_hscene:
    scene thenaturalspring_hscene2

    ## They continue playing with each other until they all cum in the spring
    $ renpy.pause()
    
    menu:
        "Cum":
            pass
        "Continue":
            jump lbl_the_natural_spring_hscene

    scene bg thenaturalspring_2_5
    with vpunch
    $ renpy.pause()
    pov "{i}*Pants*{/i}"
    pov "Thanks, girls."
    pov "I feel- totally relaxed now."

    mum "Good to hear, honey."

    sis "I'm not ready to leave yet."

    ## SCENE END

    $ mumsiscamp_path = 5

    jump lbl_the_purple_trail

image thenaturalspring_hscene1:
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_1.jpg"
    pause 0.4
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_2.jpg"
    pause 0.4
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_3.jpg"
    pause 0.4
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_4.jpg"
    pause 0.4
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_2.jpg"
    pause 0.4
    repeat

image thenaturalspring_hscene2:
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_1.jpg"
    pause 0.25
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_2.jpg"
    pause 0.25
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_3.jpg"
    pause 0.25
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_4.jpg"
    pause 0.25
    "/scenes/campsite/story/thenaturalspring/assets/bg_thenaturalspring_2_2.jpg"
    pause 0.25
    repeat
