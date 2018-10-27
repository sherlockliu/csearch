import React, { Component } from 'react';
import Hot from "./Hot";
import PropTypes from 'prop-types';

class HotContainer extends Component {

  constructor(props) {
    super(props);
    this.state = {
      data: [],
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
    this.setState({
      data: [
        {
          title: '有没有早餐?',
        },
        {
          title: '能不能带宠物?',
        },
        {
          title: '房间大不大?',
        },
        {
          title: '能不能加床?',
        },
      ],
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
