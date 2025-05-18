label lbl_rocksolid_modelling:
    default map_blocking = False
    $ map_blocking = False
    #[MC’s Bedroom, Afternoon - “Rock Solid Modeling”  - hitomi_path = 12]#11

    #-Scene takes place in Mc’s room after having brought Hitomi in with him,
    # nobody is at the house currently so she is feeling rather nervous-
    #-Scene fades in with Mc and  Hitomi entering his room-

            ## SPRITEWORK ##

    scene bg mybedroom_day
    with fade

    show pov neutral_talk at left
    show hit embarrassed at right
    with dissolve
    pov "-And we are here!"
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "Again, I’m so sorry for intruding…"
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "I’ve told you, Hitomi, there’s nothing for you to be sorry for. I was the one who invited you here, in the first place, remember?"
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "I-I know, I know."
    hit "It’s just that this is the first time I’ve come to a guy’s house on my own."
    show pov embarrassed at left
    show hit confused_talk at right
    hit "-Let alone a guy’s room…"
    show pov neutral at left
    show hit embarrassed at right
    hit "S-So, I’m a little bit nervous…"
    show pov smirk_talk at left
    show hit confused at right
    pov "You go to guys’ houses in a group, then?"
    show pov smirk at left
    show hit confused_talk at right
    hit "W-Well, mostly for parties or for meetings with independent suppliers, with my dad, for the shop."
    hit "So I'm always with somebody else or I'm there to discuss some kind of business for the shop. Never for something like this."
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "A lot of your life revolves around that shop, doesn’t it?"
    show pov neutral_talk at left
    show hit embarrassed_talk at right
    hit "Well, it is my dad’s baby - and it’s helped pay the bills plenty of times."
    show pov confused_talk at left
    show hit confused at right
    pov "And does a comicbook shop really pay enough for all that?"
    show pov confused at left
    show hit shocked_talk at right
    hit "Oh, that isn’t all my dad does for a living. He owns a variety of businesses outside of town too."
    show pov shocked at left
    show hit neutral_talk at right
    hit "He actually owns the land around the store itself, so we don’t have to worry about things like rent and other such things."
    show hit embarrassed_talk at right
    hit "The comic book shop is actually more of his own personal thing, amongst his other more boring businesses, but since he has to travel often to check on them, he leaves me in charge!"
    show pov bored at left
    show hit neutral_talk at right
    hit "It’s really good work experience and he also pays for my apartment, so I do live on my own."
    show pov smirk_talk at left
    show hit neutral at right
    pov "Wow, you got a pretty sweet deal going there!"
    show pov smirk at left
    show hit embarrassed_talk at right
    hit "I definitely can’t complain, especially since he is so supportive of my interests."
    show pov confused at left
    show hit sad_talk at right
    hit "Though I do wish I could see him more often. He is constantly moving between towns to keep on supervising things."
    show pov smirk_talk at left
    show hit neutral at right
    pov "I guess one can’t have everything in life."
    show pov shocked at left
    show hit smirk_talk at right
    hit "True…"
    show pov neutral at left
    show hit neutral_talk at right
    hit "Anyway, enough about that. I don’t want to bore you with my life story more than I have to."
    show pov smirk_talk at left
    show hit embarrassed at right
    pov "You could never bore me; if anything I find you quite interesting actually."
    show pov neutral_talk at left
    show hit shocked at right
    pov "I mean, there’s a reason I keep coming to see you, you know?"
    show pov neutral at left
    show hit shocked_talk at right
    hit "A-A reason?"
    show pov smirk_talk at left
    show hit shocked at right
    pov "Yeah, I like spending time with you."
    show pov confused at left
    show hit shocked_talk at right
    hit "T-That’s…"
    hit "I-I’m sorry, I’m not sure how I should reply to that…"
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "You don’t have to. I’m just making small talk to try and get you to be less nervous."
    show pov embarrassed_talk at left
    show hit confused at right
    pov "Is it working?"
    show pov embarrassed at left
    show hit confused_talk at right
    hit "K-Kind of?"
    show pov embarrassed at left
    show hit embarrassed_talk at right
    hit "Though somehow I feel even more nervous than before, at the same time…"
    show pov neutral_talk at left
    show hit neutral at right
    pov "Maybe we should start and just make small talk as we go on?"
    show pov embarrassed_talk at left
    pov "The nervousness should cease once you focus on your drawing, right?"
    show pov smirk at left
    show hit embarrassed_talk at right
    hit "T-That sounds like a good idea, yes…"
    show pov neutral_talk at left
    show hit embarrassed at right
    pov "Alright, just find a comfortable place to sit and set up - and I’ll guess I’ll get to undressing."
    show pov neutral at left
    show hit smirk_talk at right
    hit "H-How can you be so calm about all this?"
    show pov embarrassed_talk at left
    show hit smirk at right
    pov "Funny enough, I think I’ve gotten far too used to being seen naked by other people ever since I moved to this town, you know?"
    show pov smirk_talk at left
    show hit neutral at right
    pov "And the fact that we are in my room makes it a bit more comfortable for me."
    show pov embarrassed at left
    show hit smirk_talk at right
    hit "How so?"
    show pov smirk_talk at left
    show hit shocked at right
    pov "Well, I do sleep in the nude, so it feels like I’m preparing to have a nap or something."
    show pov embarrassed at left
    show hit embarrassed_talk at right
    hit "I-I see…"

    #-Scene now fades out and back in to indicate passage of time-

    show black
    with fade
    $ renpy.pause()
    "After stripping down..."
    hide black
    with fade

    #-Scene now shows hitomi sitting on the bed with her drawing notebook, the Mc
    # in front of her completely in the nude striking a pose, similar to what
    # they were doing in the nerdcave-

    ## CG SCENE ##

    scene bg rocksolidmodelling_1
    with fade
    pov "Are you comfortable? Need me to get you anything before we start?"

    show bg rocksolidmodelling_2
    hit "N-No, I’m perfectly fine."
    hit "The lighting is quite good here actually."
    hit "I feel confident I can work here without any issues."

    show bg rocksolidmodelling_1
    pov "That’s a relief, then. I was worried, doing this here was gonna be too much for you, but I didn’t want to do it in the living room in case anyone came over unexpectedly."

    show bg rocksolidmodelling_3
    hit "Do you remember the pose we left off with last time?"

    show bg rocksolidmodelling_4
    pov "Sure do. Something like this right?"

    show bg rocksolidmodelling_5
    hit "Perfect. Just stay still for a moment."

    show bg rocksolidmodelling_6
    pov "Yeah, of course."

    #-The following dialogue occurs within the MC’s thoughts-

    pov "{i}Alright… Keep your cool, this is just like before.{/i}"
    show bg rocksolidmodelling_7
    pov "{i}Just focus on keeping the pose and breathing regularly.{/i}"
    pov "{i}Don’t think about the fact you have a cute girl on your room all alone while you are buck naked.{/i}"
    pov "{i}Nor about the fact she is staring at your every detail while concentrating on capturing you and biting her lip as she does so…{/i}"
    show bg rocksolidmodelling_6
    pov "{i}Oh god, please tell me I watched over my endurance enough!{/i}"
    pov "{i}Come on, [povname]. Focus!{/i}"

    #[If at any point the player chooses an option regarding Hitomi or runs out
    # of stamina, it is an instant fail, but regardless of their final result, it
    # still continues the scene until all three choices are gone through]

    menu:
        #=CHOICE 1= (-2 Stamina Points)
        "Think about the philosophical reason for human sentience"if skill_sta >= 2:
            $ renpy.notify("You used 2 Stamina Points")
            $ skill_sta -= 2
    #=OR=
        "Think about how Hitomi keeps taking glances at your crotch":
            jump lbl_rocksolid_modelling_fail_skip

    #-Change Mc’s Pose-
    menu:
    #=CHOICE 2= (-2 Stamina Points)
        "Think about the hierarchy within baboon society"if skill_sta >= 2:
            $ renpy.notify("You used 2 Stamina Points")
            $ skill_sta -= 2
    #=OR=
        "Think about the way Hitomi keeps biting on her lower lip":
            jump lbl_rocksolid_modelling_fail_skip
    #=CHOICE END=

    #-Change Mc’s Pose-
    menu:
    #=CHOICE 3= (-2 Stamina Points)
        "Think about the journey we have traveled on so far together"if skill_sta >= 2:
            $ renpy.notify("You used 2 Stamina Points")
            $ skill_sta -= 2
    #=OR=
        "Think about how Hitomi is giving you lustful eyes":
            pass
    #=CHOICE END=
    #=END=

    #-Regardless of choice of result, it all leads to the same point, failing the
    # event simply leads you to the next dialogue choice-

label lbl_rocksolid_modelling_fail_skip:
    show bg rocksolidmodelling_8
    hit "Hey, [povname]?"

    show bg rocksolidmodelling_9
    pov "Y-Yeah, Hitomi?"

    show bg rocksolidmodelling_10
    hit "You… don’t have a girlfriend or anything like that at the moment, right?"

    show bg rocksolidmodelling_11
    pov "U-Uhhh, what’s with the sudden question?"

    show bg rocksolidmodelling_10
    hit "W-Well, I never see you around with anyone specifically…"
    hit "Plus, I’ve never asked, and I’m realizing now that we are in a position that any girlfriend would have huge issues with."
    hit "With a random girl in their boyfriend’s room while he is completely naked, and she is drawing him in detail, and all…"

    show bg rocksolidmodelling_11
    pov "I…"
    pov "Yeah, I can see how that would be a problem in most circumstances…"
    pov "You are just realizing this now?"

    show bg rocksolidmodelling_10
    hit "W-Well, it just sort of popped into my mind, you know?"
    hit "Along with the fact we are always talking about me and not enough about you, so I don’t know if you have one or not…"

    show bg rocksolidmodelling_11
    pov "I don’t mind talking about you, Hitomi. If anything, I’d say I'm a much better listener."

    show bg rocksolidmodelling_10
    hit "And I really appreciate that… Honestly, you make me feel really comfortable, just being around you."
    hit "And I feel I can really just talk about anything and you would still listen."

    show bg rocksolidmodelling_11
    pov "With good company conversations a breeze, right?"

    show bg rocksolidmodelling_10
    hit "Totally. Which is why I’m comfortable enough to tell you something I’ve been meaning to say for a while now."

    show bg rocksolidmodelling_11
    pov "You know you can always tell me anything, what is it?"

    show bg rocksolidmodelling_10
    hit "Well, you’ve been at... half mast… the entire time. And I just wanted to ask if that hurt?"

    show bg rocksolidmodelling_11
    pov "Wait, what?!"
    show bg rocksolidmodelling_12
    pov "god, I’m so sorry Hitomi. I didn’t-!"

    show bg rocksolidmodelling_13
    hit "No, no, no! It’s okay, it’s okay!"
    show bg rocksolidmodelling_14
    hit "H-Honestly I don’t really mind…"
    hit "I-I took the chance and tried practicing how to draw its shape and general look of the area around it."
    hit "It’s gonna be very useful when I have to do risque panels and the like…"

    show bg rocksolidmodelling_15
    pov "S-Still, I should have been more careful, I-"

    show bg rocksolidmodelling_14
    hit "I’m telling you, [povname], it’s alright."
    hit "I’m the one who has you nude, so it’s natural something like this happens."
    hit "A-And, I would be lying if I said I didn’t find it a bit flattering that you are getting that way because of me…"

    # hit "U-Um… for the purposes of further study…"
    # hit "Do you mind if I give it a closer look?"

    # show bg rocksolidmodelling_15
    # pov "N-no, not all…"

    # #-Change scene to a close up of Hitomi kneeling down in front of the MC right
    # # by his dick which by now is fully erect-

    #         ## CG HSCENE ##

    # hit "W-Woah…"

    # pov "S-Sorry about that."

    # hit "N-No need. I’m the one who got closer… If anything, this gives me a clear idea of how it looks at this angle…"
    # hit "Do you… Think you could make it even harder?"
    # hit "J-Just so I can take a look at it from some other angles, of course…"

    # pov "U-Umm… Sure, Hitomi, but these kinds of things fade away with time, you know?"
    # pov "Can’t keep it up forever, just like that."

    # hit "T-that’s completely understandable, I guess it’s unrealistic of me to expect that…"
    # hit "I- I'll be quick..."
    # hit "W-Would it help if I… stimulated a little?"

    # pov "It… certainly is an option…"

    # hit "A-Alright…"
    # hit "B-But I’m gonna need my hands, in order to draw so…"
    # hit "J-Just remember that this is my first time doing something like this!"
    # hit "A-And please promise you’ll keep it a secret!"

    # pov "Not a word comes out of my lips, I swear!"

    # hit "G-Good… OK… Here I go…"

    #=HITOMI BLOWJOB SCENE TAKES PLACE HERE=

    #-scene focuses on Hitomi blowing you hands free, playing with it a little
    # before fully getting into it and sucking you off, once you cum and the loop
    # ends however, the door to your room opens revealing sister coming into the
    # room without knocking to ask you something-

    sis "Hey, can you let me borrow some mon-WOAH MAMA!"

    #-Scene turns back to regular character poses-

            ## SPRITEWORK ##

    show pov shocked at left
    show hit shocked_talk at Position(xpos=1400)
    show sis shocked at right
    with dissolve
    hit "Oh, sweet Jesus!"
    show pov angry_talk at left
    show hit shocked at Position(xpos=1400)
    show sis bored at right
    pov "D-Dude, why can’t you ever freaking knock?!"
    show pov angry at left
    show hit embarrassed at Position(xpos=1400)
    show sis smirk_talk at right
    sis "Yo, is that freaking Hitomi?!"
    show pov confused at left
    show hit embarrassed_talk at Position(xpos=1400)
    show sis smirk at right
    hit "P-Please don’t look at me right now!"
    show pov shocked at left
    show hit sad_talk at Position(xpos=1400)
    hit "I’m sorry, [povname]. But I really have to go!"

    #-Hitomi quickly rushes out of the room embarrassed, face blushing up a
    # storm and covered in cum-
    show pov shocked_talk at left
    hide hit
    with dissolve
    show sis smirk at right
    pov "H-Hitomi, wait!"
    show pov angry at left
    show sis bored_talk at right
    sis "Dude, put on some pants before you go out chasing people!"
    show sis smirk_talk at right
    sis "Seriously man, you cum like a geyser!"

    #-Sister leaves the scene, leaving the MC alone-
    show pov shocked_talk at left
    hide sis
    with dissolve
    pov "Oh shit, oh fuck, I gotta get dressed!"
    pov "I gotta beg [sister] not to say anything first and then find Hitomi!"

    #=SCENE END=

    jump lbl_sister_teasing
