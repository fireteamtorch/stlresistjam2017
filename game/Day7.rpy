label Day7Block:

    scene black
    with dissolve

    play music "jingle_dayTitleDenoise.wav" noloop

    show text "Week 7" at Transform(xalign = 0.5, yalign = 0.47) as text1
    #show top_text at truecenter
    with Dissolve(2.0)
    show text "Marching towards the future" at Transform(xalign = 0.5, yalign = 0.53) as text2
    with Dissolve(2.0)
    
    pause 1

    hide text1
    hide text2
    with Dissolve(2.0)

    scene bgBarNight
    show bgCounterTop
    with dissolve

    play music "noir_v002_lpf_LOOPedit.wav"
    #play music "lux_v001_lpf_LOOPedit.wav" fadein 1.0


    "The tension around the town exploded after Charles' exposé."
    
    "This is it... your last day here."
    
    "Jens is stressing out about the diner, but he was too proud to let you see it."
    
    "After he headed home, you decide to get some fresh air. Someone had left a fresh copy of the newspaper next to the front door."
    
    bartender "I guess Charles is still avoiding people."
    
    "You walk back inside, and start flipping through the pages."
    
    "It would seem a large protest is happening later tonight, and all throughout the weekend in front of the governor's mansion."
    
    "Footsteps..."
    
    "Frank steps inside, and sits down at his favorite spot. He looks down at his watch."
    
    frank "Figured I got another hour or so before I gotta head out."
    
    "You hand him a beer."
    
    frank "Hah! You know me well."
    
    "Frank takes a sip, then looks at the table."
    
    frank "Oh dear Lord, you actually served me a lime beer."
    
    "Frank chuckles, then finishes it in one big gulp. He maintained a cool composure, but a subtle frown begins to form."
    
    bartender "Need a normal beer to wash that down?"
    
    frank "Yes, please!"
    
    "Frank accepts the new can with a smile. He takes a large sip, and gargles to rinse the lime flavor away before swallowing."
    
    frank "Much better... Oh God, the taste doesn't go away easy."
    
    bartender "Hah. You didn't have to drink it you know, I was messing."
    
    frank "A beer's a beer... Besides, it's your last day, here ain't it?"
    
    bartender "Yeah, gonna head home."
    
    frank "Ah..."
    
    "Frank nods his head, but it's not hard to tell he's feeling down."
    
    bartender "Heading to the protest?"
    
    frank "Yep... just me."
    
    "Frank takes another sip."
    
    bartender "No one else going?"
    
    frank "Claire wanted to come, but the company she works for is a subsidiary of the people building that plant."
    
    frank "Told her she worked hard to earn that job, and I wouldn't be disappointed in her if she didn't come. She offered to drive me there but I told her I'd be fine."
    
    frank "Poor ol' Charles is avoiding people right now, and I don't blame him. He's having a rough week already... People there would probably recognize him."
    
    frank "And Braxton, well... He's got too many contractor buddies who really need the work. It would be pretty darn awkward."
    
    "Frank looks toward the door, then back to you."
    
    frank "And Elli is working overtime."
    
    bartender "Ah... peacekeeping?"
    
    frank "Just doing her job. I made an extra sign, just in case she changes her mind, since she's already there... Nah... I'm just being dumb..."
    
    "Frank lets out a long sigh."
    
    frank "Everyone's got their reasons... And there'll be people there, on the otherside, who's gonna yell 'QUIT PROTESTING AND GET A JOB!'"
    
    frank "And... maybe I'll even recognize their faces..."
    
    frank "I'm tired... I remember when things were so much simpler... and I think about how much nicer it is to just stay home, and watch shows online."
    
    frank "I'm walking out there cause someone's got to..."
    
    "Frank silently processes his thoughts."
    
    braxton "Wow, Frank took his hat off, truly must be the end of days, I'm gonna need a beer too."
    
    "Braxton enters."
    
    "You slide a beer over the table, and Braxton catches it easily. He puts a hand on Frank's back."
    
    braxton "Hey, Frank. Why the waterworks? You put on that perfume again?"
    
    "Frank's face brightens."
    
    frank "Shut up, I smelled nice."
    
    "Braxton looks over at you and does a subtle headshake."
    
    braxton "Figured I'd come with you."
    
    frank "Oh."
    
    braxton "I mean, I had some talk with my pals. It's not like we 'hate progress' or 'want the local businesses to fail' or whatever it is that people say."
    
    "Braxton takes a long swig of his beer."
    
    frank "I have an extra sign."
    
    braxton "Nice. I guess I don't have to make a sign that rhymes 'regulation' with 'next generation'."
    
    "Frank looks at you and gives you a subtle headshake."
    
    braxton "We should probably head out."
    
    "They settle their tabs and both smile at you."
    
    frank "Thanks for the beers."
    
    braxton "Have a safe trip home."
    
    "After they depart, you take your time putting everything away."
    
    "The lock clicks as you turn the diner keys for the last time. Chilling wind blows past your face, your breath puffs, then fades."
    
    "Everything comes to an end..."
    
    "Jens hugs you warmly as you dropped off the keys, and promises to come up for Thanksgiving."
    
    "It's going to be a long drive home..."


    stop music fadeout 1.0
    pause 1
    show text "End of Day" at truecenter as text3
    with dissolve
    play music "jingle_endOfDayDenoise.wav" noloop
    pause 2
    hide text3
    with dissolve
    pause 3

return