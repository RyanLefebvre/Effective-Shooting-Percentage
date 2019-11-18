import React, { Component } from "react";
import {
MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavItem, 
MDBNavLink, MDBNavbarToggler, MDBCollapse
} from "mdbreact";
import MainInfoComp from './MainInfoComp';
import AnalysisComp from './analysis';
import DataComp from './data';
import AboutComp from './about';
import { HashRouter as Router , Route, Switch, } from 'react-router-dom';
import { red } from "@material-ui/core/colors";

class NavBarComp extends Component {

state = {
  isOpen: false
};

toggleCollapse = () => {
  this.setState({ isOpen: !this.state.isOpen });
}



render() {
    const navBarStyles = {
        marginBottom:'20px'
    }

    const noMatchingPathStyles = {
      width:'80%',
      display:'block',
      margin:'auto',
      textAlign:'center'
    }

    const noMatchingPath = ({location}) =>
    (
      <div style={noMatchingPathStyles}>
          <strong><h1> 404 error page not found <br></br><br></br> use the navbar above to find a page </h1></strong>
      </div>
    )

  return (
    <Router  basename={'/effectiveShootingPercentage'}  >
      <MDBNavbar color="indigo" dark expand="md" style={navBarStyles}>
        <MDBNavbarBrand>
        <MDBNavLink to="/"><strong className="white-text">Effective Shooting%</strong></MDBNavLink>
        </MDBNavbarBrand>
        <MDBNavbarToggler onClick={this.toggleCollapse} />
        <MDBCollapse id="navbarCollapse3" isOpen={this.state.isOpen} navbar>
          <MDBNavbarNav left>
            <MDBNavItem>
              <MDBNavLink to="/data">Data</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/analysis">Analysis</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/about">About</MDBNavLink>
            </MDBNavItem>
          </MDBNavbarNav>
        </MDBCollapse>
      </MDBNavbar>


      <Switch>
        <Route exact path="/" component={MainInfoComp} />
        <Route exact path='/analysis' component={AnalysisComp} />
        <Route exact path='/data' component={DataComp} />
        <Route exact path='/about' component={AboutComp} />
        <Route component={noMatchingPath}></Route>
      </Switch>

    </Router>
    );
  }
}


export default NavBarComp;
