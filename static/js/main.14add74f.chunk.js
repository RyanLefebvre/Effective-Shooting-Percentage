(this["webpackJsonpeffective-shooting-percentage"]=this["webpackJsonpeffective-shooting-percentage"]||[]).push([[0],{192:function(e,t,a){e.exports=a(284)},197:function(e,t,a){},203:function(e,t,a){},273:function(e,t,a){},274:function(e,t,a){},275:function(e,t,a){},276:function(e,t,a){},277:function(e,t,a){},278:function(e,t,a){},279:function(e,t,a){},280:function(e,t,a){},284:function(e,t,a){"use strict";a.r(t);var n=a(0),l=a.n(n),r=a(20),s=a.n(r),o=(a(197),a(31)),i=a(32),c=a(34),m=a(33),h=a(35),d=a(2),u=a(8),p=a.n(u),f=a(9),g=a.n(f),b=a(66),E=a.n(b),w=a(67),y=a.n(w),v=a(68),x=a.n(v);a(203);var S=function(){return l.a.createElement("div",{id:"graphFlex"},l.a.createElement("div",{className:"flexManager"},l.a.createElement("div",{className:"flexImage imgWrapper"},l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:y.a,alt:"Connor Buczek"}),l.a.createElement("div",null,"Connor Buczek rips two point goal."))),l.a.createElement("div",{className:"flexChildBig"},l.a.createElement(p.a,{className:"cardContentStyles"},l.a.createElement(g.a,null,"The dataset used for this project contains information about 872 professional lacrosse games ranging from 2001-2019. This data was scraped from the official MLL and PLL website using python scripts, then converted into a format that would be useful for an analysis. To learn more about the data for this project, visit the ",l.a.createElement("a",{className:"link",href:"https://ryanlefebvre.github.io/Effective-Shooting-Percentage/#/effectiveShootingPercentage/data"},"data page")," of this site.",l.a.createElement("br",null),l.a.createElement("br",null),"In order to determine whether or not a significant relationship exists between shooting efficiency and success in lacrosse, I used regression analysis. Linnear regression is used to estimate the strength of the relationship between two variables and is a technique that can be applied to the MLL and PLL data I scraped.",l.a.createElement("br",null),l.a.createElement("br",null),"Each of the following scatterplots represent the results of a regression analysis. The coordinate pairs plotted in blue represent an (x,y) pairing for a team's performance over a specific season. These coordinate pairs were created by calculating season stats for professional lacrosse teams using the previously mentioned game dataset.")))),l.a.createElement("div",{class:"fivePixMarg"}),l.a.createElement("div",{className:"flexManager",id:"flexReverse"},l.a.createElement("div",{className:"flexChildBig"},l.a.createElement(p.a,{className:"cardContentStyles"},l.a.createElement(g.a,null,"The x-coordinate of the plotted points represents a team\u2019s average performance for a statistic of interest over a given season. The y-coordinate of the point represents that teams winning percentage for the same season. The line of best fit plotted in pink represents the predicted winning percentage for a team whose performance in the statistic of interest is equal to the x-coordinate of the point that falls on that line. In other words, for each (x, y) coordinate pair that falls on the line of best fit, we would expect a winning percentage of y based upon the team\u2019s performance of x.",l.a.createElement("br",null),l.a.createElement("br",null),"The reason I used average performance for a statistic of interest instead of absolute performance is because it is a better representation of how a team performed game in and game out over a given season. For example, imagine a team's shooting performance over 3 games. Games one and two they played slightly below average teams in the league and shot very poorly. In game three they played the worst team in the league. This team\u2019s goalie couldn't stop a beach ball and our imaginary team shot very well. Respectively over the 3 games they shot 3/12, 2/16 and 18/27. Their inability to shoot well against slightly below average teams would indicate they are a team that in general shoots poorly, but how well is this reflected by our statistic of interest after the outlier game against the worst team in the league?",l.a.createElement("br",null),l.a.createElement("br",null),"This team\u2019s performances result in an absolute shooting percentage of ((3 + 2 + 18) / (12 + 16 + 27)) = 23/55 = 41.8%. However, this teams average shooting percentage is ((3/12 + 2/16 + 18/27) / 3) = 34.7%. While the difference between absolute and average shooting percentage for this example may appear small at only 7%, the relative decrease from absolute to average is 17% which is a more significant difference. This has to do with why the average shooting percentage is a more accurate representation of how we would expect a given team to shoot. This is because taking the average of each game is able to reduce how the outlier game against the worst team in the league impacts the statistic of interest."))),l.a.createElement("div",{className:"flexImage imgWrapper"},l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:E.a,alt:"Myles Jones"}),l.a.createElement("div",null,"Myles Jones dodging against Lizards.")),l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:x.a,alt:"Adam Ghitelman"}),l.a.createElement("div",null,"Adam Ghitelman lets in full field goal.")))))},N=a(50),L=a(70),k=a.n(L),I=a(49),T=(a(273),function(e){function t(){var e,a;Object(o.a)(this,t);for(var n=arguments.length,r=new Array(n),s=0;s<n;s++)r[s]=arguments[s];return(a=Object(c.a)(this,(e=Object(m.a)(t)).call.apply(e,[this].concat(r)))).chartRef=l.a.createRef(),a}return Object(h.a)(t,e),Object(i.a)(t,[{key:"componentDidMount",value:function(){var e=this,t=[],a=[],n=[];this.props.xValues.forEach((function(a){t.push({x:a,y:e.props.yValues[e.props.xValues.indexOf(a)]}),n.push("blue")}));for(var l=t.map((function(e){return e.x})),r=t[l.indexOf(Math.min.apply(Math,Object(N.a)(l)))],s=t[l.indexOf(Math.max.apply(Math,Object(N.a)(l)))],o=(s.x-r.x)/100,i=r.x;i<=s.x;i+=o){var c=i*this.props.m+this.props.b;a.push({x:i,y:c})}var m=this.chartRef.current.getContext("2d");new k.a(m,{type:"scatter",data:{datasets:[{label:this.props.title,data:t,backgroundColor:"blue",pointBackgroundColor:n,pointRadius:3,pointHoverRadius:6},{label:"Best Fit",data:a,pointBackgroundColor:"#ff19af",showLine:!0,backgroundColor:"#ff19af",fill:"none",borderColor:"#ff19af",pointRadius:0}]},options:{scales:{yAxes:[{scaleLabel:{display:!0,labelString:this.props.yLabel}}],xAxes:[{scaleLabel:{display:!0,labelString:this.props.xLabel}}]}}})}},{key:"render",value:function(){return l.a.createElement(I.a,{id:"canvasWrapper"},l.a.createElement(I.b,null,l.a.createElement("canvas",{id:"myChart",ref:this.chartRef})))}}]),t}(n.Component)),C={title:"AES% vs WIN%",xLabel:"AES%",yLabel:"WIN%",xValues:[.289,.284,.307,.289,.303,.324,.553,.494,.505,.522,.524,.566,.57,.493,.509,.492,.491,.486,.494,.509,.532,.515,.447,.447,.487,.522,.473,.49,.533,.504,.51,.501,.49,.477,.511,.452,.514,.482,.492,.505,.476,.507,.465,.511,.487,.44,.499,.535,.438,.506,.513,.451,.417,.443,.521,.473,.491,.492,.474,.505,.499,.481,.487,.503,.45,.491,.537,.496,.506,.402,.499,.486,.528,.486,.518,.462,.481,.479,.519,.501,.466,.5,.643,.417,.48,.488,.528,.571,.441,.513,.469,.469,.529,.459,.505,.474,.51,.451,.457,.468,.467,.511,.482,.498,.476,.51,.36,.447,.463,.439,.49,.452,.506,.358,.514,.458,.465,.447,.456,.526,.495,.507,.389,.594,.466,.478],yValues:[.667,.538,.5,.538,.167,.583,.625,.625,.625,.5,.688,.933,.75,.538,.615,.714,.615,.636,.727,.6,.5,.571,.429,.357,.688,.75,.462,.571,.533,.5,.533,.75,.6,.286,.75,.357,.214,.571,.533,.429,.357,.6,.786,.615,.462,.545,.417,.615,0,.5,.429,.533,.214,.286,.5,.357,.357,.533,.214,.357,.357,.5,.429,.286,.214,.688,.562,.6,.533,.143,.143,.533,.571,.562,.688,.429,.5,.167,.786,.692,.417,0,1,0,.5,.286,.75,1,0,.714,.286,.333,.533,.417,.571,.462,.417,.364,.364,.5,.25,.643,.333,.25,.3,.273,0,.417,.333,.364,.538,.455,.692,.444,.5,.333,.455,.333,.167,.571,.786,.857,0,1,.333,1],m:1.6576335687654042,b:-.3096038470502954},j={title:"AES%D vs WIN%",xLabel:"AES%D",yLabel:"WIN%",xValues:[.004,-.015,-.017,.01,-.019,.038,.053,.009,-.025,-.052,.044,.143,.072,-.017,-.001,.021,.012,-.009,.007,.029,-.021,.045,.023,-.032,.038,.059,-.012,.019,.016,.014,-.041,.014,-.016,.004,.036,-.092,-.026,.012,.037,.014,-.049,.005,.016,.058,.022,-.043,.012,.061,-.138,.006,-.01,-.054,-.114,-.053,-.009,-.005,.002,.024,-.024,.055,-.014,-.01,-.02,0,-.056,.021,.031,.033,-.017,-.118,-.088,.003,.062,-.002,.061,-.051,-.008,-.013,.059,.006,.014,.012,.226,-.226,.038,-.057,.059,.13,-.13,.013,-.11,-.004,.028,-.011,-.002,-.014,-.08,-.052,.002,.015,-.027,.062,-.054,-.049,.026,-.032,-.076,-.056,-.03,-.055,.043,-.051,.059,-.031,.086,.008,-.068,-.081,-.082,.026,.073,.117,-.205,.205,-.103,.049],yValues:[.667,.538,.5,.538,.167,.583,.625,.625,.625,.5,.688,.933,.75,.538,.615,.714,.615,.636,.727,.6,.5,.571,.429,.357,.688,.75,.462,.571,.533,.5,.533,.75,.6,.286,.75,.357,.214,.571,.533,.429,.357,.6,.786,.615,.462,.545,.417,.615,0,.5,.429,.533,.214,.286,.5,.357,.357,.533,.214,.357,.357,.5,.429,.286,.214,.688,.562,.6,.533,.143,.143,.533,.571,.562,.688,.429,.5,.167,.786,.692,.417,0,1,0,.5,.286,.75,1,0,.714,.286,.333,.533,.417,.571,.462,.417,.364,.364,.5,.25,.643,.333,.25,.3,.273,0,.417,.333,.364,.538,.455,.692,.444,.5,.333,.455,.333,.167,.571,.786,.857,0,1,.333,1],m:2.652192280169307,b:.4933827325186005},M={title:"ASh% vs WIN%",xLabel:"ASh%",yLabel:"WIN%",xValues:[.261,.272,.286,.273,.286,.299,.543,.484,.487,.512,.501,.544,.541,.476,.483,.471,.468,.469,.448,.483,.511,.495,.444,.43,.462,.452,.438,.447,.522,.475,.483,.491,.477,.458,.493,.431,.495,.452,.45,.499,.463,.485,.444,.471,.456,.425,.494,.5,.438,.487,.491,.443,.395,.418,.478,.434,.481,.479,.458,.486,.493,.456,.473,.48,.434,.485,.522,.473,.492,.394,.457,.475,.523,.468,.506,.438,.444,.445,.509,.491,.435,.5,.619,.361,.452,.469,.518,.524,.441,.487,.458,.45,.487,.412,.479,.461,.494,.432,.426,.468,.438,.498,.47,.474,.461,.486,.334,.401,.443,.407,.471,.446,.495,.339,.503,.444,.431,.43,.41,.475,.48,.484,.389,.531,.44,.478],yValues:[.667,.538,.5,.538,.167,.583,.625,.625,.625,.5,.688,.933,.75,.538,.615,.714,.615,.636,.727,.6,.5,.571,.429,.357,.688,.75,.462,.571,.533,.5,.533,.75,.6,.286,.75,.357,.214,.571,.533,.429,.357,.6,.786,.615,.462,.545,.417,.615,0,.5,.429,.533,.214,.286,.5,.357,.357,.533,.214,.357,.357,.5,.429,.286,.214,.688,.562,.6,.533,.143,.143,.533,.571,.562,.688,.429,.5,.167,.786,.692,.417,0,1,0,.5,.286,.75,1,0,.714,.286,.333,.533,.417,.571,.462,.417,.364,.364,.5,.25,.643,.333,.25,.3,.273,0,.417,.333,.364,.538,.455,.692,.444,.5,.333,.455,.333,.167,.571,.786,.857,0,1,.333,1],m:1.5507673708139031,b:-.22477089418696755},W={title:"ASh%D vs WIN%",xLabel:"ASh%D",yLabel:"WIN%",xValues:[-.007,-.004,-.018,.012,-.007,.024,.073,.022,-.023,-.034,.036,.132,.078,.012,.002,.016,.004,.009,.015,.022,-.04,.034,.035,-.033,.033,.023,-.041,-.005,.018,-.006,-.043,.044,-.01,.003,.023,-.091,-.022,-.009,.006,.024,-.026,.024,.023,.048,.009,-.039,.014,.05,-.138,-.003,-.009,-.049,-.123,-.067,-.025,-.012,.015,.032,-.016,.047,-.005,-.018,-.014,.001,-.055,.029,.029,.019,-.02,-.111,-.075,-.001,.081,-.002,.062,-.048,-.01,-.017,.064,.023,.011,.012,.258,-.258,.03,-.023,.073,.083,-.083,.026,-.083,-.005,.008,-.024,.006,.004,-.073,-.049,.001,.015,-.023,.068,-.032,-.035,.022,-.043,-.074,-.077,-.042,-.075,.035,-.035,.059,-.024,.082,.009,-.057,-.07,-.107,.012,.073,.108,-.142,.142,-.093,.049],yValues:[.667,.538,.5,.538,.167,.583,.625,.625,.625,.5,.688,.933,.75,.538,.615,.714,.615,.636,.727,.6,.5,.571,.429,.357,.688,.75,.462,.571,.533,.5,.533,.75,.6,.286,.75,.357,.214,.571,.533,.429,.357,.6,.786,.615,.462,.545,.417,.615,0,.5,.429,.533,.214,.286,.5,.357,.357,.533,.214,.357,.357,.5,.429,.286,.214,.688,.562,.6,.533,.143,.143,.533,.571,.562,.688,.429,.5,.167,.786,.692,.417,0,1,0,.5,.286,.75,1,0,.714,.286,.333,.533,.417,.571,.462,.417,.364,.364,.5,.25,.643,.333,.25,.3,.273,0,.417,.333,.364,.538,.455,.692,.444,.5,.333,.455,.333,.167,.571,.786,.857,0,1,.333,1],m:2.7151236602984277,b:.49294561833431394};a(274);var A=function(){return l.a.createElement("div",{id:"parent"},l.a.createElement("div",{className:"plotParent"},l.a.createElement("div",{className:"plotWrapper"},l.a.createElement(T,M)),l.a.createElement("div",{className:"plotWrapper"},l.a.createElement(T,C))),l.a.createElement(p.a,{className:"cardContentStyles"},l.a.createElement(g.a,null,"When performing a regression analysis, a 'correlation coefficient' is used to determine the strength of a linear relationship. Values of a correlation coefficient can range from -1.00 to 1.00, values closer to -1.00 or 1.00 indicate a strong relationship while values closer to 0.00 indicate no relationship. The following guidelines will be used to interpret the correlation coefficients yielded by the regression analyses conducted for this project (",l.a.createElement("a",{className:"link",href:"http://www.dmstat1.com/res/TheCorrelationCoefficientDefined.html"},"Interpetaion guidlines"),").",l.a.createElement("br",null),l.a.createElement("br",null),"The first scatter plot showcases the relationship between a team's average shooting percentage (ASh%) and a team's winning percentage (Win%). The correlation coefficient yielded by this regression analysis is 0.404 indicating a positive moderate relationship between ASh% and Win%. The second scatter plot explores the relationship between average effective shooting percentage (AES%) and Win%. This analysis yielded similar results as the first with a correlation coefficient of 0.433 which also indicates a positive moderate relationship between AES% and Win%.")),l.a.createElement("div",{className:"plotParent"},l.a.createElement("div",{className:"plotWrapper"},l.a.createElement(T,W)),l.a.createElement("div",{className:"plotWrapper"},l.a.createElement(T,j))),l.a.createElement(p.a,{className:"cardContentStyles"},l.a.createElement(g.a,null,"After conducting the first two regression analyses I wondered if there was a more meaningful way to analyze a teams shooting efficiency. I came up with the idea of looking at the difference between a teams shooting efficiency compared to their opponents. I called this statistic, average effective shooting percentage difference (AES%D). The same concept could be applied to traditional shooting percentage to create a statistic called average shooting percentage difference (ASh%D). I hypothesized that if I conducted regression analyses exploring the relationship between these statistics and Win% that there would be a stronger relationship then the relationships found in the initial analyses.",l.a.createElement("br",null),l.a.createElement("br",null),"My hypothesis was correct. The regression analyses conducted using the difference of a team\u2019s shooting performance and their opponents shooting performance had a larger correlation coefficient than the initial analyses. The regression analysis using ASh%D yielded a correlation coefficient of 0.76 and the analysis using AES%D yielded a correlation coefficient of 0.781. Both of these correlation coefficients indicate a strong positive relationship between their respective measures of shooting performance and Win%.")))},P=(a(275),a(71)),O=a.n(P),D=a(72),B=a.n(D);var R=function(){return l.a.createElement("div",null,l.a.createElement(p.a,{className:"cardContentStyles"},l.a.createElement(g.a,null,'Professional field lacrosse leagues have created a "two-point line". If a player stands behind this line when shooting, a goal is worth two points instead of one. Effective Shooting Percentage (ES%) is a new lacrosse statistic that accounts for the fact that a two-point goal is worth more than a one-point goal. The formula for ES% is shown below.')),l.a.createElement("br",null),l.a.createElement("div",{id:"containerContainer"},l.a.createElement("div",{id:"imageContainer"},l.a.createElement("img",{alt:"ES% formula from es%.py",id:"formula",src:B.a}),l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{alt:"Two point shot attempt",id:"twoPointer",src:O.a}),l.a.createElement("div",null,"Tom Schreiber taking a two point shot.")))),l.a.createElement("br",null),l.a.createElement(p.a,{className:"cardContentStyles"},l.a.createElement(g.a,null,"ES% is inspired by a powerful statistic in basketball called effective field goal percentage (EFG%). EFG% accounts for the fact that three point shots are worth more than two point shots. EFG% has been a significant predicator of a team\u2019s offensive performance. For example, in 2013, the Miami Heat and San Antonio Spurs had the highest EFG% in the league and ended up meeting in the NBA finals that year.",l.a.createElement("br",null),l.a.createElement("br",null),"This project aims to explore if a similar relationship to the one seen in basketball between shooting efficiency and team success exists in professional lacrosse. I will compare the relationship between shooting efficiency and team success with the relationship between traditional shooting percentage and team success as a baseline.")))},F=a(73),G=a.n(F),H=a(74),J=a.n(H),z=a(75),V=a.n(z);a(276);var U=function(){return l.a.createElement("div",{className:"flexManager"},l.a.createElement("div",{className:"flexChildBig"},l.a.createElement(p.a,{className:"cardContentStyles fullWidthCard"},l.a.createElement(g.a,null,"The difference in the results seen from using ES% instead of Sh% as a measure of a team\u2019s shooting performance were negligible. The correlation coefficients were very similar even when the statistics were adjusted to look at the difference between a team and their opponents shooting performance. This has to do with the proportion of total shot attempts that result in two point goals. For this project\u2019s dataset, the average number of shots taken by a team per game is 26 while the average number of two point goals per game is 0.6.  This means we would not even expect a team to score a two-point goal every game.",l.a.createElement("br",null),l.a.createElement("br",null),"Because the average amount of two point goals per game is so low, the difference between Sh% and ES% is also very small. However, I still believe that ES% is a superior statistic because in the case of a game where a larger amount of two point goals are scored than normal. ES% and ES%D would take into account the fact that those two point goals were worth 100% more than a one point goal but, Sh% and Sh%d would not account for this. This is reflected by the slightly larger correlation coefficients for the regression analyses using ES% and ES%D. Thus, indicating a slightly stronger relationship between ES%/ES%D and Win% in comparison to the relationship between Sh%/Sh%D and Win%.",l.a.createElement("br",null),l.a.createElement("br",null),"In my opinion the most valuable outcome of this project was the observation that the difference between a measure of a team's shooting performance and their opponents seems to be a significant predictor of team success. Both ES%D and AES%D had strong positive relationships with Win%. This makes sense because both statistics take into context the performance of an opponent while ES% and Sh% do not. This is a reason why ES% and Sh% only had a moderate positive relationship with Win%.",l.a.createElement("br",null),l.a.createElement("br",null),"In conclusion I believe that ES% and ultimately ES%D are valuable team statistics for professional lacrosse. ES%D is a statistic that is able to represent an entire team\u2019s performance offensively and defensively. This is because it is necessary to not only shoot efficiently as a team to maximize ES%D, but it is also necessary to play good enough defense that an opponent is not shooting efficiently. This finding can be applied to college, high school and youth lacrosse as well. These lower levels do not have a two-point goal rule, however traditional Sh% and Sh%D can be used as measures of team performance."))),l.a.createElement("div",{className:"flexImage imgWrapper"},l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:V.a,alt:"Brent Adams"}),l.a.createElement("div",null,"Brent Adams dodging against Archer's midfielder.")),l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:J.a,alt:"Andy Towers"}),l.a.createElement("div",null,"PLL coach Andy Towers talking to player.")),l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:G.a,alt:"Tehoka Nanticoke"}),l.a.createElement("div",null,"Tehoka Nanticoke taking it to the cage against Syracuse."))))};a(277);var _=function(){return l.a.createElement("div",{id:"wrapper"},l.a.createElement("h1",{className:"headerStyles"}," Project Definition "),l.a.createElement(R,null),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement("h1",{className:"headerStyles"}," Analysis "),l.a.createElement(S,null),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement("h1",{className:"headerStyles"}," Results "),l.a.createElement(A,null),l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement("h1",{className:"headerStyles"}," Conclusion "),l.a.createElement(U,null),l.a.createElement("br",null),l.a.createElement("br",null))},q=a(76),X=a.n(q),Z=a(77),$=a.n(Z),K=a(78),Q=a.n(K),Y=a(79),ee=a.n(Y),te=a(80),ae=a.n(te),ne=a(81),le=a.n(ne),re=a(82),se=a.n(re),oe=a(83),ie=a.n(oe),ce=a(84),me=a.n(ce),he=a(85),de=a.n(he);a(278);var ue=function(){return l.a.createElement("div",{className:"wrapperStyles"},l.a.createElement("div",{className:"flexManager"},l.a.createElement("div",{className:"flexChildBig"},l.a.createElement("h1",{className:"headerStyles"}," Data Collection "),l.a.createElement(p.a,{className:"cardContentStyles fullWidthCard"},l.a.createElement(g.a,null,"Unlike other professional sports, lacrosse has a relatively small following. For this reason, the data used for this project was not readily available. There are currently two professional field lacrosse leagues, the",l.a.createElement("a",{href:"https://stats.premierlacrosseleague.com/"}," PLL")," and",l.a.createElement("a",{href:"http://mll.stats.pointstreak.com/scoreboard.html"}," MLL. "),"Each league maintains statistics on their websites.",l.a.createElement("br",null),l.a.createElement("br",null),"To extract and aggregate data for both professional lacrosse leagues I used the",l.a.createElement("a",{href:"https://www.crummy.com/software/BeautifulSoup/bs4/doc/"}," Beautiful Soup "),"Python library,",l.a.createElement("a",{href:"https://selenium-python.readthedocs.io/"}," Selenium")," and general knowledge of website architecture. The scripts I wrote to scrape and analyze the data can be downloaded below. Also available and likely more useful are the datasets yielded from my scraping scripts.",l.a.createElement("br",null),l.a.createElement("br",null)," It should be noted if the regression analysis script is run using both the MLL scraper and PLL scraper then the script will run for over 2 hours because each game in the MLL dataset must be loaded in the browser.",l.a.createElement("br",null),l.a.createElement("br",null),"Scripts: ",l.a.createElement("a",{href:me.a,className:"link"},"Scraping.zip"),l.a.createElement("br",null),"Data:\xa0\xa0\xa0 ",l.a.createElement("a",{href:de.a,className:"link"},"Data.zip")))),l.a.createElement("div",{className:"imgWrapper"},l.a.createElement("img",{className:"imgInside",src:X.a,alt:"beautifulSoup"}))),l.a.createElement("br",null)," ",l.a.createElement("br",null),l.a.createElement("div",{className:"flexManager"},l.a.createElement("div",{className:"flexChildBig"},l.a.createElement("h1",{className:"headerStyles"}," PLL Data "),l.a.createElement(p.a,{className:"cardContentStyles fullWidthCard"},l.a.createElement(g.a,null,"Gathering data for the PLL was not terribly difficult. The league has only existed for one year and all stats were well tracked. Each game of the 2019 season has its own page on the site. Instead of scraping the pages directly I chose to make a GET request to the PLL's server and retrieve the JSON that they were loading game data from.",l.a.createElement("br",null),l.a.createElement("br",null),"This approach made gathering the data almost effortless but did require some work to gather the URL's for each game's JSON. This is because I needed to reload each page while I had Google Chrome's developer tools open and watch the network tab to see when the JSON was sent to the client.",l.a.createElement("br",null),l.a.createElement("br",null),"In retrospect, this approach is not very scalable and if I plan to update this project each year as new games are played then I am going to need to automate finding the URL's for each game's JSON or write a true scraper.",l.a.createElement("br",null),l.a.createElement("br",null),"Below is an example of one of the JSON's that is used to load stats for games. I noticed in multiple places on the PLL website that the JSON's sent to the client contained much more information than was displayed on the page.",l.a.createElement("br",null),l.a.createElement("br",null),"The PLL JSON is worth looking at, some of the information is interesting for individual players like shots on goal, and shooting percentage for one and two point shots.",l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement("a",{href:"https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_WHP_20190921_1.json",className:"link"},"PLL  GAME JSON")))),l.a.createElement("div",{className:"flexImage imgWrapper"},l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:Q.a,alt:"Connor Farrell"}),l.a.createElement("div",null,"Connor Farrell after a faceoff win.")),l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:se.a,alt:"Chrome dev tools netowrk tab"}),l.a.createElement("div",null,"Google Chrome's developer tool's Network tab.")))),l.a.createElement("br",null)," ",l.a.createElement("br",null),l.a.createElement("div",{className:"flexManager"},l.a.createElement("div",{className:"flexChildBig"},l.a.createElement("h1",{className:"headerStyles"}," MLL Data "),l.a.createElement(p.a,{className:"cardContentStyles fullWidthCard"},l.a.createElement(g.a,null,"When compared to the PLL data, the MLL dataset was much larger, harder to gather and the statistics were tracked poorly. While the PLL recently finished their inaugural season, the MLL has been around since 2001 and has many years\u2019 worth of data available through the league's website.",l.a.createElement("br",null),l.a.createElement("br",null),"The MLL outsources their statistics tracking to ",l.a.createElement("a",{href:"https://pointstreak.com/",className:"link"}," Pointstreak.com "),"and store their individual game data in HTML files they call gamesheets. Below is an example of a game sheet.",l.a.createElement("br",null),l.a.createElement("br",null),l.a.createElement("a",{href:"http://mll.stats.pointstreak.com/gamesheet_full.html?gameid=3209601",className:"link"},"Game Sheet Example"),l.a.createElement("br",null),l.a.createElement("br",null),"Unlike the PLL, I couldn't find any JSON being sent to the client to extract data from. This forced me to scrape the game sheets which ended up being difficult for multiple reasons. One of these reasons is that my initial scraping attempts with Beautiful Soup returned an almost empty HTML file with none of the stats I needed.",l.a.createElement("br",null),l.a.createElement("br",null),"This is because the stats for each game sheet are rendered after the browser loads the page with JavaScript. For this reason, I used Selenium to load the page, render the components that displayed the stats and then scraped the page using Beautiful Soup.",l.a.createElement("br",null),l.a.createElement("br",null),"Once I had the HTML for each gamesheet I still needed to parse through the HTML and extract the stats I needed for this project. This was harder than usual because the gamesheets were laid out in an interesting way.",l.a.createElement("br",null),l.a.createElement("br",null),'In general, when scraping HTML files, you will look for id or class attributes of HTML elements to use to locate important information. For example, there may be a table that contains all of the players on a team and the id for that table might be "playerTable". The gamesheets however had almost no elements with attributes that could be used to locate important information.',l.a.createElement("br",null),l.a.createElement("br",null),"Instead, I ended up creating a list of all the tables in the page and figuring out the indexes of where the information I needed would be in that list through trial and error. This resulted in the code for the MLL scraper taking a while to develop and not making much sense unless you understand the exact layout of the tables in the gamesheet files."))),l.a.createElement("div",{className:"flexImage imgWrapper"},l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:$.a,alt:"trevor-baptiste"}),l.a.createElement("div",null,"Trevor Baptiste clearing the ball.")),l.a.createElement("img",{className:"imgInside",src:le.a,alt:"Point Streak Logo"}),l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{className:"imgInside",src:ae.a,alt:"Html 5 class attribute example"}),l.a.createElement("div",null,"HTML5 Class attribute example in React.")))),l.a.createElement("br",null)," ",l.a.createElement("br",null),l.a.createElement("div",{className:"flexManager"},l.a.createElement("div",{className:"flexChildBig"},l.a.createElement("h1",{className:"headerStyles"}," Regression Data "),l.a.createElement(p.a,{className:"cardContentStyles fullWidthCard"},l.a.createElement(g.a,null,"The data used for the regression analyses I conducted in this project are just subsets of the data that was gathered form the MLL and PLL. Once I had collected all of the PLL and MLL game data I was able to create a nested Python Dictionary from that list of games.",l.a.createElement("br",null),l.a.createElement("br",null),"Python Dictionaries map keys to values. My outer dictionary mapped teams to seasons and my inner dictionary mapped seasons to team stats. The nested dictionary structure looked like the following:",l.a.createElement("br",null),l.a.createElement("br",null),"Teams -> Seasons -> Stats",l.a.createElement("br",null),l.a.createElement("br",null),"As mentioned before some of the data from the MLL was poorly tracked and had to be excluded. For example, if we take a look at the gamesheet file I link to in the MLL data section, we can see there are no statistics recorded for shots attempted by either team. This makes all of our statistics of interest impossible to calculate.",l.a.createElement("br",null),l.a.createElement("br",null),"I filtered these games out of the data for the regression analysis but left them in the datasets I exported to csv format. I also removed any All-Star games from the data set since these were likely not representative of a normal lacrosse game.",l.a.createElement("br",null),l.a.createElement("br",null),"Also interesting to point out, the game sheet I linked to says Baltimore had 433 ground balls in one game. This is obviously not true and I am assuming these are season totals but, this is another good example of why the data from the older gamesheets can't be trusted."))),l.a.createElement("div",{className:"flexImage imgWrapper"},l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{class:"imgInside",src:ie.a,alt:"Callum Robinson"}),l.a.createElement("div",null,"Callum Robinson defending at X.")),l.a.createElement(d.o,{domElement:!0,placement:"bottom"},l.a.createElement("img",{class:"imgInside",src:ee.a,alt:"cannons attack"}),l.a.createElement("div",null,"Finn Sullivan slides to the body on Zed Williams.")))))},pe=a(86),fe=a.n(pe),ge=a(87),be=a.n(ge),Ee=a(88),we=a.n(Ee);a(279);var ye=function(){return l.a.createElement("div",{className:"flexParent"},l.a.createElement(d.g,{className:"flexChild"},l.a.createElement(d.b,{className:"centerCards",style:{width:"22rem"}},l.a.createElement(d.d,{className:"img-fluid",src:be.a,waves:!0}),l.a.createElement(d.c,null,l.a.createElement(d.f,null,"About Me"),l.a.createElement(d.e,null,"My name is Ryan Lefebvre. I am a Computer Science major at University of New Hampshire. Other projects I have worked on can be found through my GitHub below."),l.a.createElement(d.a,{href:"https://github.com/RyanLefebvre"},"Github")))),l.a.createElement(d.g,{className:"flexChild"},l.a.createElement(d.b,{className:"centerCards",style:{width:"22rem"}},l.a.createElement(d.d,{className:"img-fluid",src:fe.a,waves:!0}),l.a.createElement(d.c,null,l.a.createElement(d.f,null,"Why Lacrosse?"),l.a.createElement(d.e,null,"My best memories from high school are all from my time playing lacrosse. This project was a fun way to revisit something I am passionate about.")))),l.a.createElement(d.g,{className:"flexChild"},l.a.createElement(d.b,{className:"centerCards",style:{width:"22rem"}},l.a.createElement(d.d,{className:"img-fluid",src:we.a,waves:!0}),l.a.createElement(d.c,null,l.a.createElement(d.f,null,"Professional"),l.a.createElement(d.e,null,"I spent Summer 2019 working as a full-stack web development intern. I plan to continue pursuing full-stack opportunities. Below is my LinkedIn."),l.a.createElement(d.a,{href:"https://www.linkedin.com/in/ryan-lefebvre/"},"LinkedIn")))))},ve=a(23),xe=a(18);var Se=Object(xe.f)((function(e){var t=e.history,a=e.children;return Object(n.useEffect)((function(){var e=t.listen((function(){window.scrollTo(0,0)}));return function(){e()}}),[t]),l.a.createElement(n.Fragment,null,a)})),Ne=(a(280),function(e){function t(){var e,a;Object(o.a)(this,t);for(var n=arguments.length,l=new Array(n),r=0;r<n;r++)l[r]=arguments[r];return(a=Object(c.a)(this,(e=Object(m.a)(t)).call.apply(e,[this].concat(l)))).state={isOpen:!1},a.toggleCollapse=function(){a.setState({isOpen:!a.state.isOpen})},a}return Object(h.a)(t,e),Object(i.a)(t,[{key:"render",value:function(){return l.a.createElement(ve.a,{basename:"/effectiveShootingPercentage"},l.a.createElement(d.k,{color:"indigo",dark:!0,expand:"md",id:"navBar"},l.a.createElement(d.l,null,l.a.createElement(d.j,{to:"/"},l.a.createElement("strong",{className:"white-text"},"Effective Shooting%"))),l.a.createElement(d.n,{onClick:this.toggleCollapse}),l.a.createElement(d.h,{id:"navbarCollapse3",isOpen:this.state.isOpen,navbar:!0},l.a.createElement(d.m,{left:!0},l.a.createElement(d.i,null,l.a.createElement(d.j,{to:"/data"},"Data")),l.a.createElement(d.i,null,l.a.createElement(d.j,{to:"/about"},"About"))))),l.a.createElement("div",{id:"pageContentStyles"},l.a.createElement(Se,null,l.a.createElement(xe.c,null,l.a.createElement(xe.a,{exact:!0,path:"/",component:_}),l.a.createElement(xe.a,{exact:!0,path:"/data",component:ue}),l.a.createElement(xe.a,{exact:!0,path:"/about",component:ye}),l.a.createElement(xe.a,{component:function(e){e.location;return l.a.createElement("div",{id:"noMatchingPath"},l.a.createElement("strong",null,l.a.createElement("h1",null," 404 error page not found ")))}})))))}}]),t}(n.Component));var Le=function(){return l.a.createElement("div",{className:"App"},l.a.createElement(Ne,null))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));a(281),a(282),a(283);s.a.render(l.a.createElement(Le,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))},66:function(e,t,a){e.exports=a.p+"static/media/mylesJones.890861fd.jpg"},67:function(e,t,a){e.exports=a.p+"static/media/buczek2bomb.71d5e2ef.gif"},68:function(e,t,a){e.exports=a.p+"static/media/ghitelman.049f1d48.gif"},71:function(e,t,a){e.exports=a.p+"static/media/2pg.90099611.jpg"},72:function(e,t,a){e.exports=a.p+"static/media/formula.ae689752.png"},73:function(e,t,a){e.exports=a.p+"static/media/tehoka.8cbcbb42.jpg"},74:function(e,t,a){e.exports=a.p+"static/media/towers.0c1ed6a0.jpg"},75:function(e,t,a){e.exports=a.p+"static/media/brentAdams.c2d8db9c.jpg"},76:function(e,t,a){e.exports=a.p+"static/media/beautifulSoup.5edd424b.png"},77:function(e,t,a){e.exports=a.p+"static/media/trevor-baptiste.1b210776.jpg"},78:function(e,t,a){e.exports=a.p+"static/media/farrell.89c52546.jpg"},79:function(e,t,a){e.exports=a.p+"static/media/cannons.003d88fd.jpg"},80:function(e,t,a){e.exports=a.p+"static/media/html5Class.6e40933a.gif"},81:function(e,t,a){e.exports=a.p+"static/media/pointStreak.904b22b4.jpg"},82:function(e,t,a){e.exports=a.p+"static/media/networkTab.b7ea2bff.gif"},83:function(e,t,a){e.exports=a.p+"static/media/callumRobinson.897c5041.jpg"},84:function(e,t,a){e.exports=a.p+"static/media/Scraping.4b86f287.zip"},85:function(e,t,a){e.exports=a.p+"static/media/Data.77e1462d.zip"},86:function(e,t,a){e.exports=a.p+"static/media/gonkLax.8dfc65b4.png"},87:function(e,t,a){e.exports=a.p+"static/media/profile.21358354.png"},88:function(e,t,a){e.exports=a.p+"static/media/webDev.ccdd7b8b.jpg"}},[[192,1,2]]]);
//# sourceMappingURL=main.14add74f.chunk.js.map