import React, { Component } from 'react';
import { Breadcrumb, Layout } from 'antd';

const { Content } = Layout;

class Main extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <div>
        <Content style={{ padding: '0 50px' }}>
          <div  className="App-main" style={{ background: '#fff', padding: 24, minHeight: 280 }}>{this.props.subComponent}</div>
        </Content>
      </div>
    )
  }
}

export default Main;
