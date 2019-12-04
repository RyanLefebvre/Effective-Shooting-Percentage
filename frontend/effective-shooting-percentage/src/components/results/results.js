import React from 'react';
import ScatterPlot from '../scatterPlot/scatterPlot'
import AESP_vs_WINP from '../../regression/AES%_vs_WIN%'
import AESPD_vs_WINP from '../../regression/AES%D_vs_WIN%'
import AShP_vs_WINP from '../../regression/ASh%_vs_WIN%'
import AShPD_vs_WINP from '../../regression/ASh%D_vs_WIN%'
import Card from '@material-ui/core/Card'
import CardContent from '@material-ui/core/CardContent'
import './results.css'

function ResultsComp() {
  return( 
    <div id ="parent">
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
        When performing a regression analysis, a 'correlation coefficient' is used to determine the strength of a linnear relationship. Values of a correlation 
        coefficeint can range from -1.00 to 1.00, values closer to -1.00 or 1.00 indicate a strong relationship while values closer to 0.00 indicate no relationship.
        The following guidlines will be used to interpret the correlation coefficeints yielded by the regression analyses conducted for this project
        (<a href="http://www.dmstat1.com/res/TheCorrelationCoefficientDefined.html">Interpetaion guidlines</a>).
        <br></br><br></br>
        The first scatter plot showcases the relationship between a team's average shooting percentage (ASh%) and a team's winning percentage (Win%). The correlation
        coefficeint yielded by this regression analysis is 0.404 indicating a positive moderate relationship between ASh% and Win%. The second scatter plot explores the 
        relationship between average effective shooting percentage (AES%) and Win%. This analysis yielded similar results as the first with a correlation coefficeint of 
        0.433 which also indicates a positive moderate relationship between AES% and Win%.
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
        After conducting the first two regression analyses I wondered if there was a more meaningful way to analyze a teams shooting efficiency. I came up with the 
        idea of looking at the difference between a teams shooting efficiency compared to their opponents. I called this statistic, average effective shooting percentage 
        difference (AES%D). The same concept could be applied to traditional shooting percentage to create a statistic called average shooting percentage difference (ASh%D).
        I hypothesized that if I conducted regression analyses exploring the relationship between these statistics and Win% that there would be a stronger relationship then 
        the relationships found in the inital analyses. 
        <br></br><br></br>
        My hypothesis was correct. The regression analyses conducted using the difference of a teams shooting performance and their opponents shooting performance had 
        a larger correlation coefficeint than the inital analyses. The regression analyses using ASh%D yielded a correlation coefficient of 0.76 and the analyses using
        AES%D yielded a correlation coefficeint of 0.781. Both of these correlation coefficients indicate a strong positive relationship between their respective 
        measures of shooting performance and Win%. 
      </CardContent>
    </Card>
    </div> 
  );  
}


export default ResultsComp;
