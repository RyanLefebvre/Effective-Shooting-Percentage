import React from 'react';
import ScatterPlot from '../scatterPlot/scatterPlot'

function AnalysisComp() {

  const graphWrap = {
    width:'70%',
    display:'block',
    margin:'auto'
  }

  const graphStyles = {

  }

  //CHART DATA 

  const EffectiveDifferenceData = {
    title: "AES%D vs Win% ",
    xLabel: " ES%D",
    yLabel: " Win%" , 
    xValues: [ 1 , 2, 3 , 4 , 5 , 6 , 7 , 8 ,9 ],
    yValues: [ 1 , 2, 3 , 4 , 5 , 6 , 7 , 8 ,9 ],
    m: 0.494,
    b: 0.779
  }


  return(  
  
  <div style = {graphWrap}> 
      <ScatterPlot {...EffectiveDifferenceData} style={graphStyles}>
        </ScatterPlot>
  </div> );  
}


export default AnalysisComp;
