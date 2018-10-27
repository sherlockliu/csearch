import React, { Component } from 'react';
import AutoSuggestSearch from "./AutoSuggentSearch";
import HotContainer from "../Result/HotContainer";
import SearchHistoryContainer from "../Result/SearchHistoryContainer";

class AutoSuggestSearchContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      hotelId: '',
    }
  }

  componentDidMount() {
    // request function that takes requestData as arg and makes the request
    // const requestData = {
    //   apiEndPoint: CSEARCH.ENDPOINT.GET_ALL_HOTEL,
    // }
    // onRequest(requestData).then((data) => {
    //   this.setState({
    //     data,
    //   })
    // })
    const hotelId = window.location.href.split('/').pop();
    this.setState({
      hotelId,
    })
  }

  onSearch = (value) => {
    window.location.href = `${window.location.origin}/result/${value}`;
  }

  onHandleSuggest = (value) => {
    return ['d','ddd','dddd'];
  }

  render() {
    return (
      <div className="App-search-container">
        <AutoSuggestSearch
          onHandleSuggest={this.onHandleSuggest}
          onClickSearch={this.onSearch}
        />
        <div className="hot-container">
          <h4 style={{ marginBottom: 16 }}>History:</h4>
          <SearchHistoryContainer
            onClickSearch={this.onSearch}
          />
          <h4 style={{ margin: '16px 0' }}>Hot:</h4>
          <HotContainer
            onClickSearch={this.onSearch}
          />
        </div>
      </div>
    )
  }
}

export default AutoSuggestSearchContainer;
