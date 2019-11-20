import React from 'react';
import AnalysisComp from '../components/analysis/analysis'
import ResultsComp from '../components/results/results'
import OverviewComp from '../components/overview/overview'
function MainInfoComp() {

  const wrapperStyle = {
      margin:'0',
      padding:'0',
  }
  return (    
    <div style={wrapperStyle} >
      <h1 className ="headerStyles"> Project Definition </h1>
      <OverviewComp></OverviewComp>
      <br></br><br></br>
      <h1 className = "headerStyles"> Analysis </h1>
      <AnalysisComp></AnalysisComp>
      <br></br><br></br>
      <h1 className = "headerStyles"> Results </h1>
      <ResultsComp></ResultsComp>
    </div>
  );
}


export default MainInfoComp;
