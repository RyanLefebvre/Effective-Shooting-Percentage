import React, { Component } from 'react'
import Chart from "chart.js";
import classes from "./LineGraph.module.css";

export default class ScatterPlot extends Component {
    chartRef = React.createRef();
    


    componentDidMount() {


        let regrData = []
        // create dat from xVals an yVals 
        this.props.xValues.forEach( (value) => {
            regrData.push({ x:value , 
                y:this.props.yValues[this.props.xValues.indexOf(value)]
            })
        });


        const myChartRef = this.chartRef.current.getContext("2d");       
        new Chart(myChartRef, {
            type: "scatter",
            data: {
                datasets: [
                    {
                        label: this.props.title,
                        data: regrData,
                    }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                      scaleLabel: {
                        display: true,
                        labelString: this.props.yLabel
                      }
                    }],
                    xAxes: [{
                        scaleLabel: {
                          display: true,
                          labelString: this.props.xLabel
                        }
                      }]
                  } 
            }
        });
    }
    render() {
        return (
                <canvas
                    id="myChart"
                    ref={this.chartRef}
                />
        )
    }
}