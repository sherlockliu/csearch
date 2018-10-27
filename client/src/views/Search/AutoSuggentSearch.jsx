import React, { Component } from 'react';
import { AutoComplete, Button, Icon, Input } from 'antd';
import './AutoSuggestSearch.css';
import PropTypes from 'prop-types';

class AutoSuggestSearch extends Component {
  handleSearch = (value) => {
    // const dataSource = await this.props.onHandleSuggest(value);
    // this.setState({
    //   dataSource: dataSource.suggestions,
    //   value,
    // });
    this.setState({
      dataSource: !value ? [] : [
        value,
        value + value,
        value + value + value,
      ],
    });
  }

  onSelect(value) {
    this.setState({
      value,
    })
    console.log(this.state)
  }

  onSearch = () => {
     this.props.onClickSearch(this.state.value);
  }

  constructor(props) {
    super(props);
    this.state = {
      dataSource: [],
      // value: '',
    }
  }

  render() {
    const {dataSource} = this.state;
    return (
      <div className="global-search-wrapper">
        <AutoComplete
          className="global-search"
          size="large"
          style={{ width: '70%' }}
          dataSource={dataSource}
          onSearch={this.handleSearch}
          placeholder="Search here."
        >
          <Input
            suffix={(
              <Button className="search-btn" onClick={this.onSearch} size="large" type="primary">
                <Icon type="search"/>
              </Button>
            )}
          />
        </AutoComplete>
      </div>
    );
  }
}

AutoSuggestSearch.propTypes = {
  onHandleSuggest: PropTypes.func.isRequired,
  onClickSearch: PropTypes.func.isRequired,
};


export default AutoSuggestSearch;
