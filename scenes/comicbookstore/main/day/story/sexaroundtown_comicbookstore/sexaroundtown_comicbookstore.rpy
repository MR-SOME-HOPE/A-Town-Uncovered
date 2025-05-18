## Sex Around Town (Comic Book Store) ##
label lbl_sex_around_town_comicbookstore:
    pov "{i}Where's Hitomi?{/i}"
    pov "{i}Talk about a quiet day.{/i}"
    pov "{i}Wait... I hear something coming from the back room{/i}"
    $ sexaroundtowncomicbookstore += 2

    jump lbl_comicbookstore_day_setup

label lbl_sex_around_town_comicbookstore_1:

    scene bg hitomi_sexworldgangbang_1
    with fade
    show bg hitomi_sexworldgangbang_1
    $ renpy.pause(1,hard=True)
    show bg hitomi_sexworldgangbang_2
    $ renpy.pause(1,hard=True)
    show bg hitomi_sexworldgangbang_1
    $ renpy.pause(1,hard=True)
    show bg hitomi_sexworldgangbang_2
    $ renpy.pause(1,hard=True)
    pov "{i}Oh my God. That- is- utterly disgusting.{/i}"
    pov "{i}Hitomi, how could you... with him?{/i}"

    menu:
        "Get out of there":
            pov "{i}Like hell am I going into that rank sausage fest.{/i}"

            jump lbl_sex_around_town_comicbookstore_1_1
        "Walk in and fight for her" if hitomibeachaccident_firsttimedone == 1:# hitomi_points >= 5
            show bg hitomi_sexworldgangbang_3
            $ renpy.pause(1,hard=True)
            show bg hitomi_sexworldgangbang_4
            hit "[povname]! Hey, how's it going?"
            if skill_str <= 7:
                show bg hitomi_sexworldgangbang_5
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_6
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_7
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_8
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_9
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_10
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_17
                hit "Oh my God! [povname]! Are you okay?"
                show bg hitomi_sexworldgangbang_11
                menu:
                    "Yeah..":
                        pov "Mmm.. yeah. I'm fine."
                        show bg hitomi_sexworldgangbang_4
                        hit "Why the hell did you swing at Kev?"
                        lor "It's Lord Kevlamin, you whore!"
                        show bg hitomi_sexworldgangbang_15
                        hit "Shut up and finish already."
                        if skill_str >= 1:
                            $ skill_str -= 1
                            $ renpy.notify("You lost a Strength Point")#\nYour relationship with Lord Kevlamin has decreased
                        else:
                            $ skill_str = 0
                        #if lordkevlamin_points >= 1:
                        #    $ lordkevlamin_points -= 1
                        #else:
                        #    $ lordkevlamin_points = 10


                        jump lbl_sex_around_town_comicbookstore_1_1
                    "Stay Silent":
                        pov "..."
                        show bg hitomi_sexworldgangbang_15
                        hit "Did you antagonize him, Kev?"
                        lor "I have done no such thing. I have no idea what his problem is."
                        show bg hitomi_sexworldgangbang_16
                        lor "Thanks for protecting me, Davendithas."
                        dav "..."
                        if skill_str >= 1:
                            $ skill_str -= 1
                            $ renpy.notify("You lost a Strength Point")#\nYour relationship with Lord Kevlamin has decreased
                        else:
                            $ skill_str = 0
                        #if lordkevlamin_points >= 1:
                        #    $ lordkevlamin_points -= 1
                        #else:
                        #    $ lordkevlamin_points = 10


                        jump lbl_sex_around_town_comicbookstore_1_1
            else:
                show bg hitomi_sexworldgangbang_5
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_6
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_7
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_12
                $ renpy.pause(1,hard=True)
                lor "What the fuck!"
                show bg hitomi_sexworldgangbang_15
                hit "Hey! Watch it!"
                show bg hitomi_sexworldgangbang_16
                hit "What the fuck are you doing, [povname]?!"
                show bg hitomi_sexworldgangbang_17
                lor "Yeah, you peasant! Get this fool out of here."
                show bg hitomi_sexworldgangbang_13
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_14
                $ renpy.pause(1,hard=True)
                show bg hitomi_sexworldgangbang_11
                $ renpy.pause(1,hard=True)
                if hitomi_points >= 1:
                    $ hitomi_points -= 1
                else:
                    $ hitomi_points = 10
                #if lordkevlamin_points >= 1:
                #    $ lordkevlamin_points -= 1
                #else:
                #    $ lordkevlamin_points = 10
                #$ renpy.notify("Your relationship with Hitomi has decreased\nYour relationship with Lord Kevlamin has decreased")

label lbl_sex_around_town_comicbookstore_1_1:
    $ sexaroundtowncomicbookstore -= 1

    jump lbl_comicbookstore_day_setup

label lbl_sex_around_town_comicbookstore_2:
    show bg hitomi_sexworldgangbang_1
    with fade
    $ renpy.pause()
    show bg comicbookstore_daysexworld
    with fade
    pov "{i}Jeez.. Why'd I look in here again.{/i}"
    pov "{i}Hitomi.. You deserve better than that.{/i}"

    jump lbl_comicbookstore_day_setup
