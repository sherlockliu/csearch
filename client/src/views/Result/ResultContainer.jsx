import React, { Component } from 'react';
import Result from "./Result";


class ResultContainer extends Component {
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
    const listData = [];
    for (let i = 0; i < 23; i++) {
      listData.push({
        title: `ant design part ${i}`,
        description: 'Ant Design, a design language for background applications, is refined by Ant UED Team.',
        content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
      });
    }
    this.setState({
      data: {
        structData: {
          roomInfo: "有阳台",
          roomSetting: "房间带有浴缸",
          hotelSetting: "酒店在公园旁边"
        },
        comments: [
          {
            title: '酒店还是不错的',
          },
          {
            title: '房间很大,给力',
          },
          {
            title: '早餐好吃,很好吃',
          },
          {
            title: '安静',
          },
        ],
        QA: listData
      },
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
