/* eslint-disable no-restricted-globals */
import React, { Component } from 'react';
import './App.css';
import { Layout } from "antd";
import Head from "./Layout/Head";
import Foot from "./Layout/Foot";
import 'antd/dist/antd.css';

const { Content } = Layout;

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      hotelId: '',
    }
  }

  render() {
    return (
      <div>
        <Layout className="layout">
          <Head/>
          <Content style={{ padding: '0 50px', margin: '30px 0' }}>
            <div className="App-main"
                 style={{ background: '#fff', padding: 24, minHeight: 280 }}>{this.props.children}</div>
          </Content>
          <Foot/>
        </Layout>
      </div>
    );
  }
}

export default App;
