import React, { Component } from 'react'
import Chart from "chart.js";
import { Card , CardContent } from '@material-ui/core';

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
        const regrDataMapped_xTimesy = regrData.map( element => element.x * element.y  )
        const min = regrData[ regrDataMapped_xTimesy.indexOf( Math.min( ...regrDataMapped_xTimesy ) ) ]
        pointBackgroundColors[regrData.indexOf(min)] = 'red'
        const max = regrData[ regrDataMapped_xTimesy.indexOf( Math.max( ...regrDataMapped_xTimesy ) ) ]
        pointBackgroundColors[regrData.indexOf(max)] = 'green'

        const suggestedMinX = Math.floor(  min.x - ( min.x * .10 ) )
        const suggestedMaxX = Math.ceil(  max.x + ( max.x * .10 ) )
        const suggestedMinY = Math.floor(  min.y - ( min.y * .10 ) )
        const suggestedMaxY= Math.floor(  min.y - ( min.y * .10 ) )

        //plot the line of best fit ( 100 points )
        const incrementAmount = Math.ceil( ( suggestedMaxX - suggestedMinX ) / 100 )
        for( let i = suggestedMinX; i <= suggestedMaxX; i = i + incrementAmount ){
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
                    },
                    ticks:{
                        suggestedMin: suggestedMinY,
                        suggestedMax: suggestedMaxY
                      }
                    }],
                    xAxes: [{
                        scaleLabel: {
                          display: true,
                          labelString: this.props.xLabel
                        }
                        ,
                    ticks:{
                        suggestedMin: suggestedMinX,
                        suggestedMax: suggestedMaxX
                      }
                      }]
                  } ,
            }
        });
    }
    render() {
        return (
            <Card>
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