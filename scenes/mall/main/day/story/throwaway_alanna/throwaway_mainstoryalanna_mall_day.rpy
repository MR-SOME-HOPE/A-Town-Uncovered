## Alanna Main Story Throwaway Conversations Mall ##
default sexaroundtownalanna = 0

## Sex Around Town Alanna
label lbl_mall_day_alanna_sexworld:
    if sexaroundtownalanna == 0:
        ## Sprite Start
        show pov confused_talk at left
        with dissolve
        show alasw neutral at right
        call lbl_icecreampy_counter_check
        with dissolve
        pov "Alanna?!"
        show pov confused at left
        show alasw neutral_talk at right
        ala "Hey, [povname]. You here to work?"
        show pov confused_talk at left
        show alasw neutral at right
        pov "No?!"
        pov "Why are you naked and covered in icecream?"
        show pov embarrassed_talk at left
        show alasw confused at right
        pov "Did a vat of icecream fall on you or something?"
        show pov embarrassed at left
        show alasw confused_talk at right
        ala "What are you on, [povname]?"
        show pov shocked at left
        show alasw neutral_talk at right
        ala "This is our uniform. You wear the exact same thing."
        show pov shocked_talk at left
        show alasw confused at right
        pov "{i}This{/i} is our uniform?"
        show pov shocked at left
        show alasw confused_talk at right
        ala "Duhh, how else are people going to try samples?"
        ala "Off of a spoon?"
        show pov confused at left
        show alasw angry_talk at right
        ala "Pfft, how barbaric."
        show pov confused_talk at left
        show alasw confused at right
        pov "Are you telling me that, customers... lick it off my dick?"
        show pov neutral at left
        show alasw smirk_talk at right
        ala "If it ain't a clit, it's probably a dick."
        show pov smirk at left
        show alasw bored_talk at right
        ala "Ehh... close enough rhyme."
        show pov smirk_talk at left
        show alasw neutral at right
        pov "Maybe I should... work... today."
        show pov embarrassed at left
        show alasw neutral at right
        pov "{i}No... I can't... there's something bigger going on here.{/i}"
        show pov smirk at left
        show alasw neutral at right
        pov "{i}And I'm not talking about my dick.{/i}"
        show pov sad at left
        show alasw neutral at right
        pov "{i}Although the icecream might make it shrink in size...{/i}"
        show pov sad at left
        show alasw confused_talk at right
        ala "You okay, dude? You just staring into space there."
        show pov sad_talk at left
        show alasw confused at right
        pov "I've- gotta go..."

        $ sexaroundtownalanna = 1

    else:
        show pov neutral at left
        with dissolve
        show alasw neutral_talk at right
        call lbl_icecreampy_counter_check
        with dissolve
        ala "Ready to work, [povname]?"
        show pov embarrassed_talk at left
        show alasw neutral at right
        pov "Not really..."
        show pov embarrassed_talk at left
        show alasw bored at right
        pov "Just came to see the- uniform..."
        show pov neutral at left
        show alasw bored_talk at right
        ala "Yup... this is what it looks like... All... rainbow-ish."

    jump lbl_mall_day

## Buukakki Followers Are Everywhere - Alanna
label lbl_buukakki_followers_are_everywhere_alanna:
    ## SPRITE START NO BG NEEDED
    show pov neutral_talk at left
    show ala bored at right
    pov "Hey, Alanna."
    show pov neutral
    show ala bored_talk
    ala "Here to work?"
    show pov neutral_talk
    show ala confused
    pov "Nup!"
    show pov embarrassed
    show ala bored_talk
    ala "Well don’t sound so happy about it."
    show pov confused_talk
    show ala confused
    pov "I wanna know if you’ve seen anything weird happen with these flyer distributors."
    pov "You seem to have a really good view of the mall from the store."
    pov "Any strange actions from them?"
    show pov confused
    show ala confused_talk
    ala "Aside from literally throwing and shoving flyers into people as they walk past?"
    show ala shocked_talk
    ala "I mean some of them even chased people."
    ala "People ran, [povname]. In a shopping mall."
    show ala confused_talk
    ala "I don’t know why it’s taking security so long to deal with them."
    show ala bored_talk
    ala "I reckon even they are part of this whole schmuck scheme."
    show pov confused
    show ala bored
    pov "Hmmm-"
    show pov confused_talk
    pov "That certainly is unusual."
    pov "This definitely shouldn’t be happening in a mall and yet, they’re here and disturbing the public."
    show pov bored
    show ala smirk_talk
    ala "It’s kinda funny to watch though."
    show pov bored_talk
    show ala smirk
    pov "Alanna."
    show pov bored
    show ala smirk_talk
    ala "What?! I’m bored as fuck here, this is entertainment."
    show pov neutral_talk
    show ala confused
    pov "Whatever, I’ll ski-daddle. Thanks for the talk."
    show pov embarrassed
    show ala bored_talk
    ala "Work some shifts will ya?"

    $ buukakkifollowers_alanna = 1

    call lbl_buukakki_followers_are_everywhere_check

    jump lbl_mall_day_setup
