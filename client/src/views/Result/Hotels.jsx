import React, { Component } from 'react';
import { List } from "antd";
import PropTypes from 'prop-types';

class Hotels extends Component {

  constructor(props){
    super(props);
  }

  render() {
    return (
      <List
        itemLayout="horizontal"
        dataSource={this.props.data}
        renderItem={item => (
          <List.Item>
            <List.Item.Meta
              title={<a href={"search/"+item.hotel_id}>{item.hotel_name}</a>}
            />
          </List.Item>
        )}
      />
    )
  }
}

Hotels.propTypes = {
  data: PropTypes.array.isRequired,
};

export default Hotels;
