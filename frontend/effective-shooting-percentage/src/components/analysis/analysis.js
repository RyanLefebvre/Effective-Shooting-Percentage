import React from 'react';
import ScatterPlot from '../scatterPlot/scatterPlot'
import AESP_vs_WINP from '../../regression/AES%_vs_WIN%'
import AESPD_vs_WINP from '../../regression/AES%D_vs_WIN%'
import AShP_vs_WINP from '../../regression/ASh%_vs_WIN%'
import AShPD_vs_WINP from '../../regression/ASh%D_vs_WIN%'
import './analysis.css'


function AnalysisComp() {

  return(  
    
  <div id="graphFlex"> 
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

  </div> );  
}

export default AnalysisComp;
