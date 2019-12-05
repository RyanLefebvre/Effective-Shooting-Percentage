import React from 'react';
import { MDBBtn, MDBCard, MDBCardBody, MDBCardImage, MDBCardTitle, MDBCardText, MDBCol } from 'mdbreact';
import gonk from '../../images/gonkLax.png'
import profile from '../../images/profile.png'
import webDev from '../../images/webDev.jpg'
import './about.css'


function AboutComp() {
  return(  <div className="flexParent">
    <MDBCol className="flexChild">
      <MDBCard className='centerCards' style={{ width: "22rem" }}>
        <MDBCardImage className="img-fluid" src={profile} waves />
        <MDBCardBody>
          <MDBCardTitle>About Me</MDBCardTitle>
          <MDBCardText>
            My name is Ryan Lefebvre. I am a Computer Science major at University of New Hampshire.
            Other projects I have worked on can be found through my github below.
          </MDBCardText>
          <MDBBtn href="#">MDBBtn</MDBBtn>
        </MDBCardBody>
      </MDBCard>
    </MDBCol>

    <MDBCol className="flexChild">
      <MDBCard className='centerCards' style={{ width: "22rem" }}>
        <MDBCardImage className="img-fluid" src={gonk} waves />
        <MDBCardBody>
          <MDBCardTitle>Why Lacrosse?</MDBCardTitle>
          <MDBCardText>
            My best memories form high school are all from my time playing Lacrosse.
            This project was a fun way to revisit something I am passionate about. 
          </MDBCardText>
          <MDBBtn href="#">MDBBtn</MDBBtn>
        </MDBCardBody>
      </MDBCard>
    </MDBCol>

    <MDBCol className="flexChild">
      <MDBCard className='centerCards' style={{ width: "22rem" }}>
        <MDBCardImage className="img-fluid" src={webDev} waves />
        <MDBCardBody>
          <MDBCardTitle>Professional</MDBCardTitle>
          <MDBCardText>
            I spent Summer 2019 working as a full-stack web development intern.
            I plan to continue pursuing full-stack oppourtunites. Below 
            is my LinkedIn.
          </MDBCardText>
          <MDBBtn href="#">MDBBtn</MDBBtn>
        </MDBCardBody>
      </MDBCard>
    </MDBCol>
  </div> );  
}


export default AboutComp;
