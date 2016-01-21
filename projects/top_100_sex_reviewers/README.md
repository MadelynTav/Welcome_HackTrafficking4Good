# t100sr

## Review Site Analysis ##

<b>Project Background: </b> “John boards” are sites where prospective and high frequency buyers review individuals and venues  associated with the illegal sex trade (think a Yelp for paid sex). By actively participating in these sites, these buyers move into the category of “promoting” or facilitating the illegal sex marketplace. This is the primary engagement portal for the highest frequency buyers – i.e. those buyers who represent only 5% of the market but account for 50% of all transactions. They are also the source of a disproportionate share of the revenue that fuels the sex trade and attracts traffickers. These sites contain important data to help law enforcement identify the leading facilitators of exploitation while also generating leads to uncover victims / trafficked women.


<b>Project #1:</b> Create a profiling tool that analyzes the most frequent reviewers on popular sex buyer review sites capturing

<ol>
<li>Rubmaps </li>
<ul>
<li>National massage parlor review site offering information on illicit massage parlor activity.</li>
</ul>
<li>The Erotic Review</li> 
<ul>
<li>Self-proclaimed community of hobbyists and prostituted individuals including escort reviews, site reviews, discussion boards, live chat and guides.</li>
</ul>
<li>USA Sex Guide</li>
<ul>
<li>A free forum for the exchange of information between men who are looking for sex with women.</li>
</ul>
</ol>

Data collection and analysis would include:
<ol>
<li>Top reviewers by screenname</li>
<li>Most reviewed venues</li>
<li>Chat logs searchable by screenname</li>
<li>Delineation of posts/reviews by direct reviews or ongoing conversations between revewiers</li>
</ol>

<b>Project #2</b> Utilizing provided screen names of the top 100 posters on a selected site, analyze their blog posts and direct chatter. Develop a visual social networking tool depicting the relationship between higheset frequency buyers and their: 
<ol>
<li>Buying preferences (i.e., type of location, time, buying frequency, etc.)</li>
<li>Preferred venues and providers</li>  
<li>Relationships with other review site users</li>
</ol>

<b>Project Resources:</b>

<b>Aggregated Data for Review Sites:</b> 
<ol>
<li>USA Sex Guide </li>
<li>The Erotic Review </li>
<li>Eccie</li>

</ol>

<b>Aggregated Data Includes:</b>
<ol>
<li>Metrics</li>
<ul>
<li> Messages – the number of posts including duplicates/reposts</li></ul>
<ul>
<li> Unique_messages – the number of posts excluding duplicates/reposts</li></ul>
<ul>
<li> Unique_users – the number of unique users based on phone number or author name</li></ul>
<ul>
<li> Unique_super_users – the number of users who posted more than 30 unique posts </li></ul>

<li>Dimensions</li>
<ul>
<li> Month (2014-11 to 2015-10) – the data can be aggregated by month</li></ul>
<ul>
<li> Source (Eccie, The Erotic Review, USA Sex Guide) </li></ul>
</ol>

<b>Log-level Data for Review Sites: </b>
<ol>
<li>USA Sex Guide </li>
<li>The Erotic Review </li>
<li>Rubmaps</li>
<li>Eccie</li>
</ol>

<b>Log-Level Data Includes:</b>
<ol>
<li>Metrics</li>
<li>guid</li>
<li>creation_date – this includes the creation date and the time</li>
<li>source (e.g, backpage, cityvibe, etc)</li>
<li>url</li>
<li>title</li>
<li>text – the content of the ad/post</li>
<li>author</li>
<li>author_age</li>
<li>city_state</li>
<li>coordinates – some of the ads/posts include geo coordinates which are determined </li>
<li>by the website</li>
<li>phone number</li>
<li>post_id</li>
<li>timezone_label – ET, PT, etc.</li>
<li>timezone_offset – difference between UTC and the local time zone</li>
</ol>


<b>Additional Resources Include:<b>

<ol>

<li>Top 100 Posters </li>
<li><a href="https://gephi.org/">Gephi</a></li>
<li><a href="https://github.com/Berico-Technologies/CLAVIN">CLAVIN</a></li>
<li><a href="https://github.com/rkuykendall/map-world-news">Sentiment Analysis</a></li>
</ol>
