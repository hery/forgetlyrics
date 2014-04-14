ForgetLyrics
==========

Ever get tired of those lyrics websites full of ads? 
We all do, which is why I wrote this small script that fetches lyrics in your terminal.
Why ForgetLyrics? Because I can never remember these freaking lyrics, and with this app, I can now forget them for good and just read them. (Assuming there is a terminal within reach)

# Installation

## Dependencies

+ python 2.7
+ requests (pip install requests)

## Api Key

The api key that is hard-coded in the script is mine, but feel free to sign up to musixmatch.com to get yours and replace it, as each API key has a limited number of calls.

## System wide (optional step)
For a system wide installation you have the give the execution permission for .py file:
  ```chmod a+x forgetlyrics.py```

Then, link it in the /usr/bin directory (you may need sudo):
  ```ln -s /path/to/forgetlyrics.py /usr/bin/forgetlyrics```

# Usage

    python forgetlyrics.py
    or
    python forgetlyrics.py 'artistName' 'songTitle'

# Demo 1

    $ python forgetlyrics.py
    Artist name contains:
    imagine
    Track title contains:
    demons
    When the days are cold
    And the cards all fold
    And the saints we see
    Are all made of gold
    When your dreams all fail
    And the ones we hail
    Are the worst of all
    And the blood’s run stale

    I want to hide the truth
    I want to shelter you
    But with the beast inside
    There’s nowhere we can hide
    No matter what we breed
    We still are made of greed
    This is my kingdom come
    This is my kingdom come

    When you feel my heat
    Look into my eyes
    It’s where my demons hide
    It’s where my demons hide

    Don’t get too close
    It’s dark inside
    It’s where my demons hide
    It’s where my demons hide

    When the curtain’s call
    Is the last of all
    When the lights fade out
    All the sinners crawl
    So they dug your grave
    And the masquerade
    Will come calling out
    At the mess you made

#Demo 2

    python forgetlyrics.py creedence 'seen the rain'
    Someone told me long ago there's a calm before the storm
    I know, it's been comin' for some time
    When it's over, so they say, it'll rain a sunny day
    I know, shinin' down like water
    
    I wanna know, have you ever seen the rain?
    I wanna know, have you ever seen the rain
    Comin' down on a sunny day?
    
    Yesterday and days before, sun is cold and rain is hard
    I know, been that way for all my time
    'Til forever, on it goes through the circle, fast and slow
    I know, it can't stop, I wonder
    
    I wanna know, have you ever seen the rain?
    I wanna know, have you ever seen the rain
    Comin' down on a sunny day?
    
    Yeah, I wanna know, have you ever seen the rain?
    I wanna know, have you ever seen the rain
    Comin' down on a sunny day?
