Twitter Trends
==========

This is a python package, which can be used to get the twitter trends from different countries and number of  trends. For this package I have used the twitter package from python library. It will return the list of trends of a country.

Install
~~~~~~~

::
    git clone git@github.com:saudBinHabib/twitter_trends.git
    vi ~/.bashrc
    # add these 4 lines in the end of this file.
    export TWITTER_CONSUMER_KEY=Udxy6q9vuMHyESFe5a2Y3tsBv
    export TWITTER_CONSUMER_SECRET=CDlMreFFIRhjyGRtePZrOPQw3xSOslJPktmDB6P7zHHmnno4Dv
    export TWITTER_OAUTH_TOKEN=2365425174-Cqk55BEV8rSpVDwSgLGIObNow4v3arHJRIkTr1I
    export TWITTER_OAUTH_TOKEN_SECRET=JwcAgBGZk6yLK5rDRmX662tDngrsp7Z1bbstMRiGv8WJH
    source ~/.bashrc
    cd twitter_trends
    pip install -e .


~~~~~~~~~~~~~~~~
Twitter Trends Console Commands

    ::
    
    #checking the ttrends package version.
    
    ttrends_version
    
    twitter_trends --country london --top 5
    twitter_trends --country germany --top 20
    twitter_trends --country pakistan --top 10
    twitter_trends --country argentina
