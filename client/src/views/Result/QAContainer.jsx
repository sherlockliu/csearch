import React, { Component } from 'react';
import { List, message, Avatar, Spin } from 'antd';
import QA from "./QA";

const fakeDataUrl = 'https://randomuser.me/api/?results=5&inc=name,gender,email,nat&noinfo';

class QAContainer extends Component {
  state = {
    data: [],
    loading: false,
    hasMore: true,
  }

  getData = (callback) => {
    const listData = [];
    for (let i = 0; i < 23; i++) {
      listData.push({
        href: 'http://ant.design',
        title: `ant design part ${i}`,
        avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
        description: 'Ant Design, a design language for background applications, is refined by Ant UED Team.',
        content: 'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
      });
    }
    console.log(listData);
    callback(listData);
  }

  componentDidMount() {
    console.log('componentDidMount');
    this.getData((res) => {
      this.setState({
        data: res,
      });
    });
  }

  handleInfiniteOnLoad = () => {
    let data = this.state.data;
    this.setState({
      loading: true,
    });
    if (data.length > 14) {
      message.warning('Infinite List loaded all');
      this.setState({
        hasMore: false,
        loading: false,
      });
      return;
    }
    this.getData((res) => {
      data = data.concat(res.results);
      this.setState({
        data,
        loading: false,
      });
    });
  }

  render() {
    return (
      <div className="demo-infinite-container">
        <QA
          data={this.state.data}
          loading={this.state.loading}
          hasMore={this.state.hasMore}
        />
      </div>
    );
  }
}

export default QAContainer;
