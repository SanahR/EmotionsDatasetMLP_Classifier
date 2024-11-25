# Results
To create this page, I ran the program 3 times, and then I pasted the results here. Hopefully, this gives you a more complete picture of what the program does. While I did initially run it with verbose on, I decided to spare both of us the time by cutting out the unnecessary parts. 
## Trial 1: 
Your tweet was:  i think we were both feeling a little drained from work as well

The MLP algorithm classified your tweet as:  sadness
The accuracy percentage of our MLP algorithm is:  83.89999999999999

Your second tweet was:  i went around for the rest of the day feeling distressed that i changed my appearance based on someones comments how i made myself even by coincidence more appealing to him and that just felt wrong wrong wrong

The KNN algorithm classified your tweet as:  sadness
The accuracy percentage of our KNN algorithm is:  76.4

Since the emotions dataset is based off of semi-ambiguous tweets, there are several times when the classifiers can't detect sarcasm or irony, which definitely contributes to the low 80s barrier that neither of them can break through in terms of accuracy. 

## Trial 2: 
Your tweet was:  i just finished watching a korean drama secret garden omg and am feeling the way girls do after such shows a mixture of hope and a little tug of truth that says those romantic gestures only exist in films

The MLP algorithm classified your tweet as:  love
The accuracy percentage of our MLP algorithm is:  82.69999999999999

Your second tweet was:  i feel a bit dazed but so excited i am going to be so protective she is not going to be let out until she is

The KNN algorithm classified your tweet as:  joy
The accuracy percentage of our KNN algorithm is:  76.4

## Trial 3: 
Your tweet was:  i feel so lousy but i shouldnt be focusing on me now

The MLP algorithm classified your tweet as:  sadness
The accuracy percentage of our MLP algorithm is:  83.15

Your second tweet was:  i am running at an approximate minute pace which i feel is quite acceptable

The KNN algorithm classified your tweet as:  joy
The accuracy percentage of our KNN algorithm is:  76.4

## Personal Findings: 
I've ran this program quite a lot, especially when I was working out what parameters worked best, and I've seldomly seen the KNN classifier identify a more complex emotion like love. It typically only identifies joy and sadness. Perhaps in the future, I'll graph it out to see if this correlation is just in my head. 
