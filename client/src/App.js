/* eslint-disable no-restricted-globals */
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

const request = require('request-promise-native');

class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      demo: '',
    }
  }

  componentDidMount() {
    // request function that takes requestData as arg and makes the request
    const requestData = {
      apiEndPoint:'demo',
    }
    this.onRequest(requestData).then((data)=> {
       this.setState({
         demo: data,
       })
    })
  }
  // request function that takes requestData as arg and makes the request
  onRequest = requestData => request(
    {
      method: requestData.method || 'GET',
      uri: `${location.href}${requestData.apiEndPoint}`,
      json: requestData.json || true,
      body: requestData.body || {},
      resolveWithFullResponse: requestData.resolveWithFullResponse || false,
    },
  );

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {this.state.demo}
          </p>
        </header>
      </div>
    );
  }
}

export default App;
