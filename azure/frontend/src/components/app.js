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

class App extends Component {
  render() {
    return (
      <Header />
      <Navigation />
      <Footer />
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'))
