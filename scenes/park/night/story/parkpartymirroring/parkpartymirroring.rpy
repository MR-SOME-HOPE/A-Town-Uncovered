## Park Party Mirroring
label lbl_park_party_mirroring:
    # START

    # You and Effie emerge from the lake in the RW

    "Drunk People" "{i}*Cheers and hollering*{/i}"

    show pov shocked_talk at left
    show eff confused at right
    with dissolve
    pov "So this is what this Mingle-Mingle Festival is in the real world."
    show pov shocked at left
    show eff smirk_talk at right
    eff "Just a bunch of drunk people at a get-together from the looks of it."
    show pov smirk_talk at left
    show eff neutral at right
    pov "Good thing a lot of them are drunk and out of it."
    show pov smirk at left
    show eff embarrassed_talk at right
    eff "Yeah, fuck- it’s cold."
    show pov neutral at left
    show eff neutral_talk at right
    eff "Let’s get home as fast as possible."
    show pov shocked at left
    show eff smirk_talk at right
    eff "Most if not everyone’s asleep or should be so getting home should be a breeze."
    show pov smirk_talk at left
    show eff smirk at right
    pov "I see what you did there."
    show pov neutral at left
    show eff smirk_talk at right
    eff "Pfft~"
    eff "And hey, [povname]."
    show eff neutral_talk at right
    eff "Thanks for coming after to save me."
    show eff shocked_talk at right
    eff "Although I didn’t need saving, it was heroic that you did."
    show pov embarrassed_talk at left
    show eff confused at right
    pov "I did what I had to, I didn’t know you weren’t in trouble but getting you back to the real world was my top priority."
    show pov embarrassed at left
    show eff smirk_talk at right
    eff "Tonight was weird… for sure."
    show eff shocked_talk at right
    eff "I can’t help but feel that something’s not right."
    show pov neutral_talk at left
    show eff confused at right
    pov "I do too, Effie."
    pov "We may have gotten away, or should I say, they let us get away tonight, but there must be a reason for it."
    pov "They’re probably watching us somehow."
    show pov neutral at left
    show eff embarrassed_talk at right
    eff "I can feel it, all eyes on me, and it’s not because I’m completely naked right now."
    show pov shocked_talk at left
    show eff confused at right
    pov "Now you know how I’ve felt the past few weeks."
    show pov neutral_talk at left
    pov "We’ll have to meet up with the gang at the hideout sometime soon and discuss what to do or expect next."
    pov "There’s no way this war between us and Xina is over."
    show pov smirk at left
    show eff embarrassed_talk at right
    eff "I fully agree with you. But first."
    show pov neutral at left
    show eff neutral_talk at right
    eff "A good ol’ shower and a hard-sleep."
    show pov smirk at left
    show eff smirk_talk at right
    eff "I have never orgasmed so many times in one day as I did today."
    show eff neutral_talk at right
    eff "What a once in a lifetime experience."
    show pov neutral_talk at left
    show eff shocked at right
    pov "I’m glad you had fun, Effie. Truly."
    show pov neutral at left
    show eff neutral_talk at right
    eff "Get home safe, okay?"
    show pov neutral_talk at left
    show eff smirk at right
    pov "I should be telling you that, Eff."


    $ main_story = 139.1
    $ gtime = 3
    $ townmap_enabled = 0

    scene black
    $ renpy.pause()

    "Back home..."

    scene bg myhousefront_night
    with fade

    jump lbl_myhousefront_night_setup
