import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { List } from "antd";

class Hot extends Component {
  constructor(props){
    super(props);
  }
  render() {
    return (
      <List
        split="true"
        itemLayout="horizontal"
        dataSource={this.props.data}
        renderItem={item => (
          <List.Item>
            <List.Item.Meta
              title={<a href="javascript:void(0);" onClick={()=>{
                this.props.onClickSearch(item);
              }}>{item}</a>}
            />
          </List.Item>
        )}
      />
    )
  }
}

Hot.propTypes = {
  data: PropTypes.array.isRequired,
  onClickSearch: PropTypes.func.isRequired,
};


export default Hot;
