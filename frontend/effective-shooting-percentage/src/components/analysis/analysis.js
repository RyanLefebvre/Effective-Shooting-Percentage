import React from 'react';
import Card from '@material-ui/core/Card'
import CardContent from '@material-ui/core/CardContent'
import myles from '../../images/mylesJones.jpg'
import buczek from '../../images/buczek2bomb.gif'
import ghitelman from '../../images/ghitelman.gif'
import {MDBTooltip} from "mdbreact";
import './analysis.css'


function AnalysisComp() {

  return(  
    
  <div id="graphFlex"> 

  <div className="flexManager">
    <div className="flexImage imgWrapper" >
    <MDBTooltip domElement={true} placement = "bottom">
        <img  className ="imgInside"  src ={buczek} alt ="Connor Buczek"></img>
              <div>
                Connor Buczek rips two point goal.
              </div>
          </MDBTooltip>

        </div> 
    <div className="flexChildBig" >
      <Card className = "cardContentStyles" >
        <CardContent>
          The dataset used for this project contains information about 872 professional lacrosse games ranging from 2001-2019. This data was scraped from the
          official MLL and PLL website using python scripts, then converted into a format that would be useful for an analysis. To learn more about the data for this project, visit
          the < a className="link" href="https://ryanlefebvre.github.io/Effective-Shooting-Percentage/#/effectiveShootingPercentage/data">data page</a> of this site. 
          <br></br><br></br>
          In order to determine whether or not a significant relationship exists between shooting efficiency and success in lacrosse,
          I used regression analysis. Linnear regression is used to estimate the strength of the relationship between two
          variables and is a technique that can be applied to the MLL and PLL data I scraped.
          <br></br><br></br>
          Each of the following scatterplots represent the results of a regression analysis. The coordinate pairs 
          plotted in blue represent an (x,y) pairing for a team's performance over a specific season. These coordinate pairs 
          were created by calculating season stats for professional lacrosse teams using the previously mentioned game dataset. 
        </CardContent>
      </Card>
    </div>   
  </div>

  <div class='fivePixMarg'></div>

  <div className="flexManager" id="flexReverse">
    <div className="flexChildBig" >
      <Card className = "cardContentStyles" >
        <CardContent>
          The x-coordinate of the plotted points represents a team’s average performance for a statistic of interest over a given season.
          The y-coordinate of the point represents that teams winning percentage for the same season. The line of best fit plotted in pink
          represents the predicted winning percentage for a team whose performance in the statistic of interest is equal to the x-coordinate of
          the point that falls on that line. In other words, for each (x, y) coordinate pair that falls on the line of best fit, we would expect 
          a winning percentage of y based upon the team’s performance of x.
          <br></br><br></br>
          The reason I used average performance for a statistic of interest instead of absolute performance is because it is a better representation of how
          a team performed game in and game out over a given season. For example, imagine a team's shooting performance over 3 games. Games one and
          two they played slightly below average teams in the league and shot very poorly. In game three they played the worst team in the league. 
          This team’s goalie couldn't stop a beach ball and our imaginary team shot very well. Respectively over the 3 games they shot 3/12, 2/16 and
          18/27. Their inability to shoot well against slightly below average teams would indicate they are a team that in general shoots poorly,
          but how well is this reflected by our statistic of interest after the outlier game against the worst team in the league?
          <br></br><br></br> 
          This team’s performances result in an absolute shooting percentage of ((3 + 2 + 18) / (12 + 16 + 27)) = 23/55 = 41.8%. However, this teams average shooting percentage 
          is ((3/12 + 2/16 + 18/27) / 3) = 34.7%. While the difference between absolute and average shooting percentage for this example may appear small at only 7%,
          the relative decrease from absolute to average is 17% which is a more significant difference. This has to do with why the average shooting percentage is a more
          accurate representation of how we would expect a given team to shoot. This is because taking the average of each game is able to reduce how the outlier game 
          against the worst team in the league impacts the statistic of interest.
        </CardContent>
      </Card>
    </div>   
    <div className="flexImage imgWrapper" >
    <MDBTooltip domElement={true} placement = "bottom">
        <img  className ="imgInside"  src ={myles} alt ="Myles Jones"></img>
              <div>
                Myles Jones dodging against Lizards.
              </div>
          </MDBTooltip>
        <MDBTooltip domElement={true} placement = "bottom">
        <img  className ="imgInside"  src ={ghitelman} alt ="Adam Ghitelman"></img>
              <div>
                Adam Ghitelman lets in full field goal.
              </div>
          </MDBTooltip>
        </div> 
  </div>
  </div> );  
}

export default AnalysisComp;
