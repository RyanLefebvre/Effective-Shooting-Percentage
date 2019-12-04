import React from 'react';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import {MDBTooltip} from "mdbreact";
import tehoka from '../../images/tehoka.jpg'
import towers from '../../images/towers.jpg'
import brent from '../../images/brentAdams.jpg'
import './conclusion.css'

function ConclusionComp() {
  return(  
    <div className="flexManager">
    <div className="flexChildBig" >
        <Card  className="cardContentStyles fullWidthCard">
          <CardContent>
            The difference in the results seen from using ES% instead of Sh% as a measure of a teams shooting performance were negligible. The 
            correlation coefficients were very similar even when the statistics were adjusted to look at the difference between
            a team and their opponents shooting performance. This has to do with the proportion of total shot attempts that reuslt
            in two point goals. For this porject's dataset, the average number of shots taken by a team per game is 26 while the 
            average number of two point goals per game is 0.6.  This means we would not even expect a team to score a two point goal 
            every game.
            <br></br><br></br>
            Because the average amount of two point goals per game is so low, the difference between Sh% and ES% is also very small.
            However I still believe that ES% is a superior statistic because in the case of a game where a larger amount of two point 
            goals are scored than normal. ES% and ES%D would take into account the fact that those two point goals were worth 100% more than a one 
            point goal but, Sh% and Sh%d would not account for this. This is reflected by the slightly larger correlation coefficients for the 
            regression analyses using ES% and ES%D, indicating a slightly stronger relationship between ES%/ES%D and Win% in comparison to the 
            relationship between Sh%/Sh%D and Win%.  
            <br></br><br></br>
            In my opinion the most valuable outcome of this project was the observation that the difference between a measure of a 
            team's shooting performance and their opponents seems to be a significant predictor of team success. Both ES%D and AES%D
            had strong positive relationships with Win%. This makes sense because both statistics take into context the performance of an opponent 
            while ES% and Sh% do not. This is a reason why ES% and Sh% only had a moderate positive relationship with Win%. 
            <br></br><br></br>
            In conclusion I believe that ES% and ultimately ES%D are valuable team statistics for professional lacrosse. ES%D is a statistic 
            that is able to represent an entire teams performance offensively and defensively. This is because it is necessary to not only shoot
            efficiently as a team to maximize ES%D, but it is also necessary to play good enough defense that an opponent is not shooting efficiently.
            This finding can be applied to college, high school and youth lacrosse as well. These lower levels do not have a two point goal rule,
            however traditional Sh% and Sh%D can be used as measures of team performance. 
          </CardContent>
        </Card>
    </div>

    <div className="flexImage imgWrapper" >
    <MDBTooltip domElement={true} placement = "bottom">
    <img  className ="imgInside"  src ={brent} alt ="Brent Adams"></img>
          <div>
            Brent Adams dodging against Archer's midfielder.
          </div>
      </MDBTooltip>
      <MDBTooltip domElement={true} placement = "bottom">
      <img className="imgInside" src ={towers} alt ="Andy Towers"></img>
          <div>
            PLL coach Andy Towers talking to player.
          </div>
      </MDBTooltip>
      <MDBTooltip domElement={true} placement = "bottom">
      <img className="imgInside" src ={tehoka} alt ="Tehoka Nanticoke"></img>
          <div>
            Tehoka Nanticoke taking it to the cage against Syracuse.
          </div>
      </MDBTooltip>
    </div>    
  </div>
    );  
}

export default ConclusionComp;
