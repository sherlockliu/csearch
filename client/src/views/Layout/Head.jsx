import React, { Component } from 'react';
import { Layout, Menu } from 'antd';

const { Header } = Layout;

class Head extends Component {
  render() {
    return (
      <Header>
        <div className="logo" />
        <Menu
          theme="dark"
          mode="horizontal"
          defaultSelectedKeys={['2']}
          style={{ lineHeight: '64px' }}
        >
          <Menu.Item key="1"><a href="/hotels">Hotels</a></Menu.Item>
        </Menu>
      </Header>
    )
  }
}

export default Head;
