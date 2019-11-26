import React from 'react';
import AnalysisComp from '../analysis/analysis'
import ResultsComp from '../results/results'
import OverviewComp from '../overview/overview'
import './MainInfo.css'

function MainInfoComp() {

  return (    
    <div id="wrapper">
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
