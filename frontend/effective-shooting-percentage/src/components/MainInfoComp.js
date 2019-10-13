import React from 'react';
import ReactDOM from 'react-dom';
import { blockStatement } from '@babel/types';
import { brotliDecompress } from 'zlib';
// images
import twoPointer from '../images/2pg.jpg'
import formulaCode from '../images/formula.PNG'

function MainInfoComp() {


    const titleStyles = {
        color: '#e64e37' ,
        display: 'block' ,
        margin: 'auto' ,
        textAlign: 'center' ,
        maxWidth: '1000px',
        width: '80%'
    };

    const contentStyles = {
        marginTop: '25px' ,
        display: 'block' , 
        margin: 'auto' ,
        width: '80%' ,
        maxWidth: '1000px'
    };

    const formulaDisplayStyles = {
        display:'flex' ,
        flexDirection: 'col'
    }

    const formulaStyles = {
      display:'block',
      margin:'auto' ,
      maxWidth:'80%'
    }


  return (

    //LOOK INTO USING A UI LIBRARY TO MAKE THIS PART OF 
    // PAGE LOOK BETTER THAN IT DOES 
    
    <div className="MainInfo" >
      <h1 id = "title" style= {titleStyles}> Effective Shooting Percentage (ES%) </h1>
      <div id = "content" style ={contentStyles} >
      Unlike youth, high school and collegiate lacrosse, professional 
      field lacrosse leagues have created a " two point line ". If a 
      player stands behind this line when shooting, a goal is worth two 
      points instead of one. Effective Shooting Percentage (ES%) is a new 
      lacrosse statistic that accounts for the fact that a two point goal 
      is worth more than a one point goal.The forumla is: 
      <br></br><br></br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
     
          <img style={formulaStyles} src={formulaCode}/>

      <br></br><br></br>
      ES% is inspired by a relatively new and powerful statistic in basketball called 
      effective field goal percentage ( EFG% ). EFG% accounts for the fact that three point 
      shots are worth more than two point shots. EFG% has been a significant predicator of a teams 
      offensive performance: for example in 2013, the Miami Heat and San Antonio Spurs had the highest 
      EFG% and in the league and ended up meeting in the NBA finals that year. This project aims to 
      explore if a similar relationship between scoring efficiency and team/player success exists in professional lacrosse.
      </div>
    </div>
  );
}


export default MainInfoComp;
