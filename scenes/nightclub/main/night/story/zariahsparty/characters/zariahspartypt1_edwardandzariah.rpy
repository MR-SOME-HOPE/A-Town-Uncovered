## EDWARD AND ZARIAH
label lbl_zariahs_party_edward_and_zariah:
    #-Edward is holding onto some equipment as he tries to strike a conversation and flirt with Zariah, who is too busy preparing her equipment and bossing him around to notice him-
    if zariahs_party_talking_edward_and_zariah == 0:
        show pov embarrassed at left
        show edw shocked_talk at right
        with dissolve
        edw "-And I’m just saying, I think it's pretty brave of you to keep going with all of this after what happened to the van."
        show edw embarrassed_talk at right
        edw "B-But, I guess it’s still pretty in-character for you, you aren’t afraid of anything and I think that’s a really admirable trait of you and-"
        show edw shocked at Position(xpos=1400)
        show zar bored_talk at Position(xpos=1600)
        with dissolve
        zar "Pass me the dongle-thingie."
        show edw confused_talk flip at Position(xpos=1100)
        show zar bored at Position(xpos=1600)
        edw "Oh, uh… Right."
        edw "Do you want the dongle-thingie for the RCA or the dongle-thingie for the XLR?"
        show edw confused flip at Position(xpos=1100)
        show zar smirk_talk at Position(xpos=1600)
        zar "We are still working on setting up the mixer so which do you think I’m asking you to give me?"
        show edw smirk_talk flip at Position(xpos=1100)
        show zar bored at Position(xpos=1600)
        edw "RCA it is."
        show edw embarrassed flip at Position(xpos=1100)
        show zar bored_talk at Position(xpos=1600)
        zar "Thanks."
        show pov sad at left
        show edw sad_talk flip at Position(xpos=1100)
        show zar confused at Position(xpos=1600)
        edw "Yeah, no problem…"
        show pov embarrassed at left
        show edw sad flip at Position(xpos=1100)
        show zar confused_talk at Position(xpos=1600)
        zar "Were you saying something?"
        show edw sad_talk flip at Position(xpos=1100)
        show zar confused at Position(xpos=1600)
        edw "Um, well…"
        show edw sad flip at Position(xpos=1100)
        show zar shocked_talk at Position(xpos=1600)
        zar "Hold that thought, now I need the adapter."
        show pov sad at left
        show edw sad_talk flip at Position(xpos=1100)
        show zar confused at Position(xpos=1600)
        edw "Right…"
        show pov embarrassed_talk at left
        show edw sad flip at Position(xpos=1100)
        pov "You guys doing okay?"
        show pov confused at left
        show zar confused_talk at Position(xpos=1600)
        zar "Yeah, just wiring everything together."
        zar "Like I said, I’ll be streaming my whole playlist tonight, both experimental stuff and my regular jams and some remixes to them so I need a lot of odd things wired along with my normal setup."
        show pov sad at left
        show zar neutral_talk at Position(xpos=1600)
        zar "Edward’s giving me a hand with it since he is the only one besides me that can tell all the cables and connectors apart."
        show pov embarrassed at left
        show edw bored_talk flip at Position(xpos=1100)
        show zar neutral_talk at Position(xpos=1600)
        edw "Oh, I’m happy to help, plus it’s a good cause and all, plus it means that I-"
        show edw bored flip at Position(xpos=1100)
        show zar bored_talk at Position(xpos=1600)
        zar "Dude, you haven’t passed me the adaptor yet."
        show pov confused at left
        show edw sad_talk flip at Position(xpos=1100)
        show zar smirk at Position(xpos=1600)
        edw "R-Right, here you go."
        show pov embarrassed at left
        show edw sad flip at Position(xpos=1100)
        show zar bored_talk at Position(xpos=1600)
        zar "Sorry for cutting the conversation short, [povname], but I really need to focus here."
        show zar embarrassed_talk at Position(xpos=1600)
        zar "I kind of get tunnel vision when I’m wiring stuff up so I really stop listening and don’t want to make it seem like I’m ignoring you or anything."
        show edw shocked_talk flip at Position(xpos=1100)
        show zar bored at Position(xpos=1600)
        edw "Wait, so all that I was saying just now-"
        show edw shocked flip at Position(xpos=1100)
        show zar bored_talk at Position(xpos=1600)
        zar "In one ear and out the other."
        show pov sad at left
        show edw sad flip at Position(xpos=1100)
        show zar embarrassed_talk at Position(xpos=1600)
        zar "Sorry dude, I just have to hyperfocus on this since one bad connection and the whole thing can end up sounding weird or not sounding at all!"
        show zar neutral_talk at Position(xpos=1600)
        zar "Was it important?"
        show edw sad_talk flip at Position(xpos=1100)
        show zar neutral at Position(xpos=1600)
        edw "Uhh… No, not really."
        edw "Just making small talk and all that…"
        show pov embarrassed at left
        show edw bored flip at Position(xpos=1100)
        show zar neutral_talk at Position(xpos=1600)
        zar "Alright, cool."
        zar "Now, let’s get back to this."

        #-Zariah returns to wiring and setting stuff up, it’s clear she is no longer listening to either of you-"

        show edw bored_talk at Position(xpos=1400)
        hide zar neutral at Position(xpos=1600)
        with dissolve
        edw "Well, that just put a huge set back on my plans for the night."
        show pov embarrassed at left
        show edw embarrassed_talk at Position(xpos=1400)
        edw "Sorry you had to see that, dude."
        show pov neutral at left
        show edw sad_talk at Position(xpos=1400)
        edw "If it’s not much to ask, can you keep it between us?"
        show pov neutral_talk at left
        show edw embarrassed at Position(xpos=1400)
        pov "I’ll take it to the grave, dude, no worries."
        show pov neutral at left
        show edw embarrassed_talk at Position(xpos=1400)
        edw "Thanks, man."
        edw "How’s your night going?"
        show pov shocked_talk at left
        show edw confused at Position(xpos=1400)
        pov "So far, only saying hi to people and such."
        pov "You know how it is."
        show pov smirk at left
        show edw smirk_talk at Position(xpos=1400)
        edw "Yeah, I was actually looking forward to the original plan, you know?"
        edw "Just hanging out with friends, listening to music and all that without the extra pressure of being around a bunch of strangers and actually partying and such."
        show pov neutral at left
        show edw embarrassed_talk at Position(xpos=1400)
        edw "I mean, I don’t mind being a roadie, but I don’t go to parties often so I don’t really know what to do."
        show pov neutral_talk at left
        show edw embarrassed at Position(xpos=1400)
        pov "I feel ya, but hey, if it gets too much for you then you can just come up to me and the rest of the guys and we can party together."
        pov "I mean, the point of it is partying with friends and all that, right?"
        show pov smirk_talk at left
        show edw neutral at Position(xpos=1400)
        pov "It’s not like you came to a stranger’s party or something."
        show pov smirk at left
        show edw neutral_talk at Position(xpos=1400)
        edw "I guess you are right."
        edw "Thanks dude, that does put me at ease."
        show edw embarrassed_talk at Position(xpos=1400)
        edw "Specially since I don’t think my original plans on “partying” tonight are going the way I wanted them to."
        show pov smirk_talk at left
        show edw confused at Position(xpos=1400)
        pov "Night is young, you never know but…"
        pov "I guess I’d recommend you not to go for the one girl whose last thought right now is “partying” or anything alike, you know?"
        show pov smirk at left
        show edw smirk_talk at Position(xpos=1400)
        edw "Another very valid point."
        edw "Perhaps I could go for a second and see if I can-"
        show pov shocked at left
        show edw shocked at Position(xpos=1400)
        show zar confused_talk at Position(xpos=1600)
        with dissolve
        zar "Edward, If you ditch me even for a second while we are setting all this equipment up, I’m literally going to strangle you with an extension cord and hang you like a disco ball."
        show edw shocked_talk flip at Position(xpos=1100)
        with dissolve
        show zar shocked at Position(xpos=1600)
        edw "Gah!"
        edw "I thought you weren’t listening to what we were saying!"
        show pov embarrassed at left
        show edw shocked flip at Position(xpos=1100)
        show zar bored_talk at Position(xpos=1600)
        zar "I don’t need to listen to what you are saying."
        zar "I can sense your thoughts of ditching just as well as I can sense your fear."
        show edw angry_talk flip at Position(xpos=1100)
        show zar smirk at Position(xpos=1600)
        edw "That makes absolutely no sense!"
        show edw angry flip at Position(xpos=1100)
        show zar smirk_talk at Position(xpos=1600)
        zar "You should know better than to try your luck against my DJ super powers."
        show edw shocked flip at Position(xpos=1100)
        show zar bored_talk at Position(xpos=1600)
        zar "Now pass me the XLR dongle before I provide the fear of god back into your immortal soul."
        show edw shocked_talk flip at Position(xpos=1100)
        show zar bored at Position(xpos=1600)
        edw "M-Ma’am yes, Ma’am!"
        show pov embarrassed at left
        show edw embarrassed_talk at Position(xpos=1400)
        with dissolve
        show zar bored at Position(xpos=1600)
        edw "S-Sorry, [povname] but I think I have to focus here for the sake of staying alive."
        show pov embarrassed_talk at left
        show edw embarrassed at Position(xpos=1400)
        pov "Y-Yeah, don’t let me stop you."
        show edw neutral at Position(xpos=1400)
        show zar neutral at Position(xpos=1600)
        pov "See you guys later."
        show pov embarrassed at left
        show edw neutral_talk at Position(xpos=1400)
        hide zar bored at Position(xpos=1600)
        with dissolve
        edw "Yeah, see ya!"
        show pov embarrassed at left
        hide edw embarrassed_talk at Position(xpos=1400)
        with dissolve
        $ zariahs_party_talking_edward_and_zariah = 1
        #=RESULT END=
    else:
        pov "I'll let them talk."

    jump lbl_nightclubdancefloor_zariahs_party_setup
