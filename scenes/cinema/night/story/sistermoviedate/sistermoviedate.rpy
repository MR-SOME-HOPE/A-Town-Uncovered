## Sister Movie Date ##
label lbl_sister_movie_date:
    $ inventory.money -= 60
    if premoviedate_changemind == 1:
        pass
    else:
        $ renpy.notify("Current Balance: $[inventory.money]")
    if moviedate_choice == 1:
        jump lbl_sister_movie_date_action
    elif moviedate_choice == 2:
        jump lbl_sister_movie_date_horror
    elif moviedate_choice == 3:
        jump lbl_sister_movie_date_romance

label lbl_sister_movie_date_action:
    if sister_points <= 5:
        jump lbl_sister_movie_date_action_1
    elif sister_points <= 8:

        menu:
            "Just chill and enjoy the film":
                jump lbl_sister_movie_date_action_1
            "Ask [sister] for a helping hand":
                jump lbl_sister_movie_date_action_2
    else:
        menu:
            "Just chill and enjoy the film":
                jump lbl_sister_movie_date_action_1
            "Ask [sister] for a helping hand":
                jump lbl_sister_movie_date_action_2
            "Ask [sister] if she wants a movie snack":
                jump lbl_sister_movie_date_action_3

label lbl_sister_movie_date_horror:
    if sister_points <= 5:
        jump lbl_sister_movie_date_horror_1
    elif sister_points <= 8:

        menu:
            "Just chill and enjoy the film":
                jump lbl_sister_movie_date_horror_1
            "Ask [sister] for a helping hand":
                jump lbl_sister_movie_date_horror_2
    else:
        menu:
            "Just chill and enjoy the film":
                jump lbl_sister_movie_date_horror_1
            "Ask [sister] for a helping hand":
                jump lbl_sister_movie_date_horror_2
            "Ask [sister] if she wants a movie snack":
                jump lbl_sister_movie_date_horror_3

label lbl_sister_movie_date_romance:
    if sister_points <= 5:
        jump lbl_sister_movie_date_romance_1
    elif sister_points <= 8:

        menu:
            "Just chill and enjoy the film":
                jump lbl_sister_movie_date_romance_1
            "Ask [sister] for a helping hand":
                jump lbl_sister_movie_date_romance_2
    else:
        menu:
            "Just chill and enjoy the film":
                jump lbl_sister_movie_date_romance_1
            "Ask [sister] for a helping hand":
                jump lbl_sister_movie_date_romance_2
            "Ask [sister] if she wants a movie snack":
                jump lbl_sister_movie_date_romance_3
