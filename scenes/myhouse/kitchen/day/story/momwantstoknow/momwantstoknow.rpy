label lbl_mom_wants_to_know:
    #[Mc’s Home, Kitchen, Morning - “Mom wants to know”  - main_story =100]

    #-Scene takes place the morning after the previous scene with Eloise. Mom is in the kitchen as usual and greets you as you come down-
    scene bg mykitchen_day
    with fade

    show pov neutral_talk at left
    show mum neutral at right
    with dissolve
    pov "Good morning."
    show pov neutral at left
    show mum neutral_talk at right
    mum "Oh, good morning, sweetie! I was just about to check in on you."
    show pov shocked at left
    show mum embarrassed_talk at right
    mum "You gave me a bit of a scare when I didn’t see you come home last night."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "Sorry about that. I ended up having to stay a little later than usual as they gave me orientation and the like. I’m a special case so they only had people available to help me out after official hours."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "That’s alright, hun. I figured you were going to be late thanks to that man anyway, so I didn’t worry too much about it. Plus, I helped push you into this so I’m not about to get upset if work starts taking some of your time."
    show pov neutral at left
    show mum bored_talk at right
    mum "Just make sure to send me a text or something if you are going to be working late, can you do that for me, honey?"
    show pov neutral_talk at left
    show mum neutral at right
    pov "You got it. Sorry for scaring you."
    show pov bored_talk at left
    show mum confused at right
    pov "Speaking of working late, however, did the old man ever come home last night?"
    show pov smirk at left
    show mum shocked_talk at right
    mum "That’s why I was worried!"
    show pov bored at left
    show mum angry_talk at right
    mum "I’m used to not seeing him around when I get up, but I was worried he got you to do one of his overnight office stays on your first day of work."
    show pov bored_talk at left
    show mum confused at right
    pov "I’m sure he considered it and preferred to have the office all to himself."
    show pov confused_talk at left
    pov "We were about to leave when he was suddenly called back to work to fix something ASAP."
    show pov smirk_talk at left
    show mum shocked at right
    pov "I guess it took him longer than he expected."
    show pov smirk at left
    show mum bored_talk at right
    mum "Ugh, he is going to be in a bad mood when he finally comes home…"
    show pov confused_talk at left
    show mum bored at right
    pov "Are you going to be okay with that?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "I can stick around if you need me."
    show pov embarrassed at left
    show mum embarrassed_talk at right
    mum "I appreciate you saying that, hun."
    mum "But you don’t need to worry about it. I have plans today so I’m going to be out by the time he usually comes home after staying in the office all day."
    show pov confused_talk at left
    show mum embarrassed at right
    pov "Oh, anything interesting planned?"
    show pov shocked at left
    show mum embarrassed_talk at right
    mum "Just going out to get some stuff, nothing too important."
    show mum neutral_talk at right
    mum "Enough about me though, I’ve been dying to know how your first day went!"
    show pov embarrassed_talk at left
    show mum  at right
    pov "I think it went quite well all things considered!"
    pov "The people in the office are honestly quite nice and seemed happy I was coming along."
    show pov bored_talk at left
    show mum embarrassed at right
    pov "With a few obvious exceptions."
    show pov bored at left
    show mum embarrassed_talk at right
    mum "I don’t really need to even ask who was the exception, do I?"
    show pov shocked at left
    show mum sad_talk at right
    mum "Do I need to have a talk with him?"
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "You don’t have to do that, he at least knows not to be an ass while we are working."
    pov "Actually, he didn’t even acknowledge I was even there while we were inside the office."
    show pov neutral_talk at left
    pov "Though he sure had a lot to complain about afterwards. It’s a good thing he was called to do overtime so I didn't have to listen to him moan the whole way home."
    show pov confused at left
    show mum shocked_talk at right
    mum "Ugh, why am I not even surprised?"
    show pov embarrassed at left
    show mum bored_talk at right
    mum "If he ever crosses the line let me know and I’ll make sure he gets used to sleeping in the garden."
    show pov smirk_talk at left
    show mum bored at right
    pov "Thanks, but you don’t need to worry so much."
    show pov smirk at left
    show mum smirk_talk at right
    mum "I know, but I can’t help it."
    show mum bored_talk at right
    mum "I contributed to getting you into this situation in the first place."
    show pov embarrassed_talk at left
    show mum bored at right
    pov "I don’t blame you for any of this."
    show pov neutral_talk at left
    show mum embarrassed at right
    pov "You were just looking out for the best for me."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "I mean, all things considered, this is still a great opportunity, isn’t it?"
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "I’m really happy that you are seeing it this way."
    show pov neutral_talk at left
    show mum neutral at right
    pov "It’s just a temporary thing, right?"
    pov "It’s only going to lead to better things in the future."
    show pov confused at left
    show mum smirk_talk at right
    mum "Spoken like a real man, right there."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "It's about time we had a man of the house, I’m so proud of you!"

    if mum_path >= 31:
        #=If Mom has been romanced=
        show pov shocked at left
        show mum smirk_talk at right
        mum "And definitely a little turned on right now~"
        show pov smirk_talk at left
        show mum smirk at right
        pov "Oh, is that so?"
        show pov smirk at left
        show mum smirk_talk at right
        mum "Oh, absolutely~"
        mum "Just a few days ago I was getting in bed with a young man, but today I’m starting to see I’m making love to a man~"
        show pov shocked_talk at left
        show mum neutral at right
        pov "Well, this man right here needs to make sure to take care of his woman as best he can, doesn’t he?"
        show pov smirk at left
        show mum neutral_talk at right
        mum "And you do, you really really do."
        mum "You take care of me real good~"
        show pov confused_talk at left
        show mum neutral at right
        pov "Any other way I can… take care of you right now?"
        show mum embarrassed_talk at right
        mum "Oh, I’d love to, but I just cleaned this floor and as much as I want to give in, I still have chores to do."
        show pov sad at left
        show mum smirk_talk at right
        mum "So unless you are going to help out, keep it in your pants until later."
        show pov neutral_talk at left
        show mum smirk at right
        pov "Alright, alright. I’ll behave."
        show pov smirk at left
        show mum smirk_talk at right
        mum "For a big strong man, you are still such a good boy~"
        show pov smirk_talk at left
        show mum neutral at right
        pov "And you just love teasing me, don’t you?"
        show pov smirk at left
        show mum smirk_talk at right
        mum "As much as you need oxygen in order to breathe."
        mum "But really though, I’m really proud of you for making the best out of all of this."

    #=Back to general dialogue=

    show pov confused_talk at left
    show mum neutral at right
    pov "Well, I wasn’t going to let the whole thing push me down more than it has to."
    show pov embarrassed_talk at left
    pov "Plus, like I said, the people in the office are really nice for the most part and now that I know my way around the place, I can get in there without needing to interact with Him anymore than I have to."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "That’s such a relief to hear."
    show pov confused at left
    show mum smirk_talk at right
    mum "Alright, enough about work, got any plans for today?"
    show pov confused_talk at left
    show mum neutral at right
    pov "Well, I do have school today but-"

    #=Mc stops as his phone starts to vibrate indicating a text =
    show pov shocked_talk at left
    pov "Oh sorry, just a second, I got a text…"

######################################################################################
    #=Mc checks his phone to see a text from Jacob=
    scene bg momwantstoknow_1
    with dissolve
    $ renpy.pause()
    show bg momwantstoknow_2
    $ renpy.pause()
    show bg momwantstoknow_3
    $ renpy.pause()
    # jac "We need to talk."
    # jac "It’s about Effie."
    # jac "Meet me at the nerd cave in the comic book shop."

######################################################################################

    #=Mc puts the phone down once he finishes reading=
    scene bg mykitchen_day
    with fade

    show pov confused_talk at left
    show mum confused at right
    with dissolve
    pov "Oh boy…"
    show pov shocked at left
    show mum confused_talk at right
    mum "Everything okay, hun?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "I… I really hope so."
    show pov shocked at left
    show mum confused_talk at right
    mum "What’s wrong?"
    show pov embarrassed_talk at left
    show mum confused at right
    pov "I kind of messed things up with one of my friends recently…"
    show pov embarrassed at left
    show mum shocked_talk at right
    mum "Oh no, that’s terrible!"
    show mum confused_talk at right
    mum "Was it that nice girl, Effie?"
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "Y-Yeah…"
    show pov confused_talk at left
    pov "How did you know?"
    show pov confused at left
    show mum neutral_talk at right
    mum "[sister] had noticed she seemed really down in the dumps lately."
    mum "But even when she tried to approach her, Effie just told her she was fine and just needed some space."
    show pov sad at left
    show mum embarrassed_talk at right
    mum "It’s been eating at [sister] for a while not knowing what’s wrong with her."
    show pov bored_talk at left
    show mum embarrassed at right
    pov "Great, I’m also ruining her relationships with my actions…"
    show pov confused at left
    show mum embarrassed_talk at right
    mum "Oh honey, I’m sure nothing has been ruined."
    show pov embarrassed_talk at left
    show mum confused at right
    pov "Last time I talked to Effie, things went really bad…"
    pov "I pushed her too much into talking about something she didn’t want to and now she won’t even look at me…"
    show pov bored_talk at left
    pov "She took special offense over the fact that I’m asking her to share stuff when I won’t even tell her what's wrong with me…"
    show pov confused at left
    show mum embarrassed_talk at right
    mum "Feeling sorry for yourself isn’t going to fix anything, honey."
    mum "If you want Effie to forgive you, then you have to show her that you are sorry for overstepping her boundaries."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Maybe you could ask another one of your friends to be the middleman on this?"
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "I actually have."
    pov "Jacob just texted me asking to meet with him to discuss all this."
    show pov confused at left
    show mum neutral_talk at right
    mum "See? You are already making progress on fixing things!"
    show mum embarrassed_talk at right
    mum "What’s important right now is that you make an honest attempt at fixing your mistake."
    show pov bored_talk at left
    show mum confused at right
    pov "What if that’s not enough?"
    pov "What if she doesn’t want my apology in the first place or it isn’t enough?"
    show pov bored at left
    show mum embarrassed_talk at right
    mum "That’s going to be her decision."
    show mum neutral_talk at right
    mum "All you can do right now is be honest with her and do your best to show her you are sorry and learn from your mistake in the future."
    show pov sad at left
    mum "If you really want to apologize, you have to be willing to be honest with your friends."
    show pov sad_talk at left
    show mum neutral at right
    pov "…"
    show pov sad at left
    show mum neutral_talk at right
    mum "Honey, I’m not going to push you to be fully honest with me."
    show pov confused at left
    show mum embarrassed_talk at right
    mum "But did something… Bad… happened to you the night you disappeared?"
    show pov bored_talk at left
    show mum embarrassed at right
    pov "…"
    pov "Something… Almost did…"
    show pov confused_talk at left
    pov "Something I’m still trying to wrap my head around."
    show mum confused at right
    pov "Something I don’t even know how to start explaining…"
    pov "I want to tell you what happened, I really do. If only so I can finally get it out of my chest, but…"
    show pov bored_talk at left
    show mum embarrassed at right
    pov "I don’t even know where to begin…"
    show pov bored at left
    show mum neutral_talk at right
    mum "OK…"
    mum "Thank you for being honest with me, even if it’s not the whole truth."
    show mum embarrassed_talk at right
    mum "Now I know this is a sensitive issue so I won’t push you too hard with answers."
    mum "I hope you understand you don’t have to deal with all of this on your own, we are here for you."
    show pov sad_talk at left
    show mum embarrassed at right
    pov "I-I know that…"
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "I promise to tell you everything once I’m ready."
    show pov sad_talk at left
    pov "I just… I’m trying to make sure what I think happened, actually happened."
    show pov embarrassed_talk at left
    show mum embarrassed at right
    pov "If anything just to have proof so you don’t think I’m crazy."
    show pov shocked at left
    show mum embarrassed_talk at right
    mum "Honey, I could never think that."
    show pov bored_talk at left
    show mum embarrassed at right
    pov "You say that because you haven’t heard the story…"
    show pov bored at left
    show mum embarrassed_talk at right
    mum "And I’m ready to hear it whenever you feel ready to share it with me."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "Thanks… You always have my back don’t you?"
    show pov embarrassed at left
    show mum shocked_talk at right
    mum "About time you realized it!"
    show mum neutral_talk at right
    mum "Now, you better get going, don’t keep your friend waiting more than he has to."
    if mum_path >= 31:
        #=If Mom has been romanced=

        #-Mc and mom proceed to share a loving kiss-

        show pov neutral_talk at left
        show mum smirk at right
        pov "I love you."
        show pov smirk_talk at left
        pov "You know that, right?"
        show pov smirk at left
        show mum smirk_talk at right
        mum "You remind me quite often but I never get tired of hearing it~"
        show pov neutral_talk at left
        show mum shocked at right
        pov "We should go on a date soon."
        show mum neutral at right
        pov "I want to spoil you a little bit."
        show pov neutral at left
        show mum smirk_talk at right
        mum "Mmmm~ I like the sound of that~"
        mum "Now get going before I can’t hold myself back any more."

        #=RESULT END=

    show pov neutral_talk at left
    show mum neutral at right
    pov "I’ll see you later, then."
    pov "Thanks for your words."
    show pov embarrassed at left
    show mum neutral_talk at right
    mum "Thank you for opening up to me a little."
    mum "Do that with your friends and I’m sure things will be alright."
    show pov embarrassed_talk at left
    show mum neutral at right
    pov "I’ll be sure to try."

    scene bg mykitchen_day
    with dissolve

    #=SCENE END=
    $ main_story = 100
    $ townmap_enabled = 1

    jump lbl_mykitchen_day
