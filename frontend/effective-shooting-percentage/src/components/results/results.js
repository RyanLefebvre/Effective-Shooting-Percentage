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
    </div> 
  );  
}


export default ResultsComp;
