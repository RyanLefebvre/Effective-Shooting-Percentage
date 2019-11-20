import React from 'react';
import ScatterPlot from '../scatterPlot/scatterPlot'

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

  const plotStyles = {
  }

  const plotParentStyles = {
    display:'flex',
    flexWrap: 'wrap',   
    margin:'auto',
    width:'95%'
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
  
  <div style = {graphFlexStyles}> 
    <div  style ={plotParentStyles}>
      <div  style={plotWrapperStyles}>
      <ScatterPlot style={plotStyles} {...EffectiveDifferenceData} >
        </ScatterPlot>
      </div>
      <div  style={plotWrapperStyles}>
      <ScatterPlot {...EffectiveDifferenceData} >
        </ScatterPlot>
      </div>
    </div>
    <div  style ={plotParentStyles}>
    <div  style={plotWrapperStyles}>
      <ScatterPlot {...EffectiveDifferenceData}>
        </ScatterPlot>
      </div>
      <div  style={plotWrapperStyles}>
      <ScatterPlot {...EffectiveDifferenceData}>
        </ScatterPlot>
      </div>
    </div>

  </div> );  
}


export default AnalysisComp;
