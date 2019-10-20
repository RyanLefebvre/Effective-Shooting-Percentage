import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import beautifulSoup from '../images/beautifulSoup.png'
import trevor from '../images/trevor-baptiste.jpg'
import teams from '../images/teams.jpg'
import games from '../images/games.jpg'
import playerData from '../sourceCode/players.csv'

function DataComp() {

  const linkStyle = {
    textDecoration: 'underline'
  }

  const imgWrapper = {
    display:'block',
    margin:'auto'
  }

  const imgStyles = {
      display:'block',
      margin:'auto',
      maxWidth: '350px',
      marginBottom: '25px',
      marginTop:'25px',
      width:'90%',
      borderRadius:'5px'
  }

  const flexManagerStyles = {
    display:'flex',
    jusitfyContent:'center',
    flexWrap: 'wrap',
    maxWidth:'1200px',
    margin:'auto'
  }

  const flexChildBigStyles = {
    display:'block',
    margin:'auto',
    maxWidth: '700px',
    minWidth: '320px',
    width:'65%'
  }

  return(    
    <div className ="wrapperStyles">
    <h1 className="headerStyles"> Data Collection </h1>

    <div style={flexManagerStyles} class ="flexManager">
      <div style={flexChildBigStyles}>
      <Card  className="cardContentStyles">
        <CardContent>
          Unlike other professional sports, lacrosse has a relatively small following.
          The data used for this project was not readily available because of this. 
          There are currently two professional field lacrosse leagues, the PLL and MLL.
          Each league maintains player and team statistics on their websites. 
          <br></br><br></br>
          Unfortunately there is no publicly available data for previous seasons statistics, 
          all data is from the 2019 PLL and MLL seasons.I used the 'Beautiful Soup' Python library
           and general knowledge of website architecture to extract and aggregate data for both leagues.
        </CardContent>
      </Card>
      </div>
  
      <div style ={imgWrapper}>
        <img  style={imgStyles} src ={beautifulSoup} alt="beautifulSoup"></img>
      </div>
    </div>

    <br></br> <br></br>
    
      <div style={flexManagerStyles} class ="flexManager">
        <div style={flexChildBigStyles}>
          <h1 className="headerStyles"> Player Data </h1>
            <Card  className="cardContentStyles">
              <CardContent>
                Between the PLL and MLL there were 388 professional lacrosse players in 2019. 
                The dataset I compiled as a result of scraping both leagues sites for info only contains
                statistics relevant to calculating ES%. More statistics are available with the raw data.
                <br></br><br></br>
                PLL player data was easy to compile by parsing through the JSON returned from making a GET 
                request to the following URL:  
                <a href ="https://dn0a11v09sa0t.cloudfront.net/SeasonTeamAndPlayersStats.json" style={linkStyle}>PLL JSON</a>
                <br></br><br></br>
                Data for the MLL was more difficult to gather. Their website was not set up to easily scrape player statistics.
                However, by watching the network tab in google chrome's developer tools I was able to identify they were loading a component on 
                their statistics page from another site (<a style={linkStyle} href="https://iframe.faststats.online/">FastStats</a>). FastStats, appears to be the MLL's database 
                for player and team statistics and I was able to scrape player statistics from this site.

                <br></br><br></br>
                2019 PLL/MLL player Dataset: <a href ={playerData} style={linkStyle}>players.csv</a>
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
        <h1 className="headerStyles"> Team Data </h1>
          <Card  className="cardContentStyles">
            <CardContent>
              This is a long sentence that will cause a line break. if there is 
              insufficient content in the card then it is not styled correctly
            </CardContent>
          </Card>
      </div>
      <div class ="flexImage" style ={imgWrapper}>
        <img  style={imgStyles} src ={teams} alt ="trevor-baptiste"></img>
      </div>    
   </div>

   <br></br> <br></br>
    
    <div style={flexManagerStyles} class ="flexManager">
      <div style={flexChildBigStyles}>
        <h1 className="headerStyles"> Game Data </h1>
          <Card  className="cardContentStyles">
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
