import React, { Component } from 'react';
import { Layout } from 'antd';

const { Footer } = Layout;

class Foot extends Component {
  render() {
    return (
      <Footer style={{ textAlign: 'center' }}>
        CSearch Design ©2018 Created by python 大法好
      </Footer>
    )
  }
}

export default Foot;
