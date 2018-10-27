import React, { Component } from 'react';
import Result from "./Result";
const onRequest = require("../../utils/helper").default;

class ResultContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    }
  }

  componentDidMount() {
    const params = window.location.href.split('/');
    const word = params.pop();
    const hotelId = params.pop();
    // request function that takes requestData as arg and makes the request
    const requestData = {
      apiEndPoint: `hotel/${hotelId}/search/${word}`,
    }
    onRequest(requestData).then((data) => {
      this.setState({
        data,
      })
    })
  }

  render() {
    return (
      <div className="App-search-container">
        <Result data={this.state.data}/>
      </div>
    )
  }
}

export default ResultContainer;
