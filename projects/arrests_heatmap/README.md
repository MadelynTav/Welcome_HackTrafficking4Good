# ar_heatmap

<b>Challenge:</b> There is no centralized system that aggregates data collected (but not necessarily publically reported) by service providers, public media reports, diversion programs and law enforcement on arrests associated with the sex trade. Nor is there a system that provides an analysis of the operational details and demographics associated with these individual arrests. Compiling this data would serve the important public policy goal that addresses the need to eliminate the arrest of prostituted persons vs. their exploiters including buyers. Currently individual studies show that the current ratio is 10 victims arrested for every one exploiter. Mining publicly available data sets to aggregate law enforcement operations would be the first national tool of its kind and will help make the case for mandatory disaggregated reporting.


<b>Project #1:</b>  Create a system that compiles open source arrest information in the following cities into separate databases: Atlanta, Boston, Chicago, Dallas, Denver, Houston, Oakland, Phoenix, Portland, San Diego, and Seattle. Suggested databases: 
<OL>
<LI>Police Twitter Accounts
<UL>
<LI><p><a href="https://twitter.com/Atlanta_Police?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" title="Title">
Atlanta</a></p>
<LI><p><a href="https://twitter.com/bostonpolice?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor">
Boston</a></p>
<LI><p><a href="https://twitter.com/chicago_police">
Chicago</a></p>
<LI><p><https://twitter.com/DallasPD?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" title="Title">
Dallas</a></p>
<LI><p><a href="https://twitter.com/DenverPolice?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" title="Title">
Denver</a></p>
<LI><p><a href="https://twitter.com/houstonpolice?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" title="Title">
Houston</a></p>
<LI><p><a href="https://twitter.com/oaklandpoliceca?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" title="Title">
Oakland</a></p>
<LI><p><a href="https://twitter.com/phoenixpolice?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" title="Title">
Phoenix</a></p>
<LI><p><a href="https://twitter.com/PortlandPolice?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" title="Title">
Portland</a></p>
<LI><p><a href="https://twitter.com/SanDiegoPD?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" title="Title">
San Diego</a></p>
<LI><p><a href="https://twitter.com/SeattlePD?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor" title="Title">
Seattle</a></p>
</UL>
<LI>Public Complaint Platforms
<UL>
<LI><p><a href="http://acrbgov.org/complaints-reviewed/" title="Title">
Atlanta</a></p>
<LI><p><a href="http://www.cityofboston.gov/images_documents/COOP%202014%20Annual%20Report%5B1%5D_tcm3-50903.pdf" title="Title">
Boston</a></p>
<LI><p><a href="https://portal.chicagopolice.org/portal/page/portal/ClearPath/Communities/Crime_Alerts" title="Title">
Chicago</a></p>
<LI><p><a href="http://www.dallaspolice.net/publicdata/offense-search.html" title="Title">
Dallas</a></p>
<LI><p><a href="http://web6.seattle.gov/mnm/incidentresponse.aspx" title="Title">
Seattle</a></p>
</UL> 
<LI>Open Source Pubic Arrest Data
<UL>
<LI><p><a href="http://www.atlantapd.org/pdf/uniform-crime-reports/E3E0F499-C22A-40FC-A7DF-D5058AD5B59A.pdf" title="Title">
Atlanta</a></p>
<LI><p><a href="http://www.atlantapd.org/crimedatadownloads.aspx" title="Title">
Atlanta Crime Statistics</a></p>
<LI><p><a href="https://data.cityofboston.gov/Public-Safety/Crime-Incident-Reports/7cdf-6fgx" title="Title">
Boston Crime Inicident Report</a></p>
<LI><p><a href="http://www.chicagopolice.org/ps/" title="Title">
Chicago Police Records</a></p>
<LI><p><a href="https://www.dallasopendata.com/Police/75219/ki94-jaz4" title="Title">
Dallas</a></p>
<LI><p><a href="https://www.denvergov.org/content/denvergov/en/police-department/crime-information/crime-map.html" title="Title">
Denver</a></p>
<LI><p><a href="http://htowntx.com/category/arrests/" title="Title">
Houston Arrest Log</a></p>
<LI><p><a href="http://www.crimemapping.com/map.aspx?aid=aabb6970-e7b7-4ce2-b155-cf04843f1625" title="Title">
Oakland Crime Mapping</a></p>
<LI><p><a href="https://www.phoenix.gov/policesite/Documents/ucr_monthly_2015.pdf" title="Title">
Phoenix</a></p>
<LI><p><a href="https://www.crimereports.com/map/index/?search=Portland,%20OR">
Portland</a></p>
<LI><p><a href="https://www.crimereports.com/map/index/?search=SanDiego,%20CA" title="Title">
San Diego</a></p>
<LI><p><a href="http://web6.seattle.gov/mnm/policereports.aspx" title="Title">
Seattle</a></p>
</UL> 
</OL>

<b>Project #2:</b> Develop visualization tolls to display arrest data including a dynamic spatial imaging heat map platform that  can be used to display arrest data compiled from open and closed sources. Create a function that searches results by: size of operation, time and date, type of arrest (i.e., street vs. hotel), demographic data (male, female, sex buyer, exploiter, prostituted individual, etc.). <i>NOTE: We do not endorse shaming any arrested individuals. Please refrain from compiling personal identifiable information such as mugshots, names, and addresses. </i>



<b>Visualization Tools</b>
<p><a href="https://docs.djangoproject.com/en/1.8/ref/contrib/gis/" title="Title">
GeoDjango</a></p>
<p><a href="http://lumify.io/" title="Title">
Lumify</a></p>
<p><a href="http://leafletjs.com/" title="Title">
Leaflet</a>;<a href="https://github.com/EricSchles/leaflet_flask_basic" title="Title">
Intro to Leaflet</a> </p>
<p><a href="https://cartodb.com/" title="Title">
CartoDB</a></p>
