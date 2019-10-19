import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import beautifulSoup from '../images/beautifulSoup.png'
import trevor from '../images/trevor-baptiste.jpg'
import teams from '../images/teams.jpg'
import games from '../images/games.jpg'

function DataComp() {

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
    maxWidth:'1100px',
    margin:'auto'
  }

  const flexChildBigStyles = {
    display:'block',
    margin:'auto',
    maxWidth: '700px',
    minWidth:'60%'
  }

  return(    
    <div className ="wrapperStyles">
    <h1 className="headerStyles"> Data Collection </h1>

    <div style={flexManagerStyles} class ="flexManager">
    <Card style={flexChildBigStyles} className="cardContentStyles">
        <CardContent>
          Unlike other professional sports, lacrosse has a relatively small following.
          The data used for this project was not readily available because of this. 
          There are currently two professional field lacrosse leagues, the PLL and MLL.
          Each league maintains player and team statistics on their websites. I used the 
          'Beautiful Soup' Python library to extract and aggregate data for both leagues.
        </CardContent>
      </Card>
      <div style ={imgWrapper}>
        <img  style={imgStyles} src ={beautifulSoup} alt="beautifulSoup"></img>
      </div>
    </div>

    <br></br>
    
      <div style={flexManagerStyles} class ="flexManager">
        <div style={flexChildBigStyles}>
          <h1 className="headerStyles"> Player Data </h1>
            <Card  className="cardContentStyles">
              <CardContent>
                This is a long sentence that will cause a line break. if there is 
                insufficient content in the card then it is not styled correctly
              </CardContent>
            </Card>
        </div>
        <div class ="flexImage" style ={imgWrapper}>
          <img  style={imgStyles} src ={trevor} alt ="trevor-baptiste"></img>
        </div>    
      </div>

    <br></br>
    
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

   <br></br>
    
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
