import React, { Component } from 'react';
import Hotels from "./Hotels";

import CSEARCH from "../../utils/contants";
const onRequest = require("../../utils/helper").default;

class HotelsContainer extends Component {

  constructor(props) {
    super(props);
    this.state = {
      data: [],
    }
  }

  componentDidMount() {
    const requestData = {
      apiEndPoint: `${CSEARCH.ENDPOINT.GET_ALL_HOTEL}`,
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
        <Hotels data={this.state.data}/>
      </div>
    )
  }
}

export default HotelsContainer;
