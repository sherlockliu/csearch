import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Collapse, List } from "antd";
const Panel = Collapse.Panel;

class Hot extends Component {
  constructor(props){
    super(props);
  }

  callback(key) {
    console.log(key);
  }

  render() {
    return (
      <Collapse defaultActiveKey={['1']}>
        <Panel header="房间基本信息" key="1">
          <p>{this.props.data.roomInfo}</p>
        </Panel>
        <Panel header="房间设置" key="2">
          <p>{this.props.data.roomSetting}</p>
        </Panel>
        <Panel header="酒店设置" key="3">
          <p>{this.props.data.hotelSetting}</p>
        </Panel>
      </Collapse>
    )
  }
}

Hot.propTypes = {
  data: PropTypes.object.isRequired,
};


export default Hot;
