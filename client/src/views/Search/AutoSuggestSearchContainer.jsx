import React, { Component } from 'react';
import AutoSuggestSearch from "./AutoSuggentSearch";
import HotContainer from "../Result/HotContainer";
import SearchHistoryContainer from "../Result/SearchHistoryContainer";
const onRequest = require("../../utils/helper").default;

class AutoSuggestSearchContainer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      hotelId: '',
    }
  }

  componentDidMount() {
  }

  onSearch = (value) => {
    window.location.href = `${window.location.origin}/result/${window.location.href.split('/').pop()}/${value}`;
  }

  onHandleSuggest = async (value) => {
    const requestData = {
      apiEndPoint: `hotel/${window.location.href.split('/').pop()}/hot/${value}`,
    }
    const data = await onRequest(requestData);
    return data;
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
