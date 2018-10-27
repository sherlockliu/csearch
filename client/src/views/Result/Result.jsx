import React, { Component } from 'react';
import { Tabs } from 'antd';
import StructData from "./StructData";
import PropTypes from 'prop-types';
import Comments from "./Comments";
import QA from "./QA";

const TabPane = Tabs.TabPane;

class Result extends Component {
  render() {
    return (
      <Tabs defaultActiveKey="1">
        <TabPane tab="点评" key="1"><Comments data={this.props.data.comments}/></TabPane>
        <TabPane tab="问答" key="2"><QA
          data={this.props.data.questions}
          loading={false}
          hasMore={false}
        /></TabPane>
        <TabPane tab="酒店信息" key="3">
            <StructData
                data={this.props.data.data}
            />
        </TabPane>
      </Tabs>
    )
  }
}

Result.propTypes = {
  data: PropTypes.array.isRequired,
};

export default Result;
