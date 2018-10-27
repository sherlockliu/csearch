import React, { Component } from 'react';
import Hot from "./Hot";
import Comments from "./Comments";

const data = [
  {
    title: '酒店还是不错的',
  },
  {
    title: '房间很大,给力',
  },
  {
    title: '早餐好吃,很好吃',
  },
  {
    title: '安静',
  },
];

class CommentsContainer extends Component {
  render() {
    return (
      <div>
        <Comments data={data}/>
      </div>
    )
  }
}

export default CommentsContainer;
