import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import beautifulSoup from '../../images/beautifulSoup.png'
import trevor from '../../images/trevor-baptiste.jpg'
import farrell from '../../images/farrell.jpg'
import lizards from '../../images/lizards.jpg'
import './data.css'


function DataComp() {

  return(    
    <div className ="wrapperStyles">
    <div  className="flexManager">
      <div className="flexChildBig">
      <h1 className="headerStyles"> Data Collection </h1>
      <Card  className="cardContentStyles fullWidthCard" >
        <CardContent>
          Unlike other professional sports, lacrosse has a relatively small following.
          For this reason the data used for this project was not readily available. 
          There are currently two professional field lacrosse leagues, the 
          <a href = "https://stats.premierlacrosseleague.com/"> PLL</a> and
          <a href = "http://mll.stats.pointstreak.com/scoreboard.html"> MLL. </a> 
          Each league maintains statistics on their websites.
          <br></br><br></br>
           To extract and aggregate data for both professional lacrosse leagues I used the 
           <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"> Beautiful Soup </a>Python library,
           <a href="https://selenium-python.readthedocs.io/"> Selenium</a> and general knowledge of website architecture.
           The scripts I wrote to scrape and analyze the data can be downloaded below. It should be noted if the regression analysis
           script is run using both the MLL scraper and PLL scraper then the script will run for over 2 hours because each game in the 
           MLL dataset must be laoded in the browser.
           <br></br><br></br>
           Effective Shooting % Scripts: <a href ="https://selenium-python.readthedocs.io/" className="link">pLAceHoLdEr</a>
          <br></br><br></br>
        </CardContent>
      </Card>
      </div>
  
      <div className="imgWrapper">
        <img  className="imgInside" src ={beautifulSoup} alt="beautifulSoup"></img>
      </div>
    </div>

    <br></br> <br></br>
    
      <div className="flexManager">
        <div className="flexChildBig" >
          <h1 className="headerStyles"> PLL Data </h1>
            <Card  className="cardContentStyles fullWidthCard">
              <CardContent>
                Gathering data for the PLL was not terribly difficult. The league has only existed for one year 
                and all stats were well tracked. Each game of the 2019 season has its own page on the site.
                Instead of scraping the pages directly I chose to make a GET request to the PLL's server and retrieve
                 the JSON that they were loading game data from. 
                <br></br><br></br>
                This approach made gathering the data 
                almost effortless but did require some work to gather the URL's for each game's JSON. This is because I needed to 
                reload each page while I had Google Chrome's developer tools open and watch the network tab to see when the JSON 
                was sent to the client. In retrospect, this approach is not very scalable and if I plan to update this project each year as new 
                games are played then I am going to need to automate finding the URL's for each game's JSON or write a scraper. 
                <br></br><br></br>
                Below is an example of one of the JSON's that is used to load stats for games. I noticed in multiple places 
                on the PLL website that the JSON's sent to the client contained much more information than was displayed on the 
                page. The JSON is worth looking at, some of the information is interesting for individual players like shot's on goal,
                and shooting percentage for one and two point shots. 
                <br></br><br></br>
                <a href ="https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_WHP_20190921_1.json" className ='link'>PLL  GAME JSON</a>
              </CardContent>
            </Card>
        </div>

        <div className="flexImage imgWrapper" >
          <img  className ="imgInside"  src ={farrell} alt ="Connor Farrell"></img>
        </div>    
      </div>

    <br></br> <br></br>
    
    <div className="flexManager">
      <div className="flexChildBig">
        <h1 className="headerStyles"> MLL Data </h1>
          <Card  className="cardContentStyles fullWidthCard">
            <CardContent>
              When compared to the PLL data, the MLL dataset was much larger, harder to gather and the statistics were tracked
              poorly. While the PLL recently finished their inaugural season, the MLL has been around since 2001 and has many years worth of data 
              available through the league's website. The MLL outsources their statistics tracking to <a href ="https://pointstreak.com/" className ='link'> Pointstreak.com </a>
              and store their individual game data in html files they call gamesheets. Below is an example of a game sheet.
              <br></br><br></br>
              <a href ="http://mll.stats.pointstreak.com/gamesheet_full.html?gameid=3209601" className="link">Game Sheet Example</a>             
              <br></br><br></br>
              Unlike the PLL, I couldn't find any JSON being sent to the client to extract data from. This forced me to scrape the 
              game sheets which ended up being difficult for multiple reasons. One of these reasons is that my initial scraping 
              attempts with Beautiful Soup returned an almost empty html file with none of the stats I needed. This is because the stats 
              for each game sheet are rendered after the browser loads the page with JavaScript. For this reason I used Selenium to load the 
              page, render the components that displayed the stats and then scraped the page using Beautiful Soup.
              <br></br><br></br>
              Once I had the html for each gamesheet I still needed to parse through the html and extract the stats I needed for this project.
              This was harder than usual because the gamesheets were laid out in an interesting way. In general when scraping html files you will 
              look for id or class attributes of html elements to use to locate important information. For example there may be a table that 
              contains all of the players on a team and the id for that table might be "playerTable". The gamesheets however had almost no 
              elements with attributes that could be used to locate important information. Instead, I ended up creating a list of all the tables 
              in the page and figuring out the indexes of where the information I needed would be in that list through trial and error. This 
              resulted in the code for the MLL scraper taking a while to develop and not making much sense unless you understand the exact 
              layout of the tables in the gamesheet files.
            </CardContent>
          </Card>
      </div>
      <div className="flexImage imgWrapper">
        <img  className="imgInside" src ={trevor} alt ="trevor-baptiste"></img>
      </div> 
   
   </div>

   <br></br> <br></br>
    
    <div className="flexManager">
      <div className ="flexChildBig">
        <h1 className="headerStyles"> Regression Data </h1>
          <Card  className="cardContentStyles fullWidthCard">
            <CardContent>
              The data used for the regression analyses I conducted in this project are just subsets of the data that was 
              gathered form the MLL and PLL. Once I had collected all of the PLL and MLL data I was able to create 
              a nested Python Dictionary from that list. Python Dictionaries map keys to values. My outer dictionary 
              mapped teams to seasons and my inner dictionary mapped seasons to team stats. This dictionary was used to create the 
              teams.csv file available above. The nested dictionary structure looked like the following: 
              <br></br><br></br> 
              Teams -> Seasons -> Stats
              <br></br><br></br>
              As mentioned before some of the data from the MLL was poorly tracked and had to be excluded. For example if we take a look at the 
              gamesheet file I link to in the MLL data section, we can see there are no statistics recorded for shots attempted by either team.
              This makes all of our statistics of interest impossible to calculate. I filtered these games out of the data for the regression
              analysis but left them in the datsets I exported to csv format. I also removed any All-Star games from the data set since these
              were likely not representative of a normal lacrosse game. Also interseting to point out, the game sheet I linked to says Baltimore
              had 433 ground balls in one game. This is obviously not true and I am assuming these are season totals but, this is a another good 
              example of why the data from the older gamesheets can't be trusted.
            </CardContent>
          </Card>
      </div>
      <div className="flexImage imgWrapper">
        <img  class="imgInside" src ={lizards} alt ="lizards defender"></img>
      </div>    
   </div>
    </div>    
    );  
}


export default DataComp;
