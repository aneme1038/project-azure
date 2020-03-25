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
  // ============== //
  // Handle View State
  handleView = (view, postData) => {
    let pageTitle = ''
    let userInputs = {
      username: '',
      password: '',
      id: null
    }
    // decide pageTitle based on view
    switch (view) {
      case 'home':
        pageTitle = 'Home'
        break
      case 'finance':
        pageTitle = 'Finance'
        break
      case 'health':
        pageTitle = 'Health'
        break
      case 'religion':
        pageTitle = 'Religion'
        break
      case 'statistics':
        pageTitle = 'My Statistics'
        break
      case 'food':
        pageTitle = 'Diet and Nutrition'
        break
      case 'shopping':
        pageTitle = 'Shopping'
        break
      case 'education':
        pageTitle = 'Education'
        break
      case 'scheduler':
        pageTitle = 'Personal Planner'
        break
      case 'settings':
        pageTitle = 'Settings'
        break
      default:
        break
    }
    //Update state
    this.setState({
      view: {
        page: view,
        pageTitle: pageTitle
      },
      userInputs: userInputs
    })
  }
  //Handle Search
  // handleSearch(event) {
  //   console.log('This Route is Working');
  //   event.preventDefault()
  //   this.setState({
  //
  //   }, () => {
  //
  //   })
  // }
  handleChange(event) {
    this.setState({ [event.target.id]: event.target.value })
  }
  // =========== //
  // RENDER     //
  // ========== //
  render() {
    return (
      <React.Fragment >
        <Header
          handleSearch={this.handleSearch}
          handleChange={this.handleChange}
          handleView={this.handleView}
        />
        <Navigation
          handleSearch={this.handleSearch}
          handleChange={this.handleChange}
          handleView={this.handleView}
        />
        <Footer
          handleSearch={this.handleSearch}
          handleChange={this.handleChange}
          handleView={this.handleView}
        />
      </React.Fragment >
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'))
