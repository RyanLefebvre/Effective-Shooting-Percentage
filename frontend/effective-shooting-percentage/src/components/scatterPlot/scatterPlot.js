import React, { Component } from 'react'
import Chart from "chart.js";
import { Card , CardContent } from '@material-ui/core';
import './scatterPlot.css'

export default class ScatterPlot extends Component {
    chartRef = React.createRef();
    
    componentDidMount() {
        let regrData = []
        let lineOfBestFit = []
        let pointBackgroundColors = []
        // create data from xVals an yVals 
        this.props.xValues.forEach( (value) => {
            regrData.push({ x:value , 
                y:this.props.yValues[this.props.xValues.indexOf(value)]
            })
            pointBackgroundColors.push('blue')
        });
        //will be used to find min and max data points, mx of X * Y will be most northeast point
        //min will will be most southwest point
        const regrDataMapped = regrData.map( element => element.x   )
        const min = regrData[ regrDataMapped.indexOf( Math.min( ...regrDataMapped ) ) ]
        const max = regrData[ regrDataMapped.indexOf( Math.max( ...regrDataMapped ) ) ]

    
        //plot the line of best fit ( 100 points )
        const incrementAmount =  ( max.x - min.x ) / 100 
        for( let i = min.x; i <= max.x; i = i + incrementAmount ){
             const yVal = ( i * this.props.m ) + this.props.b 
             lineOfBestFit.push( { x:i,y:yVal})
        }


        const myChartRef = this.chartRef.current.getContext("2d");    
        
        new Chart(myChartRef, {
            type: "scatter",
            data: {
                datasets: [
                    {
                        label: this.props.title,
                        data: regrData,
                        backgroundColor:'blue',
                        pointBackgroundColor: pointBackgroundColors,
                        pointRadius: 3,
                        pointHoverRadius: 6
                    },
                    {
                        label: "Best Fit",
                        data: lineOfBestFit,
                        pointBackgroundColor: '#ff19af',
                        showLine:true,
                        backgroundColor:'#ff19af',
                        fill:'none',
                        borderColor:'#ff19af',
                        pointRadius: 0
                    }
                ]
            },
            options: {
                scales: {
                    yAxes: [{
                      scaleLabel: {
                        display: true,
                        labelString: this.props.yLabel,
                    }}],
                    xAxes: [{
                        scaleLabel: {
                          display: true,
                          labelString: this.props.xLabel
                        }}]
                },
            }
        });
    }
    render() {
        return (
            <Card id="canvasWrapper">
                <CardContent>
                <canvas
                    id="myChart"
                    ref={this.chartRef}
                />
                </CardContent>
            </Card>

        )
    }
}