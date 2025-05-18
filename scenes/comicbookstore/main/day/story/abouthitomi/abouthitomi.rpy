## About Hitomi ##
label lbl_about_hitomi:
    if ( gtime == 1 and (main_story in (16,17,18,19,20,21,22,24,25,26,27) or main_story >= 35) ) or (gtime == 0 and day >= 5):
        show btn_comicbookstore_day_jacob_idle2
        $ renpy.pause(0.001)

    show pov neutral at left
    with dissolve
    show hit neutral_talk at right
    with dissolve
    hit "Hey, [povname]."
    show pov neutral_talk at left
    show hit neutral at right
    pov "Hey."
    show pov embarrassed at left
    show hit embarrassed_talk at right
    hit "Jacob told me that you're looking for the latest issue of um... ‘Eff.. B-word, Pay Weekly'?"
    show pov embarrassed_talk at left
    show hit neutral at right
    pov "Ohh, no. I wasn't looking for it, I didn't even know that it was a thing before Jacob brought me along, honest."
    show pov embarrassed at left
    show hit neutral_talk at right
    hit "Don't worry. It's nothing to get embarrassed by. I know how boys are like."

    jump lbl_about_hitomi_2

label lbl_about_hitomi_2:
    menu:
        "Are you and Jacob dating?" if abouthitomi_dating == 0:
            jump lbl_about_hitomi_dating

        "I'll take the magazine." if abouthitomi_magazine == 0:
            jump lbl_about_hitomi_magazine

        "How's work?" if abouthitomi_work == 0:
            jump lbl_about_hitomi_work

        "A job" if 16 <= main_story <= 21 and nextday_ajob == 0 and comicbookstore_ajob == 0:#For if not yet bought magazine
            hide btn_comicbookstore_day_hitomi_idle2
            jump lbl_comicbookstore_day_hitomi_ajob

        "I've gotta go." if abouthitomi_go == 0:
            jump lbl_about_hitomi_go

label lbl_about_hitomi_dating:
    show pov neutral_talk at left
    show hit confused at right
    pov "Are you and Jacob dating?"
    show pov neutral at left
    show hit confused_talk at right
    hit "No, you must be mistaken, we're just friends."
    show pov embarrassed_talk at left
    show hit neutral at right
    pov "It was just that, he called you ‘babe' earlier."
    show pov neutral at left
    show hit bored_talk at right
    hit "Yeah, he does that. I tell him to stop but he insists."
    show pov neutral_talk at left
    show hit neutral at right
    pov "Sounds a little annoying to be frank."
    show pov neutral at left
    show hit neutral_talk at right
    hit "It's alright, that's just how he is with the girls."
    hit "And between you and me, Jacob is a little cringey when it comes to dating. I think he's still a virgin."

    $ abouthitomi_dating = 1
    $ abouthitomi_go = 0

    jump lbl_about_hitomi_2

label lbl_about_hitomi_magazine:
    show pov embarrassed_talk at left
    show hit neutral at right
    pov "Actually, on second thought, I'll take that magazine."
    show pov neutral at left
    show hit embarrassed_talk at right
    hit "Oh, really? That'll be $30."
    $ abouthitomi_go = 0

    jump lbl_comicbookstoremenu

label lbl_about_hitomi_work:
    show pov neutral_talk at left
    show hit neutral at right
    pov "How's work?"
    show pov neutral at left
    show hit neutral_talk at right
    hit "Work is good as usual. I like managing this place, not too busy but enough people drop by to make it not feel lonely."
    show pov neutral_talk at left
    show hit neutral at right
    pov "Is it usually guys that come here?"
    show pov neutral at left
    show hit neutral_talk at right
    hit "Yeah. But that should be expected since comic books really are a male dominated interest."
    show pov bored_talk at left
    show hit neutral at right
    pov "And the porn."
    show pov bored at left
    show hit bored_talk at right
    hit "And the porn."

    menu:
        "Do you like reading comics?":
            if hitomi_points <= 9:
                $ hitomi_points += 1
                $ renpy.notify("Your relationship with Hitomi has increased")
            else:
                $ hitomi_points = 10
            show pov neutral_talk at left
            show hit neutral at right
            pov "Do you like reading these comic books, or the manga?"
            show pov neutral at left
            show hit neutral_talk at right
            hit "I do find myself enjoying them and they are quite interesting. I guess I converted into a fangirl since the only thing I do all day is hold my post and read."

            jump lbl_about_hitomi_3
        "It seems like a boring job.":
            show pov bored_talk at left
            show hit bored at right
            pov "It seems like an excruciatingly boring job to be in."
            show pov bored at left
            show hit bored_talk at right
            hit "I mean, I guess to you but it's just the way I like it."

            jump lbl_about_hitomi_3

label lbl_about_hitomi_3:
    $ abouthitomi_work = 1
    $ abouthitomi_go = 0

    jump lbl_about_hitomi_2

label lbl_about_hitomi_go:
    show pov neutral_talk at left
    show hit neutral at right
    pov "I've gotta go. It was really nice meeting you, Hitomi. Good luck with the store."
    show pov neutral at left
    show hit neutral_talk at right
    hit "See you around, [povname]. Hope to see you in here again soon."
    if (abouthitomi_dating and abouthitomi_magazine and abouthitomi_work) == 1:
        $ hitomi_path = 1

    jump lbl_comicbookstore_day_setup
