import React, { Component } from 'react';
import {
  Route,
  Link,
  Switch
} from 'react-router-dom';
import NavReactReducer from '../reducers/NavReactReducer.js';
import LoginReactReducer from '../reducers/LoginReactReducer.js';
import HomeReactReducer from '../reducers/HomeReactReducer.js';
import AboutReactReducer from '../reducers/AboutReactReducer.js';
// TODO: App Component
class App extends Component {
  render() {
    return (
      <div>
        <NavReactReducer /><br/><br/>
        <Switch>
          <Route exact path="/" component={LoginReactReducer}/>
          <Route exact path="/Home" component={HomeReactReducer}/>
          <Route path="/About" component={AboutReactReducer}/>
        </Switch>
      </div>
    );
  }
}
// TODO: export App
export default App;
