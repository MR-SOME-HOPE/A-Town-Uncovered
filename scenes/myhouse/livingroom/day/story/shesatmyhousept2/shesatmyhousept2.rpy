## She's At My House Part 2 ##
label lbl_shes_at_my_house_pt2:

    scene bg mylivingroom_day
    with fade
    show pov embarrassed_talk at left
    with dissolve
    show eff neutral at right
    with dissolve
    pov "Effie? What are you doing here?"
    show pov embarrassed at left
    show eff neutral_talk at right
    eff "Hey, [povname]."
    eff "Just wanted to stop by to see how you were doing?"

    menu:
        "I'm good.":
            show pov embarrassed_talk at left
            show eff neutral at right
            pov "I'm good, thank for asking."
            show eff embarrassed at right
            pov "Things have been- alright recently. Nothing more to say."
            show pov embarrassed at left
            show eff sad_talk at right
            eff "You sure? What about [sister]? How is she?"
            show pov sad at left
            show eff sad at right
            pov "..."
            show pov sad_talk at left
            pov "She... left."
            pov "I don't know where she went but, she had a fight with dad, things got out of control and I have no idea where she is."
            show pov shocked at left
            show eff embarrassed_talk at right
            eff "[povname], she's staying at my place, and probably will for the next few days, maybe longer."
            show pov shocked_talk at left
            show eff embarrassed at right
            pov "She's staying with you?"
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "Mhmm, I thought that I should tell you personally."
        "Could be better.":
            show pov embarrassed_talk at left
            show eff embarrassed at right
            pov "Could be better to be honest."
            pov "Things have been... eventful around here recently. Lots of drama."
            show pov embarrassed at left
            show eff embarrassed_talk at right
            sis "Where's [sister]?"
            show pov sad_talk at left
            show eff embarrassed at right
            pov "She..."
            pov "Well, she-"
            show pov shocked at left
            show eff embarrassed_talk at right
            eff "She's at my place, [povname]."
            show pov shocked_talk at left
            show eff embarrassed at right
            pov "Oh! She is?!"
            show pov embarrassed at left
            show eff embarrassed_talk at right
            eff "Yeah, that's pretty much the reason I stopped by. To let you know."
        "Not too hot.":
            show pov sad_talk at left
            show eff sad at right
            pov "Not too hot, Eff."
            pov "Things have been going south recently. It sucks real bad."
            show pov sad at left
            show eff sad_talk at right
            eff "You wanna talk about it?"
            show pov sad_talk at left
            show eff sad at right
            pov "Not right now. It's really a family matter."
            show pov shocked at left
            show eff embarrassed_talk at right
            eff "Well, where's [sister]?"
            show pov embarrassed_talk at left
            show eff sad at right
            pov "Oh, [sister]?"
            pov "She's..."
            show pov sad_talk at left
            show eff sad at right
            pov "Gone."
            show pov shocked at left
            show eff sad_talk at right
            eff "She's at my place, [povname]."
            show pov shocked_talk at left
            show eff embarrassed at right
            pov "She is?!"
            show pov shocked at left
            show eff embarrassed_talk at right
            eff "Yeah, it's the main reason why I stopped by."
    show pov confused at left
    show eff embarrassed_talk at right
    eff "And she asked me to check on you."
    show pov sad at left
    show eff sad_talk at right
    eff "She's really worried about you."
    show pov sad_talk at left
    show eff embarrassed at right
    pov "Why would she be worried about me? I'm worried about her."
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "She didn't want you to feel like she abandoned you."
    show pov sad at left
    show eff sad_talk at right
    eff "She just really felt like she wasn't safe here right now."
    show pov embarrassed_talk at left
    show eff embarrassed at right
    pov "I understand, Effie. Thanks for telling me."
    show pov sad_talk at left
    pov "Can I come by and see her?"
    show pov embarrassed at left
    show eff confused_talk at right
    eff "Now?"
    show pov sad at left
    show eff sad_talk at right
    eff "I wouldn't if I were you. She's really-"
    eff "I hate to say depressed but really emotionally unstable."
    eff "Like I feel she's experiencing some mild case of PTSD."
    show eff embarrassed_talk at right
    eff "But even that's a bit too-"
    eff "Y'know, just."
    eff "Not right now, [povname]. She's not ready."
    show pov embarrassed_talk at left
    show eff embarrassed at right
    pov "I understand. She just needs time and space, right?"
    show pov sad at left
    show eff embarrassed_talk at right
    eff "That's possible. But I wouldn't count on it."
    show eff sad_talk at right
    eff "She does a lot of crying, not a lot of talking."
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "The best I can do is be the girl friend that she needs. Someone that can get through to her."
    show pov embarrassed_talk at left
    show eff embarrassed at right
    pov "Thank, Effie."
    show pov sad_talk at left
    show eff shocked at right
    pov "And I'm sorry if this whole thing is putting too much pressure on-"
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "Oh, [povname]. You don't have to apologise. I love [sister] like she was the sister I never had."
    eff "It's no trouble at all. And I know she would do the same for me."
    show pov embarrassed_talk at left
    show eff embarrassed at right
    pov "Thanks, Effie."
    pov "Thanks again."
    pov "Maybe I'll drop by next week?"
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "Yeah, I think that's a good start. See where things go from there."
    eff "I gotta bounce, dude."
    show pov embarrassed_talk at left
    show eff embarrassed at right
    pov "Alright, I'll see you around, Effie."
    show pov embarrassed at left
    show eff embarrassed_talk at right
    eff "Peace be with you, other half."
    $ sister_path = 28
    $ townmap_enabled = 1

    jump lbl_mylivingroom_day_setup
