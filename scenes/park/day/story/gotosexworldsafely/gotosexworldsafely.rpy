## Go To Sexworld Safely
label lbl_go_to_sexworld_safely:
    ## SPRITEWORK of JUST pov
    scene bg park_daysexworld
    with fade
    show pov confused_talk
    with dissolve
    pov "Okay…"
    pov "I just realized something."
    show pov bored_talk
    pov "The park is packed full of people."

    jac "*/.. And?*"

    jac "*/.. That shouldn’t stop you from walking straight into the lake, should it?*"
    show pov confused_talk
    pov "What if one of them is watching and tries chasing after me to try and rescue me?"
    show pov smirk_talk

    pov "Wouldn’t that put them at risk of drowning or even getting transported themselves."
    show pov smirk
    edw "*/.. Look, we could either way for night time, or just get in there, agent.*"
    show pov embarrassed_talk
    pov "I wanted to go during the night but you guys wouldn’t let me."
    show pov embarrassed
    edw "*/.. Only because it was too soon to do so.*"

    edw "*/.. It’s a safety thing.*"

    jac "*/.. Yeah, it’s a safety thing.*"
    show pov sad
    pov "{i}*Sigh*{/i}"

    pov "I’m just gonna walk in nonchalantly. Maybe if I do it normally enough, people won’t notice the weird guy disappearing."

    edw "*/.. That’s the spirit.*"
    show pov confused
    jac "*/.. I could come over and cause a distraction.*"
    show pov smirk_talk
    pov "No time, Jacob."
    show pov embarrassed_talk at left
    pov "Let’s just get this over and done with."

    ## CG
    ## MC Walks into the lake and disappears, diving into the portal rather than being sucked under.

    $ insexworld = 1

    ## A few moments later, he appears on the shore again, coughing.
    ## He is awaken by the drunk girl giving him CPR while cock warming him.
    ## He’s also surrounded by people.

    scene bg gotosexworldsafely_1
    with fade

    drug "OMG, you’re alive."

    "Stranger #1" "You okay, pal?"

    "Stranger #2" "You appeared out of the lake out of nowhere, it startled us."

    drug "We thought you were dead, but lucky I took a CPR lesson!"
    drug "Can you breathe alright? What’s your name? What day is it today?"

    ## MC Has options to answer correctly or worryingly.

    menu:
        "Yeah, [povname], Monday." if day == 0:
            pass
        "Yeah, [povname], Tuesday." if day == 1:
            pass
        "Yeah, [povname], Wednesday." if day == 2:
            pass
        "Yeah, [povname], Thursday." if day == 3:
            pass
        "Yeah, [povname], Friday." if day == 4:
            pass
        "I don't know, Frank, Frumday?":
            drug "Ah- good enough."

    drug "{i}*Phew*{/i}"
    drug "Alright, good."
    drug "You should be alright, then."
    drug "No need for the hospital, right?"

    pov "Oh, no. Definitely not."
    pov "I don’t have time for that-"
    pov "As much as it would be nice to see that nurse again…"

    edw "*/.. [povname]?*"
    edw "*/.. [povname]-!*"
    edw "*/.. Do you copy?*"

    jac "*/.. Can you hear us, dude?*"

    pov "Yeah-"
    pov "Yeah, hey. I can hear you guys!"
    pov "I’m alright! I’m-"
    pov "Wow… this communication device actually works."

    edw "*/.. It fucking works, dude!!*"

    jac "*/.. Let’s fucking gooooooo!*"

    edw "*/.. Let’s get it, let’s fucking gooo! Oh my fucking God!*"

    drug "Ar- are you sure, you’re okay?"
    drug "What are you talking about?"

    pov "Oh- uhhh nothing. Don’t worry."
    pov "It’s just an inside joke from a… movie I watched."
    pov "..."
    pov "I like reciting them to myself..."

    drug "Mmm… hmm.."
    drug "Well, alright."
    drug "Will you be okay getting back home?"

    pov "Hmph?"
    pov "Yes."
    pov "Very much so."

    menu:
        "Will you be able to finish me off though?":
            jump lbl_go_to_sexworld_safely_hscene

        "Thank you so much for saving me.":
            jump lbl_go_to_sexworld_safely_end

label lbl_go_to_sexworld_safely_hscene: ##
    pov "Will you be able to finish me off though?"
    drug "Oh- of course."
    drug "Just feel free to cum whenever you’re ready."
    drug "Everyone, can you give us some space please, you’re crowding too much."

label lbl_go_to_sexworld_safely_end:
    ## SPRITEWORK of pov and drug
    show pov smirk_talk at left
    show drug neutral at right
    with dissolve
    pov "Thank you so much for saving me."
    show pov smirk at left
    show drug neutral_talk at right
    drug "It was my pleasure, deary."
    drug "I’m glad I was able to put my training to good use."
    show pov neutral at left
    show drug shocked_talk at right
    drug "Alright, everyone!"
    drug "Give him some space, there’s nothing left to see here."
    show pov embarrassed at left
    show drug neutral_talk at right
    drug "He’s alright!"
    show pov confused at left
    show drug neutral at right
    edw "*/.. What’s going on there, [povname]?*"
    show pov confused_talk at left
    pov "Shh-"
    show pov shocked at left
    show drug neutral_talk at right
    drug "Hm?"
    show pov embarrassed_talk at left
    show drug neutral at right
    pov "Nothing, thank you once again."

    ## MC Stands up

    scene bg park_daysexworld
    with fade

    show pov confused
    with dissolve

    ## MC In thought

    pov "{i}Okay, everyone’s walked off…{/i}"
    pov "{i}I knew I’d make a scene but lucky it wasn’t too bad.{/i}"
    pov "{i}There’s no sign of VI or Xina anywhere so that’s good, I guess…{/i}"
    pov "{i}I need a safe place to get to before I think about searching for Effie.{/i}"
    pov "{i}There’s a good chance she’s trapped at the TRC building somewhere.{/i}"
    pov "{i}Or she’s possibly at home under house arrest. Her dad may be tasked to keep her there.{/i}"
    pov "{i}Or she’s allowed to roam freely but kept under eye at all times.{/i}"
    pov "{i}I can’t really find out for certain at this point.{/i}"
    pov "{i}Maybe I should head home like that girl said.{/i}"
    pov "{i}I think [missus] would be on my side and assist me with my mission. I know she will.{/i}"

    ## Back to regular

    show pov confused_talk
    pov "Hey, Edward, can you hear me?"

    show pov confused
    edw "*/.. {i}*Munch*{/i} Go on.*"

    show pov sad_talk
    pov "What’s Effie’s vitals at? Is she still okay?"

    show pov bored
    edw "*/.. {i}*Chewing*{/i} She’s- she’s doing fine. The signal is weak but it’s there."

    jac "*/.. {i}*Crunchh*{/i} These nachos are so fucking good.*"
    jac "*/.. [povname]. You should really try Edward’s nacho recipe.*"

    show pov confused_talk
    pov "Save some for me for after I rescue Effie."

    show pov confused
    jac "*/.. I don’t think they’d be as nice by then-*"

    edw "*/.. Shut up, Jacob. He’s doing a cool hero line.*"

    jac "*/.. {i}*Chew chew*{/i} Ah- ah- my B, dog.*"

    show pov smirk_talk
    pov "Tsk…"
    pov "Alright, let’s go meet up with [missus]."

    call lbl_next_date

    $ main_story = 127

    scene black
    with fade
    $ renpy.pause()

    "Reaching home..."

    scene bg myhousefront_day
    with fade

    jump lbl_myhousefront_day_setup
