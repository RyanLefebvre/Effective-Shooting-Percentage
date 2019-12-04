import React from 'react';
import Card from '@material-ui/core/Card';
import {MDBTooltip} from "mdbreact";
import CardContent from '@material-ui/core/CardContent';
import './overview.css';
// images
import twoPointer from '../../images/2pg.jpg'
import formulaCode from '../../images/formula.png'

function OverviewComp() {

  return( <div >         
    <Card className ="cardContentStyles">
        <CardContent>
      Professional field lacrosse leagues have created a "two point line". If a 
      player stands behind this line when shooting, a goal is worth two 
      points instead of one. Effective Shooting Percentage (ES%) is a new 
      lacrosse statistic that accounts for the fact that a two point goal 
      is worth more than a one point goal. The forumla for ES% is shown below: 
        </CardContent>
      </Card>

      <br></br>
      <div id ="containerContainer" >
      <div id ="imageContainer">
          <img alt="ES% formula from es%.py" id="formula"    src={formulaCode}/>
          <MDBTooltip domElement={true} placement = "bottom">
              <img alt="Two point shot attempt"  id="twoPointer" src={twoPointer}/> 
              <div>
                Tom Schreiber taking a two point shot.
              </div>
          </MDBTooltip>

      </div>
      </div>
      <br></br>

      <Card className ="cardContentStyles">
        <CardContent>
        ES% is inspired by a powerful statistic in basketball called effective field goal percentage (EFG%). 
        EFG% accounts for the fact that three point shots are worth more than two point shots. 
        EFG% has been a significant predicator of a teams offensive performance. For example in 2013, 
        the Miami Heat and San Antonio Spurs had the highest EFG% in the league and ended up meeting in the NBA finals that year. 
        <br></br><br></br>
        This project aims to explore if a similar relationship to the one seen in basketball between shooting efficiency and
        team success exists in professional lacrosse. I will compare the realtionship between shooting efficiency and team success with
        the relationship between traditional shooting percentage and team success as a baseline.
        </CardContent>
      </Card>
  </div> );
}


export default OverviewComp;
