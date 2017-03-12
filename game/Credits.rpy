label CreditsBlock:

    scene black
    with dissolve

    play music "lux_v001_lpf_LOOPedit.wav" fadein 1.0 fadeout 1.0
    
    show text "{size=100}'Bar Story'{/size}{size=60}\n\nA Resist Jam Game\nMarch 3 - 12, 2017\nMade in Ren'Py{/size}" at truecenter
    with Fade(1.0, 0.0, 1.0)
    $ renpy.pause(2.0,hard='True')
    pause 2.0
    
    show text "{size=100}Concept & Design{/size}{size=60}\n\nChris House\nDavid Song\nJeffrey Hsu\nJonathan Bo\nSarah Wahoff\nYi Zhu{/size}" at truecenter
    with Fade(1.0, 0.0, 1.0)
    pause 4.0
    
    show text "{size=100}Programming{/size}{size=60}\n\nJeffrey Hsu\nDavid Song\nYi Zhu{/size}" at truecenter
    with Fade(1.0, 0.0, 1.0)
    pause 4.0
    
    show text "{size=100}Art & Visual Design{/size}{size=60}\n\nChris House{/size}" at truecenter
    with Fade(1.0, 0.0, 1.0)
    pause 4.0
    
    show text "{size=100}Music & Sound{/size}{size=60}\n\nDavid Song\nSarah Wahoff{/size}" at truecenter
    with Fade(1.0, 0.0, 1.0)
    pause 4.0
    
    show text "{size=100}Story & Writing{/size}{size=60}\n\nYi Zhu\nJonathan Bo{/size}" at truecenter
    with Fade(1.0, 0.0, 1.0)
    pause 4.0
    
    show text "{size=100}Special Thanks To{/size}{size=60}\n\nSt. Louis Game Developer Co-op{/size}" at truecenter
    with Fade(1.0, 0.0, 1.0)
    pause 4.0
    
    show text "{size=100}Presented By{/size}{size=60}\n\nTeamTBA\nStudio PaintedBlade{/size}" at truecenter
    with Fade(1.0, 0.0, 1.0)
    pause 4.0
    
    show text "{size=100}Thank you for playing!{/size}" at truecenter
    with Fade(1.0, 0.0, 1.0)
    
    ""
    hide text
    with dissolve

return