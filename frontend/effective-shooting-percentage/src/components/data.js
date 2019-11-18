import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import beautifulSoup from '../images/beautifulSoup.png'
import trevor from '../images/trevor-baptiste.jpg'
import farrell from'../images/farrell.jpg'
import teams from '../images/teams.jpg'
import games from '../images/games.jpg'
import playerData from '../sourceCode/players.csv'
import teamData from '../sourceCode/teams.csv'


function DataComp() {

  const linkStyle = {
    textDecoration: 'underline'
  }

  const imgWrapper = {
    display:'block',
    margin:'auto',
    width:'35%'
  }

  const imgStyles = {
      display:'block',
      margin:'auto',
      maxWidth: '450px',
      marginBottom: '25px',
      marginTop:'25px',
      width:'90%',
      borderRadius:'5px'
  }

  const flexManagerStyles = {
    display:'flex',
    jusitfyContent:'center',
    flexWrap: 'wrap',
    maxWidth:'1300px',
    margin:'auto',
  }

  const flexChildBigStyles = {
    display:'block',
    margin:'auto',
    maxWidth: '800px',
    minWidth: '320px',
    width:'65%'
  }

  const cardStyles = {
    width: '100%'
  }

  return(    
    <div className ="wrapperStyles">
    <div style={flexManagerStyles} class ="flexManager">
      <div style={flexChildBigStyles}>
      <h1 className="headerStyles"> Data Collection </h1>
      <Card  className="cardContentStyles" style ={cardStyles}>
        <CardContent>
          Unlike other professional sports, lacrosse has a relatively small following.
          For this reason the data used for this project was not readily available . 
          There are currently two professional field lacrosse leagues, the 
          <a href = "https://stats.premierlacrosseleague.com/"> PLL</a> and
          <a href = "http://mll.stats.pointstreak.com/scoreboard.html"> MLL. </a> 
          Each league maintains statistics on their websites.
          <br></br><br></br>
           To extract and aggregate data for both professional lacrosse leagues I used the 
           <a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/"> Beautiful Soup </a>Python library,
           <a href="https://selenium-python.readthedocs.io/"> Selenium</a> and general knowledge of website architecture.
           The scripts I wrote to scrape and analyze the data can be downloaded below. It should be noted if the regression analysis
           script is run using both the MLL scraper then the script will run for over 2 hours because of the way I had to scrape the MLL data.
           <br></br><br></br>
           Effective Shooting % Scripts: <a href ="" style={linkStyle}>pLAceHoLdEr</a>
          <br></br><br></br>
        </CardContent>
      </Card>
      </div>
  
      <div style ={imgWrapper}>
        <img  style={imgStyles} src ={beautifulSoup} alt="beautifulSoup"></img>
      </div>
    </div>

    <br></br> <br></br>
    
      <div style={flexManagerStyles} class ="flexManager">
        <div style={flexChildBigStyles} >
          <h1 className="headerStyles"> PLL Data </h1>
            <Card  className="cardContentStyles" style ={cardStyles}>
              <CardContent>
                Gathering data for the PLL was not terribly difficult. The league has only existed for one year 
                and all stats were well tracked. Each game of the 2019 season has its own page on the site and can easily be scraped.
                Instead of scraping the pages directly I chose to make a GET request to the PLL's 
                backend and retrieve the JSON that they were loading game data from. 
                <br></br><br></br>
                This approach made gathering the data 
                almost effortless but did require some work to gather the URL's for each game. This is because I needed to 
                reload each page while I had Google Chrome's developer tools open and watch the network tab to see when the JSON 
                was sent. In retrospect, this approach is not very scalable and if I plan to update this project each year as new 
                games are played then I am going to need to automate finding the URL's for each games JSON or write a scraper. 
                <br></br><br></br>
                Below is an example of one of the JSON's that is used to load stats for games. I noticed in multiple places 
                on the PLL website that the JSON's sent to the client contained much more information than was displayed on the 
                page. The JSON is worth looking at, some of the information is interesting for individual players like shot's on goal,
                and shooting percentage for one and two point shots. 
                <br></br><br></br>
                <a href ="https://dn0a11v09sa0t.cloudfront.net/BoxScores/PLL_RED_WHP_20190921_1.json" style={linkStyle}>PLL  GAME JSON</a>
              </CardContent>
            </Card>
        </div>

        <div class ="flexImage" style ={imgWrapper}>
          <img  style={imgStyles} src ={farrell} alt ="Connor Farrell"></img>
        </div>    
      </div>

    <br></br> <br></br>
    
    <div style={flexManagerStyles} class ="flexManager">
      <div style={flexChildBigStyles}>
        <h1 className="headerStyles"> MLL Data </h1>
          <Card  className="cardContentStyles" style ={cardStyles}>
            <CardContent>
              This is a really long placeholder sentence about how I scraped the MLL data for this project so 
              that this will be styled correctly 
              <br></br><br></br>
            </CardContent>
          </Card>
      </div>
      <div class ="flexImage" style ={imgWrapper}>
        <img  style={imgStyles} src ={trevor} alt ="trevor-baptiste"></img>
      </div> 
   
   </div>

   <br></br> <br></br>
    
    <div style={flexManagerStyles} class ="flexManager">
      <div style={flexChildBigStyles}>
        <h1 className="headerStyles"> Regression Data </h1>
          <Card  className="cardContentStyles" style ={cardStyles}>
            <CardContent>
              This is a long sentence that will cause a line break. if there is 
              insufficient content in the card then it is not styled correctly
            </CardContent>
          </Card>
      </div>
      <div class ="flexImage" style ={imgWrapper}>
        <img  style={imgStyles} src ={games} alt ="trevor-baptiste"></img>
      </div>    
   </div>
    </div>    
    );  
}


export default DataComp;
