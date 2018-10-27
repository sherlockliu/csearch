import React, { Component } from 'react';
import { Button, Tag } from "antd";
import PropTypes from 'prop-types';

class SearchHistory extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    const tags = []
    if (this.props.data) {
      this.props.data.forEach((item) => {
        tags.push(
          <Button size="small" onClick={()=>{this.props.onClickSearch(item);}}>{item}</Button>
        );
      })
    }
    return (
      <div>
        {tags}
      </div>
    )
  }
}

SearchHistory.propTypes = {
  data: PropTypes.array.isRequired,
  onTagClick: PropTypes.func.isRequired,
};

export default SearchHistory;
