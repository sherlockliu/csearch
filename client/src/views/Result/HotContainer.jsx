import React, { Component } from 'react';
import Hot from "./Hot";
import PropTypes from 'prop-types';
const onRequest = require("../../utils/helper").default;

class HotContainer extends Component {

  constructor(props) {
    super(props);
    this.state = {
      data: [],
    }
  }

  componentDidMount() {
      const requestData = {
          apiEndPoint: `hotel/${window.location.href.split('/').pop()}`,
      }
      onRequest(requestData).then((data) => {
          console.log(data);
          this.setState({
              data,
          })
      })
  }

  render() {
    return (
      <div>
        <Hot data={this.state.data} onClickSearch={this.props.onClickSearch}/>
      </div>
    )
  }
}

HotContainer.propTypes = {
  onClickSearch: PropTypes.func.isRequired,
};

export default HotContainer;
