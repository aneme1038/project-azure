//==========================================//
//---------------APP-----------------------//
//    This is the main container for all  //
//          React Components             //
//======================================//
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Header from './Header';
import Footer from './Footer';
import Navigation from './Navigation';
require('dotenv').config();

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      view: {
        page: 'home',
        pageTitle: ''
      },
    }
    //this.handleBLANK = this.handleBLANK.bind(this)
  }
  // ============== //
  // HANDLERS      //
  render() {
    return (
      <Header />
      <Navigation />
      <Footer />
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'))
