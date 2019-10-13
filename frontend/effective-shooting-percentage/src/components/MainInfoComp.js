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
        width: '80%' ,
        maxWidth: '1000px' ,
        backgroundColor:'white'
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
      width:'90%'
    };

    const twoPointerStyles ={
      display:'block',
      margin:'auto',
      maxWidth: '400px',
      width:'90%'
    };

    const containerContainerStyles = {
      maxWidth: '950px',
      display:'block',
      margin:'auto'
    };

    const headerWrapperStyles = {
      color: 'ghostwhite',
      width: '99%',
      textAlign:'center',
      display:'block',
      margin:'auto',
      backgroundColor: '#fc654e',
      borderColor:'#fc654e',
      borderWidth:'5px',
      borderStyle:'solid',
      borderBottomLeftRadius: '10px',
      borderBottomRightRadius: '10px',
      marginBottom: '10px',
      marginTop: '0'
    };


  return (    
    <div className="MainInfo" >
      
  
        <div id ="headerWrapper" style={headerWrapperStyles}>
          <h1 id = "title" > Effective Shooting Percentage  </h1>
        </div> 
 
      
      <Card style={contentStyles}>
        <CardContent>
        Unlike youth, high school and collegiate lacrosse, professional 
      field lacrosse leagues have created a " two point line ". If a 
      player stands behind this line when shooting, a goal is worth two 
      points instead of one. Effective Shooting Percentage (ES%) is a new 
      lacrosse statistic that accounts for the fact that a two point goal 
      is worth more than a one point goal. The forumla is: 
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
        ES% is inspired by a relatively new and powerful statistic in basketball called 
      effective field goal percentage ( EFG% ). EFG% accounts for the fact that three point 
      shots are worth more than two point shots. EFG% has been a significant predicator of a teams 
      offensive performance: for example in 2013, the Miami Heat and San Antonio Spurs had the highest 
      EFG% and in the league and ended up meeting in the NBA finals that year. This project aims to 
      explore if a similar relationship between scoring efficiency and team/player success exists in professional lacrosse.
        </CardContent>
      </Card>

    </div>
  );
}


export default MainInfoComp;
