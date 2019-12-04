import React from 'react';
import AnalysisComp from '../analysis/analysis'
import ResultsComp from '../results/results'
import OverviewComp from '../overview/overview'
import ConclusionComp from '../Conclusion/conclusion'
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
      <br></br><br></br>
      <h1 className = "headerStyles"> Conclusion </h1>
      <ConclusionComp></ConclusionComp>
      <br></br><br></br>
    </div>
  );
}


export default MainInfoComp;
