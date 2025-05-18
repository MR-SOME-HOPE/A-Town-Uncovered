## Trust and Safety Shield | 0 - Shield Disabled | 1 - Shield Enabled
init -5:
    if renpy.loadable ("g33ptchi.rpy") == True:
        $ trustandsafety_shield = 0
    else:
        $ trustandsafety_shield = 0 ## Originally 1