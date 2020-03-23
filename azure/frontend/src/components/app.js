//==========================================//
//---------------APP-----------------------//
//    This is the main container for all  //
//          React Components             //
//======================================//
import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Header from './Header';

class App extends Component {
  render() {
    return (
      <Header />
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'))
