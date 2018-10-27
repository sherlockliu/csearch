import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { List } from "antd";
import Highlighter from "react-highlight-words";

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
            <Highlighter
                highlightClassName="YourHighlightClass"
                searchWords={["and", "or", "the"]}
                autoEscape={true}
                textToHighlight="The dog is chasing the cat. Or perhaps they're just playing?"
            />
        )}
      />
    )
  }
}

Comments.propTypes = {
  data: PropTypes.array.isRequired,
};


export default Comments;
