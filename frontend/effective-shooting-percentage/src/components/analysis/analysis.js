import React from 'react';
import ScatterPlot from '../scatterPlot/scatterPlot'
import AESP_vs_WINP from '../../regression/AES%_vs_WIN%'
import AESPD_vs_WINP from '../../regression/AES%D_vs_WIN%'
import AShP_vs_WINP from '../../regression/ASh%_vs_WIN%'
import AShPD_vs_WINP from '../../regression/ASh%D_vs_WIN%'
function AnalysisComp() {

  const graphFlexStyles = {
    display:'block',
    margin:'auto'
  }

  const plotWrapperStyles = {
    display:'block',
    margin: 'auto',
    marginBottom:'10px',
    minWidth:'320px',
    width:'45%'
  }

  const plotParentStyles = {
    display:'flex',
    flexWrap: 'wrap',   
    margin:'auto',
    width:'95%'
  }

  return(  
  
  <div style = {graphFlexStyles}> 
    <div  style ={plotParentStyles}>
      <div  style={plotWrapperStyles}>
      <ScatterPlot  {...AShP_vs_WINP} >
        </ScatterPlot>
      </div>
      <div  style={plotWrapperStyles}>
      <ScatterPlot {...AESP_vs_WINP} >
        </ScatterPlot>
      </div>
    </div>
    <div  style ={plotParentStyles}>
    <div  style={plotWrapperStyles}>
      <ScatterPlot {...AShPD_vs_WINP}>
        </ScatterPlot>
      </div>
      <div  style={plotWrapperStyles}>
      <ScatterPlot {...AESPD_vs_WINP}>
        </ScatterPlot>
      </div>
    </div>

  </div> );  
}

//helper method that parses csv files containing regr data 
// returns an instance of the regr data class that the scatterplot 
//component is expecting 
function readRegrFile( filePath ){
  //console.log( filePath )
}


export default AnalysisComp;
