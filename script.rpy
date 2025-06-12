# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define moss = Character("Moss",color = "#8A9A5B")
define Character_Menu = Character("Character Menu", color="#ffffff")

# The game starts here.

label start:
    scene None
    show None
    #voice speaking

    Character_Menu "Click a charater to select"

    menu:
        "Moss":
            scene moss_bg at center:
                zoom .5
                blur 15
            show moss_idle at center:
                zoom 2.3
            "moss"
            jump start

        "Sana":
            scene sana_room at center:
                zoom 1.5
                blur 15
            show sana_idle at center:
                zoom 1.5
            "sana"
            jump start

        "beelz":
            scene beelz_room at center:
                zoom 1.5
            "beelz"
            jump start

        "brick":
            scene brick_room at center:
                zoom 1.8
                blur 15
            "brick"
            jump start

        "joy":
            scene joy_idle at center:
                zoom .8
            "joy"
            jump start

    return




