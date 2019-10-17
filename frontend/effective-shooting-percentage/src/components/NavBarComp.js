import React, { Component } from "react";
import {
MDBNavbar, MDBNavbarBrand, MDBNavbarNav, MDBNavItem, 
MDBNavLink, MDBNavbarToggler, MDBCollapse
} from "mdbreact";
import MainInfoComp from './MainInfoComp';
import PlayerComp from './players'
import DataComp from './data'
import GamesComp from './games'
import TeamComp from './teams'
import AboutComp from './about'
import { BrowserRouter as Router , Route, Switch, } from 'react-router-dom';

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
    <Router >
      <MDBNavbar color="indigo" dark expand="md" style={navBarStyles}>
        <MDBNavbarBrand>
        <MDBNavLink to="/"><strong className="white-text">Effective Shooting%</strong></MDBNavLink>
        </MDBNavbarBrand>
        <MDBNavbarToggler onClick={this.toggleCollapse} />
        <MDBCollapse id="navbarCollapse3" isOpen={this.state.isOpen} navbar>
          <MDBNavbarNav left>
            <MDBNavItem active>
              <MDBNavLink to="/players">Players</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/teams">Teams</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/games">Games</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/data">Data</MDBNavLink>
            </MDBNavItem>
            <MDBNavItem>
              <MDBNavLink to="/about">About</MDBNavLink>
            </MDBNavItem>
          </MDBNavbarNav>
        </MDBCollapse>
      </MDBNavbar>


      <Switch>
        <Route exact path="/" component={MainInfoComp} />
        <Route exact path='/players' component={PlayerComp} />
        <Route exact path='/data' component={DataComp} />
        <Route exact path="/teams" component={TeamComp} />
        <Route exact path='/games' component={GamesComp} />
        <Route exact path='/about' component={AboutComp} />
        <Route component={noMatchingPath}></Route>
      </Switch>

    </Router>
    );
  }
}


export default NavBarComp;
