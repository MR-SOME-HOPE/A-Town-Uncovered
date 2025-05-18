## Mom Movie Date ##
label lbl_mom_movie_date:
    if winc == 0:
        jump lbl_mom_movie_date_winc0
    $ inventory.money -= 60
    if premoviedate_changemind == 1:
        pass
    else:
        $ renpy.notify("Current Balance: $[inventory.money]")
    if moviedate_choice == 1:
        jump lbl_mom_movie_date_action
    elif moviedate_choice == 2:
        jump lbl_mom_movie_date_horror
    elif moviedate_choice == 3:
        jump lbl_mom_movie_date_romance

label lbl_mom_movie_date_action:
    if mum_points <= 5:
        jump lbl_mom_movie_date_action_1
    elif mum_points <= 8 or momhasdonebj == 0:

        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_action_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_action_2
    else:
        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_action_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_action_2
            "Ask Mom if she wants a movie snack":
                jump lbl_mom_movie_date_action_3

label lbl_mom_movie_date_horror:
    if mum_points <= 5:
        jump lbl_mom_movie_date_horror_1
    elif mum_points <= 8 or momhasdonebj == 0:

        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_horror_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_horror_2
    else:
        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_horror_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_horror_2
            "Ask Mom if she wants a movie snack":
                jump lbl_mom_movie_date_horror_3

label lbl_mom_movie_date_romance:
    if mum_points <= 5:
        jump lbl_mom_movie_date_romance_1
    elif mum_points <= 8 or momhasdonebj == 0:

        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_romance_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_romance_2
    else:
        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_romance_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_romance_2
            "Ask Mom if she wants a movie snack":
                jump lbl_mom_movie_date_romance_3

## NO WINC ##
label lbl_mom_movie_date_winc0:
    $ inventory.money -= 60
    if premoviedate_changemind == 1:
        pass
    else:
        $ renpy.notify("Current Balance: $[inventory.money]")
    if moviedate_choice == 1:
        jump lbl_mom_movie_date_action_winc0
    elif moviedate_choice == 2:
        jump lbl_mom_movie_date_horror_winc0
    elif moviedate_choice == 3:
        jump lbl_mom_movie_date_romance_winc0

label lbl_mom_movie_date_action_winc0:
    if mum_points <= 5:
        jump lbl_mom_movie_date_action_1
    elif mum_points <= 8 or momhasdonebj == 0:

        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_action_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_action_2
    else:
        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_action_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_action_2
            "Ask Mom if she wants a movie snack":
                jump lbl_mom_movie_date_action_3

label lbl_mom_movie_date_horror_winc0:
    if mum_points <= 5:
        jump lbl_mom_movie_date_horror_1
    elif mum_points <= 8 or momhasdonebj == 0:

        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_horror_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_horror_2
    else:
        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_horror_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_horror_2
            "Ask Mom if she wants a movie snack":
                jump lbl_mom_movie_date_horror_3

label lbl_mom_movie_date_romance_winc0:
    if mum_points <= 5:
        jump lbl_mom_movie_date_romance_1
    elif mum_points <= 8 or momhasdonebj == 0:

        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_romance_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_romance_2
    else:
        menu:
            "Just chill and enjoy the film":
                jump lbl_mom_movie_date_romance_1
            "Ask Mom for a helping hand":
                jump lbl_mom_movie_date_romance_2
            "Ask Mom if she wants a movie snack":
                jump lbl_mom_movie_date_romance_3
