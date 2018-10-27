import React from 'react';
import App from './views/App';
import { Router, Route, browserHistory } from 'react-router';
import AutoSuggestSearchContainer from "./views/Search/AutoSuggestSearchContainer";
import ResultContainer from "./views/Result/ResultContainer";
import HotelsContainer from "./views/Result/HotelsContainer";

const Home = () => {
  return (
    <Router history={browserHistory}>
      <Route path="/" component={App}>
        <Route path="/hotels" components={HotelsContainer}/>
        <Route path="/search/:id" component={AutoSuggestSearchContainer}/>
        <Route path="/result/:id/:word" component={ResultContainer}/>
      </Route>
    </Router>
  );
};

export default Home;
