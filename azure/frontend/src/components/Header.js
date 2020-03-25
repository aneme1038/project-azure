//==========================================//
//---------------HEADER--------------------//
//The Header will only contain the title, //
//clock/time/date, and a few other things //
//=======================================//
import React, { Component } from 'react'
import Login from './header-layout/Login';
export class Header extends Component {
  render() {
    return (
      <header>
        {/* ======================== APP TITLE ======================== */}
        <h1 onClick={() => { {this.props.handleView('home')} }}>Azure</h1>
        {/* ======================= LOGO ========================= */}
        {/* ======================= USER LOGIN =================== */}
        <div>
        {/* We want to be able to set a conditional possibly that will determine if the user has logged in already or needs to login, so kind of like checking for User Session here. Something like below? --Aaron/Isaiha */}
          {(this.props.session)} ? <Login session={this.props.session} handleView={this.props.handleView} />
        </div>
      </header>
    )
  }
}

export default Header
