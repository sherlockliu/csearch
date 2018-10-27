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
    // request function that takes requestData as arg and makes the request
    const requestData = {
      apiEndPoint: `hotel/346693/search/${window.location.href.split('/').pop()}`,
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
