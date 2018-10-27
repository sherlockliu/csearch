import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Collapse, List } from "antd";
import Highlighter from "react-highlight-words";
const Panel = Collapse.Panel;


class StructData extends Component {
  constructor(props){
    super(props);
  }

  callback(key) {
    console.log(key);
  }

  render() {
    let content = '';
    if (this.props.data){
        content = JSON.stringify(this.props.data);
    }
    return (
      <Collapse defaultActiveKey={['1']}>
        <Panel header="房间基本信息" key="1">
            <Highlighter
                 highlightClassName="YourHighlightClass"
                 searchWords={[]}
                 autoEscape={true}
                 textToHighlight={content}
            />
        </Panel>
      </Collapse>
    )
  }
}

StructData.propTypes = {
  data: PropTypes.object.isRequired,
};


export default StructData;
