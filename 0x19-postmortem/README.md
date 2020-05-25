LEAD UP
From the time of 13:44 and 18:29 on the date of the 20th of August 2012, an error in the configuration file of the server appeared as a typo, calling a file using the wrong suffix. This caused the web page to load an error 400 page upon trying to access the site.

FAULT
The event arose from a simple misprint, everyone makes mistakes and sometimes, after working for hours, we miss a typo and it causes our entire server to crash :(. The implementation was made during 13:43. 

IMPACT
The method used to solve the issue was to find the file that was misprinted, locate the correct file name, and swap the strings out completely. This allowed us to run our server without unwanted 400 responses. 

DETECTION
The main bug in this report is a failure to load the appropriate resources needed to load the web server, which was identified by a misspelled file. An initial method was implemented by the use of tmux and strace to help identify the error. However, upon being faced with a stream of information (sometimes there’s a huge amount of information to parse and could take time to go through), the decision was made to try and google “common 400 errors wordpress response issues.” A few StackOverflow threads later and the consensus was to first look at the server logs, then, try to locate the configuration file. After finding the error, (THREE HOURS LATER), the line 98 had a misspelled file causing the server to crash.

RESPONSE
The issue was identified using Google. The query implemented was "common 400 wordpress response issues." Upon loading, multiple sources suggested looking into the configuration file. This file contains most of the resources and implementations necessary to run a web server. A sed command was used to find the typo and replace it using a simple regex expression!

RECOVERY
Often times we won't have the luxury to have much downtime on our servers. This could mean loss of potential traffic and inturn could cause major financial mishaps for a company. Luckily, our server is just hosting a blog, which could be frustrating to visitors interested in our content but isn't too dire a situation. Approximately 100% of all users were affected.

TIMELINE
<13:00> - User decides to look through configuration file
<13:03> - User changes file to add new feature to site
<13:19> - User restarts server to view newest implementations
<13:24> - User adds another feature to the site
<13:32> - User adds another feature to the site
<13:33> - Server returns 400 response
<18:13> - User tries to run tmux, strace
<18:44> - tmux, strace return set of information
<18:45> - Google is searched for possible errors
<18:48> - Typo is fixed using sed command to fix and change string
<18:49> - Server returns 200 response code, blog is back up, live and serving content

