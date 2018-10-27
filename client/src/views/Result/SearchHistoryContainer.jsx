
import React, { Component } from 'react';
import SearchHistory from "./SearchHistory";
import PropTypes from 'prop-types';

class SearchHistoryContainer extends Component {

  constructor(props) {
    super(props);
    this.state = {
      data: [],
    }
  }

  componentDidMount() {
    this.setState({
      data:['房型','能不能带宠物','wifi','退款'],
    })
  }

  render() {
    return (
      <div className="App-search-container">
        <SearchHistory
          data={this.state.data}
          onClickSearch={this.props.onClickSearch}
        />
      </div>
    )
  }
}

SearchHistoryContainer.propTypes = {
  onClickSearch: PropTypes.func.isRequired,
};

export default SearchHistoryContainer;
