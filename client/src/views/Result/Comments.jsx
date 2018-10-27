import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { List } from "antd";

class Comments extends Component {
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
              title={item.comment_content}
            />
          </List.Item>
        )}
      />
    )
  }
}

Comments.propTypes = {
  data: PropTypes.array.isRequired,
};


export default Comments;
