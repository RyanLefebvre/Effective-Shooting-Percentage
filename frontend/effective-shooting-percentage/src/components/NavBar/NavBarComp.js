import React, { Component } from "react";
import {
MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavItem, 
MDBNavLink, MDBNavbarToggler, MDBCollapse
} from "mdbreact";
import MainInfoComp from '../MainInfo/MainInfoComp';
import DataComp from '../data/data';
import AboutComp from '../about/about';
import { HashRouter as Router , Route, Switch, } from 'react-router-dom';
import './NavBar.css'

class NavBarComp extends Component {

state = {
  isOpen: false
};

toggleCollapse = () => {
  this.setState({ isOpen: !this.state.isOpen });
}

render() {
    const noMatchingPath = ({location}) =>
    (
      <div id="noMatchingPath">
          <strong><h1> 404 error page not found </h1></strong>
      </div>
    )

  return (
    <Router  basename={'/effectiveShootingPercentage'}  >
      <MDBNavbar color="indigo" dark expand="md" id="navBar">
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
              <MDBNavLink to="/about">About</MDBNavLink>
            </MDBNavItem>
          </MDBNavbarNav>
        </MDBCollapse>
      </MDBNavbar>


      <div id="pageContentStyles">
      <Switch>
        <Route exact path="/" component={MainInfoComp} />
        <Route exact path='/data' component={DataComp} />
        <Route exact path='/about' component={AboutComp} />
        <Route component={noMatchingPath}></Route>
      </Switch>
      </div>


    </Router>
    );
  }
}


export default NavBarComp;
