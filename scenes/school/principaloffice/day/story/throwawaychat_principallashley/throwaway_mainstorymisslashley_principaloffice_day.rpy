## Director Lashley Main Story Throwaway Conversations Director's Office ##
default sexaroundtownprincipallashley = 0

## Sex Around Town Principal Lashley
label lbl_principaloffice_day_principallashley_sexworld:
    if sexaroundtownprincipallashley == 0:
        ## Sprite Start
        show pov confused_talk at left
        with dissolve
        hide btn principaloffice_day_principallashley_idle
        show pri confused at right
        call lbl_principaloffice_counter_check
        with dissolve
        pov "Director Lashley!"
        show pov sad at left
        show pri confused_talk at right
        pri "Hi, [povname]. You seem to be in a panic. What's the matter?"
        pri "Is the university burning down?"
        show pov confused at left
        show pri neutral_talk at right
        pri "Hahahaha~!"
        show pov confused at left
        show pri confused_talk at right
        pri "Oh my... I actually hope not."
        show pov confused at left
        show pri neutral_talk at right
        pri "I would lose my job."
        show pov confused_talk at left
        show pri neutral at right
        pov "No- well- I don't know. Not quite?"
        pov "But..."
        show pov embarrassed_talk at left
        show pri confused at right
        pov "I don't mean to be a tattle-tale of sorts but..."
        pov "Are you aware that there are people having sex all over university?"
        show pov confused_talk at left
        show pri confused at right
        pov "And I'm not talking about in secret, I mean like... out in the open for everyone to see."
        if main_story > 32:
            pov "And the weird this is that Miss Allaway seems to be in on it...?"
        show pov angry_talk at left
        show pri angry at right
        pov "What the hell is going on?!"
        show pov bored at left
        show pri angry_talk at right
        pri "Erm, excuse yourself, [povname]. Language."
        show pov confused at left
        show pri neutral_talk at right
        pri "I don't see an issue with what you're saying."
        pri "There aren't any rules about sex."
        show pov confused at left
        show pri bored_talk at right
        pri "You're free to do it as you please but we have zero tolerance for bullying."
        show pov sad at left
        show pri angry_talk at right
        pri "If you're witnessing some sexual abuse then definitely report that to me."
        show pov confused at left
        show pri confused at right
        pov "..."
        show pov confused_talk at left
        show pri confused at right
        pov "Are you in on it too?"
        show pov confused at left
        show pri neutral_talk at right
        pri "This has always been the rules. You can see for yourself in the university manual."
        show pov angry_talk at left
        show pri angry at right
        pov "I... gotta find out what the fuck is-"
        show pov angry at left
        show pri angry_talk at right
        pri "Language! [povname]. I'm not going to say it again."
        show pov confused at left
        show pri bored_talk at right
        pri "Now if you'll excuse me, I have to do my afternoon prayers before I go down on a student's parent."

        $ sexaroundtownprincipallashley = 1

    else:
        show pov confused at left
        with dissolve
        hide btn principaloffice_day_principallashley_idle
        show pri angry_talk at right
        call lbl_principaloffice_counter_check
        with dissolve
        pri "I'm sorry, [povname]. We've already discussed the rules and regulations of the university."
        pri "It may not be what you're used to back home but it is allowed here."
        show pov bored at left
        show pri bored_talk at right
        pri "Now if you'll excuse me-"
        show pov confused at left
        show pri angry_talk at right
        pri "I need to start my prayer all over again."

    jump lbl_principaloffice_day
