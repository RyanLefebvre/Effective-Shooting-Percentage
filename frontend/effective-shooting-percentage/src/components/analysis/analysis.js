import React from 'react';
import ScatterPlot from '../scatterPlot/scatterPlot'
import AESP_vs_WINP from '../../regression/AES%_vs_WIN%'
import AESPD_vs_WINP from '../../regression/AES%D_vs_WIN%'
import AShP_vs_WINP from '../../regression/ASh%_vs_WIN%'
import AShPD_vs_WINP from '../../regression/ASh%D_vs_WIN%'
import Card from '@material-ui/core/Card'
import CardContent from '@material-ui/core/CardContent'
import './analysis.css'


function AnalysisComp() {

  return(  
    
  <div id="graphFlex"> 

  <Card className = "cardContentStyles" >
        <CardContent>
          The dataset used for this project contains information about 872 professional lacrosse games ranging from 2001-2019. This data was scraped from the
          official MLL and PLL website, then converted into a format that would be useful for an analysis and then exported to csv format. To learn more about 
          the data for this project, visit the data page of this site. 
          <br></br><br></br>
          In order to determine whether or not a significant relationship exists between shooting efficiency and success in lacrosse,
          I will be using regression analysis. Linnear regression is used to estimate the strength of the relationship between two
          variables and is a technique that can applied to the MLL and PLL data I scraped.
          <br></br><br></br>
          Each of the following scatterplots represent the results of a regression analysis. The coordinate pairs 
          plotted in blue represent an (x,y) pairing for a team's performance over a specific season. These coordinate pairs 
          were created using the game dataset to calculate season stats for professional lacrosse teams. 
          <br></br><br></br>
          The x-coordinate of the plotted points represents a teams average performance for a statistic of interest over a given season.
          <h1>MORE HERE ABOUT y coord and Line of best fit</h1>
          The reason I used  average performance for a statistic instead of absolute performance is because it is a better representation of how that team performed game in and 
          game out. For example imagine a team's shooting performance over 3 games. Games one and two they played two average teams in the league and shot very poorly.
          In game three they played the worst team in the league and shot very well. Respectively they shot 3/12 , 2/16 and 18/27.
          <br></br><br></br> 
          This results in an absolute shooting percentage of ((3 + 2 + 18) / (12 + 16 + 27)) =  23/55 = 41.8%. However, This teams average shooting percentage 
          is ((3/12  + 2/16 + 18/27 ) / 3) = 34.7%. While the difference between absolute and average shooting percentage for this example may appear small at only 7%,
          the relative decrease from absolute to average is 17% which is a more significant difference. This has to do with why the average shooting percentage is a more
          accurate value. This is because taking the average of each game is able to reduce how the outlier game against the worst team in the league impacts the statistic of
          interest. 
        </CardContent>
      </Card>

    <div  className ="plotParent">
      <div  className="plotWrapper">
      <ScatterPlot  {...AShP_vs_WINP} >
        </ScatterPlot>
      </div>
      <div  className="plotWrapper">
      <ScatterPlot {...AESP_vs_WINP} >
        </ScatterPlot>
      </div>
    </div>

    <Card className = "cardContentStyles" >
        <CardContent>
      Results of initial linnear regression
        </CardContent>
      </Card>


    <div  className ="plotParent">
    <div  className="plotWrapper">
      <ScatterPlot {...AShPD_vs_WINP}>
        </ScatterPlot>
      </div>
      <div  className="plotWrapper">
      <ScatterPlot {...AESPD_vs_WINP}>
        </ScatterPlot>
      </div>
    </div>

    <Card className = "cardContentStyles" >
        <CardContent>
      Results of second linnear regression
        </CardContent>
      </Card>

  </div> );  
}

export default AnalysisComp;
