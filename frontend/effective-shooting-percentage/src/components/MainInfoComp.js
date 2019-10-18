import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
// images
import twoPointer from '../images/2pg.jpg'
import formulaCode from '../images/formula.PNG'


function MainInfoComp() {

    const contentStyles = {
        marginTop: '25px' ,
        display: 'block' , 
        margin: 'auto' ,
        width: '95%' ,
        maxWidth: '1000px' ,
        backgroundColor:'white' ,
    };

    const imageContainerStyles = {
      display:'flex',
      jusitfyContent:'spaceBetween',
      flexWrap: 'wrap'
    };

    const formulaStyles = {
      display:'block',
      margin:'auto',
      maxWidth: '500px',
      marginBottom: '25px',
      width:'90%',
      borderRadius:'5px'
    };

    const twoPointerStyles ={
      display:'block',
      margin:'auto',
      maxWidth: '400px',
      width:'90%',
      borderRadius:'5px'
    };

    const containerContainerStyles = {
      maxWidth: '950px',
      display:'block',
      margin:'auto'
    };

    const headerStyles = {
      textAlign:'center'
    }

    const wrapperStyles = {
      marginBottom: '25px'
    }

  return (    
    <div className="MainInfo" style={wrapperStyles} >

      <h1 style = {headerStyles}> Project Definition </h1>
      
      <Card style={contentStyles}>
        <CardContent>
      Professional field lacrosse leagues have created a "two point line". If a 
      player stands behind this line when shooting, a goal is worth two 
      points instead of one. Effective Shooting Percentage (ES%) is a new 
      lacrosse statistic that accounts for the fact that a two point goal 
      is worth more than a one point goal. The forumla for ES% is shown below: 
        </CardContent>
      </Card>


      <br></br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <div id ="containerContainer" style ={containerContainerStyles}>
      <div id ="imageContainer" style ={imageContainerStyles}>
          <img alt="ES% formula from es%.py" style={formulaStyles} src={formulaCode}/>
          <img alt="Two point shot attempt" style={twoPointerStyles} src={twoPointer}/> 
      </div>
      </div>
      <br></br><br></br>

      <Card style={contentStyles}>
        <CardContent>
        ES% is inspired by a powerful statistic in basketball called effective field goal percentage (EFG%). 
        EFG% accounts for the fact that three point shots are worth more than two point shots. 
        EFG% has been a significant predicator of a teams offensive performance: for example in 2013, 
        the Miami Heat and San Antonio Spurs had the highest EFG% and in the league and ended up meeting in the NBA finals that year. 
        This project aims to explore if a similar relationship between scoring efficiency and team/player success exists in professional lacrosse.
        </CardContent>
      </Card>

      <br></br>
      <h1 style = {headerStyles}> Results </h1>

    </div>
  );
}


export default MainInfoComp;
