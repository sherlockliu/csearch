import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Icon, List, Spin } from "antd";
import InfiniteScroll from 'react-infinite-scroller';

class QA extends Component {

  constructor(props) {
    super(props);
    console.log(props);
  }

  render() {
    const IconText = ({ type, text }) => (
      <span>
        <Icon type={type} style={{ marginRight: 8 }}/>
        {text}
       </span>
    );

    return (
      <InfiniteScroll
        initialLoad={false}
        pageStart={0}
        loadMore={this.handleInfiniteOnLoad}
        hasMore={!this.props.loading && this.props.hasMore}
        useWindow={false}
      >
        <List
          itemLayout="vertical"
          size="large"
          dataSource={this.props.data}
          renderItem={item => (
            <List.Item
              key={item.question_id}
              actions={[<IconText type="star-o" text="156"/>, <IconText type="like-o" text="156"/>,
                <IconText type="message" text="2"/>]}
            >
              <List.Item.Meta
                title={<a href={item.href}>{item.question}</a>}
                description={item.answer}
              />
            </List.Item>
          )}
        >
          {this.props.loading && this.props.hasMore && (
            <div className="demo-loading-container">
              <Spin/>
            </div>
          )}</List>
      </InfiniteScroll>
    )
  }
}

QA.propTypes = {
  data: PropTypes.array.isRequired,
  loading: PropTypes.bool.isRequired,
  hasMore: PropTypes.bool.isRequired,
};


export default QA;
